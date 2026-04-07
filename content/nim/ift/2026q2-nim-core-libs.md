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
* status: in progress (25%)
* start-date: 2026/04/01
* end-date: 2026/04/20

#### Description
- Finalize the Nim Protobuf library implementation and bring it to a stable, production-ready state.
- Close the remaining functionality, quality, and API gaps needed for broader adoption in IFT and Logos work.

#### Deliverables
- [status-im/nim-protobuf-serialization#67](https://github.com/status-im/nim-protobuf-serialization/pull/67) Fix: treat unexpected wire type as unknown field
- [status-im/nim-protobuf-serialization#68](https://github.com/status-im/nim-protobuf-serialization/pull/68) Improve test suite
- [status-im/nim-protobuf-serialization#66](https://github.com/status-im/nim-protobuf-serialization/pull/66) Fix: length delimited records must only accept varint int32 length

### Multithreading and Thread Pool Library

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:thread-pool-library`
* owner: Nitely
* status: not started
* start-date: 2026/04/21
* end-date: 2026/05/15

#### Description
- Improve [`nim-taskpools`](https://github.com/status-im/nim-taskpools), with particular attention to the gaps tracked in issue `#6` and related missing functionality.
- Review and evaluate the existing implementations that Mamy built in the [`mratsim/constantine`](https://github.com/mratsim/constantine) library.
  - The Constantine thread pools build on `nim-taskpools`.
- Extract and adapt reusable components from Constantine where appropriate.
- Reach out to Mamy for potential collaboration and explore EF funding options.
- Merge the learnings into a robust, well-tested thread pool library and implement the missing parts identified during the review.

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
- This work should prepare for near-term needs around generating Nim code from CDDL, or the reverse direction, as those capabilities are expected to be needed soon.

#### Deliverables
- PRs/Issues/Docs/Reports

### Unittest2 Expected Failures

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:unittest2-expected-failures`
* owner: Constantine
* status: not started
* start-date: 2026/05/15
* end-date: 2026/05/30

#### Description
- Add support for expected failures in `nim-unittest2`.
- Enable the testing workflow needed when work starts on larger features that require temporarily tracking known failing cases without losing test signal.

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
- Build on the stabilized protobuf library and make the integration practical for real libp2p protocol work.

#### Deliverables
- PRs/Issues/Docs/Reports

### PCP Support in nim-nat-traversal

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:nat-traversal-pcp-support`
* owner: Constantine
* status: not started
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description
- Implement PCP support in [`nim-nat-traversal`](https://github.com/status-im/nim-nat-traversal/issues/41).
- Evaluate the preferred option of wrapping `libplum`, removing the other two libraries, and getting rid of the current make-based build system.
- Keep the native Chronos-based implementation as an alternative if it proves more practical.

#### Deliverables
- PRs/Issues/Docs/Reports

### Nim LSP Stability and Editor Support

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:lsp-editor-support`
* owner: Constantine
* status: in progress (20%)
* start-date: 2026/04/01
* end-date: 2026/06/01

#### Description
- Improve the Nim LSP implementation to make editor support substantially more stable and usable.
- Continue bug hunting and implementation work already started in Q1.
- Treat `nimsuggest` as the practical short-term path: fix low-hanging-fruit bugs with immediate benefits, improve stability and performance for Nim 2 codebases of our size, and then work toward better feature completeness on the LSP side.
- The end goal is better `nim-langserver` behavior and better integration in editors such as VS Code, with the added benefit that language servers may also be used as MCP providers.

#### Deliverables
- PRs/Issues/Docs/Reports

### Documentation

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:docs`
* owner: Constantine
* status: in progress (20%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Produce documentation for the core libs.

#### Deliverables
- [nim-lang/nimble#1657](https://github.com/nim-lang/nimble/pull/1657) Fix nimble installation instructions

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:maintenance`
* owner: Constantine
* status: in progress (10%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- [status-im/nim-stint#157](https://github.com/status-im/nim-stint/issues/157) Implement carryingAdd on uint64 for 32-bit platforms
- [status-im/nim-stint#179](https://github.com/status-im/nim-stint/issues/179) CI failing on 32-bit Linux
- [nim-lang/nimble#1663](https://github.com/nim-lang/nimble/issues/1663) `nimble dump` resolves absolute paths incorrectly
