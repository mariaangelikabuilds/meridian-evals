# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0331 | 2.4s | real-night-kiosk, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.34s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.15s | $0.003198 |
| real-donor-export | yes | P2 | software | 0.7 | 2.74s | $0.003465 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.57s | $0.003396 |
| real-night-kiosk | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.91s | $0.003525 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.37s | $0.004392 |
| vip-lockout | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.12s | $0.00261 |
| everything-down | yes | P1 | outage | 0.9 | 1.89s | $0.002763 |
| vague-slowness | yes | P4 | software | 0.6 | 2.4s | $0.003168 |
| ransom-note | yes | P1 | security | 0.98 | 2.24s | $0.002907 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.81s | $0.003708 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.92s | $0.000206 |
| real-donor-export | yes | P1 | software | 0.9 | 1.3s | $0.000178 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.34s | $0.000192 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.56s | $0.000234 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.05s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.39s | $0.000189 |
| vip-lockout | yes | P2 | access | 0.9 | 1.29s | $0.000177 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.19s | $0.000187 |
| everything-down | yes | P1 | outage | 1 | 1.35s | $0.000172 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.41s | $0.000201 |
| ransom-note | yes | P1 | security | 0.95 | 1.27s | $0.000169 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.27s | $0.000175 |
