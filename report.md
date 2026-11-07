# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0395 | 2.49s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0022 | 0.97s | none | none |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 2.49s | $0.003543 |
| real-donor-export | yes | P2 | software | 0.65 | 2.7s | $0.0036 |
| real-partner-mailbox | yes | P1 | software | 0.8 | 2.33s | $0.003351 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.74s | $0.003174 |
| calm-phish-click | yes | P2 | security | 0.75 | 3.0s | $0.00369 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.51s | $0.004017 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.27s | $0.00309 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.48s | $0.00267 |
| everything-down | yes | P1 | outage | 0.9 | 1.85s | $0.002733 |
| vague-slowness | yes | P4 | software | 0.6 | 2.16s | $0.003153 |
| ransom-note | yes | P1 | security | 0.98 | 1.75s | $0.002622 |
| after-hours-badge | yes | P2 | security | 0.75 | 2.88s | $0.003858 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 2.32s | $0.00019 |
| real-donor-export | yes | P2 | software | 0.9 | 1.21s | $0.000213 |
| real-partner-mailbox | yes | P1 | software | 0.9 | 0.91s | $0.00017 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.1s | $0.000224 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.97s | $0.000176 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 0.83s | $0.000189 |
| vip-lockout | yes | P2 | access | 0.9 | 0.91s | $0.000172 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.88s | $0.000162 |
| everything-down | yes | P1 | outage | 0.95 | 1.17s | $0.000188 |
| vague-slowness | yes | P4 | software | 0.8 | 0.94s | $0.000196 |
| ransom-note | yes | P1 | security | 0.95 | 0.9s | $0.000177 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.03s | $0.000191 |
