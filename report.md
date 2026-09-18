# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0449 | 3.42s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 2.16s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 3.26s | $0.003738 |
| real-donor-export | yes | P2 | software | 0.65 | 3.42s | $0.00303 |
| real-partner-mailbox | yes | P1 | software | 0.85 | 2.79s | $0.002946 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.22s | $0.003984 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.79s | $0.0039 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.78s | $0.007527 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.37s | $0.00336 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.51s | $0.00255 |
| everything-down | yes | P1 | outage | 0.9 | 2.59s | $0.002703 |
| vague-slowness | yes | P4 | software | 0.55 | 3.48s | $0.003303 |
| ransom-note | yes | P1 | security | 0.98 | 3.7s | $0.003867 |
| after-hours-badge | yes | P2 | security | 0.72 | 3.83s | $0.003978 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.92s | $0.000207 |
| real-donor-export | yes | P1 | software | 0.9 | 2.08s | $0.000173 |
| real-partner-mailbox | yes | P1 | access | 0.95 | 2.06s | $0.000178 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.31s | $0.000234 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.11s | $0.000214 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.56s | $0.0002 |
| vip-lockout | yes | P2 | access | 0.9 | 2.2s | $0.000185 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.64s | $0.000136 |
| everything-down | yes | P1 | outage | 0.95 | 2.15s | $0.00018 |
| vague-slowness | yes | P3 | hardware | 0.7 | 2.02s | $0.000186 |
| ransom-note | yes | P1 | security | 0.95 | 2.64s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.16s | $0.000185 |
