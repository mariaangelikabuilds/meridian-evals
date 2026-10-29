# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0397 | 2.73s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.5s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.65s | $0.003168 |
| real-donor-export | yes | P2 | software | 0.72 | 2.73s | $0.00351 |
| real-partner-mailbox | known gap (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-night-kiosk | yes | P3 | software | 0.6 | 5.6s | $0.007449 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.74s | $0.0036 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.45s | $0.003987 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.75s | $0.00327 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.09s | $0.002745 |
| everything-down | yes | P1 | outage | 0.9 | 2.21s | $0.002973 |
| vague-slowness | yes | P4 | software | 0.55 | 1.86s | $0.002448 |
| ransom-note | yes | P1 | security | 0.98 | 2.02s | $0.002637 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.48s | $0.003948 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.59s | $0.000223 |
| real-donor-export | yes | P2 | software | 0.9 | 2.18s | $0.000194 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.35s | $0.000189 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.92s | $0.000232 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.12s | $0.000182 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.08s | $0.0002 |
| vip-lockout | yes | P2 | access | 0.9 | 1.35s | $0.00019 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.22s | $0.000168 |
| everything-down | yes | P1 | outage | 0.95 | 1.42s | $0.000166 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.17s | $0.00017 |
| ransom-note | yes | P1 | security | 1 | 1.55s | $0.000156 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.5s | $0.000183 |
