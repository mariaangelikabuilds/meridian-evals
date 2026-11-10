# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0442 | 2.32s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.62s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 2.65s | $0.003948 |
| real-donor-export | yes | P2 | software | 0.65 | 2.57s | $0.003165 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.3s | $0.003276 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.62s | $0.004734 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.11s | $0.00288 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.62s | $0.007812 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 1.96s | $0.00294 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.0s | $0.00255 |
| everything-down | yes | P1 | outage | 0.9 | 1.98s | $0.002868 |
| vague-slowness | yes | P4 | software | 0.6 | 1.97s | $0.002823 |
| ransom-note | yes | P1 | security | 0.98 | 2.32s | $0.003117 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.36s | $0.004098 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 4.34s | $0.000193 |
| real-donor-export | yes | P2 | software | 0.9 | 1.11s | $0.000182 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.24s | $0.000176 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.49s | $0.000242 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.39s | $0.000179 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.62s | $0.000215 |
| vip-lockout | yes | P2 | access | 0.9 | 1.07s | $0.000166 |
| routine-onboarding | yes | P4 | request | 0.9 | 2.28s | $0.000149 |
| everything-down | yes | P1 | outage | 1 | 1.48s | $0.000182 |
| vague-slowness | yes | P4 | hardware | 0.7 | 3.02s | $0.00021 |
| ransom-note | yes | P1 | security | 0.95 | 1.93s | $0.000188 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.23s | $0.000202 |
