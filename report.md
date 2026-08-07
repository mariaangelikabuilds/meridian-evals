# Meridian triage brains, scored

The same golden set of labeled incidents, real and adversarial, fired at both production brains.

| brain | pass rate | cases | total cost | median latency | failures | known context gaps |
|---|---|---|---|---|---|---|
| claude-sonnet-5 (Anthropic API) | 82% | 9/11 | $0.038 | 4.01s | real-night-kiosk, vip-lockout | real-partner-mailbox |
| gpt-4.1-mini (Azure Functions + Azure OpenAI) | 91% | 10/11 | $0.0023 | 2.54s | vague-slowness | real-partner-mailbox |

## claude: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.75 | 8.43s | $0.008028 |
| real-donor-export | yes | P2 | software | 0.65 | 3.23s | $0.002715 |
| real-partner-mailbox | known gap (Unterminated string starting at: line 1 column 523 (char 522) | - | - | 0 | 0s | $0 |
| real-night-kiosk | NO: error (Unterminated string starting at: line 1 column 568 (char 567) | - | - | 0 | 0s | $0 |
| calm-phish-click | yes | P1 | security | 0.85 | 4.01s | $0.003465 |
| quiet-security-tell | yes | P2 | security | 0.55 | 7.69s | $0.007992 |
| vip-lockout | NO: error (Unterminated string starting at: line 1 column 601 (char 600) | - | - | 0 | 0s | $0 |
| routine-onboarding | yes | P4 | access | 0.9 | 2.7s | $0.002655 |
| everything-down | yes | P1 | outage | 0.9 | 3.58s | $0.002688 |
| vague-slowness | yes | P4 | software | 0.55 | 4.24s | $0.002973 |
| ransom-note | yes | P1 | security | 0.98 | 7.94s | $0.003462 |
| after-hours-badge | yes | P2 | security | 0.75 | 5.33s | $0.004008 |

## azure: per case

| case | pass | severity | category | conf | latency | cost |
|---|---|---|---|---|---|---|
| real-imaging-down | yes | P1 | outage | 0.9 | 3.72s | $0.00019 |
| real-donor-export | yes | P2 | software | 0.9 | 2.5s | $0.000194 |
| real-partner-mailbox | known gap | P2 | software | 0.9 | 3.26s | $0.000194 |
| real-night-kiosk | yes | P2 | hardware | 0.9 | 3.16s | $0.000234 |
| calm-phish-click | yes | P2 | security | 0.9 | 3.56s | $0.000185 |
| quiet-security-tell | yes | P2 | hardware | 0.7 | 2.66s | $0.000196 |
| vip-lockout | yes | P2 | access | 0.9 | 2.5s | $0.000212 |
| routine-onboarding | yes | P4 | request | 0.9 | 2.19s | $0.000147 |
| everything-down | yes | P1 | outage | 0.95 | 2.54s | $0.000192 |
| vague-slowness | NO: category | P4 | performance | 0.6 | 2.42s | $0.000214 |
| ransom-note | yes | P1 | security | 0.9 | 2.05s | $0.000182 |
| after-hours-badge | yes | P2 | security | 0.9 | 2.09s | $0.000161 |
