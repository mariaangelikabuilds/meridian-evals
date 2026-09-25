# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0389 | 3.12s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.29s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 3.07s | $0.003423 |
| real-donor-export | yes | P2 | software | 0.65 | 3.29s | $0.003405 |
| real-partner-mailbox | yes | P1 | software | 0.85 | 3.25s | $0.003366 |
| real-night-kiosk | yes | P3 | hardware | 0.55 | 2.91s | $0.003384 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.12s | $0.00315 |
| quiet-security-tell | yes | P2 | security | 0.65 | 3.58s | $0.004017 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 3.19s | $0.00309 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.4s | $0.002685 |
| everything-down | yes | P1 | outage | 0.9 | 2.6s | $0.002568 |
| vague-slowness | yes | P4 | software | 0.55 | 2.66s | $0.002883 |
| ransom-note | yes | P1 | security | 0.98 | 2.87s | $0.003147 |
| after-hours-badge | yes | P2 | security | 0.65 | 4.48s | $0.003783 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.74s | $0.000223 |
| real-donor-export | yes | P2 | software | 0.9 | 1.23s | $0.000195 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.29s | $0.000178 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.58s | $0.000229 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.21s | $0.00016 |
| quiet-security-tell | yes | P2 | hardware | 0.85 | 2.3s | $0.000228 |
| vip-lockout | yes | P2 | access | 0.9 | 1.25s | $0.00017 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.17s | $0.000155 |
| everything-down | yes | P1 | outage | 0.9 | 1.54s | $0.000192 |
| vague-slowness | yes | P4 | software | 0.8 | 1.23s | $0.000175 |
| ransom-note | yes | P1 | security | 0.95 | 1.21s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.8s | $0.000194 |
