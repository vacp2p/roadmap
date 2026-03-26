---
title: 2026q2 Nim Core Libraries
tags:
  - "2026q2"
  - "nim"
  - "ift"
draft: false
description: Continue evolving Nim core libraries.
---

`ift-ts:nim:ift:2026q2-nim-core-libs`

## Description
Maintain and extend the foundational Nim libraries required by IFT teams.

## Task List

### Protobuf Library Stabilization

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:protobuf-library`
* owner: Nitely
* status: not started
* start-date: 2026/04/01
* end-date: 2026/04/20

#### Description
- Finalize the Nim Protobuf library implementation and bring it to a stable, production-ready state.
- Close the remaining functionality, quality, and API gaps needed for broader adoption in IFT and Logos work.

#### Deliverables
- PRs/Issues/Docs/Reports

### Multithreading and Thread Pool Library

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:thread-pool-library`
* owner: Nitely
* status: not started
* start-date: 2026/04/21
* end-date: 2026/05/15

#### Description
- Review and evaluate existing implementations that Mamy did Constantine.
  - the Constantine thread pools build on nim-taskpools
- extract and adapt reusable components from Constantine
- Reach out to Mamy for potential collaboration and explore EF funding options.
- Merge learnings into a robust, well-tested thread pool lib; implement what is missing (needs to be identified)

#### Deliverables
- PRs/Issues/Docs/Reports

### CBOR Library CDDL Parsing

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:cbor-cddl-parsing`
* owner: Nitely
* status: not started
* start-date: 2026/05/15
* end-date: 2026/05/30

#### Description
- Implement CDDL parsing in the CBOR library.
- Establish the foundation needed for future CBOR/CDDL-driven features while keeping the scope focused on parser support for Q2.

#### Deliverables
- PRs/Issues/Docs/Reports

### Protobuf Serialization in libp2p

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:libp2p-protobuf-serialization`
* owner: Nitely/Constantine
* status: not started
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description
- Add protobuf serialization support within libp2p, aligning scope and design with the existing libp2p stack and future messaging needs.

#### Deliverables
- PRs/Issues/Docs/Reports

### Nim LSP Stability and Editor Support

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:lsp-editor-support`
* owner: Constantine
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/01

#### Description
- Improve the Nim LSP implementation to make editor support substantially more stable and usable.
- Continue bug hunting and implementation work already started in Q1.

#### Deliverables
- PRs/Issues/Docs/Reports

### Documentation

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:docs`
* owner: Constantine
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Produce documentation for the core libs.

#### Deliverables
- PRs/Issues/Docs/Reports

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:maintenance`
* owner: Constantine
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- PRs/Issues/Docs/Reports
