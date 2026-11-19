# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0399 | 2.75s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.29s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.65s | $0.003258 |
| real-donor-export | yes | P2 | software | 0.65 | 2.52s | $0.003 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.84s | $0.003381 |
| real-night-kiosk | yes | P2 | hardware | 0.65 | 3.39s | $0.003699 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.93s | $0.004125 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.16s | $0.004062 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.75s | $0.003825 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.76s | $0.002535 |
| everything-down | yes | P1 | network | 0.85 | 2.66s | $0.002823 |
| vague-slowness | yes | P4 | software | 0.55 | 1.75s | $0.002643 |
| ransom-note | yes | P1 | security | 0.97 | 1.79s | $0.002562 |
| after-hours-badge | yes | P2 | security | 0.72 | 3.39s | $0.003963 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.24s | $0.000201 |
| real-donor-export | yes | P2 | software | 0.9 | 1.37s | $0.000206 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.33s | $0.00016 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.35s | $0.000237 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.29s | $0.000192 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.25s | $0.0002 |
| vip-lockout | yes | P2 | access | 0.9 | 1.24s | $0.000201 |
| routine-onboarding | yes | P4 | request | 0.9 | 0.81s | $0.000136 |
| everything-down | yes | P1 | outage | 0.95 | 0.99s | $0.000169 |
| vague-slowness | yes | P3 | software | 0.7 | 1.05s | $0.000169 |
| ransom-note | yes | P1 | security | 0.95 | 1.47s | $0.000166 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.18s | $0.000182 |
