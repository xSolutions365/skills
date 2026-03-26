# Auto-Researcher Example

Snapshot example derived from the analyzed Raidar docs pattern. This shows how a focused workflow reference can explain one subsystem without repeating the README.

`auto_researcher` is an objective-led optimization workflow that sits above the base experiment surface:

- It creates a canonical scenario draft for a measurable goal.
- It seeds a pinned benchmark baseline.
- It runs bounded research loops and updates the best known benchmark when improvements are confirmed.

## 1. Core Components

- `auto_researcher/objectives/<objective-id>/`: lifecycle state, brief, report, plans, and loop state.
- `auto_researcher/roles/`: planner, critic, and runner prompt definitions.
- `scenarios/`: canonical scenario once approved.
- `experiments/benchmarks/`: pinned benchmark experiments for each objective.
- `experiments/research_loops/`: loop experiments generated while executing objective improvements.

## 2. Public Workflow

Use the public make surface:

```bash
make auto-research-init GOAL="..." TARGET_HARNESS=codex-cli TARGET_MODEL=codex/gpt-5.4-mini
make auto-research-approve-scenario OBJECTIVE_ID=...
make auto-research-run OBJECTIVE_ID=...
make auto-research-status OBJECTIVE_ID=...
make auto-research-report OBJECTIVE_ID=...
```

Optional controls from the Make targets:

- `MAX_REVISIONS`
- `BENCHMARK_REPEATS`
- `BENCHMARK_REPEAT_PARALLEL`
- `RESEARCH_REPEATS`
- `RESEARCH_REPEAT_PARALLEL`
- `MAX_PARALLEL_LOOPS`

## 3. What "benchmark" Means

- Stored as an experiment with `experiment_kind=benchmark` under `experiments/benchmarks/`.
- Tracked in objective state as `best_benchmark_ref`.
- Used to compare future loop outputs for relative and absolute movement.

## 4. What "research loop" Means

- Stored as `experiment_kind=research-loop` experiments under `experiments/research_loops/`.
- Executed after scenario approval once an objective is active.
- Can generate candidate improvements, and a successful candidate may update benchmark state in the objective.

## 5. Inspecting Evidence

- `make auto-research-status OBJECTIVE_ID=...`
- `auto-researcher status --objective-id ... --json`
- `make auto-research-report OBJECTIVE_ID=...`
- experiment artifacts under `experiments/benchmarks/*` and `experiments/research_loops/*`
