# Michigan — Michigan Gaming Control Board (MGCB)

**Code:** MI · **Products:** sportsbook + iGaming · **Key authority:** Lawful Internet Gaming Act (2019 PA 152, MCL 432.301–432.322) & Lawful Sports Betting Act (2019 PA 149, MCL 432.401 et seq.) + Mich. Admin. Code R 432.601–432.676 (internet gaming) and R 432.701–432.776 (internet sports betting; largely parallel numbering)

## Payments-relevant requirements

### Licensing & change management

- Internet gaming operator license (tribal/commercial casino), internet gaming platform provider = supplier license; lesser vendors register. Payment processors typically fall under supplier licensing or vendor registration depending on function — confirm tier with compliance (MEDIUM confidence).
- MGCB formally adopts GLI-19 "Standards for Interactive Gaming Systems" v3.0 (July 17, 2020) by reference for internet gaming platforms (R 432.633(2)); sports betting platforms have a parallel technical-standards rule (R 432.733).
- The platform must be submitted to the board or a board-approved independent testing laboratory (GLI was the first authorized lab) for certification testing, and offering internet gaming without certification is prohibited (R 432.633(3)-(4)).
- Post-launch software changes are governed by MGCB technical bulletins on approved software (e.g., Technical Bulletin 2024-02): changes to critical components generally require ITL certification/board approval before deployment — bulletin text not directly verified in this research; obtain current bulletin from MGCB (MEDIUM confidence).
- Internal control standards require board approval, and amendments to internal controls follow R 432.663a; emergency procedures per R 432.663b.

### Deposits & permitted payment methods

- Permitted funding (R 432.655a): credit or debit card; cash/cash equivalent at a board-approved cashiering location; verified non-transferable reloadable prepaid card; promotional credit; winnings; documented operator adjustments; ACH transfer (with ACH-fraud security measures and controls); wire transfer; other board-approved means. Credit cards are allowed.
- Failed ACH deposits (R 432.655b): temporarily block the account for fraud investigation after 5 consecutive failed ACH deposit attempts within 10 minutes; suspend after 5 additional consecutive failures; a failed ACH attempt is not treated as fraudulent if the participant previously deposited successfully via ACH with no outstanding chargebacks.
- Transfers of funds between authorized participants/accounts are prohibited (R 432.655c).
- Negative internet wagering account balances are prohibited (R 432.647).
- One wagering account per participant per operator for internet wagering (R 432.651).

### Withdrawals & payout timelines

- Participants must be allowed to withdraw account funds, and operators must honor withdrawal requests within 10 business days of the request (R 432.655d) — the most concrete payout clock of the three deep states.
- A request is considered honored notwithstanding delays by a payment processor, card issuer, or account custodian once the operator has processed it (R 432.655d).
- Withdrawal may be declined only on a good-faith belief of fraud or conduct violating the act/rules; the operator must then give the participant notice describing the investigation, investigate "in a reasonable and expedient fashion," and provide status updates every 10 business days (R 432.655d).
- No explicit reverse-withdrawal provision in R 432.655d; treat withdrawal-cancellation features as requiring compliance sign-off (LOW confidence area).

### Player funds segregation / reserve

- Reserve requirement (R 432.644 internet gaming; R 432.744 internet sports betting, verified text): reserve ≥ sum of (a) daily ending cashable balance of all accounts, (b) pending withdrawals, (c) accepted wagers awaiting outcome, and (d) unpaid winning wagers through the payout period.
- Permitted reserve forms: cash/cash equivalents in a segregated U.S. bank account, irrevocable letter of credit, bond, other board-acceptable form, or any combination (R 432.744(1) and iGaming parallel) — notably more flexible than NJ/PA pure-segregation models.
- Monthly attestation filed with the board that funds are safeguarded; board may audit the reserve at any time and order corrective action (R 432.744(6)-(7)).
- Non-redeemable (promo) amounts may be excluded from the reserve calculation (R 432.744(4)).

### Responsible gambling

- Operators must provide an "easy and obvious" method for self-imposed limits on internet wagering parameters including at minimum deposits, wagers, and time (R 432.653(2)).
- Limits must be implemented immediately (or at the time clearly indicated to the participant) once set (R 432.653(2)(a)); self-imposed limits may only be made LESS restrictive upon 24 hours' notice, or as the board requires (R 432.653(2)(c)).
- Self-imposed limits cannot override more restrictive operator-imposed limits (R 432.653(2)(b)); limit tools must be offered at account creation, at deposit, and at login (R 432.653(3)).
- Statewide MGCB responsible gaming database: establishment R 432.671, voluntary placement for 1 or 5 years R 432.672, distribution to operators R 432.673; separate operator self-exclusion list R 432.674; prohibited persons R 432.675; operator duties to enforce (block accounts/wagers/marketing) R 432.676.
- Responsible gaming page with helpline (Michigan problem gambling helpline), MGCB resource links, and operator RG policy statement (R 432.654).
- Dormant accounts handled per R 432.658; suspension/restoration per R 432.659 (details not verified — pull text before coding).

### KYC / age / geolocation

