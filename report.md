# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0415 | 2.98s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.33s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P2 | outage | 0.6 | 6.62s | $0.008508 |
| real-donor-export | yes | P2 | software | 0.7 | 4.29s | $0.00285 |
| real-partner-mailbox | known gap (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.93s | $0.003924 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.98s | $0.00351 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.73s | $0.004062 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.14s | $0.003105 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.03s | $0.00255 |
| everything-down | yes | P1 | outage | 0.9 | 2.31s | $0.002718 |
| vague-slowness | yes | P4 | software | 0.6 | 2.53s | $0.003018 |
| ransom-note | yes | P1 | security | 0.98 | 2.57s | $0.003087 |
| after-hours-badge | yes | P2 | security | 0.72 | 4.2s | $0.004173 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.72s | $0.000193 |
| real-donor-export | yes | P1 | software | 0.9 | 1.33s | $0.000154 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.18s | $0.000181 |
| real-night-kiosk | yes | P2 | hardware | 0.8 | 1.44s | $0.000246 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.38s | $0.000187 |
| quiet-security-tell | yes | P2 | hardware | 0.85 | 1.61s | $0.000213 |
| vip-lockout | yes | P2 | access | 0.95 | 1.19s | $0.000172 |
| routine-onboarding | yes | P4 | request | 1 | 1.42s | $0.000133 |
| everything-down | yes | P1 | outage | 0.95 | 1.19s | $0.000176 |
| vague-slowness | yes | P3 | software | 0.7 | 1.28s | $0.000185 |
| ransom-note | yes | P1 | security | 0.95 | 1.08s | $0.000185 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.22s | $0.000186 |
