# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0395 | 2.43s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.11s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.69s | $0.004398 |
| real-donor-export | yes | P2 | software | 0.72 | 1.82s | $0.002805 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.37s | $0.003156 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.8s | $0.003579 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.86s | $0.00372 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.0s | $0.003837 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.43s | $0.003225 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.15s | $0.00264 |
| everything-down | yes | P1 | outage | 0.9 | 1.91s | $0.002808 |
| vague-slowness | yes | P4 | software | 0.55 | 1.96s | $0.003078 |
| ransom-note | yes | P1 | security | 0.97 | 2.02s | $0.002757 |
| after-hours-badge | yes | P2 | security | 0.72 | 2.44s | $0.003453 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 6.48s | $0.000199 |
| real-donor-export | yes | P2 | software | 0.9 | 1.08s | $0.000194 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 0.99s | $0.000179 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.14s | $0.000229 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.95s | $0.000163 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.29s | $0.000186 |
| vip-lockout | yes | P2 | access | 0.9 | 1.11s | $0.000201 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.18s | $0.000166 |
| everything-down | yes | P1 | outage | 1 | 1.08s | $0.000153 |
| vague-slowness | yes | P4 | hardware | 0.8 | 1.19s | $0.00017 |
| ransom-note | yes | P1 | security | 0.9 | 1.05s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.07s | $0.000161 |
