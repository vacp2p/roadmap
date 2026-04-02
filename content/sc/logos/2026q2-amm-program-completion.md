---
title: AMM Program Completion
tags:
  - "2026q2"
  - "sc"
  - "logos"
draft: false
description: Complete AMM program hardening, fee system, and remaining missing features to make the LEZ AMM production-ready.
---

`ift-ts:sc:logos:2026q2-amm-program-completion`

## Description

The LEZ AMM has a working core (NewDefinition, AddLiquidity, RemoveLiquidity, Swap with constant product formula), but several hardening tasks, missing features, and the fee system remain before it is production-ready.

This commitment completes all outstanding AMM work: merging the near-complete PR #371 (minimum liquidity protection and surplus recovery), adding exact output swap tests, implementing configurable fee tiers with LP trading fees, fixing the `remove_lp` delta calculation to correctly distribute fee surplus, and deploying the full program suite to testnet 0.2.

Transaction expiry support is tracked but blocked pending block context support in LEZ.

## Task List

### Complete and merge PR #371

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:complete-pr-371`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/15

#### Description

Finalize and merge [logos-execution-zone PR #371](https://github.com/logos-blockchain/logos-execution-zone/pull/371), which implements:
- `SyncReserves` instruction to reconcile tracked reserves with actual vault balances
- `RecoverSurplus` instruction to recover directly-transferred tokens from inactive (zero LP supply) pools
- `MINIMUM_LIQUIDITY=1` LP lock to prevent the first-depositor attack (dead shares protection)

Address any outstanding review comments, ensure full test coverage, and get the PR merged.

#### Deliverables

- [ ] PR #371 merged with all review comments resolved
- [ ] Test coverage for SyncReserves, RecoverSurplus, and minimum liquidity protection

### Complete exact output swap (tests + PR)

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:exact-output-swap-tests`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/15

#### Description

The exact output swap implementation was completed in Q1 but lacks tests and a merged PR.
Write comprehensive tests covering exact output swap scenarios (including slippage, edge cases, and fee interactions) and get the PR reviewed and merged.

#### Deliverables

- [ ] Test suite for exact output swap scenarios
- [ ] PR with code review and merge

### Implement configurable fee tiers

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:fee-tiers`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Implement configurable fee tiers for the AMM supporting 0.01%, 0.05%, 0.3%, and 1% fee rates as required by RFP-004.
The `fees: u128` field already exists in `PoolDefinition` but is unused. Wire it up so pool creators can select a fee tier at pool creation time.

#### Deliverables

- [ ] Configurable fee tiers (0.01%, 0.05%, 0.3%, 1%) implemented in the AMM program
- [ ] Fee tier validated at pool creation
- [ ] Test coverage for all fee tier values
- [ ] PR with code review

### Implement trading fees for LPs

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:trading-fees`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Implement trading fee accumulation so that liquidity providers earn a portion of each swap based on the pool's configured fee tier.
Fees accumulate as surplus in the pool vaults above the tracked reserves and are distributed to LPs proportionally when they remove liquidity.

#### Deliverables

- [ ] Trading fee accumulation implemented in the swap instruction
- [ ] Test coverage for fee accumulation across multiple swaps
- [ ] PR with code review

### Fix remove_lp to distribute proportional vault balance

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:fix-remove-lp-delta`
* owner: TBD
* status: not started
* start-date: 2026/05/01
* end-date: 2026/05/31

#### Description

The `remove_lp` delta LP calculation is currently a no-op (always returns the raw `removeAmount`).
Once trading fees accumulate as surplus in pool vaults, exiting LPs must receive their proportional share of the actual vault balance — not just the tracked reserves.
Update `remove_lp` to calculate the LP's proportional share of the real vault balance so that fee earnings are correctly distributed on exit.

#### Deliverables

- [ ] Updated `remove_lp` delta calculation returning proportional share of vault balance
- [ ] Test coverage verifying LPs receive correct fee surplus on exit
- [ ] PR with code review

### Add transaction expiry/deadline support

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:transaction-expiry`
* owner: TBD
* status: blocked
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Add expiry/deadline fields to swap transaction data to protect users from stale transactions being executed at unfavorable prices.
This feature is **blocked** on block context (block timestamp) support landing in LEZ — no block timestamp is currently available in the execution environment.
Once LEZ provides block context, implement and test the deadline check in the swap instruction.

#### Deliverables

- [ ] Transaction deadline field added to swap instruction
- [ ] Deadline validation implemented once block context is available in LEZ
- [ ] Test coverage for expired transaction rejection
- [ ] PR with code review

### Deploy programs to testnet 0.2

* fully qualified name: `ift-ts:sc:logos:2026q2-amm-program-completion:deploy-testnet-02`
* owner: TBD
* status: not started
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description

Deploy the completed AMM, ATA, and token programs from `lez-programs` to testnet 0.2.
Verify that all instructions (NewDefinition, AddLiquidity, RemoveLiquidity, Swap, SyncReserves, RecoverSurplus) work correctly end-to-end on the live testnet.

#### Deliverables

- [ ] AMM, ATA, and token programs deployed to testnet 0.2
- [ ] Verification that all AMM instructions work end-to-end on testnet 0.2
- [ ] Deployment documentation (program IDs, testnet configuration)
