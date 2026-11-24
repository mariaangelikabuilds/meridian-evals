# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0391 | 2.51s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.96s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 2.51s | $0.003963 |
| real-donor-export | yes | P2 | software | 0.7 | 2.2s | $0.002745 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.49s | $0.003291 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.99s | $0.003609 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.96s | $0.003855 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.5s | $0.004152 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.59s | $0.00318 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.09s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 2.02s | $0.002448 |
| vague-slowness | yes | P4 | software | 0.55 | 2.13s | $0.002868 |
| ransom-note | yes | P1 | security | 0.97 | 2.05s | $0.002667 |
| after-hours-badge | yes | P2 | security | 0.72 | 3.06s | $0.003633 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.77s | $0.000206 |
| real-donor-export | yes | P1 | software | 0.9 | 1.71s | $0.000192 |
| real-partner-mailbox | yes | P1 | software | 0.9 | 1.96s | $0.000173 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.81s | $0.000206 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.33s | $0.000169 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.53s | $0.0002 |
| vip-lockout | yes | P2 | access | 0.9 | 2.31s | $0.000201 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.2s | $0.000176 |
| everything-down | yes | P1 | outage | 0.95 | 2.15s | $0.000163 |
| vague-slowness | yes | P3 | hardware | 0.7 | 2.03s | $0.00021 |
| ransom-note | yes | P1 | security | 0.95 | 1.16s | $0.000174 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.07s | $0.000183 |
