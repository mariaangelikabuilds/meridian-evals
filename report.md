# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0381 | 2.95s | calm-phish-click, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.3s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.82s | $0.003573 |
| real-donor-export | yes | P2 | software | 0.65 | 2.95s | $0.00279 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 4.71s | $0.003231 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.68s | $0.003864 |
| calm-phish-click | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.52s | $0.006117 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 3.63s | $0.003585 |
| routine-onboarding | yes | P4 | access | 0.9 | 9.26s | $0.00264 |
| everything-down | yes | P1 | outage | 0.88 | 2.94s | $0.003078 |
| vague-slowness | yes | P4 | software | 0.6 | 2.79s | $0.002913 |
| ransom-note | yes | P1 | security | 0.98 | 2.61s | $0.002697 |
| after-hours-badge | yes | P2 | security | 0.72 | 3.84s | $0.003573 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.88s | $0.000204 |
| real-donor-export | yes | P1 | software | 0.9 | 1.43s | $0.000181 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.33s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.37s | $0.000237 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.3s | $0.000179 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.18s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.13s | $0.00019 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.13s | $0.000162 |
| everything-down | yes | P1 | outage | 0.9 | 1.02s | $0.000177 |
| vague-slowness | yes | P4 | software | 0.8 | 1.04s | $0.000186 |
| ransom-note | yes | P1 | security | 0.95 | 1.04s | $0.00018 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.33s | $0.000162 |
