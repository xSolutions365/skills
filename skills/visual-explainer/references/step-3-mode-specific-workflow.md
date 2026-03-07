# Step 3 Workflow: Apply mode-specific rules

## Objective

Apply the chosen mode's deep requirements while loading only necessary reference files.

## Required actions

1. For Mermaid-based modes:
   - Apply Mermaid theming and direction guidance from the active core library reference selected in [reference-loading-map.md](reference-loading-map.md).
   - Apply container, scaling, and zoom/pan controls from the active pattern reference selected in [reference-loading-map.md](reference-loading-map.md).
2. For table-heavy modes:
   - Apply semantic table and sticky header patterns from the active pattern reference selected in [reference-loading-map.md](reference-loading-map.md).
   - Use reference table composition from [../templates/data-table.html](../templates/data-table.html).
3. For multi-section pages (4+ sections):
   - Apply navigation behavior from [responsive-nav.md](responsive-nav.md).
4. For slide mode:
   - Apply planning/completeness and slide engine rules from [slide-patterns.md](slide-patterns.md).
   - Use [../templates/slide-deck.html](../templates/slide-deck.html) as structural reference.
5. If `--codex` is present:
   - Run one explicit pass against [codex-design-guardrails.md](codex-design-guardrails.md) before finalizing.
   - Confirm the output uses the strict Codex core references instead of the default expressive ones.
   - Remove decorative hero copy, default AI-dashboard motifs, and generic typography/color shortcuts that slipped in during mode-specific authoring.

## Done when

- Mode-specific requirements are applied for the selected output.
- Irrelevant mode references are not loaded.
