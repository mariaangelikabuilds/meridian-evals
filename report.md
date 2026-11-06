# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0393 | 2.43s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.23s | real-imaging-down | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.68s | $0.003543 |
| real-donor-export | yes | P2 | software | 0.7 | 2.05s | $0.00294 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.24s | $0.003441 |
| real-night-kiosk | yes | P2 | hardware | 0.55 | 2.45s | $0.003429 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.43s | $0.00321 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.35s | $0.003807 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.47s | $0.00321 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.04s | $0.002685 |
| everything-down | yes | P1 | outage | 0.9 | 1.99s | $0.002763 |
| vague-slowness | yes | P4 | software | 0.6 | 1.92s | $0.002958 |
| ransom-note | yes | P1 | security | 0.98 | 1.98s | $0.002517 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.7s | $0.004773 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.04s | $0.000215 |
| real-donor-export | yes | P1 | software | 0.9 | 0.99s | $0.000171 |
| real-partner-mailbox | yes | P1 | access | 0.95 | 1.16s | $0.000214 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.23s | $0.0002 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.24s | $0.000187 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.23s | $0.000207 |
| vip-lockout | yes | P2 | access | 0.9 | 0.99s | $0.000194 |
| routine-onboarding | yes | P4 | request | 0.9 | 0.95s | $0.000171 |
| everything-down | yes | P1 | outage | 0.95 | 1.37s | $0.000184 |
| vague-slowness | yes | P4 | hardware | 0.7 | 1.13s | $0.000186 |
| ransom-note | yes | P1 | security | 1 | 1.26s | $0.00019 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.86s | $0.000161 |
