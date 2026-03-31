# Structure Outline

- Created: 2026-03-24
- Last updated: 2026-03-24T09:14:00Z

## Interfaces

- Interface 1: `run_phase.py prepare --phase research --artifact-root .plan/create-execplan/canonical`

## Boundaries

- Boundary 1: parent agent owns user interaction and checkpoint recording; fresh worker subagents own single-phase reasoning only.

## Data Flow

- Flow 1: scaffold -> workspace artifacts -> prepare -> worker subagent -> apply -> parent checkpoint -> next phase

## Planned Slice Order

- Slice 1: scaffold and runner/controller contracts
- Slice 2: rubric validation and references/examples updates
