"""Scoring: does the brain's judgment satisfy the case's expectations?
Expectations are bounds, not exact labels, because reasonable triage has range;
the gates' correctness is scored as a hard pass or fail."""
from .gates import SEVERITY_RANK


def score_case(case: dict, result: dict) -> dict:
    exp = case["expect"]
    v = result["verdict"]
    checks = {}

    if "min_severity" in exp:
        checks["min_severity"] = SEVERITY_RANK[v["severity"]] >= SEVERITY_RANK[exp["min_severity"]]
    if "max_severity" in exp:
        checks["max_severity"] = SEVERITY_RANK[v["severity"]] <= SEVERITY_RANK[exp["max_severity"]]
    if "category_any" in exp:
        checks["category"] = v["category"] in exp["category_any"]
    if exp.get("security_floor_must_hold"):
        checks["security_floor"] = SEVERITY_RANK[v["severity"]] >= SEVERITY_RANK["P2"]

    passed = all(checks.values())
    return {
        "id": case["id"],
        "passed": passed,
        "checks": checks,
        "severity": v["severity"],
        "category": v["category"],
        "confidence": v["confidence"],
        "latency_s": result["latency_s"],
        "cost_usd": result["cost_usd"],
    }


def summarize(rows: list[dict]) -> dict:
    n = len(rows)
    passed = sum(1 for r in rows if r["passed"])
    lat = sorted(r["latency_s"] for r in rows)
    return {
        "cases": n,
        "passed": passed,
        "pass_rate": round(passed / n, 3) if n else 0,
        "total_cost_usd": round(sum(r["cost_usd"] for r in rows), 4),
        "median_latency_s": lat[n // 2] if n else 0,
        "failures": [r["id"] for r in rows if not r["passed"]],
    }
