# Codex CSS Patterns

## Objective

Provide the strict `--codex` replacement for `css-patterns.md` covering backgrounds, components, layout composition, and motion with an Uncodixfy-style bias for points 1-4.

## Activation rule

- Use this file only when the request includes `--codex`.
- In `--codex` mode, use this file instead of [css-patterns.md](css-patterns.md).

## Theme setup

Use a restrained page frame first. Let structure and spacing carry hierarchy before effects.

```css
:root {
  --font-body: "IBM Plex Sans", "Public Sans", sans-serif;
  --font-mono: "IBM Plex Mono", "Source Code Pro", monospace;

  --bg: #f7f5f2;
  --surface: #fffcf8;
  --surface-muted: #f0ebe5;
  --border: rgba(28, 25, 23, 0.12);
  --text: #1f1a17;
  --text-dim: #5f584f;
  --accent: #7c4a2a;
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #171412;
    --surface: #211d1a;
    --surface-muted: #2a2521;
    --border: rgba(245, 240, 232, 0.12);
    --text: #f5f0e8;
    --text-dim: #c4b8a8;
    --accent: #c78a5c;
  }
}
```

## Background rules

- Default to flat or lightly textured backgrounds.
- Small paper grain, ruled-line, or subtle grid textures are acceptable when they support the content.
- Do not use radial glow fields, glass haze, or decorative gradient meshes as the default background language.

```css
body {
  background: var(--bg);
  color: var(--text);
}

body[data-surface="paper"] {
  background-image: linear-gradient(
    rgba(0, 0, 0, 0.02) 1px,
    transparent 1px
  );
  background-size: 100% 28px;
}
```

## Panels and cards

- Use simple bordered containers with 8-12px radius.
- Prefer one panel style per page.
- No floating glass shells, oversized rounded rectangles, or decorative hero cards by default.
- If emphasis is needed, change density, border weight, or background tone before using shadow.

```css
.ve-panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  padding: 18px 20px;
}

.ve-panel--muted {
  background: var(--surface-muted);
}

.ve-panel--emphasis {
  border-color: color-mix(in srgb, var(--border) 40%, var(--accent) 60%);
}
```

## Labels and headings

- Plain section headings are allowed.
- Small uppercase labels, status dots, and ornamental section chips are not default patterns in `--codex` mode.
- If categorization is required, use inline plain text metadata instead of decorative badges.

## Layout composition

- Prefer content-shaped layouts over generic SaaS dashboards.
- Valid defaults:
  - single reading column for narrative explainers
  - two-column comparison or dossier layout
  - narrow rail only when navigation or metadata genuinely needs it
  - dense table-first layouts for audits and inventories
- Avoid default KPI strips, symmetric marketing-card grids, and empty “premium” whitespace.

```css
.dossier {
  display: grid;
  grid-template-columns: minmax(0, 280px) minmax(0, 1fr);
  gap: 24px;
}

.comparison {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 20px;
}

.stack {
  display: grid;
  gap: 16px;
}

@media (max-width: 900px) {
  .dossier,
  .comparison {
    grid-template-columns: 1fr;
  }
}
```

## Tables

- Keep tables dense, left-aligned, and readable.
- Prefer text and subtle background changes over badge-heavy status styling.
- Do not convert tables into card mosaics unless the request explicitly calls for that presentation.

## Mermaid containers

- Wrap Mermaid in a restrained container with border and padding.
- Center the diagram and preserve readable scale.
- Avoid decorative shells around the graph.

```css
.mermaid-wrap {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  min-height: 320px;
  padding: 24px;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 10px;
  overflow: auto;
}
```

## Motion rules

- Motion is optional and quiet.
- Prefer color/opacity transitions only.
- Avoid hover lifts, drifting cards, scale pops, bounce, and theatrical stagger as the default.

```css
a,
button,
.ve-panel {
  transition:
    color 0.15s ease,
    background-color 0.15s ease,
    border-color 0.15s ease,
    opacity 0.15s ease;
}
```

## Hard bans in `--codex` mode

- No glassmorphism default shell
- No radial glow dashboards
- No decorative hero strip unless the content truly needs a narrative lead
- No KPI-card grid as the automatic opening move
- No pill badges or chip clutter
- No oversized shadows or hover transform effects
- No multiple ornamental panel families on one page

## Decision rule

If a styling choice makes the page feel more like a generic AI-generated product dashboard than a purpose-built explainer, remove it.
