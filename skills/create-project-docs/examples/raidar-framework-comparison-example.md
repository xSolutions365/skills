# RAIDAR Framework Comparison Example

Snapshot example derived from the analyzed Raidar docs pattern. This shows how a comparison memo can live outside the README while still supporting positioning and decision-making.

## Purpose

RAIDAR is not a generic LLM eval toolkit. Its purpose is to evaluate real project-delivery tasks by treating a delivery scenario and a harness plus model pair as first-class experimental objects.

In practical terms, RAIDAR is designed to help answer questions like:

- Which harness plus model pair is best for this delivery task.
- What should be changed next: prompt, rules, starter, scenario design, or harness or model choice.
- Is a run good enough in ways that matter to delivery, not just to prompt quality.

## Key Differentiators

### Delivery-first evaluation unit

RAIDAR is centered on an explicit scenario contract for delivery work rather than on a single prompt, test case, or benchmark item.

### `AgentSpec = harness + model`

RAIDAR makes the harness or runtime part of the experimental unit, not just the model.

### Decision-grade evidence for delivery

The emphasis is on outcomes such as:

- functional correctness
- acceptance and verification quality
- execution validity
- efficiency
- repeat stability
- visual quality where relevant

### Improvement loop, not just leaderboard output

RAIDAR is designed to support decisions about what to improve next:

- prompt design
- rules
- starter scaffolding
- scenario design
- harness choice
- model choice

## Comparison Matrix

| Dimension | Weight | RAIDAR | Inspect AI | Promptfoo | DeepEval |
| --- | ---: | ---: | ---: | ---: | ---: |
| Scenario or task contract authoring flexibility | 14 | 5 | 4 | 3 | 2 |
| Harness or runtime as experimental variable | 16 | 5 | 5 | 3 | 1 |
| Model abstraction and multi-model execution | 8 | 5 | 5 | 5 | 2 |
| Matrix, repeats, and sweep support | 12 | 5 | 5 | 4 | 2 |
| Custom metrics and evaluator composition | 12 | 5 | 5 | 5 | 5 |
| Agentic or multi-step support | 10 | 5 | 5 | 4 | 3 |
| Run orchestration and logs | 10 | 4 | 5 | 4 | 3 |
| Fit for real project delivery tasks | 8 | 5 | 4 | 4 | 2 |
| Result comparison ergonomics | 5 | 4 | 4 | 5 | 2 |
| Maturity and maintenance | 5 | 2 | 4 | 5 | 5 |
| **Weighted total / 100** |  | **94.0** | **93.6** | **80.0** | **51.0** |

## Practical Takeaways

- Inspect AI is the closest architectural comparison point.
- Promptfoo is the lightweight comparison point.
- DeepEval is best treated as a companion evaluation layer rather than a direct replacement.
- RAIDAR is the most delivery-opinionated system for harness plus model decisions in this comparison.
