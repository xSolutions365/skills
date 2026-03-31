# Live Repro Green Fixture

This fixture preserves the green end-to-end package produced from a live `create-execplan` reproduction of the child-phase isolation bug on 2026-03-30.

Use it when validating:

- readiness-audit outputs for a real brownfield isolation scenario
- draft-approval and handoff-checklist evidence
- runtime-input generation from a fully specified mock package

The fixture complements the canonical example:

- `canonical/` remains the normative example package
- `live-repro-green/` captures the concrete package generated from the live bug investigation

## Root artifacts

- [context-pack.md](context-pack.md)
- [execplan.md](execplan.md)
- [review-checklist.md](review-checklist.md)

## Workspace artifacts

- [context-discovery.md](workspace/context-discovery.md)
- [context-codemap.md](workspace/context-codemap.md)
- [context-evidence.json](workspace/context-evidence.json)
- [requirements-freeze.md](workspace/requirements-freeze.md)
- [translation-validation.md](workspace/translation-validation.md)
- [planning-brief.md](workspace/planning-brief.md)
- [research-questions.md](workspace/research-questions.md)
- [research-findings.md](workspace/research-findings.md)
- [design-options.md](workspace/design-options.md)
- [structure-outline.md](workspace/structure-outline.md)
- [draft-review.md](workspace/draft-review.md)
