# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.04 | 2.81s | real-donor-export, vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.41s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 3.92s | $0.003768 |
| real-donor-export | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 2.65s | $0.003111 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.65s | $0.003834 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.81s | $0.00318 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.5s | $0.005877 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.67s | $0.00291 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.22s | $0.002595 |
| everything-down | yes | P1 | outage | 0.9 | 2.35s | $0.002748 |
| vague-slowness | yes | P4 | software | 0.6 | 2.55s | $0.003183 |
| ransom-note | yes | P1 | security | 0.98 | 3.57s | $0.003147 |
| after-hours-badge | yes | P2 | security | 0.75 | 5.52s | $0.005628 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.95 | 2.51s | $0.000185 |
| real-donor-export | yes | P1 | software | 0.9 | 1.18s | $0.000181 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.33s | $0.000192 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.2s | $0.000237 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.23s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.38s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.22s | $0.000169 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.41s | $0.000162 |
| everything-down | yes | P1 | outage | 0.9 | 1.87s | $0.000184 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.93s | $0.000206 |
| ransom-note | yes | P1 | security | 0.9 | 1.72s | $0.000193 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.28s | $0.00019 |
