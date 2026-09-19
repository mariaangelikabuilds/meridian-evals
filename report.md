# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0405 | 3.15s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.36s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 2.86s | $0.003348 |
| real-donor-export | yes | P2 | software | 0.65 | 4.43s | $0.002805 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.7s | $0.003201 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 5.83s | $0.004359 |
| calm-phish-click | yes | P1 | security | 0.75 | 3.17s | $0.00348 |
| quiet-security-tell | yes | P2 | security | 0.55 | 4.45s | $0.004647 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.15s | $0.003615 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.19s | $0.002685 |
| everything-down | yes | P1 | outage | 0.85 | 2.69s | $0.003138 |
| vague-slowness | yes | P4 | software | 0.55 | 2.77s | $0.002808 |
| ransom-note | yes | P1 | security | 0.98 | 2.3s | $0.002667 |
| after-hours-badge | yes | P2 | security | 0.6 | 3.16s | $0.003708 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.11s | $0.000225 |
| real-donor-export | yes | P2 | software | 0.95 | 1.43s | $0.000179 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.25s | $0.000192 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.92s | $0.000202 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.51s | $0.000198 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.36s | $0.000196 |
| vip-lockout | yes | P2 | access | 0.9 | 1.28s | $0.00018 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.1s | $0.000155 |
| everything-down | yes | P1 | outage | 0.95 | 1.08s | $0.000174 |
| vague-slowness | yes | P3 | software | 0.7 | 1.36s | $0.000207 |
| ransom-note | yes | P1 | security | 0.9 | 1.08s | $0.000161 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.22s | $0.000201 |
