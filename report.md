# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0392 | 2.59s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.69s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 3.12s | $0.003588 |
| real-donor-export | yes | P2 | software | 0.65 | 2.59s | $0.003135 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.78s | $0.003801 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.94s | $0.003804 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.48s | $0.003435 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.41s | $0.003882 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.73s | $0.00321 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.26s | $0.00276 |
| everything-down | yes | P1 | outage | 0.9 | 1.95s | $0.002703 |
| vague-slowness | yes | P4 | software | 0.6 | 2.17s | $0.002568 |
| ransom-note | yes | P1 | security | 0.98 | 2.06s | $0.002832 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.42s | $0.003438 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.12s | $0.000194 |
| real-donor-export | yes | P2 | software | 0.9 | 1.88s | $0.000205 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.45s | $0.000179 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.6s | $0.000206 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.72s | $0.000201 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.69s | $0.000183 |
| vip-lockout | yes | P2 | access | 0.9 | 1.67s | $0.000186 |
| routine-onboarding | yes | P4 | request | 1 | 1.18s | $0.00015 |
| everything-down | yes | P1 | outage | 1 | 1.77s | $0.00016 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.61s | $0.000172 |
| ransom-note | yes | P1 | security | 0.95 | 1.85s | $0.00018 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.49s | $0.000182 |
