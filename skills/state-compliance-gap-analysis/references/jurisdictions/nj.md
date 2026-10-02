# New Jersey — Division of Gaming Enforcement (DGE)

**Code:** NJ · **Products:** sportsbook + iGaming · **Key authority:** Casino Control Act (N.J.S.A. 5:12) + N.J.A.C. 13:69 (esp. 13:69O Internet and Mobile Gaming, 13:69D Accounting & Internal Controls, 13:69N Sports Wagering)

## Payments-relevant requirements

### Licensing & change management

- Internet gaming/sports wagering runs under a casino licensee; platform and significant service providers need a Casino Service Industry Enterprise (CSIE) license, lesser vendors an ancillary CSIE/vendor registration — payment processors typically fall in the vendor/ancillary tier (confirm tier with compliance team).
- Gaming software must be submitted to and approved by the DGE Technical Services Bureau (TSB); NJ runs its own lab review rather than simply deferring to GLI (N.J.A.C. 13:69E-1.20 inspection/approval of gaming equipment and software).
- Change control for "controlled" software: routine installs/upgrades require Release Notes to the Division 3 business days in advance, demonstrated rollback capability, and pre-deployment testing (N.J.A.C. 13:69D-2.3(f)).
- Emergency changes may be installed immediately but the Division must be notified within 1 business day and receive Release Notes within 3 business days; required source-code review/functional testing must complete within 3 business days of an emergency install (13:69D-2.3(g), (c)(3), (d)(5)).

### Deposits & permitted payment methods

- Permitted funding: deposit accounts, credit/debit cards, cash/chips at approved cashiering locations, verified non-transferable reloadable prepaid cards, promotional/bonus credit, winnings, ACH, sports wagering kiosks, gift cards, and other Division-approved methods (N.J.A.C. 13:69O-1.3(d)). Credit cards are allowed.
- Gift-card deposits are capped at $500 per patron per gaming day (13:69O-1.3(u)).
- Fraud control: after 5 consecutive failed deposit attempts within 10 minutes the account must be temporarily blocked for fraud investigation; 5 further consecutive failures escalate to suspension (13:69O-1.3(e)).
- One account per patron per operator/intermediary; accounts non-transferable; patron-to-patron transfers prohibited (13:69O-1.3(c), (h)).

### Withdrawals & payout timelines

- Permitted withdrawal channels: funding of game play, cage cash-out, transfer to deposit account/prepaid card, bank (ACH) transfer, and sports wagering kiosk withdrawal up to $3,000 (13:69O-1.3(g)).
- Card-deposit refund routing: remaining balance up to the amount of a credit/debit deposit must be refunded back to that card (13:69O-1.3(f)).
- Operators are prohibited from imposing any wagering requirement or other limitation on withdrawal of a patron's own (cashable) funds (13:69O-1.3(s)).
- Operators must not offer incentives to cancel/reverse a pending withdrawal (13:69O-1.3(t)).
- In-person withdrawals of $500+ at a casino/racetrack require photo capture and ID verification per N.J.A.C. 13:69D-1.5A (13:69O-1.4(u)).
- NJ regulation does not state a single hard "pay within X days" clock in 13:69O-1.3; DGE has policed slow payouts via bulletins/internal controls — verify current expectations with compliance (confidence: MEDIUM on absence of a codified day-count).

### Player funds segregation / reserve

- Patron funds must be held in a dedicated account at a state/federally chartered, FDIC-insured bank located in New Jersey (absent Division exception), separate from operating funds (13:69O-1.3(k)).
- The dedicated account balance must equal or exceed the sum of all patron account balances plus pending withdrawals at all times (13:69O-1.3(k)).
- Monthly filings to the Division's Revenue Certification Unit demonstrating sufficiency; monthly bank statements for the restricted patron account go to the Division (13:69O-1.3(k), 13:69O-1.9).

### Responsible gambling

