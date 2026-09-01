"""Run the golden set against one or both production brains and write the scorecard.

  python -m evals.run --brain both --out report.md
"""
import argparse
import json
import pathlib
import sys

from . import tracing
from .brains import BRAINS
from .score import score_case, summarize

GOLDEN = pathlib.Path(__file__).with_name("golden.jsonl")


def run(brain_names: list[str]) -> dict:
    cases = [json.loads(l) for l in GOLDEN.read_text(encoding="utf8").splitlines() if l.strip()]
    out = {}
    for name in brain_names:
        rows = []
        for case in cases:
            try:
                result = BRAINS[name](case)
                rows.append(score_case(case, result))
                trace = tracing.record_case(name, case, result, rows[-1])
                if trace:
                    rows[-1].update(trace)
            except Exception as err:
                rows.append({"id": case["id"], "passed": False, "checks": {"error": False}, "context_dependent": bool(case.get("context_dependent")), "severity": "-", "category": "-", "confidence": 0, "latency_s": 0, "cost_usd": 0, "error": str(err)[:160]})
                print(f"    error: {str(err)[:160]}", file=sys.stderr)
            print(f"  {name} {case['id']}: {'pass' if rows[-1]['passed'] else 'FAIL'}", file=sys.stderr)
        out[name] = {"rows": rows, "summary": summarize(rows)}
    return out


def report(results: dict) -> str:
    lines = ["# Meridian triage brains, scored", ""]
    lines.append("The same golden set of labeled incidents, real and adversarial, fired at both production brains.")
    lines.append("")
    lines.append("| brain | pass rate | cases | total cost | median latency | failures | known context gaps |")
    lines.append("|---|---|---|---|---|---|---|")
    for name, r in results.items():
        s = r["summary"]
        model = "claude-sonnet-5 (Anthropic API)" if name == "claude" else "gpt-4.1-mini (Azure Functions + Azure OpenAI)"
        lines.append(f"| {model} | {s['pass_rate']:.0%} | {s['passed']}/{s['cases']} | ${s['total_cost_usd']} | {s['median_latency_s']}s | {', '.join(s['failures']) or 'none'} | {', '.join(s.get('known_context_gaps', [])) or 'none'} |")
    lines.append("")
    for name, r in results.items():
        lines.append(f"## {name}: per case")
        lines.append("")
        lines.append("| case | pass | severity | category | conf | latency | cost |")
        lines.append("|---|---|---|---|---|---|---|")
        for row in r["rows"]:
            mark = "yes" if row["passed"] else ("known gap" if row.get("context_dependent") else "NO: " + ",".join(k for k, v in row["checks"].items() if not v))
            if row.get("error"):
                mark += f" ({row['error'][:60]})"
            lines.append(f"| {row['id']} | {mark} | {row['severity']} | {row['category']} | {row['confidence']} | {row['latency_s']}s | ${row['cost_usd']} |")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--brain", default="both", choices=["claude", "azure", "both"])
    ap.add_argument("--out", default="report.md")
    args = ap.parse_args()
    names = ["claude", "azure"] if args.brain == "both" else [args.brain]
    results = run(names)
    pathlib.Path(args.out).write_text(report(results), encoding="utf8")
    pathlib.Path("results.json").write_text(json.dumps(results, indent=1), encoding="utf8")
    print(report(results))
