# Nacha / ACH Operating Rules — e-check deposit rail

**Lane:** NACHA · **Authority:** Nacha Operating Rules (private rulebook, contractually binding) · **Researched:** Aug 2026 (2026 risk-management/fraud-monitoring amendments refresh Sep 2026)

Governs ACH/e-check (the Trustly rail). Contractual, not statute, but breach = fines + rail loss. Distinct from EFTA (consumer law) and from state failed-ACH gaming rules (which sit in the state skill / DepositPostProcessorRegulations).

## Key requirements

- **WEB debit authorization + verification:** consumer-initiated WEB debits require authorization AND a **commercially reasonable fraudulent-transaction detection system**, plus the **account validation rule** (first-use of an account number must be validated — micro-deposits, network validation, or a validation service).
- **Return-code handling:** returns have distinct obligations — **R01** (NSF, may retry within limits) vs **R10/R11** (unauthorized / customer advises not authorized → must NOT retry, treat as dispute) vs **R07** (authorization revoked) vs administrative returns. Mis-handling R10 as retryable is a rules violation.
- **Return-rate thresholds:** unauthorized-return rate cap **0.5%**, administrative **3%**, overall **15%** — monitored; breach triggers Nacha inquiry. Requires tracking/alerting on return rates.
- **Reinitiation limits:** a returned entry may be reinitiated at most **2 times** after an R01/R09 NSF, within 180 days, and only if re-authorized.
- **Same-day ACH** windows/limits if used; **Nacha data-security rule** (protect account numbers — render unreadable when stored).
- **Risk-based ACH fraud monitoring (2026 amendment) — NEW, likely binds most operators:** every ODFI and non-consumer Originator/Third-Party Sender/Third-Party Service Provider must maintain a **documented, risk-based process to detect unauthorized entries AND entries authorized under false pretenses** (social-engineering / BEC / account-takeover), reviewed at least **annually**. Phased: **Phase 1 from 2026-03-20** for parties whose 2023 ACH volume exceeded **6 million** entries; **Phase 2 from 2026-06-22** for **all** remaining originators/TPS/TPSPs regardless of volume. An operator that originates ACH/e-check deposits is in scope — confirm which phase by 2023 volume. Companion 2026 items: **standardized Company Entry Description** values (e.g. `PAYROLL` for wage PPD credits) and **non-same-day credit funds available by 9:00 a.m.** local settlement date.

## Code review focus

- Where are ACH **return codes** received (Trustly webhook / notification) and mapped? Grep `R01`, `R10`, `returnCode`, `NSF`, `reinitiate`, `retry`. Is R10 (unauthorized) routed to a no-retry/dispute path distinct from R01 (retryable)? This is the crux.
- **Reinitiation cap** — is a returned NSF deposit limited to ≤2 retries within 180 days, or can it retry unbounded? (Note: the failed-ACH *fraud* gate is a separate control.)
- **Return-rate monitoring** — any counter/alert on unauthorized/admin return rates? Likely metrics/ops.
- **Account-number storage** — rendered unreadable (KMS/tokenized), not plaintext in logs/DB.
- **Risk-based fraud monitoring (2026):** is the deposit fraud-check applied to the ACH/e-check deposit path, and is it **documented as risk-based and reviewed annually** per the amendment — not just a generic score? "False pretenses" (social engineering / authorized-push-payment) is broader than "unauthorized"; confirm the monitoring covers scam-induced authorized deposits, not only stolen-credential fraud. Company Entry Description values and the 9 a.m. funds-availability commitment are ODFI/bank-side but confirm the operator isn't setting a non-compliant SEC/description on origination.

## Test coverage focus

- **Unit** tests on the return-code → action mapping (R01→retry-eligible, R10→dispute/no-retry, R07→stop) — this is pure logic and belongs in the unit layer.
- Boundary/negative: unauthorized return must not reinitiate; 3rd reinitiation blocked.
- Note if the only ACH tests are happy-path deposit success (no return-code paths exercised).
- **2026 fraud monitoring:** a test proving the ACH deposit path actually invokes the fraud-monitoring hook (not bypassed for ACH specifically), and — where feasible — that a false-pretenses/high-risk signal is flagged, not just a stolen-card pattern. If monitoring is a documented ops process rather than in-code logic, record it as an ownership/process control, not a code gap.

## Sources & confidence

- Nacha Operating Rules (2025 edition); account-validation rule effective 2021; return-rate thresholds per Rule 2.17. (Rulebook is paywalled — cite Nacha summaries.)
- **2026 amendments (refresh Sep 2026):** risk-based ACH fraud-monitoring rule — Phase 1 **2026-03-20** (>6M 2023 entries), Phase 2 **2026-06-22** (all); standardized Company Entry Descriptions; non-same-day credit funds available by 9 a.m. Sources: [Nacha — New Rules](https://www.nacha.org/newrules) · [Nacha — new risk-management rules now in effect](https://www.nacha.org/news/new-nacha-risk-management-rules-now-effect).
- Confidence: HIGH on the rule shapes and the 2026 fraud-monitoring phase dates; MEDIUM on which phase a given operator lands in (needs 2023 ACH volume) and on exact return-rate thresholds — pull latest, Nacha updates annually.
