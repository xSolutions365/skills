# Wyoming — Wyoming Gaming Commission (WGC)

**Code:** WY · **Products:** sportsbook (online only) · **Key authority:** Wyo. Stat. § 9-24-101 et seq. (Online Sports Wagering); WGC Online Sports Wagering Rules (Wyo. Admin. Code, Agency 038, incl. Ch. 6 patron-account rules)

## Payments-relevant requirements

### Licensing & change management

- Operators may not implement "any changes or modifications of the practices, procedures, or representations upon which the approval was based" without prior written Commission approval (2021 adopted rules, Ch. 4 § 3(d) — codified numbering may differ).
- Individuals with the capability to deploy code affecting wagering outcomes must hold occupational permits; systems require evaluation by a Commission-approved independent gaming laboratory, and the Commission may demand hardware/software for evaluation or monitoring.

### Deposits & permitted payment methods

- Deposit rule (Wyo. Admin. Code 038.0002 Ch. 6 § 7) verbatim list includes: travelers checks; foreign currency/coin; certified/cashier's checks and money orders; personal checks/drafts; **"Digital, crypto and virtual currencies"**; online/mobile payment systems supporting EFT; credit and debit cards; prepaid access instruments; bonus/promo credit; winnings; documented operator adjustments; other Commission-approved means.
- Statute backs this: "cash equivalent" expressly includes "digital, crypto and virtual currencies" (Wyo. Stat. § 9-24-101). CURRENT STATUS (verified Feb 2026): Wyoming remains the only US state where sportsbook operators can directly accept crypto from patrons (other states, e.g. VT/IL/KY/NH, only allow third-party crypto-to-cash conversion). Operator adoption in practice is limited; deposits credit in USD terms with audit trail required.
- Credit cards are permitted; operators may charge and deduct fees from patron accounts.

### Withdrawals & payout timelines

- Patrons must be allowed to withdraw account funds; operator "must honor the patron's request to withdraw funds within five (5) business days" (Wyo. Admin. Code 038.0002 Ch. 6 § 9).
- Withdrawal may be declined only on a good-faith belief of fraud/rule violation, with notice to the patron and status updates every 10 business days during investigation; request counts as honored if delay is caused by third-party processors/banks. System must prevent overdrafts except payment-processing errors.

### Player funds segregation / reserve

- Reserve equal to the greater of $25,000 or (daily ending cashable balances + pending withdrawals + wagers with undetermined outcomes + unpaid winnings); forms: cash/cash equivalents in a segregated Wyoming bank account, irrevocable letter of credit, bond, payment-processor reserves/receivables, or Commission-approved alternative (2021 rules Ch. 4 § 12; codified numbering may differ).
- Monthly attestation filed with the Commission that patron funds remain safeguarded; account funds must not be auto-transferred to circumvent reserve rules.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- Players must be able to set daily/weekly/monthly deposit limits and wager (at-risk) limits; decreases effective immediately, increases only after the prior limit period expires and the player reaffirms (Wyo. Admin. Code 038.0002 Ch. 6 § 12).
- Self-exclusion program (rules Ch. 8) plus Director authority for involuntary exclusion; excluded persons are "prohibited persons" barred from holding accounts. No explicit reverse-withdrawal rule located — confidence LOW.

### KYC / age / geolocation

- Minimum wagering age is 18 (lowest of the four states) — persons under 18 are prohibited persons; identity verification required at account creation.
- Geolocation system must "reasonably detect the geolocation of a patron" at account access and wager placement; wagering outside authorized WY boundaries makes the patron a prohibited person.

### AML overlays (state-specific, beyond federal BSA)

- Rules require BSA compliance records retained ≥5 years; prompt reporting to the Commission of suspected illegal activity, identity misrepresentation, and wagering violations. Crypto acceptance heightens practical AML burden (source-of-funds, wallet screening) though the overlay itself is federal.

### Records, reporting & data

- Complaint and integrity-monitoring records ≥5 years; monthly reserve attestations; W-2G/IRS reporting compliance; PII (incl. payment instrument numbers) must be safeguarded.

## Code review focus

- Crypto deposit rail: direct acceptance is legal in WY only — feature flags must be state-scoped; conversion/valuation to USD at credit time needs a full audit trail.
- Withdrawal SLA timer: 5 business days to honor, with a fraud-hold state that emits patron notices and 10-business-day status updates.
- Overdraft prevention at authorization, with an exception path only for payment-processing errors.
- Deposit/wager limit engine: daily/weekly/monthly tiers; limit decreases apply immediately, increases deferred until period expiry + player reaffirmation.
- Reserve computation job (max($25,000, balances + pending withdrawals + open wagers + unpaid wins)) and monthly attestation reporting.
- Age gate at 18 for WY (not 21) — ensure state-specific age configuration rather than a global 21 constant.

## Sources & confidence

- [Wyo. Stat. § 9-24-101](https://law.justia.com/codes/wyoming/title-9/chapter-24/article-1/section-9-24-101/) · [Deposits rule Ch. 6 § 7](https://regulations.justia.com/states/wyoming/agency-038/sub-agency-0002/chapter-6/section-6-7/) · [Withdrawals rule Ch. 6 § 9](https://regulations.justia.com/states/wyoming/agency-038/sub-agency-0002/chapter-6/section-6-9/) · [RG limits rule Ch. 6 § 12](https://regulations.justia.com/states/wyoming/agency-038/sub-agency-0002/chapter-6/section-6-12/) · [WGC 2021 adopted rules Vixio copy](https://gamblingcompliance.vixio.com/sites/default/files/2021-08/Online%20Sports%20Wagering%20Final%20Rules%20(regular%20process).pdf) · [WGC rules page](https://gaming.wyo.gov/rules-and-regs) · [Casino.org crypto status, Feb 2026](https://www.casino.org/news/draftkings-launching-crypto-to-cash-deposits-in-quartet-of-states/)
- HIGH: crypto/digital currency as permitted deposit method, 5-business-day withdrawal, RG limit mechanics, deposit-method list (current codified rules). MEDIUM: reserve formula and change-management cites (drawn from 2021 adopted rules; codified chapter/section numbering has shifted — verify current cites). LOW: reverse-withdrawal treatment; confirm age-18 statutory cite with compliance team.
