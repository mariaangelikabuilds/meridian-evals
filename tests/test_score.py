from evals.score import score_case, summarize
from evals.gates import security_floor, parse_verdict
import pytest


def case(expect):
    return {"id": "t", "client": "c", "subject": "s", "body": "b", "expect": expect}


def result(severity="P2", category="security", conf=0.9):
    return {"verdict": {"severity": severity, "category": category, "confidence": conf}, "floor": {}, "latency_s": 1.0, "cost_usd": 0.01}


def test_min_severity_bound():
    assert score_case(case({"min_severity": "P2"}), result("P1"))["passed"]
    assert not score_case(case({"min_severity": "P2"}), result("P3"))["passed"]


def test_max_severity_bound():
    assert score_case(case({"max_severity": "P3"}), result("P4", "request"))["passed"]
    assert not score_case(case({"max_severity": "P3"}), result("P1"))["passed"]


def test_category_and_floor():
    r = score_case(case({"category_any": ["security"], "security_floor_must_hold": True}), result("P3", "security"))
    assert not r["passed"] and not r["checks"]["security_floor"]


def test_summarize_counts_failures():
    rows = [score_case(case({"min_severity": "P2"}), result(s)) for s in ("P1", "P4")]
    s = summarize(rows)
    assert s["passed"] == 1 and s["failures"] == ["t"]


def test_security_floor_raises():
    v, d = security_floor("s", "user clicked a phishing link", {"severity": "P4", "category": "software", "confidence": 0.9})
    assert v["severity"] == "P2" and d["action"] == "raise"


def test_parse_verdict_rejects_junk():
    assert parse_verdict('{"severity":"P2","category":"outage","confidence":0.8}')["severity"] == "P2"
    with pytest.raises(ValueError):
        parse_verdict("nope")
