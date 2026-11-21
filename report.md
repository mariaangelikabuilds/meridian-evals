# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0398 | 2.59s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.08s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 2.8s | $0.003873 |
| real-donor-export | yes | P2 | software | 0.75 | 2.44s | $0.003285 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.61s | $0.003621 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.73s | $0.003834 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.59s | $0.003465 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.5s | $0.003867 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.39s | $0.003045 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.85s | $0.002625 |
| everything-down | yes | P1 | outage | 0.9 | 1.54s | $0.002373 |
| vague-slowness | yes | P4 | software | 0.55 | 2.03s | $0.003033 |
| ransom-note | yes | P1 | security | 0.97 | 2.0s | $0.002907 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.24s | $0.003873 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.38s | $0.000204 |
| real-donor-export | yes | P1 | software | 0.9 | 1.21s | $0.000174 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 0.97s | $0.000176 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.08s | $0.00023 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.97s | $0.00018 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.4s | $0.000207 |
| vip-lockout | yes | P2 | access | 0.9 | 1.22s | $0.00018 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.05s | $0.000174 |
| everything-down | yes | P1 | outage | 0.95 | 1.0s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.1s | $0.000175 |
| ransom-note | yes | P1 | security | 0.9 | 1.0s | $0.000168 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.84s | $0.000177 |
