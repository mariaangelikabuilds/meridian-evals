# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0326 | 2.59s | calm-phish-click, vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.1s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.77s | $0.003513 |
| real-donor-export | yes | P2 | software | 0.7 | 2.05s | $0.00285 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.49s | $0.003291 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.82s | $0.003504 |
| calm-phish-click | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.31s | $0.004137 |
| vip-lockout | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.59s | $0.002895 |
| everything-down | yes | P1 | outage | 0.9 | 2.68s | $0.002958 |
| vague-slowness | yes | P4 | software | 0.55 | 1.73s | $0.002508 |
| ransom-note | yes | P1 | security | 0.97 | 3.22s | $0.003297 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.48s | $0.003618 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.85 | 2.41s | $0.00021 |
| real-donor-export | yes | P2 | software | 0.9 | 1.14s | $0.000213 |
| real-partner-mailbox | known gap | P2 | email | 0.9 | 1.03s | $0.000198 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.02s | $0.000219 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.1s | $0.000208 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.16s | $0.000188 |
| vip-lockout | yes | P2 | access | 0.9 | 1.17s | $0.000198 |
| routine-onboarding | yes | P4 | access | 0.9 | 0.9s | $0.000171 |
| everything-down | yes | P1 | outage | 0.95 | 1.09s | $0.000169 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.22s | $0.000214 |
| ransom-note | yes | P1 | security | 0.9 | 0.97s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.85 | 1.05s | $0.000188 |
