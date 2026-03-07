# Step 0 Workflow: Preflight context and constraints

## Objective

Lock destination, constraints, and required references before any HTML generation.

## Required actions

1. Confirm the project root as the git top-level from the current working directory when available; otherwise use the current working directory.
2. Confirm the output path will be `<project-root>/.visual-explainer/<descriptive-name>.html`.
3. Parse optional request flags before selecting references:
   - `--slides`: enable slide mode when the request also needs presentation formatting.
   - `--codex`: replace the default core references with [codex-libraries.md](codex-libraries.md) and [codex-css-patterns.md](codex-css-patterns.md), then load [codex-design-guardrails.md](codex-design-guardrails.md).
   - Any request without `--codex`: use [libraries.md](libraries.md) and [css-patterns.md](css-patterns.md), and do not load the Codex-only references.
4. Confirm browser-open command for current OS (`open` on macOS, `xdg-open` on Linux).
5. Check whether `surf` is installed with `which surf` and record availability.
6. Choose the minimal set of references to load using [reference-loading-map.md](reference-loading-map.md).
7. Confirm which template (if any) should be used for the selected mode.

## Done when

- Project root, output path, and open command are fixed.
- Optional flags and their impact on reference swapping/loading are explicit.
- Tool availability constraints are explicit.
- Required references and template are identified before build.
