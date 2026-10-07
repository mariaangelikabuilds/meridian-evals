# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0405 | 2.76s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.58s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 3.97s | $0.004803 |
| real-donor-export | yes | P2 | software | 0.65 | 1.99s | $0.002955 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 3.08s | $0.003711 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.67s | $0.003624 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.99s | $0.00378 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.55s | $0.004167 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.81s | $0.00345 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.81s | $0.00258 |
| everything-down | yes | P1 | network | 0.9 | 1.82s | $0.002493 |
| vague-slowness | yes | P4 | software | 0.55 | 2.4s | $0.002778 |
| ransom-note | yes | P1 | security | 0.98 | 2.13s | $0.002622 |
| after-hours-badge | yes | P2 | security | 0.75 | 2.76s | $0.003558 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.71s | $0.000204 |
| real-donor-export | yes | P1 | software | 0.9 | 1.4s | $0.000157 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.56s | $0.000166 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.66s | $0.000205 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.81s | $0.000204 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.63s | $0.0002 |
| vip-lockout | yes | P2 | access | 0.9 | 1.41s | $0.000169 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.58s | $0.000162 |
| everything-down | yes | P1 | outage | 0.9 | 1.15s | $0.000169 |
| vague-slowness | yes | P3 | software | 0.8 | 1.28s | $0.000196 |
| ransom-note | yes | P1 | security | 1 | 1.48s | $0.000164 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.7s | $0.000199 |
