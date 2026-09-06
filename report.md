# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0419 | 3.09s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.37s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.09s | $0.003798 |
| real-donor-export | yes | P2 | software | 0.65 | 2.45s | $0.002655 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 3.62s | $0.003966 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.47s | $0.004404 |
| calm-phish-click | yes | P1 | security | 0.85 | 2.79s | $0.003465 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.29s | $0.003747 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 3.19s | $0.003735 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.99s | $0.00255 |
| everything-down | yes | P1 | outage | 0.85 | 2.98s | $0.003408 |
| vague-slowness | yes | P4 | software | 0.55 | 2.18s | $0.002718 |
| ransom-note | yes | P1 | security | 0.97 | 2.73s | $0.003267 |
| after-hours-badge | yes | P2 | security | 0.7 | 3.84s | $0.004203 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.96s | $0.000198 |
| real-donor-export | yes | P1 | software | 0.9 | 1.09s | $0.000171 |
| real-partner-mailbox | yes | P1 | software | 0.9 | 1.07s | $0.000181 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.37s | $0.000216 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.79s | $0.000196 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.49s | $0.000223 |
| vip-lockout | yes | P2 | access | 0.9 | 1.24s | $0.000183 |
| routine-onboarding | yes | P4 | request | 1 | 1.04s | $0.00016 |
| everything-down | yes | P1 | outage | 0.9 | 1.43s | $0.000179 |
| vague-slowness | yes | P4 | hardware | 0.7 | 1.58s | $0.000185 |
| ransom-note | yes | P1 | security | 0.9 | 1.35s | $0.000163 |
| after-hours-badge | yes | P2 | security | 0.8 | 1.01s | $0.000164 |
