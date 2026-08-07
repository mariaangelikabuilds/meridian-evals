import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from evals.gates import parse_verdict


def test_parses_multiline_reasoning():
    """Claude writes reasoning across lines, which puts a raw newline inside a
    JSON string. Strict json.loads calls that an unterminated string; the
    harness repairs it instead of scoring the case as a model failure."""
    raw = '{"severity":"P2","category":"outage","confidence":0.8,"reasoning":"first line\nsecond line"}'
    v = parse_verdict(raw)
    assert v["severity"] == "P2"
    assert "second line" in v["reasoning"]


def test_parses_tabs_and_carriage_returns():
    raw = '{"severity":"P1","category":"security","confidence":0.9,"reasoning":"a\tb\r\nc"}'
    assert parse_verdict(raw)["severity"] == "P1"


def test_still_rejects_real_junk():
    import pytest

    with pytest.raises(ValueError):
        parse_verdict("no json at all")
