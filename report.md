# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0396 | 3.23s | vip-lockout, ransom-note | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.79s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 3.23s | $0.003543 |
| real-donor-export | yes | P2 | software | 0.65 | 3.12s | $0.003075 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 3.16s | $0.003321 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.44s | $0.003909 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.33s | $0.003555 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.98s | $0.006537 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.25s | $0.00342 |
| routine-onboarding | yes | P3 | access | 0.9 | 3.03s | $0.00267 |
| everything-down | yes | P1 | outage | 0.9 | 2.99s | $0.003003 |
| vague-slowness | yes | P4 | software | 0.55 | 3.0s | $0.002958 |
| ransom-note | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.42s | $0.003573 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.39s | $0.000193 |
| real-donor-export | yes | P2 | software | 0.9 | 2.03s | $0.000221 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.54s | $0.000163 |
| real-night-kiosk | yes | P2 | hardware | 0.8 | 1.7s | $0.000211 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.03s | $0.000176 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.62s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.55s | $0.000194 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.79s | $0.000168 |
| everything-down | yes | P1 | outage | 0.95 | 1.86s | $0.000184 |
| vague-slowness | yes | P3 | software | 0.7 | 1.79s | $0.000193 |
| ransom-note | yes | P1 | security | 0.9 | 1.38s | $0.000171 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.94s | $0.000174 |
