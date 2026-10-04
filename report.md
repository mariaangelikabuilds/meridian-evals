# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0407 | 2.41s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0021 | 1.39s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.59s | $0.003603 |
| real-donor-export | yes | P2 | software | 0.65 | 2.41s | $0.00279 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.39s | $0.003276 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.73s | $0.003354 |
| calm-phish-click | yes | P2 | security | 0.85 | 2.59s | $0.00342 |
| quiet-security-tell | yes | P2 | security | 0.6 | 4.54s | $0.006612 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.18s | $0.003255 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.62s | $0.00255 |
| everything-down | yes | P1 | network | 0.88 | 1.82s | $0.002718 |
| vague-slowness | yes | P4 | software | 0.6 | 2.22s | $0.002868 |
| ransom-note | yes | P1 | security | 0.98 | 1.93s | $0.002607 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.78s | $0.003693 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.98s | $0.000188 |
| real-donor-export | yes | P2 | software | 0.9 | 1.08s | $0.000139 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.34s | $0.000178 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.77s | $0.000214 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.39s | $0.000179 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.29s | $0.000196 |
| vip-lockout | yes | P2 | access | 0.9 | 1.67s | $0.000158 |
| routine-onboarding | yes | P4 | request | 1 | 4.54s | $0.000152 |
| everything-down | yes | P1 | outage | 0.95 | 1.31s | $0.000182 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.34s | $0.000174 |
| ransom-note | yes | P1 | security | 0.95 | 1.42s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.85 | 1.2s | $0.000182 |
