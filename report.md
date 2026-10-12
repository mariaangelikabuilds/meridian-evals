# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0403 | 2.74s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.42s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.88s | $0.003678 |
| real-donor-export | yes | P2 | software | 0.65 | 2.74s | $0.00339 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.49s | $0.003396 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.51s | $0.004254 |
| calm-phish-click | yes | P1 | security | 0.85 | 2.52s | $0.003255 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.66s | $0.004017 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.81s | $0.003435 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.36s | $0.00264 |
| everything-down | yes | P1 | outage | 0.9 | 1.97s | $0.002553 |
| vague-slowness | yes | P4 | software | 0.6 | 2.37s | $0.003048 |
| ransom-note | yes | P1 | security | 0.98 | 2.16s | $0.002742 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.2s | $0.003933 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.85 | 3.18s | $0.000226 |
| real-donor-export | yes | P1 | software | 0.9 | 1.24s | $0.000158 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.17s | $0.000162 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.48s | $0.000213 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.21s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.3s | $0.000186 |
| vip-lockout | yes | P2 | access | 0.9 | 1.42s | $0.000166 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.64s | $0.000186 |
| everything-down | yes | P1 | outage | 0.95 | 1.24s | $0.000182 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.47s | $0.000191 |
| ransom-note | yes | P1 | security | 0.9 | 1.27s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.52s | $0.000178 |
