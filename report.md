# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0432 | 3.04s | vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.42s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.65 | 3.09s | $0.003648 |
| real-donor-export | yes | P2 | software | 0.65 | 2.62s | $0.003015 |
| real-partner-mailbox | known gap | P2 | software | 0.72 | 2.94s | $0.003321 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 3.81s | $0.003939 |
| calm-phish-click | yes | P2 | security | 0.85 | 3.24s | $0.0036 |
| quiet-security-tell | yes | P2 | security | 0.55 | 6.79s | $0.007527 |
| vip-lockout | NO: min_severity | P3 | access | 0.75 | 3.04s | $0.003525 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.26s | $0.00255 |
| everything-down | yes | P1 | network | 0.9 | 2.31s | $0.002643 |
| vague-slowness | yes | P4 | software | 0.55 | 2.8s | $0.003078 |
| ransom-note | yes | P1 | security | 0.97 | 2.37s | $0.002682 |
| after-hours-badge | yes | P2 | security | 0.65 | 3.15s | $0.003693 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 2.93s | $0.000191 |
| real-donor-export | yes | P2 | software | 0.9 | 1.27s | $0.000189 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 1.5s | $0.000198 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 1.1s | $0.000186 |
| calm-phish-click | yes | P2 | security | 0.8 | 1.46s | $0.000184 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.42s | $0.000188 |
| vip-lockout | yes | P2 | access | 0.9 | 1.37s | $0.000194 |
| routine-onboarding | yes | P4 | request | 0.95 | 1.39s | $0.000189 |
| everything-down | yes | P1 | outage | 1 | 1.47s | $0.000177 |
| vague-slowness | yes | P3 | software | 0.7 | 1.3s | $0.000177 |
| ransom-note | yes | P1 | security | 0.95 | 1.54s | $0.00019 |
| after-hours-badge | yes | P2 | security | 0.8 | 1.13s | $0.000175 |
