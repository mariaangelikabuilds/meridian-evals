# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0425 | 3.68s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.85s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 3.33s | $0.003213 |
| real-donor-export | yes | P2 | software | 0.75 | 3.68s | $0.003585 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 4.03s | $0.003486 |
| real-night-kiosk | yes | P2 | hardware | 0.65 | 3.88s | $0.004539 |
| calm-phish-click | yes | P1 | security | 0.85 | 3.1s | $0.00345 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.92s | $0.005727 |
| vip-lockout | NO: min_severity | P3 | access | 0.72 | 2.91s | $0.003435 |
| routine-onboarding | yes | P4 | access | 0.85 | 2.15s | $0.00261 |
| everything-down | yes | P1 | outage | 0.85 | 2.48s | $0.002748 |
| vague-slowness | yes | P4 | software | 0.55 | 2.5s | $0.002913 |
| ransom-note | yes | P1 | security | 0.98 | 3.86s | $0.002862 |
| after-hours-badge | yes | P2 | security | 0.65 | 4.39s | $0.003933 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.8s | $0.000207 |
| real-donor-export | yes | P1 | software | 0.9 | 2.6s | $0.000176 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.69s | $0.000178 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.04s | $0.000222 |
| calm-phish-click | yes | P2 | security | 0.8 | 2.52s | $0.000171 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.34s | $0.000228 |
| vip-lockout | yes | P2 | access | 0.9 | 1.15s | $0.000178 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.25s | $0.000152 |
| everything-down | yes | P1 | outage | 0.95 | 2.28s | $0.000169 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.11s | $0.000177 |
| ransom-note | yes | P1 | security | 0.9 | 1.37s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.85s | $0.000188 |
