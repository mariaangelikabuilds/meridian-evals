# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0401 | 2.65s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.62s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.65s | $0.003423 |
| real-donor-export | yes | P2 | software | 0.7 | 2.5s | $0.00303 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.6s | $0.003621 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.83s | $0.003774 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.89s | $0.003435 |
| quiet-security-tell | yes | P2 | security | 0.6 | 2.78s | $0.003522 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.65s | $0.003405 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.16s | $0.002775 |
| everything-down | yes | P1 | outage | 0.9 | 1.96s | $0.002643 |
| vague-slowness | yes | P4 | software | 0.55 | 2.37s | $0.002778 |
| ransom-note | yes | P1 | security | 0.98 | 3.31s | $0.003897 |
| after-hours-badge | yes | P2 | security | 0.75 | 2.89s | $0.003813 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.03s | $0.000209 |
| real-donor-export | yes | P1 | software | 0.95 | 1.37s | $0.000166 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.65s | $0.000174 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.42s | $0.000214 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.23s | $0.000224 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.62s | $0.00022 |
| vip-lockout | yes | P2 | access | 0.9 | 1.66s | $0.000188 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.35s | $0.000184 |
| everything-down | yes | P1 | outage | 1 | 1.47s | $0.000155 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.61s | $0.000218 |
| ransom-note | yes | P1 | security | 0.95 | 1.53s | $0.000156 |
| after-hours-badge | yes | P2 | security | 0.8 | 2.63s | $0.000191 |
