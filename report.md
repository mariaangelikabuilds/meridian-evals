# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0448 | 3.86s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.9s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 4.28s | $0.003903 |
| real-donor-export | yes | P2 | software | 0.7 | 3.53s | $0.00315 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.77s | $0.003096 |
| real-night-kiosk | yes | P2 | hardware | 0.62 | 4.49s | $0.004749 |
| calm-phish-click | yes | P1 | security | 0.75 | 4.23s | $0.00327 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.78s | $0.007287 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 3.82s | $0.003495 |
| routine-onboarding | yes | P4 | access | 0.9 | 3.35s | $0.002565 |
| everything-down | yes | P1 | outage | 0.9 | 2.78s | $0.002973 |
| vague-slowness | yes | P4 | software | 0.55 | 3.86s | $0.003438 |
| ransom-note | yes | P1 | security | 0.98 | 3.6s | $0.002877 |
| after-hours-badge | yes | P2 | security | 0.7 | 4.16s | $0.004008 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.62s | $0.000214 |
| real-donor-export | yes | P2 | software | 0.9 | 1.9s | $0.000197 |
| real-partner-mailbox | yes | P1 | software | 0.9 | 2.34s | $0.000198 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 3.63s | $0.000203 |
| calm-phish-click | yes | P2 | security | 0.8 | 2.54s | $0.000179 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.51s | $0.000202 |
| vip-lockout | yes | P2 | access | 0.9 | 1.29s | $0.000182 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.72s | $0.000149 |
| everything-down | yes | P1 | outage | 0.95 | 1.58s | $0.000187 |
| vague-slowness | yes | P3 | software | 0.8 | 1.47s | $0.000178 |
| ransom-note | yes | P1 | security | 1 | 1.54s | $0.000161 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.21s | $0.000196 |
