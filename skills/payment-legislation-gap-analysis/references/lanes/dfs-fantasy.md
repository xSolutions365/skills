# DFS / Fantasy sports payment regime

**Lane:** DFS · **Authority:** State DFS statutes (~20+ states with dedicated DFS laws); UIGEA DFS carve-out (31 USC 5362(1)(E)) · **Researched:** Aug 2026

Where a codebase carries fantasy/DFS fund types (often under a legacy wire-format naming divergence) — a **separate regulatory regime** from sports betting, legal in more states, with its own payment/segregation rules — it is easy to overlook in a betting-focused gap analysis.

## Key requirements

- **Player-fund segregation:** most DFS statutes require operator to segregate player funds from operational funds and maintain a reserve ≥ player balances (similar to gaming reserve but under DFS law).
- **Separate eligibility map:** DFS is legal in a different (broader) set of states than OSB/iGaming; some states require DFS registration/licensing; a few prohibit. Per-product eligibility must not conflate DFS with sportsbook.
- **Age limits:** often 18 (vs 21 for betting) — a different age gate per product.
- **Deposit/RG controls:** many DFS laws require deposit limits, self-exclusion, and RG tooling (state-specific).
- **Payment-method rules:** some states apply the same credit-card / method rules to DFS.
- **Fund-type wire-format correctness:** any legacy fund-type naming divergence (e.g. a `FANTASY`-vs-`DFS_*` split) must translate correctly to the wallet — a mis-mapped fund type mis-segregates money.

## Code review focus

- **Fund-type handling for fantasy/DFS:** where a wire-format naming divergence exists, confirm a translation method (e.g. a `toWalletApiCode()`-style call rather than raw `.name()`) is used for wallet-bound strings — a real, code-level correctness risk. Grep `FANTASY`, `DFS_`, `toWalletApiCode`, fund-type enums.
- **Segregation:** are DFS/fantasy balances segregated from sportsbook/casino in the wallet (distinct fund types / reserve)?
- **Per-product eligibility:** does geo/jurisdiction gating distinguish DFS from OSB/iGaming, or treat a state uniformly? (A user legal for DFS but not OSB in the same state.)
- Product-specific age/RG routing.

## Test coverage focus

- **Unit** tests asserting legacy fund types serialize to the correct wallet codes via the translation method (exactly the kind of wire-format gotcha a unit test should lock down).
- Segregation: a test that DFS funds don't commingle with betting funds.
- Per-product eligibility: DFS-eligible-but-OSB-prohibited state handled correctly.

## Sources & confidence

- State DFS statutes (e.g. NY GBL Art. 14, MA, IN, VA DFS acts); UIGEA §5362(1)(E) DFS exclusion; any in-repo notes on the wallet wire-format / fund-type mapping.
- Confidence: MEDIUM — depends whether the operator actively offers DFS through these repos (confirm the product is live vs legacy fund-type scaffolding). The `toWalletApiCode()` correctness check is HIGH-confidence regardless. Pull latest for DFS-law changes.
