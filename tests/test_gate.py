import json
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from evals import gate
from evals.history import line


def write(tmp_path, results, baseline=None):
    os.chdir(tmp_path)
    (tmp_path / "results.json").write_text(json.dumps(results), encoding="utf8")
    if baseline:
        (tmp_path / "baseline.json").write_text(json.dumps(baseline), encoding="utf8")
    gate.RESULTS = tmp_path / "results.json"
    gate.BASELINE = tmp_path / "baseline.json"


def summary(passed, cases, rate, failures=()):
    return {"summary": {"passed": passed, "cases": cases, "pass_rate": rate, "failures": list(failures), "total_cost_usd": 0.01, "median_latency_s": 2.0}}


def test_gate_passes_when_above_floor(tmp_path):
    write(tmp_path, {"azure": summary(12, 12, 1.0)})
    assert gate.check(0.8) == 0


def test_gate_fails_below_floor(tmp_path):
    write(tmp_path, {"azure": summary(8, 12, 0.667, ["a", "b"])})
    assert gate.check(0.8) == 1


def test_gate_fails_on_regression_from_baseline(tmp_path):
    write(tmp_path, {"azure": summary(10, 12, 0.833)}, baseline={"azure": {"pass_rate": 1.0}})
    assert gate.check(0.8) == 1


def test_gate_allows_improvement_over_baseline(tmp_path):
    write(tmp_path, {"azure": summary(12, 12, 1.0)}, baseline={"azure": {"pass_rate": 0.833}})
    assert gate.check(0.8) == 0


def test_missing_results_is_a_failure(tmp_path):
    os.chdir(tmp_path)
    gate.RESULTS = tmp_path / "nope.json"
    assert gate.check(0.8) == 1


def test_history_line_shape(tmp_path):
    write(tmp_path, {"azure": summary(12, 12, 1.0), "claude": summary(10, 12, 0.833)})
    out = line()
    assert out.startswith("| 20") and "azure 12/12" in out and "claude 10/12" in out
