# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0394 | 3.22s | calm-phish-click, vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.94s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 2.98s | $0.003273 |
| real-donor-export | yes | P2 | software | 0.7 | 3.3s | $0.002745 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.61s | $0.003441 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.61s | $0.004179 |
| calm-phish-click | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.56s | $0.007017 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.49s | $0.00324 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.26s | $0.00267 |
| everything-down | yes | P1 | outage | 0.85 | 2.45s | $0.003048 |
| vague-slowness | yes | P4 | software | 0.55 | 2.5s | $0.003003 |
| ransom-note | yes | P1 | security | 0.98 | 3.22s | $0.003072 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.46s | $0.003693 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 4.68s | $0.000199 |
| real-donor-export | yes | P1 | software | 0.9 | 1.89s | $0.000166 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.63s | $0.000186 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.31s | $0.000218 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.94s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.46s | $0.000194 |
| vip-lockout | yes | P2 | access | 0.9 | 1.56s | $0.000178 |
| routine-onboarding | yes | P4 | request | 0.9 | 2.35s | $0.000166 |
| everything-down | yes | P1 | outage | 0.95 | 1.9s | $0.00018 |
| vague-slowness | yes | P3 | software | 0.7 | 1.65s | $0.000154 |
| ransom-note | yes | P1 | security | 0.95 | 1.85s | $0.000176 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.33s | $0.000207 |
