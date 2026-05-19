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
