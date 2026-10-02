# Missouri — Missouri Gaming Commission (MGC)

**Code:** MO · **Products:** sportsbook · **Key authority:** Mo. Const. Art. III §39(e) (Amendment 2, Nov 2024); 11 CSR 45-20 (sports wagering rules); launched Dec 1, 2025

## Payments-relevant requirements

### Licensing & change management

- Newest market of the six: rules finalized in 2025 after the Secretary of State rejected emergency rules; full launch Dec 1, 2025.
- Software change management (11 CSR 45-20.310): changes classified as core / substantial-to-core / non-core; new core functions must be tested and certified by a licensed independent testing lab (ITL) and approved by MGC before installation; substantial changes require pre-installation notice with a 3-business-day commission window to order testing; emergency changes allowed with immediate written notice and change-log entry.
- Documented change process required: roles, non-production testing, rollback procedures (20.310); equipment/platform testing under 11 CSR 45-20.240.

### Deposits & permitted payment methods

- 11 CSR 45-20.320(6) authorizes: credit cards, debit cards, gift cards, verified reloadable prepaid cards, ACH transfers, currency via licensed money transmitters, wire transfers, and promotional credits. Credit cards are permitted.

### Withdrawals & payout timelines

- Withdrawal requests honored within 5 business days (20.320(15)); winnings deposited to the account within 24 hours (20.320(7)).

### Player funds segregation / reserve

- Reserve of the greater of $500,000 or outstanding sports wagering liability (cashable account funds + open wagers + unpaid winnings); forms: cash, cash equivalents, payment processor reserves/receivables, surety bond, irrevocable letter of credit (11 CSR 45-20.190).
- Reserve assets may not be applied to other purposes; deficiency must be reported to MGC within 48 hours and remedied by end of next business day.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Responsible gaming rule 11 CSR 45-20.580 plus Compulsive Gaming Prevention Fund (20.590); account statements must include responsible gaming limit history and problem-gambling assistance info (20.320(13)) — implies player-set limits (verify exact mandatory limit types, MEDIUM).
- Dedicated self-exclusion framework: 11 CSR 45-20.600–.650 (placement, entry, confidentiality, re-establishment, licensee duties — no wagers/deposits from listed persons).
- Account suspension mechanics in 11 CSR 45-20.330.

### KYC / age / geolocation

- Identity verification via "remote multi-sourced authentication" and valid non-expired government photo ID (20.320(3)(C)); age 21+ per Amendment 2.
- Geofencing/geolocation defined in 20.010 and required for online platforms (20.270/20.290) to confine wagers to Missouri (rule-number mapping MEDIUM — verify 20.270 text).

### AML overlays (state-specific, beyond federal BSA)

- Licensees must promptly notify MGC of suspicious or illegal wagering activity, including use of funds derived from illegal activity (11 CSR 45-20.100(2)(J)); prohibited-transaction reporting under 20.110 and criminal-conduct reporting under 20.170 — a state notification duty on top of federal SAR filing.

### Records, reporting & data

- Accounting records, retention, and standard financial records: 11 CSR 45-20.500–.520; annual/special audits 20.530; commission test accounts required (20.320(18)); biometric data prohibition (20.370).

## Code review focus

- Newest rule set: verify the gateway's MO config matches final (not proposed) 11 CSR 45-20 text — rules changed during 2025 rulemaking.
- Withdrawal SLA 5 business days AND 24-hour winnings-crediting job post-settlement.
- Reserve/liability computation endpoint with 48-hour deficiency alerting to compliance.
- Payment-affecting code changes routed through core/substantial/non-core classification with ITL certification gate before deploy.
- Deposit rails limited to the 20.320(6) list; money-transmitter cash deposits must use licensed transmitters.
- Self-exclusion list sync blocks deposits and account creation; suspension states per 20.330; no biometric data stored (20.370).

## Sources & confidence

- [11 CSR 45-20 full chapter Mo. SoS](https://www.sos.mo.gov/CMSImages/AdRules/csr/current/11csr/11c45-20.pdf) · [11 CSR 45-20.320 proposed rule MGC](https://www.mgc.dps.mo.gov/RulesNRegs/csr_proposed/2025_csr_prop/11%20CSR%2045-20.320%20Proposed%20Rule.pdf) · [11 CSR 45-20.310 software change management MGC](https://www.mgc.dps.mo.gov/RulesNRegs/csr_proposed/2025_csr_prop/11%20CSR%2045-20.310%20Proposed%20Rule.pdf) · [11 CSR 45-20.190 reserve MGC](https://www.mgc.dps.mo.gov/RulesNRegs/csr_proposed/2025_csr_prop/August_2025/11%20CSR%2045-20.190%20Proposed%20Rule.pdf)
- [iGaming Business on MO rulemaking/launch timing](https://igamingbusiness.com/sports-betting/missouri-secretary-state-rejects-emergency-betting-rules/)
- Confidence: funding methods, withdrawal/winnings timelines, reserve, change management, self-exclusion structure are HIGH but partly sourced from proposed-rule text — confirm final adopted wording. Mandatory limit types and geolocation rule mapping are MEDIUM.
