# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0398 | 2.62s | real-donor-export, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0021 | 2.03s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 2.61s | $0.003768 |
| real-donor-export | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.76s | $0.004041 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.62s | $0.003669 |
| calm-phish-click | yes | P2 | security | 0.7 | 2.97s | $0.00369 |
| quiet-security-tell | yes | P2 | security | 0.6 | 4.66s | $0.006042 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.67s | $0.00336 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.74s | $0.00276 |
| everything-down | yes | P1 | outage | 0.9 | 1.57s | $0.002553 |
| vague-slowness | yes | P4 | hardware | 0.55 | 2.54s | $0.003423 |
| ransom-note | yes | P1 | security | 0.98 | 2.16s | $0.002817 |
| after-hours-badge | yes | P2 | security | 0.75 | 2.68s | $0.003693 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.64s | $0.000199 |
| real-donor-export | yes | P1 | software | 0.9 | 1.53s | $0.000146 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 2.75s | $0.00019 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.42s | $0.000224 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.51s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.03s | $0.000202 |
| vip-lockout | yes | P2 | access | 0.9 | 1.28s | $0.000178 |
| routine-onboarding | yes | P4 | request | 0.95 | 2.44s | $0.000133 |
| everything-down | yes | P1 | outage | 1 | 2.53s | $0.000166 |
| vague-slowness | yes | P3 | hardware | 0.7 | 3.23s | $0.000193 |
| ransom-note | yes | P1 | security | 0.9 | 0.95s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.88s | $0.000183 |
