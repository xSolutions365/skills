# Montana — Montana Lottery / State Lottery and Sports Wagering Commission (MT Lottery)

**Code:** MT · **Products:** sportsbook — **state-monopoly, on-premises/venue-tethered mobile only; NO statewide mobile sports wagering** · **Key authority:** MCA Title 23, ch. 7 (State Lottery, incl. Sports Wagering), enacted by 2019 HB 725 (Mont. Laws 2019, ch. 284), codified at MCA 23-7-101 et seq. (esp. 23-7-104 Authorization, 23-7-202 Commission powers, 23-7-301 Sales agents, 23-7-401 State lottery fund); ARM Title 2, ch. 63, subch. 13 — Sports Wagering (esp. 2.63.1301 Sports Wagering Accounts, 2.63.1304 Self-Exclusion, 2.63.1305 Responsible Gaming)

## Payments-relevant requirements

### Licensing & change management

- Montana is a **state-run monopoly**, not a commercial-license state: the Montana Lottery (Dept. of Administration) itself operates sports wagering under MCA 23-7-104 ("the operation of sports wagering and ancillary activities are lawful ... when conducted in accordance with the provisions of this chapter and rules of the commission"); there is no separate private "operator" license tier for a sportsbook brand (HIGH — primary statute).
- The Lottery contracts a single technology vendor (Intralot, current 7-year contract signed 1/5/2026, running its Orion platform) to power both the on-premises kiosks and the venue-tethered mobile app "Sports Bet Montana"; SB 330 (2019), a competing bill that would have let taverns run their own terminals/vendors, was **vetoed** in favor of HB 725's lottery-monopoly model (MEDIUM/HIGH — secondary trade press corroborated by the statute's monopoly structure; verify current Intralot contract term directly with Lottery procurement records if this matters for a specific decision).
- Sales agents (the licensed bars/taverns/restaurants hosting kiosks/tethered mobile) hold sports wagering licenses under MCA 23-7-301 and must keep complete, current records of their sales, open to inspection by the commission, director, Dept. of Administration, legislative auditor, or attorney general (HIGH).
- No independent-testing-lab certification requirement equivalent to CO Rule 7.6/7.7 or MD's 24-hour hash validation was located for the sports wagering system specifically — confidence LOW that no such requirement exists; verify against current ARM 2.63.13 text and the Lottery's internal control procedures before relying on this absence.

### Deposits & permitted payment methods

- ARM 2.63.1301: a sports wagering account is funded via deposit including ACH; an account may be suspended for "fraudulent or multiple failed [ACH] deposit attempts," but a single failed ACH attempt is not automatically treated as fraudulent if the player has previously deposited successfully via ACH with no outstanding chargebacks (HIGH — primary rule text via Cornell LII).
- The rule that used to enumerate all approved funding methods, ARM 2.63.409, was **repealed effective 12/7/2019**; the current, complete list of approved deposit instruments (cash at kiosk, debit card, credit card, e-wallet, etc.) was not found in a primary source during this pass. Secondary/aggregator sources describe an e-wallet tied to a debit or credit card, but describe credit cards as usable for deposit while NOT usable for withdrawal — this is **MEDIUM/LOW confidence, not verified against primary statute or current Lottery terms of service**; verify directly with the Montana Lottery before coding a MT-specific payment-method matrix.
- No mandatory per-transaction or per-day deposit dollar cap was located in MCA ch. 7 or ARM 2.63.13; the only "limits" regime found is the player-elected RG self-limit under ARM 2.63.1305 (see Responsible gambling below), not a regulator-imposed ceiling (MEDIUM).

### Withdrawals & payout timelines

- ARM 2.63.1301: funds may be withdrawn from a sports wagering account for wagers; by check or wire transfer made payable to the player and issued/delivered to the address on file; credited to the player's debit card; via a transaction on sports wagering equipment (kiosk cash-out); or other Lottery-approved means (HIGH).
- **No numeric payout SLA** (e.g., CO's 24-hour demand rule or MD's 7-day rule) was located anywhere in MCA Title 23 ch. 7 or ARM 2.63.13 — confidence LOW that none exists (absence is harder to prove than presence); verify with the Lottery's internal control procedures/contract with Intralot before assuming no SLA applies.
- Dormant-account rule: an account is suspended after 18 months of inactivity and subsequently closed, with the balance returned to the player (HIGH — ARM 2.63.1301).

### Player funds segregation / reserve

- Montana's structure differs fundamentally from private-operator states: **the state itself is the operator**, so there is no third-party "player funds vs. operator funds" segregation question in the CO/MD sense. All gross sports-wagering and lottery revenue is deposited into the statutory **"state lottery fund"** (an enterprise fund), MCA 23-7-401; the commission sets the prize/payout percentage and revenue allocation to the state general fund and the STEM scholarship program (MCA 23-7-202) (HIGH — primary statute; note the fund commingles lottery and sports-wagering revenue rather than ring-fencing sports-wagering liabilities separately).
- No CO Rule-6.9-style or MD COMAR-36.10.14.06-style reserve-ratio / segregated-cash-or-LOC requirement specific to sports wagering liabilities was located — confidence MEDIUM that none is needed given the state-fund backstop; recommend confirming with counsel rather than treating this as settled.

