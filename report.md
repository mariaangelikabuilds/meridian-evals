# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.051 | 2.73s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.14s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P2 | outage | 0.6 | 7.16s | $0.008928 |
| real-donor-export | yes | P2 | software | 0.72 | 1.96s | $0.00297 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.73s | $0.003561 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.61s | $0.004404 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.37s | $0.00312 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.0s | $0.006207 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.57s | $0.003405 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.07s | $0.002685 |
| everything-down | yes | P1 | network | 0.85 | 4.78s | $0.005883 |
| vague-slowness | yes | P4 | software | 0.55 | 2.08s | $0.002763 |
| ransom-note | yes | P1 | security | 0.98 | 2.27s | $0.002787 |
| after-hours-badge | yes | P2 | security | 0.6 | 3.18s | $0.004293 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.77s | $0.00021 |
| real-donor-export | yes | P2 | software | 0.9 | 1.12s | $0.000187 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.14s | $0.000186 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.37s | $0.000227 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.34s | $0.000214 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.31s | $0.00022 |
| vip-lockout | yes | P2 | access | 0.9 | 1.01s | $0.000182 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.16s | $0.000179 |
| everything-down | yes | P1 | outage | 1 | 1.05s | $0.000179 |
| vague-slowness | yes | P3 | hardware | 0.7 | 0.87s | $0.000185 |
| ransom-note | yes | P1 | security | 0.9 | 1.13s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.13s | $0.000194 |
