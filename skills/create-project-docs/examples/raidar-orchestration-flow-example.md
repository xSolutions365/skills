# Raidar Orchestration Flow Example

Snapshot example derived from the analyzed Raidar docs pattern. This shows how a deeper technical flow doc can sit behind the README for readers who need lifecycle detail.

## 1. Scenario Resolution

1. Select a versioned scenario file: `scenarios/<scenario-name>/v###/scenario.yaml`.
2. Load the scenario definition with name, revision, starter, prompt, verification, acceptance, and ordered metrics.
3. Resolve the starter from the scenario revision directory.
4. Copy the starter into the run workspace and inject one rules file for the selected harness.

## 2. Execution Layout

Each experiment writes to one execution root:

`experiments/{benchmarks|research_loops}/<timestamp>__<scenario>__<revision>__<harness>__<model>__xN/`

Inside that root:

- `workspace/baseline/`
- `runs/`
- `experiment.json`
- `experiment-summary.json`
- `report.md`

## 3. Run Lifecycle

1. The CLI builds a run request from the scenario plus an `AgentSpec`.
2. The runner prepares the workspace, validates starter preflight commands, and builds the Harbor scenario bundle.
3. Harbor executes the harness or model pair.
4. The runner hydrates the workspace, captures post-run evidence, and prunes transient folders.
5. Verifier artifacts are loaded and normalized into score outputs.

## 3.1 Matrix Config Contract

```yaml
matrix:
  experiment:
    timeout_sec: 1800
    repeats: 3
    repeat_parallel: 1
    retry_void: 1
  agents:
    - harness: codex-cli
      model: codex/gpt-5.4-high
    - harness: claude-code
      model: anthropic/claude-sonnet-4-5
```

## 4. Scoring Pipeline

- scenario scoring capability is defined by ordered `scenario.yaml -> metrics[]`
- `evaluation_profile` is derived from ordered metrics
- `composite_score` is gated so invalid or unscored runs score `0.0`

## 5. Canonical Analysis Inputs

- `experiments/*/experiment-summary.json`
- `experiments/*/report.md`
- `experiments/*/runs/*/run.json`
- `experiments/*/runs/*/verifier/scorecard.json`
