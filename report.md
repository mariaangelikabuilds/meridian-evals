# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0387 | 2.53s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.35s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.6 | 2.45s | $0.003423 |
| real-donor-export | yes | P2 | software | 0.72 | 2.53s | $0.00333 |
| real-partner-mailbox | known gap | P2 | software | 0.7 | 2.92s | $0.003486 |
| real-night-kiosk | yes | P2 | hardware | 0.6 | 2.84s | $0.004209 |
| calm-phish-click | yes | P2 | security | 0.75 | 2.65s | $0.003315 |
| quiet-security-tell | yes | P2 | security | 0.55 | 3.1s | $0.003717 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 1.91s | $0.002955 |
| routine-onboarding | yes | P4 | access | 0.9 | 1.76s | $0.00267 |
| everything-down | yes | P1 | outage | 0.9 | 1.37s | $0.002478 |
| vague-slowness | yes | P4 | software | 0.55 | 2.19s | $0.002733 |
| ransom-note | yes | P1 | security | 0.98 | 2.02s | $0.002757 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.0s | $0.003618 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 3.72s | $0.000207 |
| real-donor-export | yes | P2 | software | 0.9 | 1.44s | $0.000198 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 0.97s | $0.00017 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.41s | $0.0002 |
| calm-phish-click | yes | P2 | security | 0.9 | 0.99s | $0.000163 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.35s | $0.000224 |
| vip-lockout | yes | P2 | access | 0.9 | 1.35s | $0.000196 |
| routine-onboarding | yes | P4 | request | 0.95 | 0.87s | $0.000144 |
| everything-down | yes | P1 | outage | 0.95 | 0.99s | $0.000196 |
| vague-slowness | yes | P3 | software | 0.8 | 1.3s | $0.000185 |
| ransom-note | yes | P1 | security | 0.9 | 0.88s | $0.000153 |
| after-hours-badge | yes | P2 | security | 0.9 | 1.54s | $0.00019 |
