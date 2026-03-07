# Codex Libraries

## Objective

Provide the strict `--codex` replacement for `libraries.md` covering typography, color selection, and external-library usage without default AI-dashboard styling.

## Activation rule

- Use this file only when the request includes `--codex`.
- In `--codex` mode, use this file instead of [libraries.md](libraries.md).

## Typography rules

- Reuse project typography when it exists.
- Otherwise choose restrained, non-default families that fit the content and avoid generic AI output.
- Preferred fallbacks:
  - Sans: `"IBM Plex Sans"`, `"Public Sans"`, `"Source Sans 3"`, sans-serif
  - Mono: `"IBM Plex Mono"`, `"Source Code Pro"`, monospace
- Do not default to `Inter`, `Roboto`, `Arial`, `Segoe UI`, or generic system-only stacks unless the project already uses them.
- Plain headings are allowed and required for structure.
- Decorative eyebrow labels, uppercase section badges, and ornamental mini-headings are not allowed by default.

## Color rules

- Reuse project colors when available.
- Otherwise use a compact, calm palette with one accent family and strong text contrast.
- Prefer charcoal, stone, slate, moss, rust, ink, sand, or muted teal over neon/cyan control-room palettes.
- Avoid purple/indigo defaults unless the project brand requires them.
- Avoid gradient text, glow accents, and color choices whose only purpose is to look "premium."

## External-library rules

- Only include external JS when it materially improves the output.
- Mermaid remains the preferred graph engine for flowcharts, sequences, ER diagrams, state views, and mind maps where automatic routing is useful.
- Data tables should remain semantic HTML tables.
- Avoid decorative chart libraries unless the request actually needs charted quantitative data.

## Mermaid guidance for `--codex`

- Keep Mermaid page chrome minimal. The diagram should remain the focal artifact.
- Use `theme: "base"` so colors remain controllable and predictable.
- Use calm theme variables that match the page palette; avoid cyan-neon dark mode styling.
- Prefer simple containers with border, padding, and readable spacing before adding extra surfaces.
- Keep labels readable and neutral rather than aggressively branded.

### Minimal Mermaid initialization pattern

```html
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs"

  const isDark = window.matchMedia("(prefers-color-scheme: dark)").matches

  mermaid.initialize({
    startOnLoad: true,
    theme: "base",
    look: "classic",
    themeVariables: {
      primaryColor: isDark ? "#262626" : "#f5f5f4",
      primaryBorderColor: isDark ? "#525252" : "#78716c",
      primaryTextColor: isDark ? "#f5f5f5" : "#1c1917",
      secondaryColor: isDark ? "#1f2937" : "#f3f4f6",
      secondaryBorderColor: isDark ? "#4b5563" : "#9ca3af",
      secondaryTextColor: isDark ? "#f9fafb" : "#111827",
      tertiaryColor: isDark ? "#292524" : "#fafaf9",
      tertiaryBorderColor: isDark ? "#78716c" : "#a8a29e",
      tertiaryTextColor: isDark ? "#f5f5f4" : "#292524",
      lineColor: isDark ? "#737373" : "#a8a29e",
      noteBkgColor: isDark ? "#1c1917" : "#fafaf9",
      noteBorderColor: isDark ? "#57534e" : "#a8a29e",
      noteTextColor: isDark ? "#f5f5f4" : "#292524",
      fontFamily: "var(--font-body)",
      fontSize: "16px",
    },
  })
</script>
```

## Decision rule

If a library, font, or color move feels like a shortcut to "designed by AI," reject it and choose the cleaner, more product-shaped option.
