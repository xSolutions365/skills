# Codex Design Guardrails

## Objective

Add an opt-in anti-trope pass for Codex-authored visual explainers when the request includes `--codex`.

## Source and scope

- This reference adapts the anti-pattern guidance from [Uncodixfy](https://github.com/cyxzdev/Uncodixfy/tree/main) for the `visual-explainer` skill.
- Treat it as a selective guardrail set, not a literal style transplant.
- When this guidance conflicts with an established product design system or explicit user direction, preserve the existing product language first.
- In `--codex` mode this file is not additive on top of the default core references; it works with [codex-libraries.md](codex-libraries.md) and [codex-css-patterns.md](codex-css-patterns.md), which replace the default style references for points 1-4.

## Activation rule

- Load this reference only when the request explicitly includes `--codex`.
- When active, pair it with [codex-libraries.md](codex-libraries.md) and [codex-css-patterns.md](codex-css-patterns.md) instead of the default core references.
- If `--codex` is absent, ignore this file completely.

## What this guardrail is trying to prevent

Codex tends to drift toward a recognizable default AI aesthetic: soft "premium" gradients, floating glass panels, over-rounded cards, decorative eyebrow labels, generic hero blocks, hollow KPI grids, and safe default typography/color choices that make outputs feel templated instead of designed.

## Required behavior when enabled

1. Start with a visual thesis before writing HTML or CSS.
   - Pick a concrete tone such as editorial brief, technical operations board, archival reference sheet, transit-map explainer, or lab notebook.
   - The layout, type, color, and motion should all reinforce that one tone.
2. Prefer product-shaped structure over generic AI-dashboard structure.
   - Use the structure implied by the request: diagram sheet, architecture dossier, audit table, sequence view, or slide narrative.
   - Do not default to hero, KPI strip, feature cards, and sidebar shell unless the content truly needs them.
3. Use restrained, content-led hierarchy.
   - Plain headings are fine.
   - Decorative eyebrow labels, faux marketing copy, and explanatory filler text are not.
4. Choose typography intentionally.
   - Reuse project typography if it exists.
   - Otherwise choose a distinctive family that fits the tone and avoids default AI stacks.
   - Do not fall back to `Inter`, `Roboto`, `Arial`, `Segoe UI`, or generic system-only stacks unless the project already uses them.
5. Keep color calm and deliberate.
   - Reuse project colors when available.
   - Otherwise select a compact palette with strong text contrast and one clear accent family.
   - Avoid purple/indigo default AI palettes unless the project brand requires them.
6. Use depth sparingly.
   - Prefer borders, spacing, and contrast before shadow.
   - If shadow is used, keep it subtle and functional.
7. Keep motion quiet.
   - Favor opacity/color transitions over movement.
   - Avoid hover lifts, drifting panels, bounce, and "premium" motion flourishes.
8. Make distinct layout choices.
   - Vary silhouette, alignment, density, and sectional rhythm to match the content.
   - Avoid centered-max-width-plus-even-card-grid as the automatic answer.

## Explicit anti-pattern bans when enabled

- No floating glass shell as the default page frame.
- No oversized rounded corners across every component.
- No pill badges, chips, or tags unless they communicate real state.
- No decorative "live", "pulse", "snapshot", "focus", or "operator" labels unless the request or product voice requires them.
- No hero section inside internal dashboards or explainers unless the content genuinely needs a narrative lead block.
- No filler KPI cards, fake charts, or ornamental metrics.
- No gradient text, glow haze, cyan-on-blue dark themes, or default AI "control room" styling.
- No section-intro copy that merely explains what the section already shows.
- No mixing multiple ornamental panel styles on the same page.

## Adapted implementation rules for visual explainer outputs

- Mermaid outputs:
  - Keep surrounding chrome minimal so the diagram remains the focal artifact.
  - Use the page frame to support reading, not to compete with the graph.
- Table outputs:
  - Favor dense, readable tabular structure over decorative cards pretending to be tables.
  - Keep status treatments textual or lightly accented rather than badge-heavy.
- Architecture pages:
  - If cards are used, vary emphasis through spacing, scale, and grouping before adding visual effects.
  - Avoid turning every subsystem into the same rounded rectangle.
- Slide outputs:
  - Each slide needs a clear editorial point, not a generic "presentation mode" skin.
  - Avoid title-slide theatrics and decorative dividers that add no meaning.

## Final review checklist when enabled

- Did the run use the Codex replacement references instead of the default expressive ones?
- Can the page be described with a specific visual thesis instead of "modern AI dashboard"?
- Would removing gradients, glow, and badge clutter leave the hierarchy intact?
- Did the layout emerge from the content, or from a default SaaS template?
- Are headings plain and useful rather than decorative?
- Are type, color, and spacing choices deliberate enough to feel authored?
- Did any generic Codex tropes slip back in during polishing?
