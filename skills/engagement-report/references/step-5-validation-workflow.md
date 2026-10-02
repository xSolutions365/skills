# Step 5 Workflow: Validate and hand off

## Objective

Verify evidence propagation, safety, compatibility, and standalone output.

## Required actions

1. Run:

   ```bash
   python3 -m unittest discover -s tests -p 'test_*.py'
   ```

2. For a generated period, inspect the Markdown:
   - `# Timeline` rows are chronological.
   - SOW boundaries, releases, and milestones from notes are present.
   - `# Plan visual` contains every accepted local image and remote link.
3. Inspect the HTML `REPORT` object:
   - `timeline` matches the Markdown events.
   - `plan_visuals` contains every accepted image.
   - local `src` values begin with `data:image/`.
   - remote records have `remote: true` and are not used as `<img src>`.
4. Open the HTML in a browser when visual inspection is available.
5. Verify a no-date/no-image period still renders without timeline or progress slides.
6. Include rejected attachment warnings in the handoff.

## Done when

- Targeted tests pass.
- Generated Markdown and HTML contain the expected dates and images.
- The no-evidence compatibility path passes.
