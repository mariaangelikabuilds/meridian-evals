# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures |
|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 83% | 10/12 | $0.0398 | 4.59s | real-partner-mailbox, vip-lockout |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 12/12 | $0.0022 | 2.85s | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 4.59s | $0.003813 |
| real-donor-export | yes | P2 | software | 0.65 | 3.49s | $0.002685 |
| real-partner-mailbox | NO: error | - | - | 0 | 0s | $0 |
| real-night-kiosk | yes | P3 | hardware | 0.62 | 5.01s | $0.004224 |
| calm-phish-click | yes | P1 | security | 0.85 | 5.07s | $0.003495 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.97s | $0.007032 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 4.77s | $0.003375 |
| routine-onboarding | yes | P4 | access | 0.9 | 4.02s | $0.002595 |
| everything-down | yes | P1 | outage | 0.9 | 3.65s | $0.003288 |
| vague-slowness | yes | P4 | software | 0.55 | 3.32s | $0.002598 |
| ransom-note | yes | P1 | security | 0.98 | 3.92s | $0.002922 |
| after-hours-badge | yes | P2 | security | 0.72 | 4.73s | $0.003768 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.32s | $0.000223 |
| real-donor-export | yes | P2 | software | 0.9 | 2.86s | $0.000187 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 2.43s | $0.000174 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 3.04s | $0.000214 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.85s | $0.00016 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.64s | $0.000183 |
| vip-lockout | yes | P2 | access | 0.9 | 2.83s | $0.00019 |
| routine-onboarding | yes | P4 | request | 0.95 | 2.22s | $0.000168 |
| everything-down | yes | P1 | outage | 0.9 | 3.02s | $0.000166 |
| vague-slowness | yes | P3 | hardware | 0.7 | 3.34s | $0.000212 |
| ransom-note | yes | P1 | security | 0.95 | 2.61s | $0.00019 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.77s | $0.000169 |
