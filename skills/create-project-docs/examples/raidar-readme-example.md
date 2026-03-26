# Raidar README Example

Snapshot example derived from the analyzed Raidar docs pattern. Absolute file links were normalized so this example remains portable inside the skill package.

<div align="center">

<h1>Raidar</h1>

**Scenario evaluation of CLI harness + model pairs (`AgentSpec`s) to improve delivery performance using Harbor-based runs**

![Status](https://img.shields.io/badge/status-active-brightgreen.svg?style=flat-square)
![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg?style=flat-square)
![Runtime](https://img.shields.io/badge/runtime-uv%20%7C%20docker-lightgrey.svg?style=flat-square)
![Primary CLI](https://img.shields.io/badge/cli-raidar-orange.svg?style=flat-square)

</div>

## Quick Install

Prerequisites:

- `uv`
- Docker with `docker compose`
- at least one harness/provider API key in `orchestrator/.env`

Bootstrap the environment:

```bash
cp orchestrator/.env.example orchestrator/.env
make env-setup
```

Use `make help` from the repo root for the supported command surface and target descriptions.

## Quick Start

Run one review-grade experiment for one `AgentSpec` (`harness + model`).

```bash
make harness-validate HARNESS=codex-cli MODEL=codex/gpt-5.4-mini
make experiment-run \
  SCENARIO=scenarios/hello-world-smoke/v001/scenario.yaml \
  HARNESS=codex-cli \
  MODEL=codex/gpt-5.4-mini \
  RUN_COUNT=5 \
  RUN_PARALLELISM=1 \
  RERUN_UNSCORED=0
```

This writes canonical artifacts into `experiments/`, including per-run `run.json`, experiment-level `experiment.json`, `experiment-summary.json`, and `report.md`.

Use `make orchestrator-smoke` when you want a fast orchestrator smoke or debug pass for one `AgentSpec`.

```bash
make orchestrator-smoke
```

Run a structured provider comparison with the public make surface:

```bash
make matrix-run scenarios/homepage-implementation/v001/scenario.yaml codex
```

Under the hood, that generates a matrix config using the public schema:

```yaml
matrix:
  experiment:
    timeout_sec: 1800
    repeats: 5
    repeat_parallel: 1
    retry_void: 1
  agents:
    - harness: codex-cli
      model: codex/gpt-5.2-high
    - harness: codex-cli
      model: codex/gpt-5.2-low
    - harness: codex-cli
      model: codex/gpt-5.2-medium
    - harness: codex-cli
      model: codex/gpt-5.4-extra-high
    - harness: codex-cli
      model: codex/gpt-5.4-high
    - harness: codex-cli
      model: codex/gpt-5.4-mini
    - harness: codex-cli
      model: codex/gpt-5.4-medium
```

## What Raidar Does

The repository has four primary concerns:

- `orchestrator/`: CLI and runtime pipeline that executes and scores scenarios.
- `scenarios/`: versioned scenario definitions (`scenario.yaml`), prompts, rules, references, and starters.
- `auto_researcher/`: objective-led workflow for scenario design and benchmark-driven research loops.
- `experiments/`: generated experiment artifacts with per-run evidence bundles.
- `experiments/` uses canonical experiment kinds:
- `experiments/benchmarks/` for benchmark baselines.
- `experiments/research_loops/` for bounded research-loop batches.

Raidar is built to answer one practical question: how well does a given harness and model perform against delivery scenarios that look like real project work. It helps compare execution quality, reliability, and efficiency against the same scenario contract instead of relying on anecdotal impressions.

## Core Concepts

- A `scenario` is the contract: prompt, rules, starter, verification settings, acceptance requirements, metrics, and optional visual baseline.
- A `harness` is the executable or runtime surface previously referred to as an agent.
- An `AgentSpec` is one harness plus one model.
- An `experiment` is one `AgentSpec` run against one scenario, usually with repeats.
- A `benchmark` is the pinned baseline experiment used as the current comparison anchor for an autoresearch objective.
- A `research loop` is a bounded, iterative experiment batch run to improve benchmark-facing evidence for that objective.
- An `objective` is the optimization target in `auto_researcher`.
- A `matrix config` uses top-level `experiment` and `agents` blocks.

## Go Deeper

- [raidar-metrics-catalog-example.md](raidar-metrics-catalog-example.md): what each metric measures, when to use it, and where to inspect evidence.
- [raidar-homepage-walkthrough-example.md](raidar-homepage-walkthrough-example.md): a high-level teaching walkthrough of the homepage scenario and eval design flow.
- [raidar-framework-comparison-example.md](raidar-framework-comparison-example.md): comparison memo covering Raidar's delivery-focused differentiators.
- [raidar-auto-researcher-reference-example.md](raidar-auto-researcher-reference-example.md): objective-led flow for benchmarks, research loops, and status or report outputs.
- [raidar-env-var-lexicon-example.md](raidar-env-var-lexicon-example.md): fuller reference for repo-visible environment variables.
