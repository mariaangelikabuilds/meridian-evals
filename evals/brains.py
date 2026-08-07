"""The two production brains under evaluation. Both are the real deployed things:
Claude via the Anthropic API with meridian-ops's triage prompt, and the Azure
Functions brain (which applies its own ported gates server-side)."""
import json
import os
import time
import urllib.request

from .gates import security_floor, parse_verdict

SYSTEM = (
    "You are the triage brain for an MSP service desk. Classify the incident.\n"
    "Respond with a single JSON object and nothing else, no code fences.\n"
    'Schema: {"severity":"P1|P2|P3|P4","category":"security|outage|hardware|software|network|access|request",'
    '"confidence":0.0,"reasoning":"one paragraph"}'
)

# per-million pricing for cost scoring; override via env when the sheet changes
CLAUDE_IN = float(os.environ.get("CLAUDE_PRICE_IN", 3.0))
CLAUDE_OUT = float(os.environ.get("CLAUDE_PRICE_OUT", 15.0))
AZURE_IN = float(os.environ.get("AZURE_PRICE_IN", 0.40))
AZURE_OUT = float(os.environ.get("AZURE_PRICE_OUT", 1.60))


def _post(url: str, headers: dict, payload: dict, timeout: int = 60) -> dict:
    """Retry on transient upstream failures. A 429 or 5xx is the provider having a
    moment, not the brain being wrong; without this the eval scores infrastructure
    noise as bad judgment, which is how a green suite starts lying."""
    last = None
    for attempt in range(1, 4):
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json", **headers})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as res:
                return json.loads(res.read())
        except urllib.error.HTTPError as err:
            last = err
            if err.code not in (429, 500, 502, 503, 504, 529) or attempt == 3:
                raise RuntimeError(f"HTTP {err.code}: {err.read()[:180].decode(errors='replace')}") from err
        except urllib.error.URLError as err:
            last = err
            if attempt == 3:
                raise
        time.sleep(attempt * 2)
    raise RuntimeError(f"unreachable: {last}")


def run_claude(case: dict) -> dict:
    """Escalate the cap on truncation. A long reasoning field hits max_tokens and
    the JSON arrives unterminated; retrying at the same cap just truncates again.
    Same failure mode the fleet hit in production, same fix."""
    t0 = time.time()
    body = _claude_call(case, int(os.environ.get("CLAUDE_MAX_TOKENS", 1500)))
    latency = time.time() - t0
    text = "".join(b["text"] for b in body["content"] if b["type"] == "text")
    verdict = parse_verdict(text)
    verdict, floor = security_floor(case["subject"], case["body"], verdict)
    usage = body["usage"]
    cost = (usage["input_tokens"] * CLAUDE_IN + usage["output_tokens"] * CLAUDE_OUT) / 1e6
    return {"verdict": verdict, "floor": floor, "latency_s": round(latency, 2), "cost_usd": round(cost, 6)}


def _claude_call(case: dict, cap: int) -> dict:
    for _ in range(3):
        body = _post(
            "https://api.anthropic.com/v1/messages",
            {"x-api-key": os.environ["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01"},
            {
                "model": os.environ.get("CLAUDE_MODEL", "claude-sonnet-5"),
                "max_tokens": cap,
                "system": SYSTEM,
                "messages": [{"role": "user", "content": f"Client: {case['client']}\nSubject: {case['subject']}\n{case['body']}"}],
            },
        )
        if body.get("stop_reason") != "max_tokens":
            return body
        cap *= 2
    return body


def run_azure(case: dict) -> dict:
    t0 = time.time()
    url = f"{os.environ['AZURE_BRAIN_URL']}?code={os.environ['AZURE_BRAIN_KEY']}"
    body = _post(url, {}, {"subject": case["subject"], "body": case["body"], "client": case["client"]})
    latency = time.time() - t0
    floor = next((d for d in body["decisions"] if d["gate"] == "security-floor"), {"gate": "security-floor", "action": "pass"})
    usage = body["usage"]
    cost = (usage["prompt_tokens"] * AZURE_IN + usage["completion_tokens"] * AZURE_OUT) / 1e6
    return {"verdict": body["verdict"], "floor": floor, "latency_s": round(latency, 2), "cost_usd": round(cost, 6)}


BRAINS = {"claude": run_claude, "azure": run_azure}
