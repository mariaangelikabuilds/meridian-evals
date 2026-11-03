# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0421 | 2.68s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0021 | 1.26s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 3.06s | $0.004308 |
| real-donor-export | yes | P2 | software | 0.72 | 2.41s | $0.00315 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.69s | $0.003531 |
| real-night-kiosk | yes | P3 | hardware | 0.65 | 4.82s | $0.006144 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.68s | $0.003405 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.26s | $0.003972 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.58s | $0.003135 |
| routine-onboarding | yes | P4 | access | 0.85 | 1.97s | $0.00279 |
| everything-down | yes | P1 | outage | 0.9 | 1.71s | $0.002478 |
| vague-slowness | yes | P4 | software | 0.55 | 2.48s | $0.003018 |
| ransom-note | yes | P1 | security | 0.98 | 1.94s | $0.002577 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.05s | $0.003603 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.29s | $0.000191 |
| real-donor-export | yes | P1 | software | 0.9 | 1.1s | $0.000174 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.26s | $0.000186 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.28s | $0.000182 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.24s | $0.000172 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 4.83s | $0.000224 |
| vip-lockout | yes | P2 | access | 0.9 | 1.18s | $0.000174 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.98s | $0.000146 |
| everything-down | yes | P1 | outage | 0.95 | 1.5s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.21s | $0.000177 |
| ransom-note | yes | P1 | security | 1 | 1.17s | $0.000163 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.58s | $0.000164 |