- Electronic participant file: legal name, DOB, SSN or equivalent ID, account number, address, email, phone; verify age and identity and record verification date before wagering; password/security feature required (R 432.655(c), (e)).
- Minimum age 21 for internet gaming and internet sports betting (MCL 432.305/432.404 framework; age value HIGH confidence, cite MEDIUM).
- Mandatory encryption of SSN portions, passwords/PINs, and personal financial information (R 432.655(b)); data-security rules for age/identity data at R 432.651b; fraud-use handling at R 432.651c.
- Wagers only within Michigan; platform servers/geolocation per technical standards (GLI-19 adoption plus MGCB server-location guidance) (MEDIUM on specific cite).

### AML overlays (state-specific, beyond federal BSA)

- R 432.642 explicitly requires operators/platform providers to comply with the federal Bank Secrecy Act (31 USC 5311–5332) as a STATE rule violation trigger — BSA breaches are also Michigan regulatory breaches.
- Must retain all CTRs, SARs, and supporting documentation for at least 5 years and produce them to MGCB and law enforcement on request (R 432.642).
- Must notify the board in writing immediately of any IRS BSA compliance review, and submit a copy of the review report within 10 days of receipt (R 432.642).
- Integrity monitoring / suspicious wagering behavior reporting per R 432.643.

### Records, reporting & data

- Accounting records R 432.665; records retention R 432.666; annual audits and annual compliance reports R 432.665a; board access to platform data R 432.665b.
- Write-offs, amounts returned, and disputed credit/debit charges (chargebacks) are specifically regulated at R 432.668 — chargeback accounting treatment is a named compliance item.
- Account statements/transaction information to participants per R 432.656; account review requirements R 432.655e.

## Code review focus

- Verify withdrawal pipeline completes (operator-side processing) within 10 business days, with decline only on flagged fraud/violation, auto-generated participant notice, and 10-business-day status-update cadence during investigations.
- Verify limit engine: self-imposed deposit/wager/time limits apply immediately; any loosening is delayed 24 hours; operator-imposed limits always win when more restrictive; limit prompts surfaced at signup, deposit, and login.
- Check ACH failure logic: 5-consecutive-failures-in-10-minutes block, +5 escalation to suspension, and the prior-successful-ACH-no-chargeback exemption implemented exactly.
- Confirm responsible gaming database (state list) AND operator self-exclusion list are both checked before account creation, deposit acceptance, and wager placement.
- Verify reserve/ledger feed computes: cashable balances + pending withdrawals + unsettled accepted wagers + unpaid winnings, excluding non-redeemable promo funds, and supports the monthly attestation.
- Confirm no player-to-player transfers and no negative-balance settlement paths.
- Confirm chargeback/disputed-charge handling follows internal controls mapped to R 432.668 (write-off vs. recovery accounting).
- Confirm release process routes platform changes through ITL (GLI-19) certification/board approval per current MGCB technical bulletin before production deploy.

## Sources & confidence

- [MI internet gaming rules parts index Justia](https://regulations.justia.com/states/michigan/treasury/michigan-gaming-control-board/internet-gaming/) · [R 432.655a Funding Justia](https://regulations.justia.com/states/michigan/treasury/michigan-gaming-control-board/internet-gaming/part-5/section-r-432-655a/) · [R 432.655d Withdrawal Justia](https://regulations.justia.com/states/michigan/treasury/michigan-gaming-control-board/internet-gaming/part-5/section-r-432-655d/) · [R 432.655b Failed ACH Justia](https://regulations.justia.com/states/michigan/treasury/michigan-gaming-control-board/internet-gaming/part-5/section-r-432-655b/) · [R 432.653 Participant protections Justia](https://regulations.justia.com/states/michigan/treasury/michigan-gaming-control-board/internet-gaming/part-5/section-r-432-653/) · [R 432.642 BSA compliance Justia](https://regulations.justia.com/states/michigan/treasury/michigan-gaming-control-board/internet-gaming/part-4/section-r-432-642/) · [R 432.633 Technical standards / GLI-19 Cornell LII](https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-432-633) · [R 432.744 Reserve requirement, sports Cornell LII](https://www.law.cornell.edu/regulations/michigan/Mich-Admin-Code-R-432-744) · [GLI authorized as MI test lab](https://gaminglabs.com/press-releases/gaming-laboratories-international-gli-authorized-to-test-and-certify-igaming-and-mobile-sports-betting-in-michigan/) · [Lawful Internet Gaming Act PA 152 of 2019 MGCB](https://www.michigan.gov/-/media/Project/Websites/mgcb/Internet-Gaming-and-Fantasy-Contests/ActsandRules/Lawful_Internet_Gaming_Act_PA_152_of_2019.pdf?rev=cebcd69627d24920afe4a956175a898c)
- Confidence: HIGH for funding methods, 10-business-day withdrawal clock, failed-ACH thresholds, 24-hour limit-loosening delay, GLI-19 adoption/certification mandate, R 432.642 BSA overlay, and R 432.744 reserve text (iGaming R 432.644 assumed parallel — verify exact wording); MEDIUM for licensing tier of payment processors, post-launch change bulletin details, geolocation cite; LOW for reverse-withdrawal treatment. Route MEDIUM/LOW items to the client's compliance team.
