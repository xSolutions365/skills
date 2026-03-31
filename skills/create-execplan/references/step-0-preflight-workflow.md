# Step 0 Workflow: Preflight and scaffold

## Objective

Establish deterministic artifact paths under the caller project root, resolve the helper runtime, and scaffold the authoring package.

## Required actions

1. Resolve the caller project root from the current working directory.
2. Treat the directory containing `SKILL.md` as the skill root for all linked references, templates, and helper scripts.
3. Use the standard runtime-selection contract from [runtime-resolution.md](runtime-resolution.md) before invoking any Python helper.
4. Invoke `scripts/scaffold_execplan.py` from the caller project working directory so outputs land under `<project-root>/.plan/create-execplan/<timestamp>/`.
5. Confirm the scaffolded files match the package layout in [artifact-contract.md](artifact-contract.md), including `workspace/phase-manifest.json`, `workspace/phase-result.json`, `workspace/translation-validation.md`, and the intermediate research/design/structure artifacts.
6. Do not generate `workspace/execplan-runtime-input.json` during scaffold.
7. Treat the scaffolded phase manifest as the canonical contract for later `prepare/apply` phase runs and staged worker packets.

## Done when

- Artifact root exists under the caller project root.
- Authoring artifacts are present in the correct root and workspace locations.
- Phase-control artifacts and upstream phase placeholders are present in the workspace.
- The runtime input artifact is declared by contract but not generated yet.
