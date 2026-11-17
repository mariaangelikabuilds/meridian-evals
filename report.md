# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0423 | 2.78s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.56s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.79s | $0.003468 |
| real-donor-export | yes | P2 | software | 0.72 | 2.78s | $0.00318 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 1.83s | $0.002976 |
| real-night-kiosk | yes | P3 | hardware | 0.62 | 3.46s | $0.004179 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.08s | $0.00372 |
| quiet-security-tell | yes | P2 | security | 0.55 | 4.34s | $0.006192 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.39s | $0.00303 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.9s | $0.00276 |
| everything-down | yes | P1 | network | 0.9 | 2.01s | $0.002853 |
| vague-slowness | yes | P4 | software | 0.55 | 1.86s | $0.002658 |
| ransom-note | yes | P1 | security | 0.98 | 2.28s | $0.002907 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.65s | $0.004368 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.93s | $0.000193 |
| real-donor-export | yes | P2 | software | 0.9 | 1.46s | $0.000195 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.34s | $0.000187 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.56s | $0.000213 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.12s | $0.000156 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.93s | $0.000242 |
| vip-lockout | yes | P2 | access | 0.9 | 1.57s | $0.000207 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.78s | $0.000154 |
| everything-down | yes | P1 | outage | 0.95 | 1.53s | $0.000209 |
| vague-slowness | yes | P4 | hardware | 0.8 | 1.53s | $0.000215 |
| ransom-note | yes | P1 | security | 0.9 | 1.39s | $0.000177 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.62s | $0.000196 |
