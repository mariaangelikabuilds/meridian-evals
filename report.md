# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0404 | 2.41s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.41s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 2.76s | $0.003393 |
| real-donor-export | yes | P2 | software | 0.65 | 2.31s | $0.002835 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 2.41s | $0.003201 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 2.41s | $0.003489 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.58s | $0.00333 |
| quiet-security-tell | yes | P2 | security | 0.55 | 4.79s | $0.006372 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.18s | $0.00309 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.85s | $0.002715 |
| everything-down | yes | P1 | outage | 0.9 | 2.09s | $0.002523 |
| vague-slowness | yes | P4 | software | 0.55 | 2.03s | $0.002778 |
| ransom-note | yes | P1 | security | 0.98 | 2.52s | $0.002847 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.19s | $0.003843 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 9.58s | $0.00022 |
| real-donor-export | yes | P2 | software | 0.9 | 1.06s | $0.000197 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 0.99s | $0.000194 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.33s | $0.000235 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.74s | $0.000166 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.79s | $0.000186 |
| vip-lockout | yes | P2 | access | 0.9 | 1.41s | $0.000185 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.4s | $0.000152 |
| everything-down | yes | P1 | outage | 0.95 | 1.23s | $0.000193 |
| vague-slowness | yes | P3 | software | 0.8 | 1.94s | $0.000178 |
| ransom-note | yes | P1 | security | 0.95 | 1.07s | $0.00016 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.9s | $0.000183 |
