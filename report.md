# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0466 | 3.49s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.93s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 4.97s | $0.003348 |
| real-donor-export | yes | P2 | software | 0.65 | 3.0s | $0.00309 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.49s | $0.003276 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.49s | $0.004074 |
| calm-phish-click | yes | P1 | security | 0.85 | 3.62s | $0.00396 |
| quiet-security-tell | yes | P2 | security | 0.6 | 6.15s | $0.007212 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.11s | $0.003615 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.21s | $0.002565 |
| everything-down | yes | P1 | outage | 0.85 | 2.5s | $0.002748 |
| vague-slowness | yes | P4 | software | 0.55 | 2.68s | $0.002793 |
| ransom-note | yes | P1 | security | 0.98 | 2.8s | $0.002697 |
| after-hours-badge | yes | P2 | security | 0.65 | 6.25s | $0.007203 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 6.72s | $0.00018 |
| real-donor-export | yes | P2 | software | 0.9 | 1.68s | $0.000184 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.96s | $0.000195 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.86s | $0.000229 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.55s | $0.000156 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.02s | $0.000191 |
| vip-lockout | yes | P2 | access | 0.9 | 1.62s | $0.000178 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.73s | $0.000133 |
| everything-down | yes | P1 | outage | 0.9 | 1.94s | $0.000177 |
| vague-slowness | yes | P4 | hardware | 0.7 | 1.93s | $0.00019 |
| ransom-note | yes | P1 | security | 0.95 | 1.53s | $0.000168 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.07s | $0.000191 |
