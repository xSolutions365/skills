# Design Options

- Created: 2026-03-30
- Last updated: 2026-03-30T16:37:00Z

## Candidate Approaches

### Option 1

- Summary: Keep the current wrapper and rely on stronger prompt wording alone to tell child phases not to delegate or recurse.
- Pros:
  - Minimal code change in one file.
  - Leaves the wrapper and test harness shape almost untouched.
- Cons:
  - Proven insufficient because inherited global Codex instructions can override the prompt and still trigger `spawn_agent`.
  - Does not address the schema failure or the missing sandbox behavior discovered during live reproduction.

### Option 2

- Summary: Isolate child runs behind a temporary `CODEX_HOME`, seed only the auth file, pass an explicit `workspace-write` sandbox, and harden the prompt/schema so the child phase has the minimum runtime surface required for staged-artifact work.
- Pros:
  - Directly removes inherited global AGENTS/skills/state from the child runtime.
  - Fixes the schema failure and preserves the existing deterministic controller flow required by R1.
  - Is regression-testable with the current helper and live smoke harnesses, satisfying R3.
- Cons:
  - Leaves the separate brownfield research-staging gap unresolved for phases that need source evidence not present in the staged workspace.

### Option 3

- Summary: Redesign the whole planning controller so parent phases precompute and stage source excerpts or evidence snapshots for every downstream brownfield phase.
- Pros:
  - Solves the research-staging gap comprehensively.
  - Makes isolated phases more self-sufficient for brownfield work.
- Cons:
  - Much broader than the immediate isolation defect.
  - Increases controller complexity and is unnecessary to fix the reproduced nested-agent bug.

## Selected Direction

- Chosen option: Option 2
- Rationale: It is the narrowest change that fixes the reproduced schema failure and nested child-agent recursion while preserving the existing plan package structure and verification surface.
- Rejected alternatives: Option 1 rejected because prompt-only controls already failed in live reproduction; Option 3 rejected as follow-on design work outside the immediate defect scope.
