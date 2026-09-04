# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0504 | 3.74s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.85s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 4.17s | $0.004098 |
| real-donor-export | yes | P2 | software | 0.65 | 3.22s | $0.00294 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 5.92s | $0.006681 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.74s | $0.004254 |
| calm-phish-click | yes | P1 | security | 0.75 | 3.25s | $0.003465 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.85s | $0.006747 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 4.02s | $0.003825 |
| routine-onboarding | yes | P3 | access | 0.9 | 3.11s | $0.002595 |
| everything-down | yes | P1 | outage | 0.85 | 2.4s | $0.002568 |
| vague-slowness | yes | P4 | software | 0.6 | 2.9s | $0.002568 |
| ransom-note | yes | P1 | security | 0.98 | 3.45s | $0.002757 |
| after-hours-badge | yes | P2 | security | 0.65 | 6.94s | $0.007908 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.27s | $0.00021 |
| real-donor-export | yes | P1 | software | 0.9 | 1.76s | $0.000174 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.5s | $0.000176 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.12s | $0.000205 |
| calm-phish-click | yes | P2 | security | 0.9 | 2.31s | $0.00016 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.74s | $0.000224 |
| vip-lockout | yes | P2 | access | 0.9 | 1.85s | $0.000186 |
| routine-onboarding | yes | P4 | request | 1 | 1.29s | $0.000149 |
| everything-down | yes | P1 | outage | 0.95 | 1.7s | $0.000172 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.91s | $0.000161 |
| ransom-note | yes | P1 | security | 0.95 | 1.87s | $0.000179 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.48s | $0.000188 |
