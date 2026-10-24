# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0395 | 2.72s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.37s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.72s | $0.003543 |
| real-donor-export | yes | P2 | software | 0.7 | 2.28s | $0.00282 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.45s | $0.003426 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.73s | $0.003594 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.43s | $0.00396 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.23s | $0.004002 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.22s | $0.003615 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.94s | $0.002715 |
| everything-down | yes | P1 | outage | 0.9 | 1.81s | $0.002478 |
| vague-slowness | yes | P4 | software | 0.55 | 2.18s | $0.002928 |
| ransom-note | yes | P1 | security | 0.98 | 1.97s | $0.002607 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.65s | $0.003768 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.97s | $0.000194 |
| real-donor-export | yes | P2 | software | 0.9 | 1.32s | $0.000174 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.45s | $0.000179 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.74s | $0.000216 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.32s | $0.000177 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.18s | $0.000191 |
| vip-lockout | yes | P2 | access | 0.9 | 1.49s | $0.000172 |
| routine-onboarding | yes | P4 | request | 1 | 1.07s | $0.000152 |
| everything-down | yes | P1 | outage | 0.95 | 1.37s | $0.00018 |
| vague-slowness | yes | P4 | software | 0.8 | 1.39s | $0.000202 |
| ransom-note | yes | P1 | security | 0.9 | 1.34s | $0.00018 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.32s | $0.000177 |
