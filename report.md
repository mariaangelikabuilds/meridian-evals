# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0382 | 2.74s | vip-lockout, routine-onboarding | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.45s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 3.06s | $0.003858 |
| real-donor-export | yes | P2 | software | 0.65 | 2.36s | $0.00297 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.77s | $0.003261 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.75s | $0.003849 |
| calm-phish-click | yes | P1 | security | 0.85 | 2.47s | $0.00312 |
| quiet-security-tell | yes | P2 | security | 0.6 | 4.84s | $0.005937 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.74s | $0.003465 |
| routine-onboarding | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| everything-down | yes | P1 | outage | 0.85 | 2.3s | $0.002748 |
| vague-slowness | yes | P4 | software | 0.55 | 2.49s | $0.002988 |
| ransom-note | yes | P1 | security | 0.98 | 1.88s | $0.002607 |
| after-hours-badge | yes | P2 | security | 0.62 | 2.78s | $0.003348 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.31s | $0.000207 |
| real-donor-export | yes | P2 | software | 0.9 | 1.54s | $0.000184 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.17s | $0.00019 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.45s | $0.000248 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.19s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.67s | $0.000234 |
| vip-lockout | yes | P2 | access | 0.9 | 1.21s | $0.000199 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.31s | $0.000168 |
| everything-down | yes | P1 | outage | 0.95 | 1.17s | $0.000176 |
| vague-slowness | yes | P4 | hardware | 0.7 | 1.45s | $0.000191 |
| ransom-note | yes | P1 | security | 0.95 | 1.02s | $0.000152 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.25s | $0.000169 |
