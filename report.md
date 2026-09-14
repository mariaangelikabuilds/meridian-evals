# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0479 | 3.19s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0024 | 1.29s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 2.94s | $0.003573 |
| real-donor-export | yes | P2 | software | 0.65 | 3.1s | $0.002985 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.59s | $0.003276 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 4.19s | $0.005064 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.31s | $0.00354 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.94s | $0.006837 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.42s | $0.00345 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.33s | $0.00258 |
| everything-down | yes | P1 | outage | 0.88 | 3.19s | $0.003453 |
| vague-slowness | yes | P4 | software | 0.55 | 2.51s | $0.003198 |
| ransom-note | yes | P1 | security | 0.98 | 3.08s | $0.002757 |
| after-hours-badge | yes | P2 | security | 0.7 | 6.04s | $0.007203 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.74s | $0.000233 |
| real-donor-export | yes | P2 | software | 0.9 | 1.99s | $0.000202 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 2.55s | $0.000264 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.17s | $0.00023 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.94s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.12s | $0.000205 |
| vip-lockout | yes | P2 | access | 0.9 | 1.06s | $0.000186 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.3s | $0.00016 |
| everything-down | yes | P1 | outage | 1 | 1.29s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.46s | $0.000231 |
| ransom-note | yes | P1 | security | 0.95 | 1.22s | $0.000169 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.22s | $0.000194 |
