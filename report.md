# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0421 | 2.5s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.18s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.5s | $0.003438 |
| real-donor-export | yes | P2 | software | 0.65 | 2.21s | $0.002955 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.19s | $0.003141 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 3.13s | $0.003969 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.49s | $0.00342 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.16s | $0.006372 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.19s | $0.00297 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.51s | $0.002895 |
| everything-down | yes | P1 | network | 0.9 | 1.69s | $0.002673 |
| vague-slowness | yes | P4 | software | 0.55 | 2.26s | $0.003213 |
| ransom-note | yes | P1 | security | 0.98 | 2.73s | $0.003432 |
| after-hours-badge | yes | P2 | security | 0.6 | 2.61s | $0.003648 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.92s | $0.000201 |
| real-donor-export | yes | P1 | software | 0.9 | 0.95s | $0.000154 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.11s | $0.000202 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.27s | $0.000214 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.31s | $0.000195 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.38s | $0.000215 |
| vip-lockout | yes | P2 | access | 0.9 | 0.99s | $0.000175 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.85s | $0.000136 |
| everything-down | yes | P1 | outage | 0.9 | 1.27s | $0.000166 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.18s | $0.000209 |
| ransom-note | yes | P1 | security | 0.95 | 1.02s | $0.000169 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.99s | $0.000174 |
