# Step 1 Workflow: Route content to rendering approach

## Objective

Choose one rendering mode with deterministic tie-break rules.

## Required actions

1. Classify the request using this matrix:
   - Architecture with rich card copy: CSS layout + [../templates/architecture.html](../templates/architecture.html)
   - Architecture where relationships dominate: Mermaid + [../templates/mermaid-flowchart.html](../templates/mermaid-flowchart.html)
   - Flowchart, sequence, data flow, ER, state, mind map: Mermaid
   - Comparison, audit, and matrix tables: semantic table + [../templates/data-table.html](../templates/data-table.html)
   - Slide deck request (`--slides` or explicit slide ask): slide mode + [../templates/slide-deck.html](../templates/slide-deck.html)
2. Apply deterministic tie-break behavior when multiple modes fit:
   - If output is primarily rows/columns, choose table mode.
   - If output is primarily edges/nodes, choose Mermaid mode.
   - If presentation format is explicitly requested, choose slide mode.
3. Capture selected mode and load list from [reference-loading-map.md](reference-loading-map.md).
4. If the request includes `--codex`, record that the default core style references are replaced by [codex-libraries.md](codex-libraries.md) and [codex-css-patterns.md](codex-css-patterns.md), with [codex-design-guardrails.md](codex-design-guardrails.md) applied as the final review pass.

## Done when

- Exactly one rendering mode is selected.
- Template and reference load list are fixed before authoring.
