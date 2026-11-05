# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.038 | 2.36s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.47s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.82s | $0.003453 |
| real-donor-export | yes | P2 | software | 0.7 | 2.36s | $0.00282 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.19s | $0.003276 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.54s | $0.004329 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.63s | $0.003285 |
| quiet-security-tell | yes | P2 | security | 0.6 | 2.66s | $0.003357 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.36s | $0.003 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.99s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 2.01s | $0.002763 |
| vague-slowness | yes | P4 | software | 0.55 | 1.85s | $0.002523 |
| ransom-note | yes | P1 | security | 0.98 | 2.35s | $0.002952 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.88s | $0.003633 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.8s | $0.00022 |
| real-donor-export | yes | P1 | software | 0.9 | 1.47s | $0.000168 |
| real-partner-mailbox | yes | P1 | software | 0.9 | 1.33s | $0.000176 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.37s | $0.00021 |
| calm-phish-click | yes | P2 | security | 0.8 | 2.3s | $0.000177 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.61s | $0.000192 |
| vip-lockout | yes | P2 | access | 0.9 | 1.65s | $0.000194 |
| routine-onboarding | yes | P4 | request | 0.95 | 2.89s | $0.00016 |
| everything-down | yes | P1 | outage | 0.95 | 1.44s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.28s | $0.000161 |
| ransom-note | yes | P1 | security | 0.9 | 1.14s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.33s | $0.000169 |
