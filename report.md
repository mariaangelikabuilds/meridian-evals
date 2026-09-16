# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0384 | 3.07s | real-imaging-down, vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 2.18s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| real-donor-export | yes | P2 | software | 0.65 | 2.85s | $0.002775 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.56s | $0.003741 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 4.22s | $0.004359 |
| calm-phish-click | yes | P1 | security | 0.75 | 2.89s | $0.00306 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.44s | $0.006102 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.71s | $0.00324 |
| routine-onboarding | yes | P4 | access | 0.9 | 3.04s | $0.002715 |
| everything-down | yes | P1 | outage | 0.9 | 2.89s | $0.002958 |
| vague-slowness | yes | P4 | software | 0.55 | 3.07s | $0.002778 |
| ransom-note | yes | P1 | security | 0.98 | 3.55s | $0.002622 |
| after-hours-badge | yes | P2 | security | 0.72 | 4.0s | $0.004098 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.52s | $0.000188 |
| real-donor-export | yes | P2 | software | 0.9 | 1.9s | $0.000186 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 2.48s | $0.000168 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.97s | $0.000229 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.84s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 3.21s | $0.000205 |
| vip-lockout | yes | P2 | access | 0.9 | 1.99s | $0.000199 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.78s | $0.000162 |
| everything-down | yes | P1 | outage | 0.95 | 1.71s | $0.000172 |
| vague-slowness | yes | P3 | hardware | 0.7 | 13.25s | $0.000178 |
| ransom-note | yes | P1 | security | 0.95 | 1.85s | $0.000156 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.18s | $0.000166 |
