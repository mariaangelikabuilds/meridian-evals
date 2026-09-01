# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.043 | 3.75s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 2.06s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 4.14s | $0.003738 |
| real-donor-export | yes | P2 | software | 0.65 | 3.66s | $0.003165 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 4.7s | $0.004101 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.75s | $0.003549 |
| calm-phish-click | yes | P1 | security | 0.85 | 4.05s | $0.003225 |
| quiet-security-tell | yes | P2 | security | 0.6 | 6.6s | $0.006432 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 4.15s | $0.00345 |
| routine-onboarding | yes | P4 | access | 0.9 | 3.59s | $0.00264 |
| everything-down | yes | P1 | outage | 0.9 | 3.33s | $0.002928 |
| vague-slowness | yes | P4 | software | 0.55 | 3.72s | $0.003438 |
| ransom-note | yes | P1 | security | 0.98 | 3.32s | $0.002577 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.74s | $0.003783 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.3s | $0.000198 |
| real-donor-export | yes | P2 | software | 0.9 | 2.11s | $0.000214 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 2.0s | $0.000174 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.46s | $0.000219 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.06s | $0.000192 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 2.06s | $0.000208 |
| vip-lockout | yes | P2 | access | 0.9 | 2.35s | $0.000199 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.71s | $0.000146 |
| everything-down | yes | P1 | outage | 0.9 | 2.06s | $0.000195 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.59s | $0.000162 |
| ransom-note | yes | P1 | security | 1 | 1.98s | $0.000169 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.89s | $0.00017 |
