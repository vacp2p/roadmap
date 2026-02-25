---
title: AMM Fee System and Swap Improvements
tags:
  - "2026q1"
  - "sc"
  - "logos"
draft: false
description: Clarify fee requirements with ecodev team, implement trading and protocol fees, and add missing swap features.
---

`ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements`

## Description

Implement the fee system and missing swap features for the LEZ AMM program.
The AMM currently has no trading fees (LPs don't earn from swaps) and no protocol fees.
Additionally, several swap features are missing including exact output amount swaps and transaction expiry support.

Fee requirements must first be clarified with the ecodev team to determine whether trading and protocol fees are wanted and what the fee structure should be.
The `remove_lp` function's delta LP calculation also needs to be updated to properly account for accrued fees once implemented.

## Task List

### Clarify fee requirements with ecodev team

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements:clarify-fee-requirements`
* owner: r4bbit
* status: in progress (5%)
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Coordinate with the ecodev team to clarify whether trading fees (LP earnings) and protocol fees are wanted for the LEZ AMM.
If fees are desired, determine the fee structure, fee parameters, and how they should be configured (e.g., global config, per-pool config).

#### Deliverables

- [ ] Fee structure specification (if fees are wanted)
- [ ] Documentation of fee parameters and configuration approach

### Implement trading fees for LPs

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements:trading-fees`
* owner: r4bbit
* status: in progress (5%)
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Based on ecodev team clarification, implement trading fees so that liquidity providers earn a portion of each swap.
Currently, LPs don't earn anything from trading activity in the pool.

#### Deliverables

- [ ] Implementation of trading fee mechanism
- [ ] Fee accumulation and distribution logic for LPs
- [ ] Test coverage for fee calculation scenarios
- [ ] PRs with code reviews

### Implement protocol fees

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements:protocol-fees`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Based on ecodev team clarification, implement protocol fees with global configuration.
Protocol fees are a portion of trading fees directed to the protocol rather than LPs.

#### Deliverables

- [ ] Implementation of protocol fee mechanism
- [ ] Global fee configuration support
- [ ] Test coverage for protocol fee scenarios
- [ ] PRs with code reviews

### Update remove_lp delta LP calculation for fees

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements:fix-remove-lp-delta`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Fix the delta LP calculation in the `remove_lp` function which is currently a no-op (always returns `removeAmount`).
Once fees are implemented, the delta LP calculation needs to properly account for accrued trading fees so that LPs receive their fair share of accumulated fees when removing liquidity.

#### Deliverables

- [ ] Updated `remove_lp` delta LP calculation accounting for fees
- [ ] Test coverage for fee-aware liquidity removal
- [ ] PRs with code reviews

### Implement exact output amount swap

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements:exact-output-swap`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Implement the missing exact output amount swap functionality.
Currently, only exact input swaps are supported. Users should also be able to specify a desired output amount and have the required input calculated.

#### Deliverables

- [ ] Implementation of exact output amount swap
- [ ] Test coverage for exact output swap scenarios
- [ ] PRs with code reviews

### Add transaction expiry/deadline support

* fully qualified name: `ift-ts:sc:logos:2026q1-amm-fee-system-and-swap-improvements:transaction-expiry`
* owner: TBD
* status: not started
* start-date: 2026/03/01
* end-date: 2026/03/31

#### Description

Add expiry/deadline fields to transaction data to protect users from stale transactions being executed at unfavorable prices.
This is a standard AMM safety feature that prevents transactions from being held and executed later when market conditions have changed.

#### Deliverables

- [ ] Implementation of transaction expiry/deadline mechanism
- [ ] Test coverage for expired transaction rejection
- [ ] PRs with code reviews
