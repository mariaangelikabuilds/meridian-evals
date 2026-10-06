# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0422 | 2.55s | vip-lockout, ransom-note | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.61s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.81s | $0.004098 |
| real-donor-export | yes | P2 | software | 0.65 | 2.23s | $0.002895 |
| real-partner-mailbox | known gap | P2 | software | 0.75 | 2.25s | $0.003081 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.42s | $0.004134 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.74s | $0.00327 |
| quiet-security-tell | yes | P2 | security | 0.65 | 7.23s | $0.008727 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.55s | $0.003285 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.14s | $0.00258 |
| everything-down | yes | P1 | network | 0.9 | 2.28s | $0.002928 |
| vague-slowness | yes | P4 | software | 0.55 | 2.28s | $0.002823 |
| ransom-note | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| after-hours-badge | yes | P2 | security | 0.65 | 4.13s | $0.004383 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.82s | $0.000204 |
| real-donor-export | yes | P2 | software | 0.9 | 2.04s | $0.000202 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.2s | $0.000168 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.61s | $0.000213 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.57s | $0.000174 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.09s | $0.0002 |
| vip-lockout | yes | P2 | access | 0.9 | 1.6s | $0.000214 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.48s | $0.000174 |
| everything-down | yes | P1 | outage | 0.95 | 1.82s | $0.00018 |
| vague-slowness | yes | P3 | hardware | 0.8 | 1.93s | $0.000177 |
| ransom-note | yes | P1 | security | 0.9 | 1.41s | $0.000158 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.59s | $0.00018 |
