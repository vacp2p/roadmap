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
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/10

#### Description

Review and merge the open PR #1 (`chore/initial-setup`) in `logos-blockchain/lez-programs`.
The branch already contains the AMM and token programs ported over from `logos-execution-zone`, along with CI pipelines, IDL files, and Claude Code skills.
Address any review comments and get the branch merged to establish the canonical workspace.

#### Deliverables

- [ ] PR #1 reviewed and merged into `logos-blockchain/lez-programs`
- [ ] CI passing on the main branch (build, test, lint)

### Migrate ATA program into lez-programs

* fully qualified name: `ift-ts:sc:logos:2026q2-lez-programs-repo-setup:migrate-ata-program`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/15

#### Description

Migrate the Associated Token Account (ATA) program from the open PR #387 in `logos-execution-zone` into the `lez-programs` workspace.
Ensure the ATA program has the same CI coverage and IDL generation as the AMM and token programs.

#### Deliverables

- [ ] ATA program migrated to `logos-blockchain/lez-programs`
- [ ] CI covering ATA program build, test, and IDL generation
- [ ] PR with code review

### Make logos-execution-zone depend on lez-programs

* fully qualified name: `ift-ts:sc:logos:2026q2-lez-programs-repo-setup:lez-dependency-integration`
* owner: TBD
* status: not started
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
