# Planning Best Practices

Agentic planning works best when planning is treated as a staged alignment process, not a single prompt that tries to think, decide, and implement all at once. The target is consistent human-agent alignment, objective discovery, and execution plans that can be verified in small checkpoints.

## Core Rules

### 1. Use hard phase boundaries

Each major phase should run in its own fresh session with its own context window. Later phases should be oblivious to prior raw conversation and should receive only the approved artifacts from the previous phase.

- Do not carry forward full chat history.
- Do not let research inherit design opinions.
- Do not let planning inherit implementation guesses unless they were explicitly approved in design.
- Pass only the minimum artifact needed for the next step.

This keeps each phase narrow, reduces contamination, and forces explicit alignment instead of accidental context bleed.

### 2. Keep prompts single-responsibility

Each prompt should do one job only and stay under roughly 40 instructions. If a prompt needs branching logic, hidden sub-modes, or exception routing, it is too large.

- One prompt should clarify.
- One prompt should research.
- One prompt should design.
- One prompt should structure.
- One prompt should plan.
- One prompt should execute a bounded task.

Large prompts create partial compliance. Smaller prompts create predictable behavior.

### 3. Use deterministic process for control flow

Do not ask the model to be its own workflow engine. Control flow should live in deterministic code or explicit process rules.

- Use code to classify the request.
- Use code to choose the next phase.
- Use code to decide which artifact is required next.
- Use prompts for reasoning inside a phase, not for routing between phases.

If the workflow says "if X, go to Y," that decision should usually be made outside the model.

### 4. Start with clarifying questions

The first planning job is not solutioning. It is removing ambiguity.

- Ask clarifying questions early.
- Identify success criteria, constraints, risks, and non-goals.
- Resolve missing requirements before research and design.
- Do not let the model silently fill gaps with assumptions.

Clarification improves the destination before any discussion of approach.

### 5. Keep research objective

Research should describe the current system truthfully, not argue for a preferred solution.

The recommended pattern is:

1. Use one session to generate research questions from the ticket, goal, or change request.
2. Use a separate fresh session to answer those questions from the codebase without access to the ticket narrative or desired approach.
3. Return a compressed fact pack for later phases.

Research output should separate:

- facts
- assumptions
- unknowns
- risks

This keeps discovery useful instead of opinionated.

### 6. Make design goal-aware but approach-unbiased

The design phase should know the goal, constraints, and research findings, but it should not be biased toward a preselected implementation path unless that path was explicitly chosen by a human.

Good design input includes:

- the desired outcome
- clarified constraints
- objective research findings
- acceptance criteria

Good design output includes:

- candidate approaches
- tradeoffs
- chosen direction
- rejected alternatives
- risks and open decisions

Design should answer "where are we trying to get to and what shape should the solution take," not "how do we force-fit the first idea."

### 7. Define structure before detailed planning

Before writing a deep implementation plan, define the structural outline.

- interfaces
- types
- module boundaries
- ownership lines
- key signatures
- major data flows

This is the short artifact teams should review for alignment. It is far more leverage than reviewing a long generated plan.

### 8. Plan vertical slices, not horizontal layers

Plans should be broken into end-to-end slices that can be validated early.

Prefer:

- one thin path through UI, API, service, and data
- one checkpoint with visible behavior
- one testable increment at a time

Avoid plans that batch work by layer and defer validation until the end.

Vertical slices create:

- earlier feedback
- faster defect detection
- smaller rollback surfaces
- clearer progress checkpoints

### 9. Review alignment artifacts, then review code

Planning artifacts should be short and decision-dense.

The primary review sequence should be:

1. Clarified requirements
2. Research fact pack
3. Design discussion
4. Structure outline
5. Final code and tests

Do not spend team energy reviewing thousand-line generated plans when the real leverage is in design alignment and implementation quality.

### 10. Treat context as a budget

Do not fill the context window because you can. Keep each phase lean and pass forward only compressed artifacts.

- Prefer summaries over transcripts.
- Prefer structured outputs over freeform notes.
- Reset sessions between phases.
- Remove stale or duplicate context aggressively.

The goal is not maximum context. The goal is maximum relevance.

## Recommended Phase Flow

### Questions

Produce a clarified problem statement, constraints, success criteria, and unresolved questions.

### Research Question Planning

Convert the clarified request into concrete research questions.

### Research

Answer the research questions in a fresh session that is blind to the preferred solution and focused on objective codebase facts.

### Design

Use the clarified goal and research fact pack to produce an approach-unbiased design discussion with tradeoffs and a selected direction.

### Structure

Produce a concise outline of interfaces, boundaries, and system shape.

### Plan

Break the approved structure into vertical slices with explicit checkpoints, dependencies, and done criteria.

### Work

Execute one bounded slice or task packet at a time with only the context needed for that packet.

### Implement and PR

Review final code, tests, and behavioral outcomes instead of re-litigating the full generated plan.

## Artifact Expectations

Each phase should hand off a small artifact with a clear contract.

- Questions artifact: scope, constraints, success criteria, open questions
- Research artifact: facts, assumptions, unknowns, risks
- Design artifact: options, tradeoffs, chosen direction, rejected alternatives
- Structure artifact: interfaces, boundaries, types, responsibilities
- Plan artifact: vertical slices, checkpoints, dependencies, verification steps
- Work packet: exact task, edit targets, supporting context, commands, expected output

If a later phase needs information that is not in the handoff artifact, the prior phase was incomplete.

## Failure Modes To Avoid

- giant prompts that mix clarification, research, design, planning, and execution
- research that already knows the intended answer
- design sessions that inherit old conversational baggage
- plans organized by technical layer instead of functional slice
- long plan reviews that replace direct code review
- prompts used as control-flow engines
- hidden assumptions that were never clarified or documented

## Practical Standard

The operating standard is simple:

- one responsibility per prompt
- one fresh session per major phase
- deterministic routing outside the model
- goal-aware but approach-unbiased design
- objective research separated from implementation pressure
- vertical checkpoints instead of horizontal big-bang plans

This is what turns agentic planning from prompt theatre into a repeatable engineering process.
