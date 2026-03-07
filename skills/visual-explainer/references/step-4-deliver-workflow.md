# Step 4 Workflow: Deliver and quality-check

## Objective

Deliver a usable output file with mandatory visual and behavior checks.

## Required actions

1. Write the final HTML file to `<project-root>/.visual-explainer/` using a descriptive filename.
2. Open the file using platform-appropriate command (`open` or `xdg-open`).
3. Verify quality checklist:
   - Hierarchy is obvious on initial view.
   - Requested information is complete and not reduced to decorative output.
   - Overflow protections are applied where needed.
   - Mermaid visuals include required controls when Mermaid is used.
   - File loads without broken links or runtime errors.
4. Report final file path and any known limitations.

## Done when

- The file opens successfully from the generated path.
- Quality checks pass and handoff includes output path plus constraint notes.
