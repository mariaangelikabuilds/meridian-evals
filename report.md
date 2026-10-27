# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0372 | 2.37s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.42s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.37s | $0.003573 |
| real-donor-export | yes | P2 | software | 0.65 | 1.98s | $0.00279 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.24s | $0.002886 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.85s | $0.003534 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.13s | $0.002805 |
| quiet-security-tell | yes | P2 | security | 0.55 | 2.87s | $0.003537 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.57s | $0.003045 |
| routine-onboarding | yes | P4 | access | 0.85 | 2.22s | $0.002595 |
| everything-down | yes | P1 | outage | 0.9 | 2.17s | $0.002628 |
| vague-slowness | yes | P4 | software | 0.55 | 2.21s | $0.002748 |
| ransom-note | yes | P1 | security | 0.98 | 2.53s | $0.002967 |
| after-hours-badge | yes | P2 | security | 0.75 | 3.87s | $0.004128 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 2.68s | $0.00021 |
| real-donor-export | yes | P2 | software | 0.9 | 1.42s | $0.0002 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.74s | $0.000218 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.85s | $0.000248 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.17s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.32s | $0.000204 |
| vip-lockout | yes | P2 | access | 0.9 | 1.56s | $0.000178 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.01s | $0.00017 |
| everything-down | yes | P1 | outage | 0.95 | 1.34s | $0.000176 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.31s | $0.000183 |
| ransom-note | yes | P1 | security | 0.9 | 1.18s | $0.00016 |
| after-hours-badge | yes | P2 | security | 0.8 | 1.53s | $0.00017 |
