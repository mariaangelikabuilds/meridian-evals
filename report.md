# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0409 | 2.82s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.66s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 2.56s | $0.003558 |
| real-donor-export | yes | P2 | software | 0.7 | 2.11s | $0.00303 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.85s | $0.003516 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.47s | $0.003699 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.1s | $0.003885 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.69s | $0.004377 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.53s | $0.00318 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.07s | $0.002655 |
| everything-down | yes | P1 | outage | 0.88 | 2.14s | $0.002763 |
| vague-slowness | yes | P4 | software | 0.55 | 1.99s | $0.002928 |
| ransom-note | yes | P1 | security | 0.97 | 2.82s | $0.002967 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.44s | $0.004308 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.33s | $0.000214 |
| real-donor-export | yes | P2 | software | 0.9 | 1.82s | $0.00021 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.58s | $0.000174 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.68s | $0.000216 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.28s | $0.000163 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.74s | $0.000208 |
| vip-lockout | yes | P2 | access | 0.9 | 1.69s | $0.000196 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.45s | $0.000157 |
| everything-down | yes | P1 | outage | 0.95 | 1.38s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.52s | $0.000167 |
| ransom-note | yes | P1 | security | 0.95 | 1.65s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.66s | $0.000178 |
