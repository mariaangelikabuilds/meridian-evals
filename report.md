# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0389 | 2.73s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 2.32s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.74s | $0.003573 |
| real-donor-export | yes | P2 | software | 0.72 | 2.73s | $0.003075 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.72s | $0.003666 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.04s | $0.003279 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.12s | $0.00345 |
| quiet-security-tell | yes | P2 | security | 0.6 | 4.19s | $0.004407 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.35s | $0.002925 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.21s | $0.00258 |
| everything-down | yes | P1 | outage | 0.9 | 2.05s | $0.002838 |
| vague-slowness | yes | P4 | software | 0.55 | 2.57s | $0.003003 |
| ransom-note | yes | P1 | security | 0.98 | 2.15s | $0.002472 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.99s | $0.003678 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.39s | $0.00019 |
| real-donor-export | yes | P1 | software | 0.9 | 2.19s | $0.000189 |
| real-partner-mailbox | known gap | P2 | email | 0.9 | 2.46s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 3.95s | $0.000248 |
| calm-phish-click | yes | P2 | security | 0.9 | 3.22s | $0.000171 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.19s | $0.000202 |
| vip-lockout | yes | P2 | access | 0.9 | 2.08s | $0.000169 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.81s | $0.000166 |
| everything-down | yes | P1 | outage | 0.95 | 2.33s | $0.000184 |
| vague-slowness | yes | P3 | hardware | 0.8 | 2.32s | $0.000222 |
| ransom-note | yes | P1 | security | 1 | 1.82s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.17s | $0.000185 |
