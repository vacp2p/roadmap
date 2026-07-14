---
title: Logos LEZ Fuzz Testing
tags:
  - "2026q3"
  - "qa"
  - "logos"
draft: false
description: Maintain and extend LEZ fuzz testing coverage and framework reliability.
---

`ift-ts:qa:logos:2026q3-lez-fuzz-testing`

## Description
Maintain the LEZ fuzz testing framework introduced in Q2 and keep it useful as the LEZ implementation evolves.
The work includes updating fuzz targets, corpus handling, CI execution, and follow-up coverage for regressions or newly exposed execution paths.

## Task List

### Framework maintenance

* fully qualified name: `ift-ts:qa:logos:2026q3-lez-fuzz-testing:framework-maintenance`
* owner: Roman
* status: done
* start-date: 2026/07/01
* end-date: 2026/07/14

#### Description
- Maintain the LEZ fuzz testing framework and keep existing targets compatible with upstream code changes.
- Extend or adjust fuzz targets when new LEZ execution paths, invariants, or regressions are identified.
- Keep corpus update automation and CI execution useful, documenting constraints or infrastructure gaps when they appear.

#### Deliverables
- [Town Hall presentation and demo](https://youtu.be/XIwJwK0RAlk?t=357)
- [logos-blockchain/lez-fuzzing#19](https://github.com/logos-blockchain/lez-fuzzing/pull/19) chore: automated weekly corpus update
- [logos-blockchain/logos-execution-zone#609](https://github.com/logos-blockchain/logos-execution-zone/pull/609) test: Address missed mutants - bridge guard
- [logos-blockchain/lez-fuzzing#18](https://github.com/logos-blockchain/lez-fuzzing/pull/18) chore: Sync with LEZ - address mutants not fuzzable
- [logos-blockchain/lez-fuzzing#13](https://github.com/logos-blockchain/lez-fuzzing/pull/13) chore: automated weekly corpus update
- [logos-blockchain/lez-fuzzing#14](https://github.com/logos-blockchain/lez-fuzzing/pull/14) test: Transaction ordering independence
- [logos-blockchain/lez-fuzzing#15](https://github.com/logos-blockchain/lez-fuzzing/pull/15) test: Model based stateful lockstep
