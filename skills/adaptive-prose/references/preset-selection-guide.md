# Preset Selection Guide

## Objective

Choose one preset that matches the task and audience, then hold that preset consistently through drafting and review.

## Required actions

1. Require `--preset` at preflight and reject the run if it is missing.
2. Accept these canonical preset values and shorthand selectors:
   - `operator-brief`
   - `operator`
   - `brief`
   - `technical-deep-dive`
   - `technical`
   - `deep-dive`
   - `narrative-explainer`
   - `narrative`
   - `explainer`
   - `executive-decision-brief`
   - `executive`
   - `exec`
   - `exec-summary`
   - `surgical-redraft`
   - `surgical`
   - `voice-shift-redraft`
   - `voice-shift`
3. Normalize any shorthand selector to a canonical preset name before loading guidance:
   - `operator-brief` -> [preset-operator-brief.md](preset-operator-brief.md)
   - `operator` -> `operator-brief`
   - `brief` -> `operator-brief`
   - `technical-deep-dive` -> [preset-technical-deep-dive.md](preset-technical-deep-dive.md)
   - `technical` -> `technical-deep-dive`
   - `deep-dive` -> `technical-deep-dive`
   - `narrative-explainer` -> [preset-narrative-explainer.md](preset-narrative-explainer.md)
   - `narrative` -> `narrative-explainer`
   - `explainer` -> `narrative-explainer`
   - `executive-decision-brief` -> [preset-executive-decision-brief.md](preset-executive-decision-brief.md)
   - `executive` -> `executive-decision-brief`
   - `exec` -> `executive-decision-brief`
   - `exec-summary` -> `executive-decision-brief`
   - `surgical-redraft` -> [preset-surgical-redraft.md](preset-surgical-redraft.md)
   - `surgical` -> `surgical-redraft`
   - `voice-shift-redraft` -> [preset-voice-shift-redraft.md](preset-voice-shift-redraft.md)
   - `voice-shift` -> `voice-shift-redraft`
4. Load the reference guide for the canonical preset name, not the shorthand alias.
5. Choose the preset that matches the primary job of the text, not a secondary preference.
6. If two presets seem plausible, pick the one that best matches the reader outcome and state the tradeoff before drafting.
7. Do not blend presets in a single pass. Finish one pass cleanly before changing preset.

## Done when

- Exactly one canonical preset is selected and named.
- The selected preset matches the reader outcome better than the alternatives.
- The drafter can explain why this preset is the primary fit.
