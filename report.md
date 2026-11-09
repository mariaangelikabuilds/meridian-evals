# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0428 | 2.31s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0021 | 1.58s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 1.94s | $0.003213 |
| real-donor-export | yes | P2 | software | 0.65 | 2.35s | $0.003435 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 1.91s | $0.003096 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.51s | $0.003699 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.19s | $0.00336 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.1s | $0.006717 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.78s | $0.004545 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.9s | $0.00255 |
| everything-down | yes | P1 | outage | 0.9 | 1.96s | $0.002898 |
| vague-slowness | yes | P4 | software | 0.55 | 2.23s | $0.002988 |
| ransom-note | yes | P1 | security | 0.98 | 2.31s | $0.002637 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.83s | $0.003648 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.2s | $0.000183 |
| real-donor-export | yes | P1 | software | 0.9 | 1.13s | $0.000154 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 3.63s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.59s | $0.000202 |
| calm-phish-click | yes | P2 | security | 0.85 | 1.18s | $0.000158 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.31s | $0.000175 |
| vip-lockout | yes | P2 | access | 0.9 | 1.58s | $0.000196 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.16s | $0.000178 |
| everything-down | yes | P1 | outage | 0.95 | 1.14s | $0.000163 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.61s | $0.000194 |
| ransom-note | yes | P1 | security | 0.9 | 1.57s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.69s | $0.000178 |
