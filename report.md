# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0391 | 2.53s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.22s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 2.51s | $0.003693 |
| real-donor-export | yes | P2 | software | 0.65 | 1.91s | $0.002655 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.88s | $0.003726 |
| real-night-kiosk | yes | P3 | hardware | 0.62 | 2.76s | $0.003729 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.53s | $0.00357 |
| quiet-security-tell | yes | P2 | security | 0.6 | 2.88s | $0.003747 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.57s | $0.003345 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.95s | $0.00267 |
| everything-down | yes | P1 | outage | 0.9 | 2.06s | $0.002868 |
| vague-slowness | yes | P4 | software | 0.55 | 2.34s | $0.002808 |
| ransom-note | yes | P1 | security | 0.98 | 1.98s | $0.002742 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.13s | $0.003588 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.07s | $0.000182 |
| real-donor-export | yes | P2 | software | 0.9 | 1.11s | $0.000178 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.18s | $0.000206 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.2s | $0.0002 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.09s | $0.000188 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.24s | $0.000205 |
| vip-lockout | yes | P2 | access | 0.9 | 1.19s | $0.000186 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.17s | $0.00015 |
| everything-down | yes | P1 | outage | 0.95 | 1.75s | $0.000187 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.22s | $0.000202 |
| ransom-note | yes | P1 | security | 0.9 | 1.22s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.23s | $0.000178 |
