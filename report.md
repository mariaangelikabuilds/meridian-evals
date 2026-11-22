# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0378 | 2.26s | vip-lockout, everything-down | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 0.98s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.34s | $0.003453 |
| real-donor-export | yes | P2 | software | 0.7 | 2.02s | $0.002775 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.15s | $0.003201 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 1.87s | $0.002814 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.34s | $0.003465 |
| quiet-security-tell | yes | P2 | security | 0.65 | 4.57s | $0.005922 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.67s | $0.00366 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.03s | $0.00267 |
| everything-down | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| vague-slowness | yes | P4 | software | 0.55 | 2.26s | $0.002958 |
| ransom-note | yes | P1 | security | 0.98 | 2.1s | $0.002982 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.78s | $0.003858 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.75s | $0.000193 |
| real-donor-export | yes | P2 | software | 0.9 | 0.89s | $0.000173 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 0.96s | $0.000181 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 0.92s | $0.000203 |
| calm-phish-click | yes | P2 | security | 0.8 | 0.98s | $0.00018 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 0.94s | $0.000202 |
| vip-lockout | yes | P2 | access | 0.9 | 0.89s | $0.000177 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.99s | $0.000174 |
| everything-down | yes | P1 | outage | 0.95 | 0.94s | $0.000187 |
| vague-slowness | yes | P4 | software | 0.7 | 1.02s | $0.000196 |
| ransom-note | yes | P1 | security | 0.9 | 0.98s | $0.00018 |
| after-hours-badge | yes | P2 | security | 0.85 | 1.09s | $0.000178 |
