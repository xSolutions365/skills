# Step 2 Workflow: Build structure and style

## Objective

Assemble a self-contained HTML document with intentional hierarchy and styling.

## Required actions

1. Build semantic HTML structure with clear sections, headings, and table semantics where relevant.
2. Define CSS custom properties for base surfaces, text, borders, and accent palette.
3. Apply typography, color, and external-library rules from the active core library reference selected in [reference-loading-map.md](reference-loading-map.md):
   - Default: [libraries.md](libraries.md)
   - `--codex`: [codex-libraries.md](codex-libraries.md)
4. Apply layout, overflow, component, and motion rules from the active pattern reference selected in [reference-loading-map.md](reference-loading-map.md):
   - Default: [css-patterns.md](css-patterns.md)
   - `--codex`: [codex-css-patterns.md](codex-css-patterns.md)
5. If `--codex` is present, apply the final anti-trope checks from [codex-design-guardrails.md](codex-design-guardrails.md).
6. Keep substantial mode-specific implementation details in the mode references, not in `SKILL.md`.

## Done when

- Document structure is semantic and readable.
- Theme and hierarchy are explicit and consistent.
- The active default-or-Codex core references are applied explicitly based on the request flags.
- Styling guardrails are satisfied without duplicating reference content.
