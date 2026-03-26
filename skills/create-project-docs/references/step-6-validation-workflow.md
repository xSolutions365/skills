# Step 6 Workflow: Validate accuracy and flow

## Objective

Apply an evidence-backed validation gate that rejects invented content, weak information architecture, and broken navigation.

## Required actions

1. Evaluate the draft package against [validation-checklist.md](validation-checklist.md).
2. Verify every command, environment variable, file path, and config snippet against the Step 1 evidence inventory.
3. Confirm the README includes all mandatory sections and keeps them in the intended order.
4. Confirm the README stays concise:
   - one canonical install path
   - one canonical quick-start path
   - at most one advanced example
   - no exhaustive schema dumps or giant tables
5. Confirm each `docs/references/*.md` file has:
   - one clear topic
   - a documented placement reason
   - evidence-backed examples
   - no unnecessary duplication of README content
6. Check that all README links to deeper docs resolve and that every deeper doc linked from the README adds distinct value.
7. Fail the draft if:
   - any content is invented
   - any planned deeper doc lacks evidence justification
   - the README is overloaded
   - a known gap was hidden instead of reported
8. Record one evidence line for every checklist rule group.
9. Record explicit gaps and contradictions whenever repo evidence is insufficient or inconsistent.

## Done when

- All generated content is traceable to repo evidence.
- The README versus reference-doc split is coherent.
- Links resolve and every deeper doc earns its place.
- The validation result is binary and evidence-backed.
- Remaining uncertainty is reported as a gap instead of being fabricated away.
