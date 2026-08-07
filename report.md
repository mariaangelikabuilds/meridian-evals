# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0452 | 4.11s | real-night-kiosk, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 2.82s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 4.65s | $0.003693 |
| real-donor-export | yes | P2 | software | 0.7 | 3.2s | $0.00309 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 7.59s | $0.007416 |
| real-night-kiosk | NO: error (Unterminated string starting at: line 1 column 603 (char 602) | - | - | 0 | 0s | $0 |
| calm-phish-click | yes | P1 | security | 0.75 | 4.11s | $0.00306 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.49s | $0.005772 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 5.01s | $0.003465 |
| routine-onboarding | yes | P3 | access | 0.9 | 2.99s | $0.00279 |
| everything-down | yes | P1 | outage | 0.85 | 3.72s | $0.002808 |
| vague-slowness | yes | P4 | software | 0.6 | 3.96s | $0.003138 |
| ransom-note | yes | P1 | security | 0.98 | 3.85s | $0.002772 |
| after-hours-badge | yes | P2 | security | 0.72 | 7.65s | $0.007158 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.21s | $0.00019 |
| real-donor-export | yes | P1 | software | 0.9 | 2.61s | $0.000181 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 2.73s | $0.00019 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.53s | $0.000208 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.82s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.65s | $0.000231 |
| vip-lockout | yes | P2 | access | 0.9 | 2.87s | $0.000202 |
| routine-onboarding | yes | P4 | request | 0.95 | 15.62s | $0.000147 |
| everything-down | yes | P1 | outage | 0.95 | 2.89s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.7 | 3.94s | $0.000222 |
| ransom-note | yes | P1 | security | 1 | 2.19s | $0.00016 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.33s | $0.000177 |
