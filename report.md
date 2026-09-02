# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0442 | 4.11s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.84s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 3.62s | $0.003423 |
| real-donor-export | yes | P2 | software | 0.7 | 4.11s | $0.00294 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 4.14s | $0.003051 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.49s | $0.003549 |
| calm-phish-click | yes | P1 | security | 0.85 | 3.93s | $0.00366 |
| quiet-security-tell | yes | P2 | security | 0.6 | 6.59s | $0.006702 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 4.73s | $0.00363 |
| routine-onboarding | yes | P4 | access | 0.9 | 3.02s | $0.002715 |
| everything-down | yes | P1 | outage | 0.9 | 4.08s | $0.003273 |
| vague-slowness | yes | P4 | software | 0.55 | 4.47s | $0.003453 |
| ransom-note | yes | P1 | security | 0.98 | 3.65s | $0.003447 |
| after-hours-badge | yes | P2 | security | 0.7 | 4.56s | $0.004383 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.95s | $0.000194 |
| real-donor-export | yes | P1 | software | 0.9 | 1.39s | $0.000171 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.37s | $0.000189 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.82s | $0.000219 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.4s | $0.000156 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.06s | $0.000234 |
| vip-lockout | yes | P2 | access | 0.9 | 1.61s | $0.00017 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.42s | $0.000171 |
| everything-down | yes | P1 | outage | 0.95 | 2.03s | $0.000187 |
| vague-slowness | yes | P4 | hardware | 0.8 | 2.29s | $0.000191 |
| ransom-note | yes | P1 | security | 0.9 | 1.84s | $0.000174 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.18s | $0.000164 |
