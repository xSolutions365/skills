# Step 0 Workflow: Preflight target repo context

## Objective

Confirm the caller repository, documentation destinations, public entrypoints, and analysis boundaries before drafting any documentation.

## Required actions

1. Treat the caller repository as the working root for all path decisions in this workflow.
2. Detect whether `README.md` already exists.
3. Detect whether `docs/references/` already exists and whether it already contains topic docs that should be updated instead of duplicated.
4. Identify the public command surface the docs should prefer, such as:
   - root `Makefile` targets
   - root package-manager scripts
   - top-level CLIs
   - documented task runners
5. Record any analysis exclusions or user-granted path exceptions before reading deeper docs.
6. Decide the create-versus-update intent for each output path before drafting begins.

## Done when

- The repo root and intended output paths are explicit.
- The preferred public entrypoint surface is recorded.
- Path exclusions and permission boundaries are clear.
- The run knows whether it is creating or updating each target file.
