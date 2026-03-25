---
title: DEX SDK
tags:
  - "2026q2"
  - "sc"
  - "logos"
draft: false
description: Build an SDK enabling developers to integrate with the privacy-preserving DEX on LEZ, covering swap, liquidity management, pool queries, and pre-swap simulation.
---

`ift-ts:sc:logos:2026q2-dex-sdk`

## Description

Build a developer SDK for the LEZ privacy-preserving DEX as required by RFP-004.
The SDK abstracts the low-level program instruction building and account derivation, exposing a clean API for swap execution, liquidity management, pool queries, slippage configuration, and pre-swap output simulation.

The SDK will be used by the DEX logos module (mini-app) and is intended as the primary integration point for any developer building on top of the DEX.
LEZ's native privacy model (deshield/re-shield) is handled transparently by the protocol; the SDK does not need to implement it separately.

## Task List

### Clarify and decide SDK platform

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-sdk:clarify-sdk-platform`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/15

#### Description

Evaluate whether the SDK should be implemented in Rust, JavaScript/TypeScript, or both.
Key considerations: what language the logos module (C++ Qt plugin) is most easily integrated with, what clients (CLI tools, web, desktop) need to use it, and whether an FFI boundary is needed.
Produce a decision document with rationale.

#### Deliverables

- [ ] SDK platform decision document (Rust / JS/TS / both) with rationale

### Design SDK API

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-sdk:design-sdk-api`
* owner: TBD
* status: not started
* start-date: 2026/04/15
* end-date: 2026/04/30

#### Description

Design the public API surface of the SDK covering: swap (exact input and exact output), add/remove liquidity, pool queries (reserves, fee tier, LP supply), slippage tolerance configuration, and pre-swap output estimation.
Produce an API design document with type signatures and usage examples before implementation begins.

#### Deliverables

- [ ] API design document with type signatures for all SDK methods
- [ ] Usage examples for swap, liquidity management, and pool query flows

### Implement SDK core

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-sdk:implement-sdk-core`
* owner: TBD
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/15

#### Description

Implement the SDK core based on the approved API design: instruction builders for all AMM operations, PDA/account derivation helpers, transaction construction, and error handling.
Include unit tests covering instruction building and account derivation.

#### Deliverables

- [ ] SDK core implementation (instruction builders, account derivation, transaction construction)
- [ ] Unit test suite for SDK core
- [ ] PR with code review

### Implement pre-swap simulation

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-sdk:pre-swap-simulation`
* owner: TBD
* status: not started
* start-date: 2026/05/15
* end-date: 2026/06/15

#### Description

Implement a pre-swap simulation function that computes the expected output amount, price impact, and fee cost for a given swap without submitting a transaction.
This is required by RFP-004 so the DEX UI can show users a pre-swap confirmation with accurate output and cost information.

#### Deliverables

- [ ] Pre-swap simulation function (output amount, price impact, fees)
- [ ] Test coverage for simulation accuracy across fee tiers and pool sizes
- [ ] PR with code review

### SDK documentation and usage examples

* fully qualified name: `ift-ts:sc:logos:2026q2-dex-sdk:sdk-docs`
* owner: TBD
* status: not started
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description

Write SDK documentation covering installation, configuration, and usage for all major flows: swap, add/remove liquidity, pool queries, and pre-swap simulation.
Include runnable code examples.

#### Deliverables

- [ ] SDK README with installation and quick-start guide
- [ ] Documented usage examples for swap, liquidity, and pool query flows
