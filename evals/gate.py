"""CI gate: fail the build when judgment regresses.

  python -m evals.gate --min-pass-rate 0.8

Reads results.json from the run that just happened. Two rules: every brain must
clear the floor, and no brain may drop below its own committed baseline. The
baseline lives in baseline.json so a deliberate improvement is a visible commit,
not a silent drift.
"""
import argparse
import json
import pathlib
import sys

RESULTS = pathlib.Path("results.json")
BASELINE = pathlib.Path("baseline.json")


def check(min_pass_rate: float) -> int:
    if not RESULTS.exists():
        print("no results.json; the run did not produce a scorecard", file=sys.stderr)
        return 1
    results = json.loads(RESULTS.read_text(encoding="utf8"))
    baseline = json.loads(BASELINE.read_text(encoding="utf8")) if BASELINE.exists() else {}
    failures = []

    for brain, data in results.items():
        rate = data["summary"]["pass_rate"]
        if rate < min_pass_rate:
            failures.append(f"{brain}: pass rate {rate:.0%} below the floor of {min_pass_rate:.0%}")
        prior = baseline.get(brain, {}).get("pass_rate")
        if prior is not None and rate < prior:
            failures.append(f"{brain}: pass rate {rate:.0%} regressed from the committed baseline {prior:.0%}")
        cases = data["summary"]["failures"]
        if cases:
            print(f"  {brain} failing cases: {', '.join(cases)}", file=sys.stderr)

    if failures:
        for f in failures:
            print(f"FAIL {f}", file=sys.stderr)
        return 1
    print("gate passed: no brain below floor or baseline", file=sys.stderr)
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-pass-rate", type=float, default=0.8)
    sys.exit(check(ap.parse_args().min_pass_rate))
