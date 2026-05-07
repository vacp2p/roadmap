---
title: Logos LEZ Fuzz Testing
tags:
  - "2026q2"
  - "qa"
  - "logos"
draft: false
description: Define and implement initial fuzz testing coverage for LEZ ahead of Testnet v0.2.
---

`ift-ts:qa:logos:2026q2-lez-fuzz-testing`

## Description
Define and implement an initial fuzz testing effort for LEZ to improve confidence ahead of Testnet v0.2.
The work includes refining the fuzz targets with the LEZ team, implementing the first fuzzing harnesses, and evaluating whether the setup can run effectively in GitHub Actions CI.

## Task List

### LEZ fuzz testing framework

* fully qualified name: `ift-ts:qa:logos:2026q2-lez-fuzz-testing:framework`
* owner: Roman
* status: in progress (35%)
* start-date: 2026/04/13
* end-date: 2026/05/01

#### Description
- Define the first LEZ fuzz targets together with the LEZ team and confirm the closest equivalents in the current codebase.
- Implement initial fuzz testing coverage for at least four target areas:
  transaction decoding / instruction parsing,
  stateless verification checks,
  state transition / execution engine,
  block verification / replayer logic or closest current equivalent.
- Use the most practical implementation language and tooling for the current codebase; Rust is acceptable but not required.
- Evaluate whether the fuzzing setup can run in GitHub Actions runners with useful CI coverage, and document any constraints or need for stronger machines.

#### Deliverables
- Documented LEZ fuzz target definition and scope.
- PRs with initial fuzz harnesses and target implementations.
- Report on CI feasibility and recommended execution model.
- Issues / follow-up tasks for additional targets, benchmarks, or infrastructure gaps.
- [logos-blockchain/lez-fuzzing](https://github.com/logos-blockchain/lez-fuzzing) First LEZ fuzzing proof of concept
- [current_vs_alternative_approach.md](https://github.com/logos-blockchain/lez-fuzzing/blob/main/current_vs_alternative_approach.md) Alternative implementation approaches comparison
