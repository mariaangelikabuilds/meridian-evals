# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.036 | 3.2s | real-night-kiosk, vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 2.19s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.74s | $0.003333 |
| real-donor-export | yes | P2 | software | 0.7 | 3.87s | $0.00294 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.67s | $0.003216 |
| real-night-kiosk | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| calm-phish-click | yes | P1 | security | 0.85 | 3.01s | $0.003375 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.51s | $0.005907 |
| vip-lockout | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| routine-onboarding | yes | P4 | access | 0.85 | 2.26s | $0.002625 |
| everything-down | yes | P1 | outage | 0.85 | 2.23s | $0.002643 |
| vague-slowness | yes | P4 | software | 0.55 | 2.28s | $0.002763 |
| ransom-note | yes | P1 | security | 0.98 | 3.2s | $0.002802 |
| after-hours-badge | yes | P2 | security | 0.65 | 5.63s | $0.006378 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.47s | $0.000225 |
| real-donor-export | yes | P2 | software | 0.9 | 2.29s | $0.000189 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.85s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.22s | $0.000206 |
| calm-phish-click | yes | P2 | security | 0.8 | 2.1s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.99s | $0.000212 |
| vip-lockout | yes | P2 | access | 0.9 | 1.98s | $0.00018 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.62s | $0.000155 |
| everything-down | yes | P1 | outage | 1 | 2.26s | $0.000156 |
| vague-slowness | yes | P4 | hardware | 0.8 | 2.17s | $0.000207 |
| ransom-note | yes | P1 | security | 0.9 | 2.67s | $0.000168 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.19s | $0.000182 |
