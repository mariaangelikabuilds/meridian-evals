# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0415 | 2.75s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.15s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.75s | $0.003618 |
| real-donor-export | yes | P2 | software | 0.65 | 2.03s | $0.002985 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.32s | $0.003186 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.94s | $0.003609 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.56s | $0.00312 |
| quiet-security-tell | yes | P2 | security | 0.6 | 4.57s | $0.006132 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.64s | $0.003375 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.11s | $0.002685 |
| everything-down | yes | P1 | outage | 0.9 | 2.79s | $0.002568 |
| vague-slowness | yes | P4 | software | 0.55 | 2.55s | $0.003513 |
| ransom-note | yes | P1 | security | 0.98 | 3.41s | $0.002652 |
| after-hours-badge | yes | P2 | security | 0.6 | 3.13s | $0.004038 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.66s | $0.000202 |
| real-donor-export | yes | P2 | software | 0.9 | 1.15s | $0.000195 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.09s | $0.000163 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.17s | $0.000202 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.07s | $0.000164 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.15s | $0.000223 |
| vip-lockout | yes | P2 | access | 0.9 | 1.18s | $0.000199 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.15s | $0.000158 |
| everything-down | yes | P1 | outage | 0.95 | 1.15s | $0.000193 |
| vague-slowness | yes | P4 | hardware | 0.8 | 1.13s | $0.000188 |
| ransom-note | yes | P1 | security | 0.9 | 1.14s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.27s | $0.000188 |
