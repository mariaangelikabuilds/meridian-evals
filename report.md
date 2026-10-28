# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.036 | 2.53s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.51s | real-imaging-down | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.62s | $0.003543 |
| real-donor-export | yes | P2 | software | 0.72 | 2.03s | $0.002715 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.32s | $0.003291 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.42s | $0.003189 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.42s | $0.004155 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.41s | $0.003882 |
| vip-lockout | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| routine-onboarding | yes | P4 | access | 0.85 | 1.78s | $0.00261 |
| everything-down | yes | P1 | outage | 0.9 | 2.22s | $0.002988 |
| vague-slowness | yes | P4 | software | 0.6 | 2.55s | $0.003258 |
| ransom-note | yes | P1 | security | 0.98 | 2.53s | $0.002772 |
| after-hours-badge | yes | P2 | security | 0.72 | 3.0s | $0.003588 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.11s | $0.000198 |
| real-donor-export | yes | P2 | software | 0.9 | 1.66s | $0.000197 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.2s | $0.000176 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.23s | $0.000226 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.09s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.53s | $0.000204 |
| vip-lockout | yes | P2 | access | 0.9 | 1.29s | $0.000177 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.06s | $0.000147 |
| everything-down | yes | P1 | outage | 1 | 1.04s | $0.000168 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.68s | $0.000209 |
| ransom-note | yes | P1 | security | 1 | 1.51s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.57s | $0.000212 |
