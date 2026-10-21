# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.0372 | 2.65s | vip-lockout, ransom-note | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 1.78s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.93s | $0.003663 |
| real-donor-export | yes | P2 | software | 0.7 | 2.31s | $0.002835 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.42s | $0.003171 |
| real-night-kiosk | yes | P3 | hardware | 0.62 | 2.98s | $0.003909 |
| calm-phish-click | yes | P1 | security | 0.85 | 3.5s | $0.003735 |
| quiet-security-tell | yes | P2 | security | 0.6 | 3.78s | $0.004422 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 2.43s | $0.00333 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.22s | $0.002595 |
| everything-down | yes | P1 | network | 0.9 | 1.8s | $0.002538 |
| vague-slowness | yes | P4 | software | 0.6 | 2.65s | $0.003093 |
| ransom-note | NO: error (no JSON object in model output) | - | - | 0 | 0s | $0 |
| after-hours-badge | yes | P2 | security | 0.72 | 3.45s | $0.003933 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.7s | $0.000204 |
| real-donor-export | yes | P2 | software | 0.9 | 1.55s | $0.000187 |
| real-partner-mailbox | yes | P1 | access | 0.9 | 1.65s | $0.000166 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.0s | $0.000186 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.53s | $0.000168 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 2.07s | $0.000189 |
| vip-lockout | yes | P2 | access | 0.9 | 1.46s | $0.000202 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.6s | $0.000174 |
| everything-down | yes | P1 | outage | 0.9 | 1.59s | $0.000185 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.78s | $0.000199 |
| ransom-note | yes | P1 | security | 0.95 | 1.98s | $0.000184 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.49s | $0.000153 |