### Responsible gambling (limits, cooling-off, self-exclusion, reverse-withdrawal)

- ARM 2.63.1305: the Lottery must offer players self-limiting options inside their account: a deposit limit (daily/weekly/monthly), a spending limit (daily/weekly/monthly), and a daily time-based play limit (HIGH).
- ARM 2.63.1304: a voluntary self-exclusion program exists; a participant acknowledges responsibility for refraining from sports wagering for the exclusion period (HIGH).
- ARM 2.63.1301: account creation is gated on the Lottery confirming the applicant is NOT currently on the self-exclusion list (HIGH).
- No explicit cooling-off period or reverse-withdrawal rule was located in ARM 2.63.13 — confidence LOW; verify current rule text.

### KYC / age / geolocation

- **Minimum age is 18, not 21** — Montana sports wagering rides the state lottery's age floor rather than a commercial-casino 21+ floor; the Lottery must verify the applicant is 18+ and verify identity by physical or electronic means before establishing a sports wagering account (ARM 2.63.1301) (HIGH). Only one account per player is permitted (HIGH).
- **Geolocation is the central legal constraint for MT and is unlike every other state in this matrix**: it is not a state-border geofence — the platform must confirm, via approved geolocation technology, that the bettor's device is physically located **inside the premises of a licensed sales-agent establishment** (a specific bar/tavern/restaurant) at the moment each wager is placed. Corroborated by multiple secondary/trade sources (incl. reporting on the GeoComply Bluetooth-beacon-plus-device-location deployment across ~1,400 licensed venues) (MEDIUM-HIGH on the *fact pattern*; the exact ARM rule citation number for this specific venue-geofencing text was not independently confirmed against a primary rules.mt.gov page in this research pass — mark that specific citation LOW/"verify" before using it in a legal memo, even though the underlying requirement is well corroborated).
- Sports Bet Montana is described in multiple sources as the *only* licensed sports-wagering app in the state, and users can browse/view odds anywhere but can only place a wager or fund a wager while geolocated inside a licensed venue (MEDIUM/HIGH — secondary press, consistent across sources).

### AML overlays (state-specific, beyond federal BSA)

