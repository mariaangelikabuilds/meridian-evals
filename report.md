# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0386 | 2.64s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.15s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.7 | 2.58s | $0.003438 |
| real-donor-export | yes | P2 | software | 0.72 | 2.66s | $0.00288 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 3.04s | $0.003696 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.99s | $0.004359 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.64s | $0.003345 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.12s | $0.003912 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.42s | $0.00321 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.97s | $0.00243 |
| everything-down | yes | P1 | network | 0.9 | 1.79s | $0.002313 |
| vague-slowness | yes | P4 | software | 0.55 | 2.29s | $0.002928 |
| ransom-note | yes | P1 | security | 0.98 | 1.81s | $0.002502 |
| after-hours-badge | yes | P2 | security | 0.75 | 2.96s | $0.003603 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.51s | $0.00019 |
| real-donor-export | yes | P2 | software | 0.9 | 1.13s | $0.000187 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.01s | $0.000163 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 0.99s | $0.000205 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.15s | $0.000158 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.94s | $0.000202 |
| vip-lockout | yes | P2 | access | 0.9 | 1.06s | $0.000185 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.56s | $0.000165 |
| everything-down | yes | P1 | outage | 0.95 | 1.21s | $0.00019 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.13s | $0.000198 |
| ransom-note | yes | P1 | security | 0.95 | 2.16s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.99s | $0.000172 |
