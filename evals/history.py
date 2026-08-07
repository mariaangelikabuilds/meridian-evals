"""One line per nightly run, appended to history.md so the repo accumulates a
public reliability record the way the fleet accumulates run history."""
import json
import pathlib
import sys
from datetime import datetime, timezone


def line() -> str:
    results = json.loads(pathlib.Path("results.json").read_text(encoding="utf8"))
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    parts = []
    for brain, data in results.items():
        s = data["summary"]
        parts.append(f"{brain} {s['passed']}/{s['cases']} ${s['total_cost_usd']} {s['median_latency_s']}s")
    return f"| {stamp} | " + " | ".join(parts) + " |"


if __name__ == "__main__":
    print(line())
