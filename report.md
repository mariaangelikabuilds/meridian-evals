# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0387 | 2.66s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 2.37s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.66s | $0.003693 |
| real-donor-export | yes | P2 | software | 0.7 | 2.3s | $0.00297 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 3.02s | $0.003426 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.37s | $0.003219 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.67s | $0.0033 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.38s | $0.004137 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.51s | $0.00309 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.94s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 1.93s | $0.002553 |
| vague-slowness | yes | P4 | hardware | 0.55 | 2.75s | $0.003198 |
| ransom-note | yes | P1 | security | 0.98 | 2.2s | $0.002712 |
| after-hours-badge | yes | P2 | security | 0.75 | 2.93s | $0.003723 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.85s | $0.000206 |
| real-donor-export | yes | P1 | software | 0.9 | 0.99s | $0.000166 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 2.37s | $0.000221 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.66s | $0.000261 |
| calm-phish-click | yes | P2 | security | 0.8 | 2.2s | $0.000193 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 1.05s | $0.000204 |
| vip-lockout | yes | P2 | access | 0.9 | 1.04s | $0.000172 |
| routine-onboarding | yes | P4 | request | 1 | 2.57s | $0.000139 |
| everything-down | yes | P1 | outage | 0.95 | 2.44s | $0.000192 |
| vague-slowness | yes | P3 | software | 0.8 | 2.91s | $0.000175 |
| ransom-note | yes | P1 | security | 0.9 | 1.42s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.23s | $0.000182 |
