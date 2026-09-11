# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0411 | 3.37s | vip-lockout, everything-down | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 2.01s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 3.77s | $0.003318 |
| real-donor-export | yes | P2 | software | 0.65 | 4.43s | $0.002985 |
| real-partner-mailbox | yes | P1 | software | 0.85 | 3.49s | $0.003336 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.37s | $0.003834 |
| calm-phish-click | yes | P1 | security | 0.75 | 3.07s | $0.003195 |
| quiet-security-tell | yes | P2 | security | 0.62 | 4.54s | $0.003972 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.51s | $0.00294 |
| routine-onboarding | yes | P4 | access | 0.85 | 1.93s | $0.002595 |
| everything-down | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| vague-slowness | yes | P4 | software | 0.55 | 2.39s | $0.003003 |
| ransom-note | yes | P1 | security | 0.98 | 3.1s | $0.003042 |
| after-hours-badge | yes | P2 | security | 0.6 | 7.93s | $0.008898 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 4.21s | $0.000209 |
| real-donor-export | yes | P1 | software | 0.9 | 1.46s | $0.000174 |
| real-partner-mailbox | yes | P1 | software | 0.9 | 1.64s | $0.00016 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.38s | $0.00024 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.46s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.01s | $0.000218 |
| vip-lockout | yes | P2 | access | 0.9 | 2.04s | $0.000201 |
| routine-onboarding | yes | P4 | request | 0.95 | 2.23s | $0.000182 |
| everything-down | yes | P1 | outage | 1 | 1.86s | $0.000196 |
| vague-slowness | yes | P3 | hardware | 0.7 | 2.08s | $0.000204 |
| ransom-note | yes | P1 | security | 0.95 | 1.76s | $0.000176 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.98s | $0.000178 |
