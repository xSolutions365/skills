# Cross-Reference Rules

## Objective

Make every reference understandable when a reader opens one file on its own. Each reference says what it is and which file and section it lives in, as plain text.

## Required actions

1. Use only these ID prefixes, each with exactly one home file:
   - `D` deliverable: `client/engagement-plan.md` › Deliverables
   - `E` expectation: `internal/expectation-register.md`
   - `R`, `A`, `I`, `DEP` risk, assumption, issue, dependency: `internal/trade-offs-and-raid.md`
   - `OD` open decision: `internal/trade-offs-and-raid.md` › Open decisions
   - `AL`, `PL`, `C` account-lead, pitch-lead, and casting questions: `internal/pitch-lead-questions.md`
   - `L` ledger row: `internal/evidence-ledger.md`
   - `V` validation check: `internal/evidence-ledger.md` › Validation results
2. Never reuse a prefix for a different meaning.
3. On first use in each file, write the ID, a short name, and the home file and section in brackets, as plain text. For example: `D8 architecture straw man (client/engagement-plan.md › Deliverables)`.
4. On later uses in the same file, write the ID and short name, e.g. `D8 architecture straw man`.
5. Never write an ID on its own without a name.
6. Name the section by its heading text, never by an anchor code.
7. Don't add hyperlinks. The packs are local drafts, and linking is the job of whichever skill publishes them later.
8. Internal files may reference client files. Client files must not reference internal files or use the internal-only prefixes `E`, `R`, `A`, `I`, `DEP`, `OD`, `AL`, `PL`, `C`, `L` and `V`. Describe the dependency in words instead, e.g. "pending an internal scope confirmation". `D` is shared, because deliverables are client-safe.
9. Write `internal/README.md` and `client/README.md`. Each one lists its files, a one-line purpose for each, and the ID prefixes each file defines. The internal index also points to the client index.

## Done when

- Every ID is named, and each file gives its home file and section on first use.
- No prefix has two meanings.
- No client file references an internal file or uses an internal-only prefix.
- Both indexes exist, and every file and section they refer to exists.
