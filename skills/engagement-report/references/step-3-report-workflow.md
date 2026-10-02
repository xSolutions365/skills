# Step 3 Workflow: Draft or update the report

## Objective

Maintain one canonical Markdown report with evidence-backed narrative, dates, and images.

## Required actions

1. Run `generate` for a missing period or `update` for an existing period:

   ```bash
   python3 scripts/engagement_report.py update --period <period-directory>
   ```

2. Let the command create or refresh only:
   - report frontmatter fields needed for presentation rendering
   - `# Plan visual`
   - `# Timeline`
3. Preserve all other existing report sections.
4. For a new skeleton, use [the report template](../assets/templates/report-template.md), then synthesize `Overall`, `Key points`, `Actions`, `Key RAIDs`, and `Casting` from notes.
5. Keep local images as Markdown images pointing to copied `assets/report/` files.
6. Keep remote images as labelled Markdown links, not inline images.
7. Represent timeline events in a `Date | Event | Type` table.
8. Keep SOW boundaries, releases, and milestones as ordinary event rows rather than special one-off fields.
9. Do not add a `Today` row. Presentation rendering supplies one reporting-date marker only when the period end has no event.

## Done when

- The Markdown report is the canonical, human-readable source.
- Managed sections match note evidence without duplicating markers.
- Narrative and status claims are traceable to notes.
