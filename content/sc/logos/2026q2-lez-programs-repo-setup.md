---
title: LEZ Programs Repository Setup
tags:
  - "2026q2"
  - "sc"
  - "logos"
draft: false
description: Establish logos-blockchain/lez-programs as the primary development home for the AMM, ATA, and token programs, replacing the programs/ directory in logos-execution-zone.
---

`ift-ts:sc:logos:2026q2-lez-programs-repo-setup`

## Description

The LEZ smart contract programs (AMM, token, ATA) currently live inside the `logos-execution-zone` repository.
To enable faster iteration, independent CI, and cleaner versioning, they are being moved to a dedicated `logos-blockchain/lez-programs` Rust workspace.

This commitment covers getting that repository fully operational: merging the initial setup PR, migrating the remaining ATA program, integrating it as a Cargo dependency in `logos-execution-zone`, and documenting the local development workflow for the team.

## Task List

### Review, finalize, and merge initial workspace setup (PR #1)

* fully qualified name: `ift-ts:sc:logos:2026q2-lez-programs-repo-setup:merge-initial-setup`
* owner: r4bbit
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/04/10

#### Description

Review and merge the open PR #1 (`chore/initial-setup`) in `logos-blockchain/lez-programs`.
The branch already contains the AMM and token programs ported over from `logos-execution-zone`, along with CI pipelines, IDL files, and Claude Code skills.
Address any review comments and get the branch merged to establish the canonical workspace.

#### Deliverables
- [logos-blockchain/lez-programs#1](https://github.com/logos-blockchain/lez-programs/pull/1) chore: initial repository setup for programs
- [logos-blockchain/lez-programs#22](https://github.com/logos-blockchain/lez-programs/pull/22) chore: update `spel` and `logos-execution-zone` dependencies
- [logos-blockchain/lez-programs#23](https://github.com/logos-blockchain/lez-programs/pull/23) cleanup(ata): remove redundant test directive
- [logos-blockchain/lez-programs#3](https://github.com/logos-blockchain/lez-programs/pull/3) skills: update `spel-cli` references to use `spel`
- [logos-blockchain/lez-programs#41](https://github.com/logos-blockchain/lez-programs/pull/41) ci: add IDL freshness check and consolidate artifacts

### Migrate ATA program into lez-programs

* fully qualified name: `ift-ts:sc:logos:2026q2-lez-programs-repo-setup:migrate-ata-program`
* owner: r4bbit
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/04/15

#### Description

Migrate the Associated Token Account (ATA) program from the open PR #387 in `logos-execution-zone` into the `lez-programs` workspace.
Ensure the ATA program has the same CI coverage and IDL generation as the AMM and token programs.

#### Deliverables
- [logos-blockchain/lez-programs#2](https://github.com/logos-blockchain/lez-programs/pull/2) chore(ata): add IDL for ata program
- [logos-blockchain/lez-programs#24](https://github.com/logos-blockchain/lez-programs/pull/24) test(ata): add integration for private accounts create public ATAs

### Make logos-execution-zone depend on lez-programs

* fully qualified name: `ift-ts:sc:logos:2026q2-lez-programs-repo-setup:lez-dependency-integration`
* owner: Ricardo
* status: in progress (10%)
* start-date: 2026/04/10
* end-date: 2026/04/30

#### Description

Update `logos-execution-zone` to consume the programs from `lez-programs` as a Cargo dependency instead of maintaining its own copy.
Remove the duplicate `programs/` directory from `logos-execution-zone` once the dependency is working.
During the transition, keep the new `lez-programs` workspace in sync with ongoing AMM and program changes that are still landing in `logos-execution-zone`, so new functionality can be ported over without diverging code paths.

#### Deliverables

- [ ] `logos-execution-zone` builds with `lez-programs` as a Cargo dependency
- [ ] Duplicate `programs/` directory removed from `logos-execution-zone`
- [ ] Ongoing program changes ported or synchronized into `lez-programs` during the migration window
- [ ] PR with code review
- [logos-blockchain/lez-programs#43](https://github.com/logos-blockchain/lez-programs/issues/43) Update to LEZ dependency to latest version
- [logos-blockchain/lez-programs#48](https://github.com/logos-blockchain/lez-programs/issues/48) Update SPEL to the latest version
- [logos-blockchain/lez-programs#52](https://github.com/logos-blockchain/lez-programs/pull/52) chore/update lez

### Document local development setup

* fully qualified name: `ift-ts:sc:logos:2026q2-lez-programs-repo-setup:dev-setup-docs`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/30

#### Description

Write a getting-started guide covering the full local development workflow for `lez-programs`:
RISC0 toolchain installation, wallet CLI setup, `lez-cli` usage, deploying programs to devnet, and running the test suite.

#### Deliverables

- [ ] Getting-started guide in `lez-programs` repository (README or docs/)
- [ ] Instructions covering toolchain setup, deployment to devnet, and running tests
