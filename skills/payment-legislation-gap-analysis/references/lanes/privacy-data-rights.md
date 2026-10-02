# Consumer data privacy — CCPA/CPRA, state acts, PIPEDA (Canada)

**Lane:** PRIVACY · **Authority:** CCPA/CPRA (CA); VCDPA/CPA/CTDPA + other state acts; GLBA (financial data); PIPEDA (Canada) · **Researched:** Aug 2026

Payments hold sensitive PII (SSN, bank/card, transaction history). Privacy law creates a tension with gaming/BSA **retention** mandates — deletion rights vs must-retain records. GLBA may partially exempt financial data, but state acts and gaming rules still bite.

## Key requirements

- **Access / deletion / correction (DSARs):** consumers can request access, deletion, correction. **But** gaming (5-yr records, in-state residency) and BSA (5-yr) retention **override deletion** for those records — the system must resolve the conflict (retain-for-legal-obligation exemption), not blindly delete.
- **Data minimization & purpose limitation.**
- **Sensitive-data handling:** SSN, financial account numbers = sensitive; encryption at rest/in transit (we saw SSN KMS encryption).
- **Do-not-sell/share + opt-out** (CCPA/CPRA) — less payments-specific.
- **Breach notification:** state breach-notification laws (timelines vary; payment/SSN data triggers).
- **GLBA Safeguards Rule** (if a "financial institution"): security program, access controls, encryption, logging.
- **PIPEDA / Quebec Law 25 (Canada):** consent, access, breach reporting for the ON/CAD data.

## Code review focus

- **Retention-vs-deletion conflict:** on an account deletion / DSAR, are payment/ledger records that are under legal hold (gaming/BSA/in-state) **preserved**, not purged? Grep `delete`, `purge`, `dsar`, `rightToErasure`, `retention`, `legalHold`, `archive`. This is the key payments-privacy risk.
- **PII encryption** on SSN / bank / card fields at rest + redaction in logs (we saw `RedactUtil`, SSN KMS) — confirm coverage across repos.
- Data-residency for privacy (overlaps NJ/WV in-state wallet data).

## Test coverage focus

- **Unit** tests asserting deletion **preserves** legally-held payment records (the conflict resolution) — high value, unit-testable.
- Redaction: a test asserting SSN/PAN never appears in serialized logs/events (cf. the `depositResponse` object-logging risk).
- Note if deletion/DSAR is entirely upstream; flag ownership + the retention-conflict responsibility.

## Sources & confidence

- CCPA/CPRA (Cal. Civ. Code 1798.100+); state privacy acts (IAPP tracker); GLBA Safeguards Rule (16 CFR 314); PIPEDA / Quebec Law 25.
- Confidence: HIGH on the retention-vs-deletion tension being real; MEDIUM on which acts apply to the operator's structure and GLBA exemption scope — route to legal/privacy. Pull latest — new state privacy acts pass most sessions.
