# Reference Loading Map

## Objective

Define deterministic, minimal reference loading for each rendering mode.

## Mode-to-reference mapping

- Default core style/build rules for all modes:
  - [libraries.md](libraries.md)
  - [css-patterns.md](css-patterns.md)
- `--codex` core style/build swap:
  - Load [codex-libraries.md](codex-libraries.md) instead of [libraries.md](libraries.md).
  - Load [codex-css-patterns.md](codex-css-patterns.md) instead of [css-patterns.md](css-patterns.md).
  - Load [codex-design-guardrails.md](codex-design-guardrails.md) as the final anti-trope checklist.
  - Ignore all three Codex references entirely when `--codex` is absent.
- Multi-section navigation (4+ major sections):
  - [responsive-nav.md](responsive-nav.md)
- Slide mode:
  - [slide-patterns.md](slide-patterns.md)

## Template selection

- Rich architecture page: [../templates/architecture.html](../templates/architecture.html)
- Mermaid-first graph page: [../templates/mermaid-flowchart.html](../templates/mermaid-flowchart.html)
- Data table page: [../templates/data-table.html](../templates/data-table.html)
- Slide deck page: [../templates/slide-deck.html](../templates/slide-deck.html)

## Legacy references preserved in V1

- [css-patterns.md](css-patterns.md)
- [libraries.md](libraries.md)
- [codex-css-patterns.md](codex-css-patterns.md)
- [codex-libraries.md](codex-libraries.md)
- [codex-design-guardrails.md](codex-design-guardrails.md)
- [responsive-nav.md](responsive-nav.md)
- [slide-patterns.md](slide-patterns.md)

## Migration notes

- [migration-notes.md](migration-notes.md)
