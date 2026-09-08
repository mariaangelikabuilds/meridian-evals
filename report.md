# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 91% | 10/11 | $0.0446 | 3.69s | vip-lockout | none |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0022 | 1.54s | real-imaging-down | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.62 | 3.01s | $0.003573 |
| real-donor-export | yes | P2 | software | 0.65 | 2.99s | $0.00282 |
| real-partner-mailbox | yes | P1 | software | 0.85 | 3.69s | $0.003141 |
| real-night-kiosk | yes | P3 | hardware | 0.6 | 4.93s | $0.004224 |
| calm-phish-click | yes | P2 | security | 0.75 | 4.53s | $0.003945 |
| quiet-security-tell | yes | P2 | security | 0.55 | 7.01s | $0.006597 |
| vip-lockout | NO: min_severity | P3 | access | 0.7 | 2.59s | $0.003015 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.16s | $0.00258 |
| everything-down | yes | P1 | outage | 0.85 | 3.26s | $0.003903 |
| vague-slowness | yes | P4 | software | 0.55 | 3.18s | $0.003633 |
| ransom-note | yes | P1 | security | 0.98 | 4.26s | $0.003417 |
| after-hours-badge | yes | P2 | security | 0.72 | 4.98s | $0.003738 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | NO: category | P1 | network | 0.9 | 4.1s | $0.00022 |
| real-donor-export | yes | P1 | software | 0.9 | 1.27s | $0.000203 |
| real-partner-mailbox | known gap | P2 | access | 0.9 | 1.87s | $0.000171 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 2.07s | $0.000235 |
| calm-phish-click | yes | P2 | security | 0.9 | 1.26s | $0.000158 |
| quiet-security-tell | yes | P2 | hardware | 0.8 | 1.34s | $0.00021 |
| vip-lockout | yes | P2 | access | 0.9 | 1.89s | $0.000182 |
| routine-onboarding | yes | P4 | request | 0.9 | 1.79s | $0.000152 |
| everything-down | yes | P1 | outage | 0.95 | 1.09s | $0.000184 |
| vague-slowness | yes | P3 | hardware | 0.7 | 1.54s | $0.000169 |
| ransom-note | yes | P1 | security | 0.9 | 1.02s | $0.000187 |
| after-hours-badge | yes | P2 | security | 0.9 | 0.94s | $0.000154 |
