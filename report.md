# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0356 | 2.4s | quiet-security-tell, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0023 | 1.15s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 3.05s | $0.004113 |
| real-donor-export | yes | P2 | software | 0.7 | 2.38s | $0.00291 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.4s | $0.003456 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.62s | $0.003339 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.42s | $0.003165 |
| quiet-security-tell | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.53s | $0.00339 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.17s | $0.002715 |
| everything-down | yes | P1 | network | 0.9 | 1.97s | $0.002763 |
| vague-slowness | yes | P4 | software | 0.6 | 2.2s | $0.003123 |
| ransom-note | yes | P1 | security | 0.98 | 2.07s | $0.002712 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.16s | $0.003933 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.55s | $0.00022 |
| real-donor-export | yes | P2 | software | 0.9 | 1.14s | $0.00019 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 0.93s | $0.000168 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.28s | $0.000242 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.19s | $0.000196 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.49s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.08s | $0.000185 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.94s | $0.000176 |
| everything-down | yes | P1 | outage | 0.95 | 0.9s | $0.000161 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.15s | $0.000198 |
| ransom-note | yes | P1 | security | 0.95 | 1.19s | $0.000168 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.01s | $0.000177 |