- No Montana-specific AML/SAR statute beyond federal BSA was located; the closest state-specific financial-integrity controls found are the ACH-fraud account-suspension rule (ARM 2.63.1301) and the general sales-agent record-keeping duty (MCA 23-7-301) (LOW/MEDIUM — confirm with compliance/legal before treating this as a complete AML picture).
- **2025 SB 555** (signed by Gov. Gianforte) reportedly bans sweepstakes casinos, prediction markets, and other unlicensed internet gambling platforms operating in Montana, with felony-level penalties for operators (MEDIUM — secondary press only; bill number and effective text not independently verified against the Montana Legislature's bill-tracking site in this pass — mark LOW/"verify" before citing as enacted law). Relevant context: it underscores that anything resembling unlicensed/unauthorized MT sports wagering (e.g., a statewide-mobile deposit flow this codebase might enable by default) sits squarely in the illegal-market exposure this law targets.

### Records, reporting & data

- MCA 23-7-301: sales agents (kiosk/tethered-mobile hosting venues) must keep complete, up-to-date records and accounts of their sales, available for inspection by the commission, director, Dept. of Administration, office of the legislative auditor, or attorney general (HIGH).
- MCA 23-7-202: the commission holds broad rulemaking and oversight authority over sports wagering equipment and associated records (HIGH).
- No sports-wagering-specific record-retention period (e.g., a "3 years" rule like CO's) was located distinct from general Lottery practice — confidence LOW; verify current ARM text.

## Code review focus

- **Montana has no statewide-mobile commercial sports-wagering product — say this plainly in any state-enablement config.** Sports Bet Montana is a single state-monopoly product (Montana Lottery + Intralot); a wager and any deposit that funds it are only lawful when the bettor's device is geolocated **inside a licensed on-premises venue**, not merely inside Montana's borders. If this payment platform's per-state method-rail enablement defaults MT "on" the same way it defaults on true-mobile states (e.g., CO, MD), that is live **illegal-market exposure**: money movement backing a wager placed by an MT user outside a licensed premises is not authorized under MCA 23-7-104, and — because this codebase is not itself the Montana Lottery/Intralot licensee — any MT sports-wagering money movement this platform enables at all should be flagged to product/legal as a potential unauthorized/illegal-market operation, with attendant **UIGEA ("unlawful Internet gambling" under state law) and Wire Act** exposure for the payment facilitator, not just the operator.
- Add an explicit MT jurisdiction/geo constraint distinct from the standard state-boundary geofence used elsewhere: MT needs venue-level (on-premises) geolocation evidence — not just "device is somewhere in Montana" — before authorizing a deposit or wager-funding event, and the default posture for MT should be **deny**, not the default-enabled-elsewhere-so-enabled-here pattern, pending explicit legal sign-off that this platform has any legitimate MT product line at all.
- If any MT-style account path exists in this codebase: mirror the ARM 2.63.1301 ACH nuance — do not auto-flag a single failed ACH attempt as fraud-suspend-worthy when the account has a clean prior ACH deposit history; reserve suspension logic for fraudulent or multiple failures.
- If any MT-style account path exists: implement the 18-month-dormancy auto-suspend/close-with-refund behavior (ARM 2.63.1301), and wire deposit/spend/time self-limits plus self-exclusion-list gating into account creation and deposit authorization (ARM 2.63.1304/1305).
- Age gate must be parameterized per state — MT's 18+ floor is lower than the 21+ used in most other sportsbook states in this matrix; do not hardcode a single cross-state minimum age constant.
- No numeric MT payout SLA was found in primary sources — do not assume a CO-style 24-hour or MD-style 7-day clock applies to MT; if a withdrawal-timeliness control is state-parameterized in code, MT should not silently inherit another state's SLA value.

## Sources & confidence

- [MCA 23-7-104 Authorization of sports wagering](https://mca.legmt.gov/bills/mca/title_0230/chapter_0070/part_0010/section_0040/0230-0070-0010-0040.html)
- [MCA 23-7-103 Definitions](https://mca.legmt.gov/bills/mca/title_0230/chapter_0070/part_0010/section_0030/0230-0070-0010-0030.html)
- [MCA 23-7-301 Sales agents — licenses](https://archive.legmt.gov/bills/mca/title_0230/chapter_0070/part_0030/section_0010/0230-0070-0030-0010.html)
- [MCA 23-7-202 Powers and duties of commission](https://archive.legmt.gov/bills/mca/title_0230/chapter_0070/part_0020/section_0020/0230-0070-0020-0020.html)
- [MCA 23-7-201 State lottery and sports wagering commission](https://mca.legmt.gov/bills/mca/title_0230/chapter_0070/part_0020/section_0010/0230-0070-0020-0010.html)
- [HB 725 2019 session law, ch. 284](https://archive.legmt.gov/bills/2019/sesslaws/ch0284.pdf)
- [Mont. Admin. r. 2.63.1301 — Sports Wagering Accounts Cornell LII](https://www.law.cornell.edu/regulations/montana/Mont-Admin-r-2.63.1301) · [same rule Justia](https://regulations.justia.com/states/montana/department-2/chapter-2-63/subchapter-2-63-13/rule-2-63-1301/)
- [ARM 2.63.1304 Self-Exclusion / 2.63.1305 Responsible Gaming Justia subchapter 2.63.13 index](https://regulations.justia.com/states/montana/department-2/chapter-2-63/subchapter-2-63-13/)
- [Mont. Admin. r. 2.63.409 repealed eff. 12/7/2019 Cornell LII](https://www.law.cornell.edu/regulations/montana/Mont-Admin-r-2.63.409)
- [Montana Sports Betting Act, SB 330 2019, vetoed](https://archive.legmt.gov/bills/2019/billpdf/SB0330.pdf)
- [LegalSportsReport — Montana sports betting launch / geofencing tech](https://www.legalsportsreport.com/38281/montana-sports-betting-march-launch/) · [GeoComply geofencing of MT venues](https://www.legalsportsreport.com/40731/montana-sports-betting-geocomply/)
- [Intralot newsroom — Sports Bet Montana launch](https://www.intralot.com/newsroom/intralot-congratulates-montana-lottery-for-the-launch-of-sports-bet-montana/) (secondary corroboration of the 2026 contract renewal was via general web search, no single stable primary URL captured — verify directly with Montana Lottery procurement records if the contract term matters to a decision)
- Note: [sportsbetmontana.com deposit/withdrawal FAQ pages](https://sportsbetmontana.com/en/view/faqs-deposits) and [withdrawals](https://sportsbetmontana.com/en/view/faqs-withdrawals) exist but render via JavaScript and could not be fetched as text in this research pass — treat any deposit/withdrawal-method claim not tied to ARM 2.63.1301 above as MEDIUM/LOW and re-verify directly against these pages (or Lottery customer support) before relying on it.
- Confidence: HIGH on the state-monopoly structure, no-statewide-mobile / venue-geofenced model, 18+ age floor, ACH-fraud-suspension nuance, withdrawal methods, self-exclusion/RG self-limit rules, sales-agent record-keeping duty, and state-lottery-fund commingling. MEDIUM on the exact current full deposit-method list, the Intralot 2026 contract terms, and the precise ARM rule citation for the venue-level geolocation mandate. LOW / "verify": whether any payout-timeliness SLA exists, whether a sports-wagering-specific reserve/segregation rule exists beyond the state lottery fund, SB 555 (2025)'s exact bill text/effective date, and any post-2025 legislative attempt to open the market to private mobile operators (none was found as of this research pass, 2026-08).
