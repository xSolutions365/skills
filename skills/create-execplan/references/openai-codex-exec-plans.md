# OpenAI Codex Exec Plans — distilled guidance (local reference)

Source: https://developers.openai.com/cookbook/articles/codex_exec_plans/

This reference distills the core ideas from the Codex “Exec Plans” cookbook article into a format you can apply inside Enaible workflows. It is intentionally written to support _low-reasoning executors_ by emphasizing self-containment, explicit verification, and clear progress tracking.

## What an ExecPlan is

An ExecPlan is an execution-focused design doc that:

- Explains the _user-visible outcome_ first.
- Breaks the work into explicit, verifiable tasks.
- Tracks progress in a way that a stateless agent (or a novice) can resume from the plan file alone.

## Non-negotiables (why they matter)

- **Self-contained**: The plan must include everything needed to succeed without external memory. This is what makes it runnable by cheaper models and new contributors.
- **Living document**: As implementation proceeds, the plan is updated to reflect discoveries, decisions, and completed work. This prevents drift and repeat discovery.
- **Outcome + proof**: “Done” is defined by observable behavior and exact commands, not internal implementation details.

## Two-artifact strategy (best of both worlds)

To reduce cost _and_ reduce re-discovery:

1. **Context Pack** (durable, reusable): a code map with line numbers, how to run checks/tests, and other repo facts. This is the “orientation substrate” you can hand to an executor.
2. **ExecPlan** (living): the task table + decisions + verification logic that evolves during execution. It references the Context Pack instead of repeating it.

This split keeps the ExecPlan lean while still being runnable by a low-reasoning executor.

## Intake discipline for low-reasoning executors

- Run discovery in rounds until requirements are concrete.
- Freeze the final requirement list in the plan.
- Require explicit user confirmation before planning continues.
- Do not allow hidden assumptions after requirements are frozen.

## Greenfield vs brownfield planning mode

- **Greenfield mode**:
  - Prioritize established libraries to reduce build effort.
  - Compare viable approaches and select a low-complexity recommendation.
  - Capture rationale for stack and dependency decisions.
- **Brownfield mode**:
  - Prioritize deep codebase analysis and integration safety.
  - Map exact touch points with `path:line` anchors.
  - Minimize risk by preferring smallest safe change sets.

## Recency + reuse discipline

- When requirements depend on external or fast-moving facts, gather fresh sources and record publication/retrieval dates.
- Prefer primary sources for technical decisions (official docs, release notes, maintainer repositories).
- For greenfield planning, compare established libraries before choosing bespoke implementation.
- Record why each option is adopted or rejected, and link decisions to evidence IDs.

## What each core section contributes

Use these section intents to avoid boilerplate. If a section does not add execution value for this task, omit it.

### Purpose / Big Picture

Explains what changes for a user after the work ships and why it matters.

### Success Criteria / Acceptance Tests

Defines “done” as things a human can run/observe. These criteria are the anchor for tasks and quality gates.

### Constraints & Guardrails

Captures non-negotiable standards (coding rules, quality gates, security constraints) so the executor never has to infer them.

### Requirements Freeze

Captures the user-confirmed requirement list that planning and execution must follow. Prevents scope drift and repeat discovery.

### Context & Orientation (or “See Context Pack”)

Provides a navigational map to relevant code so the executor can jump straight to edits without repo-wide searching.

### Phases + Task Table

Turns the objective into an explicit sequence of small, verifiable steps. The task table is the _single source of truth_ for progress.

### Decision Log / Surprises & Discoveries

Records why choices were made and what was learned mid-flight. This is what prevents future rework and confusion when resuming.

### Test Plan + Quality Gates

States what to run and what outputs indicate success. Keeps “verification” concrete and repeatable.

## Writing tasks for low-reasoning executors

Prefer tasks that include:

- **Where**: `path/to/file:line` anchors
- **What**: edit intent (add/modify/remove) and the target behavior
- **How**: exact commands to run
- **Proof**: expected outputs / conditions

Avoid tasks like “investigate”, “review”, or “refactor” without explicit entry points and completion criteria.