- System must offer daily/weekly/monthly deposit limits, spend (at-risk) limits, and daily time-based limits (13:69O-1.4(n)).
- Limit decreases take effect at next login; increases take effect only after the previous limit's period has expired — no early loosening (13:69O-1.4(n)).
- Self-suspension (cooling off) must be offered for a patron-specified period of not less than 72 hours (13:69O-1.4(j)); while suspended, no wagers or deposits (except to cure a negative balance) and withdrawals restricted, with prominent notice (13:69O-1.4(k)).
- Lifetime-deposit threshold: when cumulative deposits exceed $2,500 the system must halt wagering until the patron acknowledges the threshold, responsible gaming options, and 1-800-GAMBLER; re-acknowledgment annually (13:69O-1.4(r)-(s)).
- On self-exclusion notification: void pending wagers within 3 days and refund cashable balance within 90 days (balances under $1.00 exempt) (13:69O-1.3(p)); exclusion-list check required at account creation and before play (13:69O-1.3(b)(5)).
- Dormant accounts: 30-day notice before removing funds ≥$1.00; by the 5th of each month all cashable funds must be swept from accounts that went dormant the prior month (13:69O-1.3(o)).

### KYC / age / geolocation

- Electronic patron file with verified legal name, DOB, SSN (last 4 acceptable), address, email, phone; multi-source authentication is the primary KYC method before account creation, with logged manual fallback (13:69O-1.3(b)).
- Minimum age 21; identity verification per 13:69D-1.5A (security questions — 3 attempts/5 minutes, phone verification, credential examination, or Division-approved alternative) (13:69O-1.3(b)(3)).
- Periodic re-verification required on reasonable suspicion an identity is compromised (13:69O-1.3(m)).
- Wagers only within NJ borders via Division-approved geolocation (13:69O-1.2/1.4; the CSIE/geolocation framework is well established — treat exact cite as MEDIUM confidence).

### AML overlays (state-specific)

- Federal BSA/Title 31 applies (casino operators are BSA financial institutions); DGE additionally expects prompt reporting of suspicious/criminal activity and cooperation with DGE investigations — the state-specific SAR-copy mechanics should be confirmed with compliance (confidence: LOW on specific cite).
- Encryption mandated for SSNs, passwords/PINs, and financial account data in the patron file (13:69O-1.3(b)(10)).

### Records, reporting & data

- Daily reports per gaming day: Patron Account Summary (deposits, withdrawals, transfers to/from game, adjustments, ending balances), Wagering Summary, non-cashable promo balance and forfeited bonus winnings reports (13:69O-1.9).
- Daily variance report reconciling patron-account totals against wagering totals, with documented reasons and manual revenue adjustment where unexplained (13:69O-1.9(f)).
- Test accounts: individually assigned, fully logged, with internal controls for funding and out-of-state testing authorization (13:69O-1.9(o)).

## Code review focus

- Verify limit-increase logic: an increase to deposit/spend/time limits must not activate until the current limit period expires; decreases apply at next login.
- Verify the 5-failed-deposits-in-10-minutes counter triggers a temporary account block, and 5 more failures trigger suspension.
- Confirm withdrawal flow has no wagering/playthrough gate on cashable funds and no UI or messaging that incentivizes cancelling a pending withdrawal.
- Confirm card deposits are refunded back to the source card up to the deposited amount before other withdrawal rails are used.
- Check gift-card deposit aggregation enforces the $500/gaming-day cap per patron.
- Check self-exclusion handling: block at deposit AND wager placement, void pending wagers within 3 days, auto-refund within 90 days.
- Check the $2,500 lifetime-deposit acknowledgment interrupt (and annual re-trigger) blocks further wagering until acknowledged.
- Confirm deployment pipeline supports DGE change control: 3-business-day advance Release Notes, rollback capability, and emergency-change notification within 1 business day.

## Sources & confidence

- [N.J.A.C. 13:69O-1.3 Cornell LII](https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69O-1-3) · [N.J.A.C. 13:69O-1.4 Cornell LII](https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69O-1-4) · [N.J.A.C. 13:69O-1.9 Cornell LII](https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69O-1-9) · [N.J.A.C. 13:69D-2.3 Cornell LII](https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69D-2-3) · [N.J.A.C. 13:69E-1.20 Cornell LII](https://www.law.cornell.edu/regulations/new-jersey/N-J-A-C-13-69E-1-20) · [DGE Technical Services Bureau](https://www.njoag.gov/about/divisions-and-offices/division-of-gaming-enforcement-home/slot-laboratory-tsb/) · [DGE Chapter 69O text nj.gov](https://www.nj.gov/lps/ge/docs/Regulations/CHAPTER69O.pdf)
- Confidence: HIGH for items with 13:69O/13:69D cites above (verified against Cornell LII current text); MEDIUM for vendor-licensing tier, geolocation cite, and absence of a codified payout day-count; LOW for state-specific AML reporting mechanics — confirm those three areas with the client's compliance team.
