# Context Code Map

- Created: 2026-03-30
- Last updated: 2026-03-30T16:07:46Z

| Area | File anchor | Current behavior | Planned change |
| ---- | ----------- | ---------------- | -------------- |
| Durable context handoff | `context-pack.md:1` | Consolidates the frozen requirements, evidence limits, and blocked downstream posture for this plan package. | Replace the template with an evidence-backed context pack that records the blocker and preserves the approved scope. |
| Frozen requirement baseline | `workspace/requirements-freeze.md:1` | Defines the confirmed scope: preserve deterministic package flow, prevent nested child-agent recursion, and keep verification anchored to repo-local checks plus the live Codex smoke. | No direct change in this phase; this remains the authoritative requirement source. |
| Discovery baseline | `workspace/context-discovery.md:1` | Captures the approved problem statement, available artifact list, and no-online-research rule. | No direct change in this phase; use it to frame the context pack boundaries. |
| Research blocker record | `workspace/research-findings.md:1` | Shows that the implementation and test files needed for concrete analysis were referenced but not staged locally. | No direct change in this phase; this remains the primary blocker evidence. |
| Design decision hold | `workspace/design-options.md:1` | Selects an evidence-based hold instead of speculative design because the required source artifacts are missing. | No direct change in this phase; use it to justify blocked status in the context pack. |
| Structural hold | `workspace/structure-outline.md:1` | Limits the phase output to a blocked structural outline that preserves interfaces and boundaries without inventing seams. | No direct change in this phase; use it to bound the context pack content. |
| Machine-readable evidence inventory | `workspace/context-evidence.json:1` | Tracks which evidence was staged and inspected versus which referenced implementation and test files remain unstaged. | Refresh metadata and separate available evidence from missing sources so downstream phases can see the blocker immediately. |
