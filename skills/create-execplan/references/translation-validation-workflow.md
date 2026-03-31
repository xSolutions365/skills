# Translation Validation Workflow

## Objective

Run one concise skeptical review before any user-facing approval gate so candidate artifacts are checked against their authoritative inputs for loss, weakening, optionality drift, and unsupported inference.

## Required actions

1. Choose the candidate artifact and its authoritative input set for the current step.
2. Use one fresh-context skeptical evaluator when available:
   - prefer one fresh worker subagent with no prior thread context
   - give it only the explicit input set plus the candidate artifact under review
   - instruct it to compare source obligations against the artifact and report only material translation defects
3. If a fresh worker subagent is unavailable, perform an equivalent skeptical review without relying on prior conversational memory.
4. Apply this review question set:
   - Did the artifact preserve the same normative force as the source?
   - Did it introduce optionality, fallback behavior, or advisory language not present in the source?
   - Did it drop operative semantics, named controls, named tools, named ADR actions, sequencing constraints, or compliance details?
   - Did it overstate the sufficiency of an existing baseline that the source marked as missing or inadequate?
   - Did it silently infer a missing decision instead of flagging ambiguity?
5. Record the result in `workspace/translation-validation.md` with:
   - step identifier
   - candidate artifact
   - authoritative inputs reviewed
   - verdict (`pass` or `fail`)
   - concise findings summary
   - resolution status (`resolved` or `blocked`)
   - timestamp
6. If the verdict is `fail`, resolve the findings before presenting the artifact to the user for approval.
7. Do not ask the user for approval while any translation-validation entry for the current step remains unresolved.

## Done when

- The current approval-gated artifact has a fresh skeptical validation entry in `workspace/translation-validation.md`.
- Any material translation defects are corrected before the artifact reaches the user.
