# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0419 | 2.77s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.34s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.7s | $0.003648 |
| real-donor-export | yes | P2 | software | 0.7 | 2.28s | $0.00291 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 3.07s | $0.003951 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 4.99s | $0.006204 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.97s | $0.00384 |
| quiet-security-tell | yes | P2 | security | 0.65 | 3.22s | $0.003597 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.24s | $0.00303 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.86s | $0.002595 |
| everything-down | yes | P1 | outage | 0.9 | 1.85s | $0.002493 |
| vague-slowness | yes | P4 | software | 0.55 | 2.77s | $0.003108 |
| ransom-note | yes | P1 | security | 0.98 | 2.17s | $0.002727 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.35s | $0.003798 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.8 | 2.71s | $0.000199 |
| real-donor-export | yes | P2 | software | 0.9 | 1.39s | $0.000182 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.34s | $0.000198 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.53s | $0.000198 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.18s | $0.000176 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.27s | $0.000184 |
| vip-lockout | yes | P2 | access | 0.9 | 1.27s | $0.000177 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.07s | $0.000142 |
| everything-down | yes | P1 | outage | 0.95 | 1.37s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.15s | $0.000161 |
| ransom-note | yes | P1 | security | 0.95 | 1.19s | $0.000176 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.76s | $0.00019 |
