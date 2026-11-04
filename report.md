# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0402 | 2.69s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.71s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.59s | $0.004668 |
| real-donor-export | yes | P2 | software | 0.7 | 2.24s | $0.002745 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.5s | $0.003111 |
| real-night-kiosk | yes | P2 | hardware | 0.62 | 3.25s | $0.004089 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.63s | $0.003105 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.44s | $0.003897 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.69s | $0.003405 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.77s | $0.00252 |
| everything-down | yes | P1 | outage | 0.9 | 2.41s | $0.003138 |
| vague-slowness | yes | P4 | software | 0.55 | 2.69s | $0.003078 |
| ransom-note | yes | P1 | security | 0.97 | 2.22s | $0.002607 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.3s | $0.003798 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.72s | $0.000182 |
| real-donor-export | yes | P1 | software | 0.9 | 1.34s | $0.000176 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.71s | $0.000165 |
| real-night-kiosk | yes | P2 | hardware | 0.85 | 1.48s | $0.0002 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.38s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.45s | $0.000207 |
| vip-lockout | yes | P2 | access | 0.9 | 1.32s | $0.000172 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.64s | $0.000174 |
| everything-down | yes | P1 | outage | 0.9 | 1.74s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.87s | $0.000183 |
| ransom-note | yes | P1 | security | 0.95 | 1.73s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.91s | $0.000191 |
