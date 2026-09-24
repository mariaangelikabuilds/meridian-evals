# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.046 | 3.43s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0021 | 1.44s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.72 | 3.43s | $0.003813 |
| real-donor-export | yes | P2 | software | 0.65 | 3.03s | $0.003 |
| real-partner-mailbox | yes | P1 | software | 0.85 | 2.76s | $0.003006 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 4.26s | $0.004734 |
| calm-phish-click | yes | P1 | security | 0.8 | 3.17s | $0.00348 |
| quiet-security-tell | yes | P2 | security | 0.62 | 6.23s | $0.007092 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.75s | $0.002835 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.37s | $0.00273 |
| everything-down | yes | P1 | network | 0.85 | 5.29s | $0.006078 |
| vague-slowness | yes | P4 | software | 0.55 | 2.77s | $0.002703 |
| ransom-note | yes | P1 | security | 0.98 | 2.3s | $0.002652 |
| after-hours-badge | yes | P2 | security | 0.62 | 3.54s | $0.003873 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.93s | $0.000196 |
| real-donor-export | yes | P1 | software | 0.9 | 1.17s | $0.000142 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.57s | $0.0002 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.44s | $0.000211 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.56s | $0.000177 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.37s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.3s | $0.00017 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.03s | $0.000134 |
| everything-down | yes | P1 | outage | 0.95 | 1.4s | $0.000184 |
| vague-slowness | yes | P3 | software | 0.8 | 1.46s | $0.000186 |
| ransom-note | yes | P1 | security | 0.9 | 1.03s | $0.000156 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.61s | $0.000174 |
