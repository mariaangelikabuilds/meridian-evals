# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.045 | 3.01s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.6s | real-imaging-down | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 3.14s | $0.003573 |
| real-donor-export | yes | P2 | software | 0.65 | 2.76s | $0.003165 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.79s | $0.003456 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.18s | $0.004104 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.14s | $0.00372 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.26s | $0.007392 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 3.01s | $0.003735 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.44s | $0.00273 |
| everything-down | yes | P1 | outage | 0.9 | 2.58s | $0.002778 |
| vague-slowness | yes | P4 | software | 0.55 | 2.5s | $0.003153 |
| ransom-note | yes | P1 | security | 0.98 | 2.66s | $0.003072 |
| after-hours-badge | yes | P2 | security | 0.7 | 3.9s | $0.004143 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.8 | 3.69s | $0.000199 |
| real-donor-export | yes | P1 | software | 0.9 | 1.35s | $0.00017 |
| real-partner-mailbox | yes | P1 | access | 0.95 | 1.67s | $0.000166 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.84s | $0.000234 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.6s | $0.000171 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.8s | $0.000253 |
| vip-lockout | yes | P2 | access | 0.9 | 1.12s | $0.000188 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.44s | $0.00017 |
| everything-down | yes | P1 | outage | 0.95 | 1.34s | $0.000179 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.54s | $0.000215 |
| ransom-note | yes | P1 | security | 0.9 | 1.2s | $0.000164 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.96s | $0.000183 |
