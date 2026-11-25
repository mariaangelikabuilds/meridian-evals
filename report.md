# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0517 | 2.89s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.49s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | security | 0.55 | 6.95s | $0.009063 |
| real-donor-export | yes | P2 | software | 0.65 | 2.44s | $0.003075 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.89s | $0.003516 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.7s | $0.003684 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.02s | $0.003315 |
| quiet-security-tell | yes | P2 | security | 0.6 | 6.78s | $0.008562 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.23s | $0.00396 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.04s | $0.00237 |
| everything-down | yes | P1 | network | 0.9 | 2.33s | $0.003093 |
| vague-slowness | yes | P4 | software | 0.55 | 2.02s | $0.002913 |
| ransom-note | yes | P1 | security | 0.98 | 2.46s | $0.003132 |
| after-hours-badge | yes | P2 | security | 0.65 | 4.66s | $0.004998 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.4s | $0.00022 |
| real-donor-export | yes | P2 | software | 0.9 | 1.81s | $0.000181 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.46s | $0.000166 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.5s | $0.00023 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.11s | $0.000163 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.53s | $0.000191 |
| vip-lockout | yes | P2 | access | 0.9 | 1.49s | $0.000201 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.4s | $0.000173 |
| everything-down | yes | P1 | outage | 0.95 | 1.46s | $0.000185 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.38s | $0.000191 |
| ransom-note | yes | P1 | security | 0.95 | 1.21s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.49s | $0.000167 |
