# Step 4 Workflow: Render the standalone presentation

## Objective

Render portable HTML from the canonical Markdown report.

## Required actions

1. Run `generate` or `update`; both rebuild the presentation.
2. Preserve legacy data consumers:
   - `REPORT.plan_visual` is `null` when absent.
   - `REPORT.plan_visual` is the single local image data URI when exactly one local image exists.
   - `REPORT.timeline` remains an array of `{date, label, type}` objects.
3. Use `REPORT.plan_visuals` for zero, one, or many local and remote image records.
4. Create one progress-visual slide per image so multiple charts remain readable.
5. Embed copied local assets as data URIs.
6. Render remote images as safe external links with `noopener noreferrer`; never use their URLs as image sources.
7. Render the timeline as a chronological vertical card grid with past, current, and future states relative to `period_end`.
8. Add a single `Reporting date` marker only if no event already falls on `period_end`.
9. Escape report text and JSON data before inserting them into HTML.

## Done when

- The HTML opens without local file dependencies.
- Multiple images and dense timelines remain legible.
- Remote content is not fetched by the presentation.
