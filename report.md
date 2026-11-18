# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0416 | 2.77s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 100% | 11/11 | $0.0021 | 1.03s | none | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 3.11s | $0.003228 |
| real-donor-export | yes | P2 | software | 0.65 | 2.57s | $0.00291 |
| real-partner-mailbox | yes | P1 | software | 0.75 | 3.94s | $0.003966 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.19s | $0.003519 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.66s | $0.0033 |
| quiet-security-tell | yes | P2 | security | 0.6 | 5.3s | $0.006417 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.17s | $0.002895 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.84s | $0.002685 |
| everything-down | yes | P1 | network | 0.9 | 1.93s | $0.002733 |
| vague-slowness | yes | P4 | software | 0.55 | 2.31s | $0.003393 |
| ransom-note | yes | P1 | security | 0.98 | 2.77s | $0.002937 |
| after-hours-badge | yes | P2 | security | 0.6 | 2.83s | $0.003633 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.35s | $0.00019 |
| real-donor-export | yes | P1 | software | 0.9 | 0.89s | $0.000165 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.03s | $0.000189 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.41s | $0.00023 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.97s | $0.000172 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.24s | $0.000196 |
| vip-lockout | yes | P2 | access | 0.9 | 0.97s | $0.000175 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.07s | $0.000158 |
| everything-down | yes | P1 | outage | 0.95 | 0.93s | $0.000166 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.66s | $0.00018 |
| ransom-note | yes | P1 | security | 0.9 | 0.92s | $0.000172 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.99s | $0.000154 |
