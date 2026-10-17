# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0353 | 2.62s | real-imaging-down, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.32s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-donor-export | yes | P2 | software | 0.72 | 2.62s | $0.00309 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.79s | $0.003201 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.46s | $0.003054 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.84s | $0.00348 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.26s | $0.003987 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.27s | $0.003225 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.99s | $0.002625 |
| everything-down | yes | P1 | outage | 0.9 | 1.64s | $0.002493 |
| vague-slowness | yes | P4 | hardware | 0.55 | 2.73s | $0.003393 |
| ransom-note | yes | P1 | security | 0.97 | 2.45s | $0.002997 |
| after-hours-badge | yes | P2 | security | 0.72 | 2.93s | $0.003768 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.81s | $0.000239 |
| real-donor-export | yes | P2 | software | 0.9 | 1.41s | $0.000206 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.16s | $0.000176 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.28s | $0.000182 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.32s | $0.000193 |
| quiet-security-tell | yes | P2 | hardware | 0.85 | 1.79s | $0.000197 |
| vip-lockout | yes | P2 | access | 0.9 | 1.27s | $0.000182 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.02s | $0.000138 |
| everything-down | yes | P1 | outage | 0.95 | 1.49s | $0.000182 |
| vague-slowness | yes | P4 | hardware | 0.8 | 1.43s | $0.000215 |
| ransom-note | yes | P1 | security | 0.9 | 1.25s | $0.000176 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.16s | $0.000169 |
