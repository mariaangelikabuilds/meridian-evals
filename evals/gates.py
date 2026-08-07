"""The deterministic gates, ported from meridian-ops so both brains are judged
with the same rules they run behind in production. Model proposes, code decides."""
import re

SEVERITY_RANK = {"P4": 1, "P3": 2, "P2": 3, "P1": 4}

# prefix-matching on purpose: "phish" must catch "phishing", "ransom" must catch
# "ransomware". A trailing \b here silently broke exactly that; the unit test caught it.
SECURITY_TEXT = re.compile(
    r"\b(phish|breach|ransom|malware|compromis|unauthoriz|credential|password reset|"
    r"lockout after|suspicious (login|email|link)|antivirus|quarantin|encrypted)",
    re.I,
)


def security_floor(subject: str, body: str, verdict: dict) -> tuple[dict, dict]:
    is_security = verdict["category"] == "security" or SECURITY_TEXT.search(f"{subject} {body}")
    if not is_security or SEVERITY_RANK[verdict["severity"]] >= SEVERITY_RANK["P2"]:
        return verdict, {"gate": "security-floor", "action": "pass"}
    raised = dict(verdict, severity="P2")
    return raised, {"gate": "security-floor", "action": "raise", "before": verdict["severity"]}


def parse_verdict(raw: str) -> dict:
    import json
    stripped = re.sub(r"^\s*```(?:json)?\s*", "", raw)
    stripped = re.sub(r"\s*```\s*$", "", stripped)
    start, end = stripped.find("{"), stripped.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object in model output")
    v = json.loads(stripped[start : end + 1])
    if v.get("severity") not in SEVERITY_RANK:
        raise ValueError(f"bad severity: {v.get('severity')}")
    if not isinstance(v.get("confidence"), (int, float)):
        raise ValueError("missing confidence")
    return v
