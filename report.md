# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.038 | 2.47s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.13s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 1.95s | $0.003363 |
| real-donor-export | yes | P2 | software | 0.65 | 2.05s | $0.002955 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.53s | $0.003471 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.56s | $0.003369 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.54s | $0.003405 |
| quiet-security-tell | yes | P2 | security | 0.55 | 2.56s | $0.003087 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.24s | $0.00318 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.19s | $0.002715 |
| everything-down | yes | P1 | network | 0.9 | 2.06s | $0.002643 |
| vague-slowness | yes | P4 | software | 0.55 | 1.68s | $0.002643 |
| ransom-note | yes | P1 | security | 0.98 | 2.47s | $0.002877 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.19s | $0.004278 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.87s | $0.000204 |
| real-donor-export | yes | P2 | software | 0.9 | 1.4s | $0.000214 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.13s | $0.000187 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.35s | $0.000245 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.96s | $0.000176 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.07s | $0.000215 |
| vip-lockout | yes | P2 | access | 0.9 | 1.05s | $0.000175 |
| routine-onboarding | yes | P4 | request | 0.9 | 0.93s | $0.000158 |
| everything-down | yes | P1 | outage | 0.95 | 1.13s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.07s | $0.00017 |
| ransom-note | yes | P1 | security | 1 | 0.96s | $0.000148 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.39s | $0.000172 |
