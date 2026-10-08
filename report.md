# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0419 | 2.56s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.81s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.94s | $0.003978 |
| real-donor-export | yes | P2 | software | 0.65 | 2.15s | $0.002865 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.56s | $0.003321 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.41s | $0.002784 |
| calm-phish-click | yes | P2 | security | 0.8 | 2.74s | $0.003135 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.25s | $0.007602 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.96s | $0.00342 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.41s | $0.002865 |
| everything-down | yes | P1 | network | 0.9 | 1.92s | $0.002628 |
| vague-slowness | yes | P4 | software | 0.55 | 1.74s | $0.002418 |
| ransom-note | yes | P1 | security | 0.98 | 2.51s | $0.002907 |
| after-hours-badge | yes | P2 | security | 0.65 | 4.94s | $0.003978 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.92s | $0.000191 |
| real-donor-export | yes | P2 | software | 0.9 | 1.5s | $0.000189 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.78s | $0.000192 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.06s | $0.000184 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.81s | $0.000163 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.93s | $0.000207 |
| vip-lockout | yes | P2 | access | 0.9 | 2.01s | $0.000217 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.71s | $0.000174 |
| everything-down | yes | P1 | outage | 0.95 | 1.36s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.91s | $0.000196 |
| ransom-note | yes | P1 | security | 0.9 | 1.66s | $0.000158 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.74s | $0.000177 |
