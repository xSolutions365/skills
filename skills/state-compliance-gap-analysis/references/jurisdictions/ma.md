# Massachusetts — Massachusetts Gaming Commission (MGC)

**Code:** MA · **Products:** sportsbook · **Key authority:** M.G.L. c. 23N; 205 CMR 200-series (esp. 238, 243, 244, 248)

## Payments-relevant requirements

### Licensing & change management

- 205 CMR 243.01 adopts GLI-33 (Event Wagering Systems, v1.1) by reference with MA-specific amendments; 205 CMR 244 governs approval of sports wagering equipment and independent testing laboratories.
- MA amendments to GLI-33 include: geolocation re-checks every 20 minutes (tighter near borders), primary servers in-Commonwealth unless approved otherwise, technical security audit within 90 days of launch then annually, independent audits at least every 2 years.

### Deposits & permitted payment methods

- 205 CMR 248.10: cash/cash equivalents, EFT (online and mobile payment systems), debit instruments incl. debit cards and prepaid access, plus promo credits, payouts and adjustments.
- CREDIT CARDS BANNED — 248.10(3): "No deposits may be made by credit card, either directly or indirectly, including without limitation through an account funded by credit card, and no Wagering on credit is allowed." (Statutory basis in c. 23N.)

### Withdrawals & payout timelines

- 248.12(5): withdrawals honored by the later of 5 business days of the request or 10 business days after required tax paperwork; delay allowed only for good-faith fraud investigation.
- 248.12(2): withdraw "in the manner in which the funds were deposited, to the extent technologically feasible"; requested amount must be immediately frozen from further use.
- Wagers/withdrawals may not take available balance below $0 (248.08).

### Player funds segregation / reserve

- 205 CMR 238.12: reserve = 110% of total funds in sports wagering accounts (per most recent quarterly report); wagering-liability portion backed by Commission-approved irrevocable letters of credit; patron funds held in trust, not commingled, unavailable to creditors; monthly compliance attestation to MGC.

### Responsible gambling (deposit/spend/time limits, cooling-off, self-exclusion, reverse withdrawal rules)

- 248.16(1): operators MUST offer daily, weekly and monthly deposit limits and daily/weekly/monthly wager (funds-at-risk) limits.
- Limit decreases apply immediately; increases only after the prior limit period expires (confidence MEDIUM on exact mechanics).
- Voluntary self-exclusion program plus 205 CMR 254 temporary (involuntary) prohibition and 205 CMR 255 play management; excluded patrons must be blocked and funds handled per rule.

### KYC / age / geolocation

- 248.03/248.04: registration data = full legal name, DOB, physical address, SSN (or federal equivalent), phone; electronic verification of name/DOB/SSN at account establishment; 21+.
- Geolocation per GLI-33 as amended: 20-minute re-check interval, tighter checks near state borders; wagers only within MA.

### AML overlays (state-specific, beyond federal BSA)

- MA amendment triggers personal-information collection at $10,000 wagers or $600 winnings at 300x odds (tax/AML data capture); no separate state AML program verified beyond BSA — confidence MEDIUM.

### Records, reporting & data

- 205 CMR 238 accounting/internal-control standards; 205 CMR 257 sports wagering data privacy restricts use of patron data.
- Dormancy: accounts inactive 3 years presumed abandoned → Commonwealth Treasurer, with 60-day prior notice and re-verification before reactivation (248.19).

## Code review focus

- Absolute credit card block at deposit, including indirect funding (credit-funded wallets/prepaid) — BIN/funding-source detection required.
- Withdrawal SLA logic: later-of 5 business days / 10 business days post-tax-forms; immediate freeze of requested amount; closed-loop payout to deposit source where feasible.
- Balance floor: reject any wager/withdrawal that would drive available balance below $0.
- Mandatory daily/weekly/monthly deposit and wager limit configuration exposed at registration; decreases immediate, increases deferred.
- Geolocation re-validation every ≤20 minutes during active sessions.
- Dormant-account job: 3-year inactivity flag, 60-day notice, escheatment to Treasurer, re-verification on access.

## Sources & confidence

- [205 CMR 248 account management mass.gov PDF](https://www.mass.gov/doc/205-cmr-248-sports-wagering-account-management/download) · [205 CMR 238.12 reserve Justia](https://regulations.justia.com/states/massachusetts/205-cmr/title-205-cmr-238-00/section-238-12) · [205 CMR 243.01 GLI-33 adoption Cornell LII](https://www.law.cornell.edu/regulations/massachusetts/205-CMR-243-01) · [205 CMR 244 testing labs](https://mass.gov/regulations/205-CMR-24400-approval-of-sports-wagering-equipment-and-testing-laboratories) · [205 CMR 254 temporary prohibition](https://www.mass.gov/regulations/205-CMR-25400-temporary-prohibition-from-sports-wagering)
- HIGH: credit card ban, withdrawal SLA, 110% reserve, GLI-33 adoption, deposit/wager limits, dormancy. Verify with compliance team: limit-increase cooldown mechanics, current GLI-33 version incorporated, self-exclusion rule cites.
