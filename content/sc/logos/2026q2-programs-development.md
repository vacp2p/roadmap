---
title: Programs Development
tags:
  - "2026q2"
  - "sc"
  - "logos"
draft: false
description: Ongoing hardening and maintenance work across Logos LEZ programs.
---

`ift-ts:sc:logos:2026q2-programs-development`

## Description

Ongoing development, maintenance, and security hardening for Logos LEZ programs,
including follow-up work across token, ATA, and AMM program boundaries.

## Task List

### Chores

* fully qualified name: `ift-ts:sc:logos:2026q2-programs-development:chores`
* owner: Ricardo/r4bbit
* status: in progress (75%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Track recurring program hardening, defensive checks, dependency upkeep,
and follow-up issues across the LEZ token, ATA, and AMM programs.

#### Deliverables
- [logos-blockchain/lez-programs#70](https://github.com/logos-blockchain/lez-programs/issues/70) Lock token-program ownership and chained-call dispatch across AMM, ATA, and token
- [logos-blockchain/lez-programs#80](https://github.com/logos-blockchain/lez-programs/issues/80) Reject foreign-owned token definitions in InitializeAccount
- [logos-blockchain/lez-programs#73](https://github.com/logos-blockchain/lez-programs/pull/73) chore: fix RISC-V guest build on macOS 26
- [logos-blockchain/lez-programs#87](https://github.com/logos-blockchain/lez-programs/issues/87) Staged lint-baseline track for workspace members and guest crates
- [logos-co/spel#172](https://github.com/logos-co/spel/issues/172) Expose trusted execution context inside instruction handlers
- [logos-blockchain/lez-programs#102](https://github.com/logos-blockchain/lez-programs/pull/102) chore: update LEZ to v0.2.0-rc3
- [logos-blockchain/lez-programs#85](https://github.com/logos-blockchain/lez-programs/pull/85) feat: make use of spel's `[#account_type]` directive
- [logos-blockchain/lez-programs#79](https://github.com/logos-blockchain/lez-programs/pull/79) chore(amm): validate fee tier in `sync_reserves`
- [logos-blockchain/lez-programs#78](https://github.com/logos-blockchain/lez-programs/pull/78) chore(amm): add defensive check for lp token solvency
- [logos-blockchain/lez-programs#71](https://github.com/logos-blockchain/lez-programs/pull/71) fix(amm): validate user deposit accounts are owned by vault's token program
- [logos-blockchain/lez-programs#53](https://github.com/logos-blockchain/lez-programs/issues/53) ATA transfer recipient handling
- [logos-blockchain/lez-programs#103](https://github.com/logos-blockchain/lez-programs/pull/103) fix(ata): lock down `ATA::Transfer` recipient contract
- [logos-blockchain/lez-programs#83](https://github.com/logos-blockchain/lez-programs/issues/83) ATA token program dispatch and occupant validation
- [logos-blockchain/lez-programs#108](https://github.com/logos-blockchain/lez-programs/pull/108) fix(ata): namespace accounts by token program
- [logos-blockchain/lez-programs#89](https://github.com/logos-blockchain/lez-programs/issues/89) Implement `open_position`
- [logos-blockchain/lez-programs#104](https://github.com/logos-blockchain/lez-programs/pull/104) feat(stablecoin): implement `open_position`
- [logos-blockchain/lez-programs#96](https://github.com/logos-blockchain/lez-programs/issues/96) Price feed interface follow-up
- [logos-blockchain/lez-programs#107](https://github.com/logos-blockchain/lez-programs/pull/107) fix(integration_tests) remove no longer needed program ID
- [logos-co/spel#191](https://github.com/logos-co/spel/pull/191) fix(idl-gen): exclude ProgramContext from runtime-generated IDL
- [logos-blockchain/lez-programs#105](https://github.com/logos-blockchain/lez-programs/pull/105) chore: update spel
- [logos-blockchain/lez-programs#110](https://github.com/logos-blockchain/lez-programs/pull/110) chore: update spel to v0.3.0
- [TWAP Oracle account design research](https://notes.status.im/4PlwprLaQEWW4Q_SDT36zw)
- [logos-blockchain/lez-programs#112](https://github.com/logos-blockchain/lez-programs/pull/112) feat(stablecoin): implement withdraw_collateral 
- [logos-blockchain/lez-programs#90](https://github.com/logos-blockchain/lez-programs/issues/90) Implement Deposit Collateral
- [logos-blockchain/lez-programs#123](https://github.com/logos-blockchain/lez-programs/pull/123) docs: update README and CLAUDE.md to reflect current state
- [logos-blockchain/lez-programs#122](https://github.com/logos-blockchain/lez-programs/pull/122) refactor: move programs into `programs` and UIs into `apps`
- [logos-blockchain/lez-programs#121](https://github.com/logos-blockchain/lez-programs/pull/121) chore(Makefile): add `idl` command to `Makefile`
- [logos-blockchain/lez-programs#95](https://github.com/logos-blockchain/lez-programs/issues/95) Stablecoin program follow-up
- [logos-co/scaffold#202](https://github.com/logos-co/scaffold/issues/202) Local sequencer integration-test follow-up
- [logos-co/scaffold#203](https://github.com/logos-co/scaffold/issues/203) Local sequencer integration-test follow-up
- [logos-co/scaffold#204](https://github.com/logos-co/scaffold/issues/204) Local sequencer integration-test follow-up
- [logos-co/scaffold#205](https://github.com/logos-co/scaffold/issues/205) Local sequencer integration-test follow-up
- [logos-co/scaffold#206](https://github.com/logos-co/scaffold/issues/206) Local sequencer integration-test follow-up
- [logos-co/scaffold#207](https://github.com/logos-co/scaffold/issues/207) Local sequencer integration-test follow-up
- [logos-co/scaffold#208](https://github.com/logos-co/scaffold/issues/208) Local sequencer integration-test follow-up
