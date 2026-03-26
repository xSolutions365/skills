# Metrics Catalog Example

Snapshot example derived from the analyzed Raidar docs pattern. This shows how a compact catalog can carry dense detail without forcing it into the README.

| Metric | What it measures | When to use it | Requires in `scenario.yaml` | Inspect | Role |
| --- | --- | --- | --- | --- | --- |
| `functional` | Whether the run completed the expected build or test workflow successfully. | Use for every scenario where passing the delivery workflow matters. | Include `functional` in `metrics[]`; scenario verification should define the commands the run must satisfy. | `run.json.scores.functional` | Quality signal and performance-gate input. |
| `acceptance` | Whether the delivered output satisfies deterministic acceptance checks and review criteria. | Use when the scenario has clear outcome requirements beyond build or test success. | `acceptance.deterministic_checks` and or `acceptance.requirements`; include `acceptance` in `metrics[]`. | `run.json.scores.acceptance.checks[]` and `run.json.scores.acceptance.score` | Quality signal. |
| `verification-stability` | How noisy or repeat-failure-prone the verification gates were during the run. | Use when you care about reliability, not just eventual success. | Include `verification-stability` in `metrics[]`; define meaningful verification gates. | `run.json.scores.verification_stability` | Quality signal. |
| `execution-validity` | Whether the run is valid for ranking at all. | Use when comparisons should exclude broken or incomplete runs. | Include `execution-validity` in `metrics[]`. | `run.json.scores.execution_validity.checks[]` and verifier execution-validity output. | Ranking gate. |
| `resource-efficiency` | Token, command, and verification-round efficiency after a valid run completes. | Use when cost and operational efficiency matter for comparisons. | Include `resource-efficiency` in `metrics[]`. | `run.json.scores.resource_efficiency` | Ranking score after execution validity passes. |
| `test-coverage` | Whether measured test coverage meets the scenario threshold. | Use when test-backed delivery quality matters. | `verification.coverage_threshold`; include `test-coverage` in `metrics[]`. | `run.json.scores.test_coverage` | Diagnostic signal and performance-gate input. |
| `requirements-coverage` | Whether stated requirements are present and mapped to tests. | Use when you want explicit requirement-to-test accountability. | `acceptance.requirements`; include `requirements-coverage` in `metrics[]`. | `run.json.scores.requirements_coverage` | Diagnostic signal and performance-gate input. |
| `llm-judge` | Subjective review criteria captured in the acceptance rubric. | Use when code quality or UX qualities cannot be captured deterministically. | `acceptance.llm_judge_rubric`; include `llm-judge` in `metrics[]`. | `run.json.scores.acceptance.checks[]` filtered to `type=llm_judge` and aggregate metric outcomes. | Acceptance input and diagnostic signal. |
| `visual-regression` | Similarity to the visual reference and whether the threshold was met. | Use for layout- or design-sensitive scenarios. | `visual.reference_image`, `visual.screenshot_command`, `visual.threshold`; include `visual-regression` in `metrics[]`. | `run.json.scores.visual` and verifier visual diffs. | Quality signal and performance-gate input. |
| `artifact-checks` | Whether required files or paths exist in the run workspace. | Use when you need explicit artifact presence guarantees beyond core scoring. | `metrics[]` entry with `type: artifact-checks` and `config.required_paths`. | `run.json.scores.metric_results[]` and aggregate metric outcomes. | Audit signal unless the scenario contract promotes it to gating. |

## How To Read Roles

- `quality_score` is built from functional, acceptance, visual when configured, and verification stability.
- Ranking depends on `execution-validity` first and `resource-efficiency` second.
- `test-coverage`, `requirements-coverage`, and `artifact-checks` are best treated as diagnostic or audit signals unless the scenario contract makes them gating.
- `llm-judge` is configured as its own metric id, but its detailed evidence lives inside acceptance checks because it contributes to the acceptance view of run quality.
