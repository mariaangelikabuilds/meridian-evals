# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0406 | 2.74s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.5s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.05s | $0.003903 |
| real-donor-export | yes | P2 | software | 0.7 | 2.32s | $0.00294 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.49s | $0.003306 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.66s | $0.003654 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.0s | $0.003525 |
| quiet-security-tell | yes | P2 | security | 0.55 | 4.17s | $0.005592 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.8s | $0.0033 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.5s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 1.85s | $0.002583 |
| vague-slowness | yes | P4 | software | 0.6 | 2.3s | $0.002583 |
| ransom-note | yes | P1 | security | 0.98 | 2.74s | $0.003057 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.74s | $0.003513 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.5s | $0.000202 |
| real-donor-export | yes | P1 | software | 0.9 | 1.19s | $0.000173 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.45s | $0.000178 |
| real-night-kiosk | yes | P2 | hardware | 0.85 | 1.9s | $0.000229 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.34s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.44s | $0.000221 |
| vip-lockout | yes | P2 | access | 0.9 | 1.59s | $0.000166 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.3s | $0.000139 |
| everything-down | yes | P1 | outage | 0.9 | 1.4s | $0.000168 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.53s | $0.000175 |
| ransom-note | yes | P1 | security | 0.9 | 1.56s | $0.000185 |
| after-hours-badge | yes | P2 | security | 0.8 | 1.5s | $0.00017 |
