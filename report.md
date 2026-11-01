# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0433 | 2.26s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 1.17s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.36s | $0.003378 |
| real-donor-export | yes | P2 | software | 0.7 | 1.88s | $0.00246 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.09s | $0.002991 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.6s | $0.003534 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.34s | $0.003195 |
| quiet-security-tell | yes | P2 | security | 0.62 | 5.77s | $0.007347 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.14s | $0.002925 |
| routine-onboarding | yes | P4 | access | 0.85 | 1.95s | $0.00246 |
| everything-down | yes | P1 | outage | 0.9 | 2.12s | $0.003018 |
| vague-slowness | yes | P4 | software | 0.55 | 2.26s | $0.002988 |
| ransom-note | yes | P1 | security | 0.98 | 2.18s | $0.002652 |
| after-hours-badge | yes | P2 | security | 0.72 | 5.46s | $0.006393 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.4s | $0.000199 |
| real-donor-export | yes | P2 | software | 0.9 | 1.25s | $0.000197 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 0.97s | $0.000165 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.41s | $0.000226 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.06s | $0.000182 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.17s | $0.000232 |
| vip-lockout | yes | P2 | access | 0.9 | 1.11s | $0.000191 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.08s | $0.00016 |
| everything-down | yes | P1 | outage | 0.95 | 1.17s | $0.000193 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.06s | $0.000183 |
| ransom-note | yes | P1 | security | 0.95 | 1.04s | $0.00018 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.97s | $0.00018 |
