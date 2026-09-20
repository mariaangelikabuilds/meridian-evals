# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0431 | 2.98s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.58s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.82s | $0.003348 |
| real-donor-export | yes | P2 | software | 0.68 | 3.04s | $0.003345 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.9s | $0.003336 |
| real-night-kiosk | yes | P3 | hardware | 0.62 | 3.52s | $0.003984 |
| calm-phish-click | yes | P1 | security | 0.75 | 4.0s | $0.00447 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.62s | $0.006492 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.98s | $0.00294 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.2s | $0.00261 |
| everything-down | yes | P1 | outage | 0.9 | 2.89s | $0.002958 |
| vague-slowness | yes | P4 | software | 0.6 | 2.28s | $0.002508 |
| ransom-note | yes | P1 | security | 0.98 | 2.51s | $0.003132 |
| after-hours-badge | yes | P2 | security | 0.7 | 3.4s | $0.004008 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.23s | $0.000183 |
| real-donor-export | yes | P1 | software | 0.9 | 1.9s | $0.000173 |
| real-partner-mailbox | known gap | P1 | email | 0.9 | 1.72s | $0.00024 |
| real-night-kiosk | yes | P2 | hardware | 0.8 | 1.58s | $0.000205 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.23s | $0.000172 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.62s | $0.000204 |
| vip-lockout | yes | P2 | access | 0.9 | 1.33s | $0.000167 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.22s | $0.000147 |
| everything-down | yes | P1 | outage | 0.95 | 1.43s | $0.000176 |
| vague-slowness | yes | P4 | hardware | 0.8 | 1.43s | $0.00018 |
| ransom-note | yes | P1 | security | 0.95 | 1.28s | $0.00016 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.7s | $0.000169 |
