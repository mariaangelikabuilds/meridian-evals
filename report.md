# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0397 | 2.84s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.52s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 2.87s | $0.003693 |
| real-donor-export | yes | P2 | software | 0.7 | 2.19s | $0.00288 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 3.23s | $0.003711 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.1s | $0.004149 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.1s | $0.003765 |
| quiet-security-tell | yes | P2 | security | 0.55 | 2.84s | $0.003387 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.22s | $0.00423 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.03s | $0.002535 |
| everything-down | yes | P1 | outage | 0.9 | 1.99s | $0.002388 |
| vague-slowness | yes | P4 | hardware | 0.55 | 2.6s | $0.002958 |
| ransom-note | yes | P1 | security | 0.98 | 1.88s | $0.002427 |
| after-hours-badge | yes | P2 | security | 0.65 | 2.68s | $0.003573 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.84s | $0.000212 |
| real-donor-export | yes | P1 | software | 0.9 | 1.61s | $0.000181 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.47s | $0.000187 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.52s | $0.000198 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.83s | $0.000184 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.33s | $0.000221 |
| vip-lockout | yes | P2 | access | 0.9 | 1.34s | $0.000196 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.4s | $0.000176 |
| everything-down | yes | P1 | outage | 0.95 | 1.16s | $0.000177 |
| vague-slowness | yes | P3 | hardware | 0.7 | 2.28s | $0.000214 |
| ransom-note | yes | P1 | security | 0.9 | 1.21s | $0.000169 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.52s | $0.000186 |
