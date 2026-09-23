# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0434 | 3.35s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.23s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 3.35s | $0.003468 |
| real-donor-export | yes | P2 | software | 0.7 | 2.68s | $0.003105 |
| real-partner-mailbox | yes | P1 | software | 0.85 | 3.47s | $0.003246 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.86s | $0.003594 |
| calm-phish-click | yes | P1 | security | 0.85 | 2.91s | $0.00336 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.43s | $0.006387 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.24s | $0.00291 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.39s | $0.002625 |
| everything-down | yes | P1 | network | 0.85 | 4.39s | $0.005148 |
| vague-slowness | yes | P4 | software | 0.6 | 2.67s | $0.003228 |
| ransom-note | yes | P1 | security | 0.98 | 2.99s | $0.003027 |
| after-hours-badge | yes | P2 | security | 0.6 | 3.6s | $0.003288 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.5s | $0.000209 |
| real-donor-export | yes | P2 | software | 0.9 | 1.28s | $0.000165 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.17s | $0.000192 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.41s | $0.000219 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.14s | $0.000174 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.18s | $0.000196 |
| vip-lockout | yes | P2 | access | 0.9 | 1.31s | $0.000188 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.1s | $0.000157 |
| everything-down | yes | P1 | outage | 0.9 | 1.57s | $0.000184 |
| vague-slowness | yes | P4 | software | 0.8 | 1.23s | $0.000175 |
| ransom-note | yes | P1 | security | 0.9 | 1.22s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.93s | $0.000174 |
