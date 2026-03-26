# Creating a New Scenario Example

Snapshot example derived from the analyzed Raidar docs pattern. This shows how a workflow guide can cover authoring steps that are too specific and too long for the README.

## 1. Create Versioned Scenario Structure

Create:

- `scenarios/<scenario-name>/v001/scenario.yaml`
- `scenarios/<scenario-name>/v001/prompt/task.md`
- `scenarios/<scenario-name>/v001/rules/`
- `scenarios/<scenario-name>/v001/starter/`

## 2. Author `scenario.yaml`

Current schema excerpt:

```yaml
name: homepage-implementation
scenario_revision: v001
description: Implement homepage matching provided reference design
difficulty: medium
category: greenfield-ui
timeout_sec: 1800

starter:
  root: starter

verification:
  max_gate_failures: 3
  required_commands:
    - ["bun", "run", "typecheck"]
```

Notes:

- Keep implementation instructions in prompt artifacts, not in YAML prose blocks.
- Command fields must be argv arrays.
- Rules are single-set only.
- `metrics[]` is required and defines the evaluation profile for the scenario.

## 3. Create Rules Files

Populate `scenarios/<scenario>/v001/rules/` with harness-mapped files:

- `AGENTS.md`
- `CLAUDE.md`
- `GEMINI.md`
- `copilot-instructions.md`
- `user-rules-setting.md`

## 4. Validate and Run

```bash
make scenario-validate SCENARIO=scenarios/<scenario-name>/v001/scenario.yaml
make experiment-run \
  SCENARIO=scenarios/<scenario-name>/v001/scenario.yaml \
  HARNESS=codex-cli \
  MODEL=codex/gpt-5.4-high
```

## 5. Revision Pattern

When iterating scenario behavior, create `v002`, `v003`, and so on instead of mutating old revisions.
