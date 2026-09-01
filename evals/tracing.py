"""Public Langfuse traces for each scored case, one per case per brain.

Env-gated the same way the live scorecard is: with no LANGFUSE_* keys this is a
no-op and the run behaves exactly as before, so offline and fork runs never
depend on it. Traces are created post-hoc with explicit timestamps derived from
the measured latency, which is why langfuse is pinned below 3: the v2 SDK takes
explicit timestamps on trace and generation, and hands back the share URL.

A tracing failure must never fail a scorecard run; it degrades to a stderr line.
"""
import atexit
import os
import sys
from datetime import datetime, timedelta, timezone

_client = None


def enabled() -> bool:
    return bool(os.environ.get("LANGFUSE_PUBLIC_KEY") and os.environ.get("LANGFUSE_SECRET_KEY"))


def _lf():
    global _client
    if _client is None:
        from langfuse import Langfuse
        _client = Langfuse()
        # CI exits right after the run; without a flush the batched ingestion
        # dies with the process and traces silently vanish.
        atexit.register(_client.flush)
    return _client


def record_case(brain: str, case: dict, result: dict, row: dict):
    """One public trace: the incident in, the verdict out, the floor decision as
    its own span. Returns {trace_id, trace_url} or None."""
    if not enabled():
        return None
    try:
        end = datetime.now(timezone.utc)
        start = end - timedelta(seconds=row.get("latency_s") or 0)
        model = "claude-sonnet-5" if brain == "claude" else "gpt-4.1-mini (Azure Fn)"
        trace = _lf().trace(
            name=f"{brain}:{case['id']}",
            public=True,
            timestamp=start,
            input={"client": case["client"], "subject": case["subject"], "body": case["body"]},
            output=result.get("verdict"),
            tags=[brain, "golden-set"],
            metadata={
                "expect": case.get("expect"),
                "passed": row.get("passed"),
                "checks": row.get("checks"),
                "context_dependent": row.get("context_dependent"),
                "cost_usd": row.get("cost_usd"),
            },
        )
        trace.generation(
            name="triage-verdict",
            model=model,
            start_time=start,
            end_time=end,
            input={"system": "triage classification", "incident": case["subject"]},
            output=result.get("verdict"),
            metadata={"cost_usd": row.get("cost_usd"), "latency_s": row.get("latency_s")},
        )
        trace.event(
            name="security-floor",
            start_time=end,
            input=result.get("floor"),
            metadata={"held": (row.get("checks") or {}).get("security_floor")},
        )
        return {"trace_id": trace.id, "trace_url": trace.get_trace_url()}
    except Exception as err:  # noqa: BLE001 - tracing must never fail the run
        print(f"    langfuse: {err}", file=sys.stderr)
        return None
