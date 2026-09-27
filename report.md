# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.043 | 2.77s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.13s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.95s | $0.003873 |
| real-donor-export | yes | P2 | software | 0.65 | 2.81s | $0.002925 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.56s | $0.003216 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.75s | $0.003429 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.69s | $0.00321 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.75s | $0.007092 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.59s | $0.00318 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.33s | $0.00276 |
| everything-down | yes | P1 | outage | 0.9 | 3.11s | $0.003318 |
| vague-slowness | yes | P4 | software | 0.6 | 2.77s | $0.002958 |
| ransom-note | yes | P1 | security | 0.98 | 2.51s | $0.002952 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.52s | $0.004068 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.6s | $0.000201 |
| real-donor-export | yes | P1 | software | 0.9 | 1.13s | $0.000184 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.13s | $0.000198 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.01s | $0.0002 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.01s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 0.98s | $0.000181 |
| vip-lockout | yes | P2 | access | 0.9 | 1.25s | $0.000183 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.86s | $0.000166 |
| everything-down | yes | P1 | outage | 0.9 | 1.04s | $0.000193 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.01s | $0.00017 |
| ransom-note | yes | P1 | security | 0.9 | 1.3s | $0.000187 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.23s | $0.000207 |
