# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0381 | 2.79s | vip-lockout, ransom-note | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.18s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.79s | $0.003843 |
| real-donor-export | yes | P2 | software | 0.65 | 2.11s | $0.00294 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.86s | $0.003771 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.32s | $0.004254 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.73s | $0.00366 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.57s | $0.004167 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.83s | $0.003405 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.73s | $0.0024 |
| everything-down | yes | P1 | outage | 0.9 | 1.87s | $0.002553 |
| vague-slowness | yes | P4 | software | 0.55 | 2.62s | $0.003333 |
| ransom-note | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| after-hours-badge | yes | P2 | security | 0.6 | 3.19s | $0.003813 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.0s | $0.000231 |
| real-donor-export | yes | P2 | software | 0.9 | 1.24s | $0.000178 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.02s | $0.000179 |
| real-night-kiosk | yes | P3 | hardware | 0.9 | 1.15s | $0.000216 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.17s | $0.000171 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.36s | $0.000232 |
| vip-lockout | yes | P2 | software | 0.9 | 1.71s | $0.000198 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.09s | $0.000163 |
| everything-down | yes | P1 | outage | 1 | 1.59s | $0.000192 |
| vague-slowness | yes | P3 | software | 0.7 | 1.16s | $0.000183 |
| ransom-note | yes | P1 | security | 0.9 | 0.94s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.18s | $0.000194 |
