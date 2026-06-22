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
* status: done
* start-date: 2026/04/01
* end-date: 2026/05/12

#### Description
- Finalize the Nim Protobuf library implementation and bring it to a stable, production-ready state.
- Close the remaining functionality, quality, and API gaps needed for broader adoption in IFT and Logos work.

#### Deliverables
- [status-im/nim-protobuf-serialization#74](https://github.com/status-im/nim-protobuf-serialization/pull/74) Return whether the field is known in `readFieldInto`
- [status-im/nim-protobuf-serialization#73](https://github.com/status-im/nim-protobuf-serialization/pull/73) Validate `PBOption` inner type
- [status-im/nim-protobuf-serialization#72](https://github.com/status-im/nim-protobuf-serialization/pull/72) Fix header varint read
- [status-im/nim-protobuf-serialization#71](https://github.com/status-im/nim-protobuf-serialization/pull/71) Add `valueOr` for `PBOption`
- [status-im/nim-protobuf-serialization#67](https://github.com/status-im/nim-protobuf-serialization/pull/67) Fix: treat unexpected wire type as unknown field
- [status-im/nim-protobuf-serialization#68](https://github.com/status-im/nim-protobuf-serialization/pull/68) Improve test suite
- [status-im/nim-protobuf-serialization#66](https://github.com/status-im/nim-protobuf-serialization/pull/66) Fix: length delimited records must only accept varint int32 length
- [status-im/nim-protobuf-serialization#69](https://github.com/status-im/nim-protobuf-serialization/pull/69) import_proto3: Generate `seq[Entry]` for map type
- [status-im/nim-protobuf-serialization#75](https://github.com/status-im/nim-protobuf-serialization/pull/75) Extensions: `enum` and `results.Opt`
- [status-im/nim-protobuf-serialization#77](https://github.com/status-im/nim-protobuf-serialization/pull/77) Fix: do not add to `seq` if wire type is unexpected
- [status-im/nim-protobuf-serialization#76](https://github.com/status-im/nim-protobuf-serialization/pull/76) Fix: do not set `PBOption` if wire type is unexpected
- [status-im/nim-protobuf-serialization#79](https://github.com/status-im/nim-protobuf-serialization/pull/79) Bump to v0.4.0
- [status-im/nim-protobuf-serialization#78](https://github.com/status-im/nim-protobuf-serialization/pull/78) Fix verification error for `seq[object]` extensions
- [status-im/nim-protobuf-serialization#80](https://github.com/status-im/nim-protobuf-serialization/pull/80) Support custom seq[T] serializer for extensions
- [status-im/nim-protobuf-serialization#81](https://github.com/status-im/nim-protobuf-serialization/pull/81) Fix `newSeqUninitialized` deprecation warning
- [status-im/nim-protobuf-serialization#92](https://github.com/status-im/nim-protobuf-serialization/pull/92) Bump to v0.5.0
- [status-im/nim-protobuf-serialization#70](https://github.com/status-im/nim-protobuf-serialization/pull/70) Implement `Oneof` fields
- [status-im/nim-protobuf-serialization#86](https://github.com/status-im/nim-protobuf-serialization/pull/86) Support `results.Opt` extension in `proto3`
- [status-im/nim-protobuf-serialization#91](https://github.com/status-im/nim-protobuf-serialization/pull/91) Add missing `seq[byte]` proto2 validation
- [status-im/nim-protobuf-serialization#87](https://github.com/status-im/nim-protobuf-serialization/pull/87) Fix optional field message merging
- [status-im/nim-protobuf-serialization#84](https://github.com/status-im/nim-protobuf-serialization/pull/84) Fix `PBOption` for invalid `std/enum` values
- [status-im/nim-protobuf-serialization#85](https://github.com/status-im/nim-protobuf-serialization/pull/85) Pass `--enforce_recommended` to conformance tests
- [status-im/nim-protobuf-serialization#93](https://github.com/status-im/nim-protobuf-serialization/pull/93) Fixes #52; import_proto3: add `service` parsing & type generation hook
- [status-im/nim-protobuf-serialization#96](https://github.com/status-im/nim-protobuf-serialization/pull/96) import_proto3: parse enum field options
- [status-im/nim-protobuf-serialization#99](https://github.com/status-im/nim-protobuf-serialization/pull/99) import_proto3: fix deeply nested messages
- [status-im/nim-protobuf-serialization#100](https://github.com/status-im/nim-protobuf-serialization/pull/100) import_proto3: `optional` field support
- [status-im/nim-protobuf-serialization#101](https://github.com/status-im/nim-protobuf-serialization/pull/101) Bump to v0.5.2
- [status-im/nim-protobuf-serialization#102](https://github.com/status-im/nim-protobuf-serialization/pull/102) Validate `Opt[seq]`, `Opt[Opt]`, `Opt[PBOption]` are not allowed

### Multithreading and Thread Pool Library

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:thread-pool-library`
* owner: Nitely
* status: in progress (50%)
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
* status: done
* start-date: 2026/05/15
* end-date: 2026/05/26

#### Description
- Implement CDDL parsing in the CBOR library.
- Establish the foundation needed for future CBOR/CDDL-driven features while keeping the scope focused on parser support for Q2.
- This work should prepare for near-term needs around generating Nim code from CDDL, or the reverse direction, as those capabilities are expected to be needed soon.

#### Deliverables
- [vacp2p/nim-cbor-serialization#28](https://github.com/vacp2p/nim-cbor-serialization/pull/28) Add diagnostic notation serializer
- [vacp2p/nim-cbor-serialization#29](https://github.com/vacp2p/nim-cbor-serialization/pull/29) Add CDDL parser
- [vacp2p/nim-cbor-serialization#31](https://github.com/vacp2p/nim-cbor-serialization/pull/31) CDDL: `int` -> `int64`; `uint` -> `uint64`
- [vacp2p/nim-cbor-serialization#30](https://github.com/vacp2p/nim-cbor-serialization/pull/30) CDDL: `any` -> `CborBytes`; `tools/cddl` -> `cddl`
- [vacp2p/nim-cbor-serialization#17](https://github.com/vacp2p/nim-cbor-serialization/pull/17) Perf improvement
- [vacp2p/nim-cbor-serialization#32](https://github.com/vacp2p/nim-cbor-serialization/pull/32) Bump to v0.4.0

### Unittest2 Expected Failures

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:unittest2-expected-failures`
* owner: Constantine
* status: in progress (10%)
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
* status: in progress (50%)
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description
- Add protobuf serialization support within libp2p, aligning scope and design with the existing libp2p stack and future messaging needs.
- Build on the stabilized protobuf library and make the integration practical for real libp2p protocol work.

#### Deliverables
- [vacp2p/nim-libp2p#2166](https://github.com/vacp2p/nim-libp2p/pull/2166) chore: Use protobuf_serialization in RendezVous protocol
- [vacp2p/nim-libp2p#2477](https://github.com/vacp2p/nim-libp2p/pull/2477) Protobuf serialization of the DCUtR protocol
- [vacp2p/nim-libp2p#2608](https://github.com/vacp2p/nim-libp2p/pull/2608) Bump `protobuf_serialization` to v0.5.0

### PCP Support in nim-nat-traversal

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:nat-traversal-pcp-support`
* owner: Constantine
* status: in progress (10%)
* start-date: 2026/06/01
* end-date: 2026/06/30

#### Description
- Implement PCP support in [`nim-nat-traversal`](https://github.com/status-im/nim-nat-traversal/issues/41).
- Evaluate the preferred option of wrapping `libplum`, removing the other two libraries, and getting rid of the current make-based build system.
- Keep the native Chronos-based implementation as an alternative if it proves more practical.

#### Deliverables
- PRs/Issues/Docs/Reports
- [status-im/nim-nat-traversal#41](https://github.com/status-im/nim-nat-traversal/issues/41) PCP support in nim-nat-traversal
- [logos-storage/nim-libplum#9](https://github.com/logos-storage/nim-libplum/issues/9) Tests: Use Nim Docker image

### Nim LSP Stability and Editor Support

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:lsp-editor-support`
* owner: Constantine
* status: in progress (95%)
* start-date: 2026/04/01
* end-date: 2026/06/01

#### Description
- Improve the Nim LSP implementation to make editor support substantially more stable and usable.
- Continue bug hunting and implementation work already started in Q1.
- Treat `nimsuggest` as the practical short-term path: fix low-hanging-fruit bugs with immediate benefits, improve stability and performance for Nim 2 codebases of our size, and then work toward better feature completeness on the LSP side.
- The end goal is better `nim-langserver` behavior and better integration in editors such as VS Code, with the added benefit that language servers may also be used as MCP providers.

#### Deliverables
- [nim-lang/langserver#390](https://github.com/nim-lang/langserver/pull/390) Jump to next diagnostics
- [nim-lang/langserver#387](https://github.com/nim-lang/langserver/issues/387) Neovim 0.12 compatibility
- [nim-lang/langserver#388](https://github.com/nim-lang/langserver/pull/388) nimlangserver MCP server
- [nim-lang/langserver#393](https://github.com/nim-lang/langserver/pull/393) Fix compatibility with Neovim 0.12 diagnostic floating window
- nimlangserver 1.14.0 released and announced.
- [nim-lang/langserver#400](https://github.com/nim-lang/langserver/pull/400) MCPB bundle
- [Nim langserver MCP registry entry](https://registry.modelcontextprotocol.io/?q=nimlangserver)
- [nim-lang/langserver#416](https://github.com/nim-lang/langserver/pull/416) Speed up initialization by not waiting for nimsuggest to start
- [nim-lang/nimble#1713](https://github.com/nim-lang/nimble/issues/1713) Slow `nimble dump` issue reported with collected data

### Documentation

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:docs`
* owner: Constantine
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/21

#### Description
- Produce documentation for the core libs.

#### Deliverables
- [nim-lang/nimble#1657](https://github.com/nim-lang/nimble/pull/1657) Fix nimble installation instructions
- [status-im/nim-unittest2#70](https://github.com/status-im/nim-unittest2/pull/70) Add docs in MdBook format
- [nim-lang/nimble#1701](https://github.com/nim-lang/nimble/pull/1701) Guide: Install Nim: Add instruction about installing devel Nim
- [nim-lang/langserver#406](https://github.com/nim-lang/langserver/pull/406) Resolve conflicts in the nimlangserver mdBook PR
- HTTP client tutorial rewritten with two new chapters.

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q2-nim-core-libs:maintenance`
* owner: Constantine
* status: in progress (25%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- [status-im/nim-json-rpc#264](https://github.com/status-im/nim-json-rpc/pull/264) Make async pragma required in rpc context API
- [status-im/nim-json-rpc#271](https://github.com/status-im/nim-json-rpc/pull/271) Fix custom socket framing to support concurrency
- [status-im/nim-json-rpc#270](https://github.com/status-im/nim-json-rpc/pull/270) Fix #261 regression; support unordered responses again
- [status-im/nim-json-rpc#272](https://github.com/status-im/nim-json-rpc/pull/272) v0.6.0
- [status-im/nimbus-eth1#3914](https://github.com/status-im/nimbus-eth1/pull/3914) EthJson Rpc flavor
- [status-im/nimbus-eth2#7853](https://github.com/status-im/nimbus-eth2/pull/7853) EthJson Rpc flavor
- [status-im/nim-web3#237](https://github.com/status-im/nim-web3/pull/237) Replace JrpcConv by custom EthJson flavor
- [status-im/nim-json-rpc#275](https://github.com/status-im/nim-json-rpc/pull/275) Fix json_rpc `meth` bug
- [status-im/nim-json-rpc#274](https://github.com/status-im/nim-json-rpc/issues/274) json_rpc `meth` bug
- [nim-lang/nimble#1692](https://github.com/nim-lang/nimble/issues/1692) Nimble and Chronos issue
- [status-im/nim-json-rpc#278](https://github.com/status-im/nim-json-rpc/pull/278) Bump to v0.6.1
- [nim-lang/nimble#1693](https://github.com/nim-lang/nimble/issues/1693) `nimble upgrade pkg` issue
- [status-im/nim-stint#180](https://github.com/status-im/nim-stint/pull/180) Fixed CI for 32-bit Linux
- [status-im/nim-stint#157](https://github.com/status-im/nim-stint/issues/157) Implement carryingAdd on uint64 for 32-bit platforms
- [status-im/nim-stint#179](https://github.com/status-im/nim-stint/issues/179) CI failing on 32-bit Linux
- [nim-lang/nimble#1663](https://github.com/nim-lang/nimble/issues/1663) `nimble dump` resolves absolute paths incorrectly
- [status-im/nim-json-rpc#276](https://github.com/status-im/nim-json-rpc/pull/276) Terminate conn on invalid response `id` and do not send a response for it
- [status-im/nim-stew#271](https://github.com/status-im/nim-stew/pull/271) enums: fix `hasHoles` overflow in 32bit platforms for int32 enum values
