# Step 0 Workflow: Confirm the reporting context

## Objective

Establish explicit paths and compatibility constraints before generating output.

## Required actions

1. Locate the repository root that contains engagement directories.
2. Identify the engagement slug and ISO `period_start` and `period_end`.
3. Confirm `period_start <= period_end`.
4. Locate the period `notes/` tree and any existing `*-report.md` and `*-presentation.html`.
5. Read the previous period report when it is available, but treat current-period notes as the authority for changed facts.
6. Preserve these canonical report headings:
   - `# Overall`
   - `# Key points`
   - `# Plan visual`
   - `# Actions`
   - `# Key RAIDs`
   - `# Casting`
   - `# Timeline`
7. Resolve every local note attachment inside the reporting-period directory. Reject absolute paths, traversal outside the period, symlinks that escape it, and unsupported file types.

## Done when

- Repository, engagement, dates, notes, and output paths are explicit.
- Existing output and prior-period evidence have been identified.
- No source path outside the reporting-period trust boundary will be copied.
