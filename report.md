# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0426 | 4.06s | vip-lockout, everything-down | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.64s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.8s | $0.003408 |
| real-donor-export | yes | P2 | software | 0.65 | 4.06s | $0.003375 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 4.42s | $0.003306 |
| real-night-kiosk | yes | P2 | hardware | 0.62 | 3.32s | $0.003804 |
| calm-phish-click | yes | P1 | security | 0.85 | 2.95s | $0.003405 |
| quiet-security-tell | yes | P2 | security | 0.62 | 8.31s | $0.008202 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 4.37s | $0.003285 |
| routine-onboarding | yes | P4 | access | 0.9 | 3.52s | $0.0027 |
| everything-down | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| vague-slowness | yes | P4 | software | 0.55 | 4.72s | $0.003693 |
| ransom-note | yes | P1 | security | 0.98 | 3.98s | $0.003042 |
| after-hours-badge | yes | P2 | security | 0.65 | 5.22s | $0.004353 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.98s | $0.000202 |
| real-donor-export | yes | P2 | software | 0.9 | 1.54s | $0.000184 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.64s | $0.000195 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.45s | $0.000238 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.48s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.61s | $0.000192 |
| vip-lockout | yes | P2 | access | 0.9 | 1.66s | $0.000175 |
| routine-onboarding | yes | P4 | access | 1 | 1.54s | $0.000184 |
| everything-down | yes | P1 | outage | 0.9 | 1.56s | $0.000176 |
| vague-slowness | yes | P4 | software | 0.8 | 3.8s | $0.000193 |
| ransom-note | yes | P1 | security | 1 | 1.52s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.82s | $0.000164 |
