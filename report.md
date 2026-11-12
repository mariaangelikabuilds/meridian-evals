# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0437 | 2.26s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.82s | real-imaging-down | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.82s | $0.004218 |
| real-donor-export | yes | P2 | software | 0.65 | 1.86s | $0.00285 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.26s | $0.003276 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.86s | $0.004014 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.72s | $0.003735 |
| quiet-security-tell | yes | P2 | security | 0.55 | 5.32s | $0.006957 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.03s | $0.00285 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.11s | $0.00282 |
| everything-down | yes | P1 | outage | 0.9 | 2.14s | $0.002883 |
| vague-slowness | yes | P4 | software | 0.55 | 2.26s | $0.003168 |
| ransom-note | yes | P1 | security | 0.98 | 2.26s | $0.002862 |
| after-hours-badge | yes | P2 | security | 0.6 | 3.23s | $0.004068 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.56s | $0.000201 |
| real-donor-export | yes | P2 | software | 0.9 | 1.82s | $0.000197 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.82s | $0.000168 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.93s | $0.000208 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.13s | $0.000174 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.79s | $0.000192 |
| vip-lockout | yes | P2 | access | 0.9 | 2.0s | $0.000202 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.22s | $0.000162 |
| everything-down | yes | P1 | outage | 0.95 | 1.53s | $0.000168 |
| vague-slowness | yes | P4 | hardware | 0.8 | 1.93s | $0.00022 |
| ransom-note | yes | P1 | security | 0.9 | 1.49s | $0.000164 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.54s | $0.000198 |
