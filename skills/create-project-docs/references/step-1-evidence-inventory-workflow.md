# Step 1 Workflow: Inventory repo evidence

## Objective

Build a source-backed inventory of commands, concepts, workflows, and artifacts that generated docs may cite.

## Required actions

1. Inspect the repo's public entrypoint files first, then widen only as needed:
   - `README.md`
   - root `Makefile`
   - package-manager manifests
   - top-level CLI entrypoints
   - root config files that define setup or execution behavior
2. Extract the canonical setup path, first successful run path, quality gates, and recurring workflows from repo evidence.
3. Record the top-level project nouns and plain-English explanations for each one.
4. Capture every proposed command, environment variable, file path, and example with a source path so the generated docs can justify them later.
5. Mark gaps explicitly when the repo appears to need a section but the evidence is missing or contradictory.
6. Prefer the smallest sufficient evidence set and do not pull in additional docs unless they materially improve coverage.

## Done when

- The inventory covers setup, quick start, project purpose, core concepts, and deeper workflows.
- Each planned documentation claim traces to at least one source path.
- Missing or contradictory evidence is recorded explicitly instead of papered over.
