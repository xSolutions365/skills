# Chargebacks & dispute management (card networks)

**Lane:** CHARGEBACK · **Authority:** Visa/Mastercard dispute rules; Visa VDMP/VFMP, Mastercard ECP/ECM monitoring programs · **Researched:** Aug 2026

Card disputes/chargebacks on gaming deposits carry network monitoring-program exposure (fines, forced remediation) above thresholds. Distinct from Reg E (consumer EFT) and refund (voluntary money-back). Overlaps the gaming chargeback-accounting rule (state skill records/data).

## Key requirements

- **Dispute lifecycle handling:** receive chargeback (dispute reason codes), represent (fight) with evidence, accept, or issue credit — within network timeframes.
- **Monitoring-program thresholds:** Visa **VDMP** (dispute-monitoring) and **VFMP** (fraud-monitoring) — early-warning/standard thresholds on dispute count + ratio (e.g. ~0.9%/100 disputes standard, higher for "excessive"); Mastercard **ECM/ECP**. Breach → fines + mandatory remediation. Requires tracking dispute/fraud ratios.
- **Chargeback accounting:** write-offs vs recovery, disputed-charge treatment mapped to internal controls (cf. gaming R432.668-style rule); refundable_amount / ledger correctness on a chargeback.
- **Representment evidence:** capturing AVS/CVV/3DS/geo/device data to fight friendly-fraud (ties to card-network + fraud-signal metadata).
- **Prohibit re-deposit abuse:** blocking accounts with charged-back deposits (fraud gate).

## Code review focus

- Is there a **chargeback ingress + accounting** path? Grep `chargeback`, `dispute`, `representment`, `reasonCode`, `retrieval`, `CHARGE_BACK`.
- **Ledger effect** of a chargeback: does it correctly reverse/adjust the deposit + refundable_amount without double-effect (idempotency)?
- **Dispute-ratio monitoring / alerting** — any counter feeding VDMP/ECM thresholds? Likely ops/metrics.
- Chargeback → account fraud gate (block re-deposit).

## Test coverage focus

- **Unit** tests on chargeback ledger accounting (reversal is exact, idempotent, and caps at the original capture — reuses the refund-guard logic).
- Boundary/ratio: if dispute-rate monitoring exists, threshold tests.
- Note if chargebacks are handled entirely by the processor/ops with no code path — flag ownership + the accounting-correctness question.

## Sources & confidence

- Visa Dispute rules + VDMP/VFMP program guides; Mastercard Dispute Resolution + ECM/ECP. Program thresholds are semi-public.
- Confidence: HIGH that monitoring programs apply; MEDIUM on current thresholds/program names (networks rename/retune periodically) — pull latest. The ledger-accounting correctness check is HIGH-confidence checkable in-repo.
