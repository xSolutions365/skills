# Context Code Map

- Created: 2026-03-24

| Area | File anchor | Current behavior | Planned change |
| ---- | ----------- | ---------------- | -------------- |
| scaffolded paths | `skills/create-execplan/scripts/scaffold_execplan.py:1` | scaffolds the plan package | add phase-control and intermediate workspace artifacts |
| runtime renderer | `skills/create-execplan/scripts/render_execplan_runtime_input.py:1` | derives runtime JSON from the ExecPlan | keep the runtime packet narrow and explicit |
| execplan validator | `skills/create-execplan/scripts/validate_execplan.py:1` | enforces packet executability and plan structure | hard-fail vague packet rows |
