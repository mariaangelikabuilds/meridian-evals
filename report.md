# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0431 | 2.41s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 0.86s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.74s | $0.004158 |
| real-donor-export | yes | P2 | software | 0.65 | 1.75s | $0.00261 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.41s | $0.003786 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.38s | $0.004224 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.25s | $0.00312 |
| quiet-security-tell | yes | P2 | security | 0.6 | 4.21s | $0.006312 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.53s | $0.003435 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.89s | $0.002745 |
| everything-down | yes | P1 | outage | 0.9 | 1.7s | $0.002583 |
| vague-slowness | yes | P4 | software | 0.6 | 1.99s | $0.002928 |
| ransom-note | yes | P1 | security | 0.98 | 2.21s | $0.003252 |
| after-hours-badge | yes | P2 | security | 0.72 | 2.89s | $0.003993 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 2.75s | $0.000198 |
| real-donor-export | yes | P1 | software | 0.9 | 1.11s | $0.000173 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 0.82s | $0.000181 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.25s | $0.000253 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.86s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 0.71s | $0.000183 |
| vip-lockout | yes | P2 | access | 0.9 | 0.93s | $0.000178 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.78s | $0.00015 |
| everything-down | yes | P1 | outage | 1 | 0.82s | $0.000171 |
| vague-slowness | yes | P3 | hardware | 0.7 | 0.77s | $0.00017 |
| ransom-note | yes | P1 | security | 0.9 | 0.92s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.65s | $0.000166 |
