# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0441 | 2.75s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.31s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 2.75s | $0.003468 |
| real-donor-export | yes | P2 | software | 0.68 | 2.77s | $0.00297 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 3.63s | $0.003996 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.3s | $0.003549 |
| calm-phish-click | yes | P1 | security | 0.75 | 2.67s | $0.003345 |
| quiet-security-tell | yes | P2 | security | 0.6 | 6.47s | $0.008337 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.55s | $0.003195 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.21s | $0.00249 |
| everything-down | yes | P1 | outage | 0.85 | 2.58s | $0.002853 |
| vague-slowness | yes | P4 | software | 0.6 | 2.68s | $0.003183 |
| ransom-note | yes | P1 | security | 0.97 | 2.45s | $0.003102 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.22s | $0.003648 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.96s | $0.000199 |
| real-donor-export | yes | P1 | software | 0.9 | 1.25s | $0.000168 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.31s | $0.000181 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.48s | $0.000246 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.74s | $0.000195 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.63s | $0.000188 |
| vip-lockout | yes | P2 | access | 0.9 | 1.77s | $0.00018 |
| routine-onboarding | yes | P4 | access | 0.95 | 1.22s | $0.000158 |
| everything-down | yes | P1 | outage | 0.95 | 1.19s | $0.000164 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.21s | $0.000164 |
| ransom-note | yes | P1 | security | 0.9 | 1.19s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.11s | $0.000162 |
