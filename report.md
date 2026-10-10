# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0396 | 2.73s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.59s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 2.96s | $0.004278 |
| real-donor-export | yes | P2 | software | 0.7 | 2.07s | $0.00294 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.82s | $0.003231 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.03s | $0.003864 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.64s | $0.003105 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.39s | $0.003897 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.73s | $0.003465 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.25s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 1.88s | $0.002733 |
| vague-slowness | yes | P4 | software | 0.55 | 2.36s | $0.002958 |
| ransom-note | yes | P1 | security | 0.98 | 2.01s | $0.002592 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.8s | $0.003873 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.37s | $0.000207 |
| real-donor-export | yes | P2 | software | 0.9 | 1.44s | $0.000163 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.52s | $0.000174 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.79s | $0.000221 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.34s | $0.00016 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.65s | $0.000229 |
| vip-lockout | yes | P2 | access | 0.9 | 1.33s | $0.000188 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.42s | $0.000162 |
| everything-down | yes | P1 | outage | 1 | 2.07s | $0.00018 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.82s | $0.000183 |
| ransom-note | yes | P1 | security | 0.95 | 1.59s | $0.000174 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.5s | $0.000174 |
