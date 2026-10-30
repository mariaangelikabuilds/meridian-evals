# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0322 | 2.49s | vip-lockout, vague-slowness | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.31s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.63s | $0.003393 |
| real-donor-export | yes | P2 | software | 0.7 | 2.12s | $0.002775 |
| real-partner-mailbox | known gap (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.0s | $0.003699 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.65s | $0.00318 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.48s | $0.003792 |
| vip-lockout | NO: min_severity | P3 | access | 0.72 | 2.61s | $0.003525 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.03s | $0.002505 |
| everything-down | yes | P1 | outage | 0.9 | 2.27s | $0.002853 |
| vague-slowness | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| ransom-note | yes | P1 | security | 0.98 | 1.99s | $0.002817 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.49s | $0.003678 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.75s | $0.000209 |
| real-donor-export | yes | P1 | software | 0.9 | 1.3s | $0.000179 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.32s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.19s | $0.000206 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.39s | $0.000179 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.19s | $0.000197 |
| vip-lockout | yes | P2 | access | 0.9 | 1.49s | $0.00021 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.91s | $0.000133 |
| everything-down | yes | P1 | outage | 1 | 1.14s | $0.000176 |
| vague-slowness | yes | P4 | hardware | 0.7 | 1.31s | $0.000202 |
| ransom-note | yes | P1 | security | 0.95 | 1.32s | $0.000163 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.23s | $0.000162 |
