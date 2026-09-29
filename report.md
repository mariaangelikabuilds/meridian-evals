# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0425 | 4.27s | vip-lockout, everything-down | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.39s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 5.01s | $0.003513 |
| real-donor-export | yes | P2 | software | 0.65 | 2.58s | $0.00288 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 6.04s | $0.003156 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.02s | $0.003159 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.75s | $0.003405 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.72s | $0.006372 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 4.23s | $0.002955 |
| routine-onboarding | yes | P4 | access | 0.9 | 6.49s | $0.00258 |
| everything-down | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| vague-slowness | yes | P4 | software | 0.55 | 3.68s | $0.003798 |
| ransom-note | yes | P1 | security | 0.98 | 4.27s | $0.003252 |
| after-hours-badge | yes | P2 | security | 0.72 | 6.95s | $0.007428 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 2.65s | $0.000182 |
| real-donor-export | yes | P1 | software | 0.9 | 1.45s | $0.000186 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.52s | $0.00019 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.7s | $0.000238 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.2s | $0.000169 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.38s | $0.000183 |
| vip-lockout | yes | P2 | access | 0.9 | 1.3s | $0.000174 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.16s | $0.00017 |
| everything-down | yes | P1 | outage | 1 | 1.24s | $0.000174 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.48s | $0.00018 |
| ransom-note | yes | P1 | security | 0.9 | 1.39s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.23s | $0.000202 |
