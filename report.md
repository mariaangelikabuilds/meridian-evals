# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.042 | 2.77s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.61s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.0s | $0.003543 |
| real-donor-export | yes | P2 | software | 0.7 | 2.77s | $0.003105 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.21s | $0.003006 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.5s | $0.004149 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.79s | $0.003585 |
| quiet-security-tell | yes | P2 | security | 0.55 | 4.92s | $0.006627 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.35s | $0.003105 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.36s | $0.00249 |
| everything-down | yes | P1 | outage | 0.9 | 2.18s | $0.002568 |
| vague-slowness | yes | P4 | software | 0.55 | 2.43s | $0.003138 |
| ransom-note | yes | P1 | security | 0.98 | 2.17s | $0.002712 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.22s | $0.003993 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.06s | $0.000217 |
| real-donor-export | yes | P1 | software | 0.9 | 1.47s | $0.000154 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.39s | $0.000184 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.82s | $0.000219 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.43s | $0.000195 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.25s | $0.000237 |
| vip-lockout | yes | P2 | access | 0.9 | 1.67s | $0.000191 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.61s | $0.000174 |
| everything-down | yes | P1 | outage | 0.95 | 2.24s | $0.00018 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.37s | $0.000183 |
| ransom-note | yes | P1 | security | 0.95 | 1.36s | $0.000156 |
| after-hours-badge | yes | P2 | security | 0.8 | 1.46s | $0.000182 |
