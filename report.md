# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0376 | 2.26s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.08s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.58s | $0.003678 |
| real-donor-export | yes | P2 | software | 0.7 | 2.17s | $0.003 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.05s | $0.003141 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.09s | $0.002814 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.26s | $0.003075 |
| quiet-security-tell | yes | P2 | security | 0.6 | 2.82s | $0.003492 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.5s | $0.00336 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.14s | $0.002685 |
| everything-down | yes | P1 | network | 0.85 | 1.73s | $0.002763 |
| vague-slowness | yes | P4 | software | 0.55 | 2.31s | $0.003258 |
| ransom-note | yes | P1 | security | 0.98 | 1.85s | $0.002607 |
| after-hours-badge | yes | P2 | security | 0.72 | 2.72s | $0.003753 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.32s | $0.000194 |
| real-donor-export | yes | P1 | software | 0.9 | 1.08s | $0.000162 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.02s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.21s | $0.000226 |
| calm-phish-click | yes | P2 | security | 0.8 | 0.91s | $0.00016 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.04s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.04s | $0.000186 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.43s | $0.000227 |
| everything-down | yes | P1 | outage | 1 | 1.07s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.27s | $0.000194 |
| ransom-note | yes | P1 | security | 0.95 | 1.06s | $0.000163 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.33s | $0.000174 |
