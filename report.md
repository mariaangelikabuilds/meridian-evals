# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.037 | 2.88s | vip-lockout, ransom-note | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.7s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.88s | $0.003438 |
| real-donor-export | yes | P2 | software | 0.7 | 2.43s | $0.00267 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.79s | $0.003306 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 4.04s | $0.004104 |
| calm-phish-click | yes | P2 | security | 0.85 | 2.91s | $0.00333 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.92s | $0.003897 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.95s | $0.00387 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.95s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 2.23s | $0.002823 |
| vague-slowness | yes | P4 | software | 0.6 | 2.28s | $0.002658 |
| ransom-note | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.32s | $0.004293 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.32s | $0.000214 |
| real-donor-export | yes | P1 | software | 0.9 | 1.42s | $0.000173 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.56s | $0.000198 |
| real-night-kiosk | yes | P2 | hardware | 0.85 | 1.92s | $0.000235 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.38s | $0.000172 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.25s | $0.000224 |
| vip-lockout | yes | P2 | access | 0.9 | 1.49s | $0.000169 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.19s | $0.000125 |
| everything-down | yes | P1 | outage | 0.9 | 1.84s | $0.000192 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.78s | $0.000186 |
| ransom-note | yes | P1 | security | 0.95 | 1.37s | $0.000164 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.7s | $0.000188 |
