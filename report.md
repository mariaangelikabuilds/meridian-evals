# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0447 | 2.91s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.7s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 2.76s | $0.003858 |
| real-donor-export | yes | P2 | software | 0.65 | 3.19s | $0.003675 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 2.91s | $0.003501 |
| real-night-kiosk | yes | P3 | hardware | 0.62 | 3.44s | $0.004299 |
| calm-phish-click | yes | P1 | security | 0.85 | 2.34s | $0.00288 |
| quiet-security-tell | yes | P2 | security | 0.62 | 6.1s | $0.007302 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.6s | $0.003045 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.0s | $0.00258 |
| everything-down | yes | P1 | network | 0.85 | 3.12s | $0.003528 |
| vague-slowness | yes | P4 | software | 0.55 | 2.43s | $0.002973 |
| ransom-note | yes | P1 | security | 0.97 | 2.19s | $0.002667 |
| after-hours-badge | yes | P2 | security | 0.7 | 3.43s | $0.004353 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.78s | $0.000198 |
| real-donor-export | yes | P1 | software | 0.9 | 1.23s | $0.000158 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 2.59s | $0.000208 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.41s | $0.000234 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.72s | $0.000196 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.7s | $0.000221 |
| vip-lockout | yes | P2 | access | 0.9 | 1.39s | $0.000182 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.14s | $0.000163 |
| everything-down | yes | P1 | outage | 0.9 | 2.04s | $0.00019 |
| vague-slowness | yes | P4 | hardware | 0.7 | 1.37s | $0.000212 |
| ransom-note | yes | P1 | security | 0.9 | 2.11s | $0.000152 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.53s | $0.000199 |
