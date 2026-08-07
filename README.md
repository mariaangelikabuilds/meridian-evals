# meridian-evals

An evaluation pipeline for the triage brains behind [meridian-ops](https://github.com/mariaangelikabuilds/meridian-ops),
the 24/7 agent fleet, and its Azure re-platform
[meridian-brain-azure](https://github.com/mariaangelikabuilds/meridian-brain-azure).

Two production brains do the same job in different clouds: Claude (Anthropic API)
inside the fleet, and gpt-4.1-mini behind an Azure Function via an AI Foundry
deployment. This repo answers, with numbers, the questions that matter before
trusting either of them: does the judgment hold on hard cases, do the safety
gates actually fire, what does a verdict cost, and how fast does it come back.

## How it works

- `evals/golden.jsonl` is the golden set: incidents taken from the fleet's real
  event log plus authored adversarial cases. Each carries expectation bounds, not
  exact labels, because reasonable triage has range: a minimum severity, an
  allowed category set, and for security-flavored cases a hard requirement that
  the severity floor holds.
- `evals/brains.py` calls the two real deployed brains, not mocks.
- `evals/score.py` grades each verdict against its bounds and rolls up pass rate,
  total cost, and median latency per brain.
- `report.md` in this repo is a real committed run, not an illustration.

## Run it

```
ANTHROPIC_API_KEY=... AZURE_BRAIN_URL=... AZURE_BRAIN_KEY=... python -m evals.run --brain both
```

## What it caught before its first run

Writing the harness's unit tests exposed a latent bug in the production security
floor: the regex `\b(phish|ransom|...)\b` never matched "phishing" or
"ransomware", because the trailing word boundary demanded the keyword end the
word. The bug had survived three deployments in two codebases; earlier tests
passed because their fixtures happened to match other branches. The fix and
regression tests shipped to both clouds the same hour. That is the argument for
evaluation pipelines in one sentence.

## Findings from the committed run

- gpt-4.1-mini behind the Azure Function scored 12/12 at $0.0022 total with 2.85s
  median latency. claude-sonnet-5 scored 10/12 at $0.0398 and 4.59s.
- Both sonnet misses were client-context severity calls: a named-partner mailbox
  that is P1 by that client's contract, and a VIP lockout. Neither brain receives
  client profiles; in production the fleet's profile-aware skeptic covers exactly
  this gap, which is the architectural argument the numbers make.
- The first run also caught a coverage drift between the three gate
  implementations (the antivirus and quarantine tells were missing from the
  deployed regexes) and a token-starvation bug in this harness's own Claude
  runner. Both fixed, both regression-tested, both redeployed before this run.
- Interpretation, honestly bounded: this golden set rewards rubric-following
  under floors, not open-ended judgment. It says the cheap model is the right
  triage engine here; it does not say it is the better model in general.
