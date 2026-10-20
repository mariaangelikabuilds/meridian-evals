# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0411 | 2.65s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.4s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.65s | $0.003453 |
| real-donor-export | yes | P2 | software | 0.72 | 2.3s | $0.003 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.47s | $0.003246 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.14s | $0.003819 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.76s | $0.003375 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.08s | $0.003882 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.67s | $0.00321 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.27s | $0.00258 |
| everything-down | yes | P1 | outage | 0.9 | 2.16s | $0.002733 |
| vague-slowness | yes | P4 | software | 0.6 | 1.99s | $0.002658 |
| ransom-note | yes | P1 | security | 0.98 | 1.91s | $0.002682 |
| after-hours-badge | yes | P2 | security | 0.72 | 5.91s | $0.006453 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.55s | $0.000215 |
| real-donor-export | yes | P2 | software | 0.9 | 1.26s | $0.000181 |
| real-partner-mailbox | yes | P1 | access | 0.95 | 1.2s | $0.000171 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.8s | $0.000277 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.25s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.22s | $0.000208 |
| vip-lockout | yes | P2 | access | 0.9 | 1.88s | $0.000188 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.16s | $0.000155 |
| everything-down | yes | P1 | outage | 1 | 1.03s | $0.000179 |
| vague-slowness | yes | P3 | software | 0.7 | 1.45s | $0.000174 |
| ransom-note | yes | P1 | security | 0.9 | 1.4s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.58s | $0.000201 |
