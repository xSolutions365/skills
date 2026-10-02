# Step 2 Workflow: Collect period evidence

## Objective

Convert notes into a reviewable set of timeline events and report images.

## Required actions

1. Read [source-note-conventions.md](source-note-conventions.md).
2. Scan every Markdown file under the period's `notes/` tree, including `notes/processed/`.
3. Extract explicit timeline tables and list entries first.
4. Extract ordinary prose only when it contains an ISO date and milestone language such as SOW, statement of work, release, milestone, launch, go-live, deadline, phase, kickoff, start, or end.
5. When a non-ISO date is unambiguous from context, normalize it to ISO in the report and retain the original note as evidence.
6. Deduplicate equivalent date-and-label pairs and sort events by date, then label.
7. Extract Markdown images with alt text and optional title captions.
8. Include unreferenced attachments only from a note-local `assets/` or `images/` directory.
9. Copy valid local images into `assets/report/` using collision-safe names.
10. Record remote `https://` images as links. Do not download, proxy, or embed them.
11. Report rejected image references rather than silently replacing them.

## Done when

- Dated events are normalized, deduplicated, and chronological.
- Every image has a caption, source, kind, and local-or-remote disposition.
- Unsafe or unsupported references are visible in command output.
