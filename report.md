# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0399 | 2.62s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.5s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.46s | $0.003483 |
| real-donor-export | yes | P2 | software | 0.7 | 2.27s | $0.002745 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.31s | $0.003246 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.08s | $0.004509 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.0s | $0.00324 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.27s | $0.004092 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.3s | $0.00318 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.99s | $0.002625 |
| everything-down | yes | P1 | outage | 0.9 | 2.9s | $0.003108 |
| vague-slowness | yes | P4 | software | 0.6 | 2.62s | $0.003243 |
| ransom-note | yes | P1 | security | 0.98 | 2.08s | $0.002892 |
| after-hours-badge | yes | P2 | security | 0.72 | 2.85s | $0.003498 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P2 | network | 0.8 | 2.89s | $0.000202 |
| real-donor-export | yes | P1 | software | 0.9 | 1.39s | $0.000187 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.37s | $0.0002 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.48s | $0.000222 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.57s | $0.000188 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.43s | $0.000192 |
| vip-lockout | yes | P2 | access | 0.9 | 1.57s | $0.000185 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.44s | $0.000141 |
| everything-down | yes | P1 | outage | 0.95 | 1.28s | $0.000188 |
| vague-slowness | yes | P4 | software | 0.8 | 1.67s | $0.000183 |
| ransom-note | yes | P1 | security | 0.9 | 1.5s | $0.000176 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.56s | $0.000178 |
