# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0515 | 3.46s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.51s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 8.51s | $0.009513 |
| real-donor-export | yes | P2 | software | 0.7 | 3.68s | $0.002805 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.57s | $0.003246 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.27s | $0.003324 |
| calm-phish-click | yes | P1 | security | 0.85 | 3.02s | $0.00345 |
| quiet-security-tell | yes | P2 | security | 0.6 | 6.13s | $0.006642 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.93s | $0.003375 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.12s | $0.00261 |
| everything-down | yes | P1 | outage | 0.85 | 2.31s | $0.002793 |
| vague-slowness | yes | P4 | software | 0.55 | 2.39s | $0.002913 |
| ransom-note | yes | P1 | security | 0.98 | 3.46s | $0.002967 |
| after-hours-badge | yes | P2 | security | 0.6 | 7.0s | $0.007833 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.34s | $0.00021 |
| real-donor-export | yes | P1 | software | 0.9 | 1.41s | $0.00017 |
| real-partner-mailbox | yes | P1 | access | 0.95 | 1.51s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.66s | $0.00023 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.62s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.35s | $0.000194 |
| vip-lockout | yes | P2 | access | 0.9 | 1.37s | $0.000215 |
| routine-onboarding | yes | P4 | request | 1 | 1.43s | $0.000168 |
| everything-down | yes | P1 | outage | 0.95 | 1.26s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.7 | 2.3s | $0.000169 |
| ransom-note | yes | P1 | security | 0.9 | 1.42s | $0.000184 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.55s | $0.000174 |
