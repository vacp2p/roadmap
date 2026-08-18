---
title: 2026q3 Nim Core Libraries
tags:
  - "2026q3"
  - "nim"
  - "ift"
draft: false
description: Continue evolving Nim core libraries.
---

`ift-ts:nim:ift:2026q3-nim-core-libs`

## Description
Maintain and extend the foundational Nim libraries required by IFT teams.

## Task List

### NAT traversal and nim-libplum

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:nat-traversal-nim-libplum`
* owner: Constantine
* status: done
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Continue the NAT traversal work through [`nim-libplum`](https://github.com/logos-storage/nim-libplum), using libplum as the preferred path for PCP, NAT-PMP, and UPnP support.
- Avoid expanding [`nim-nat-traversal`](https://github.com/status-im/nim-nat-traversal/issues/41) directly unless the libplum approach proves unsuitable.
- Decide whether consumers should migrate directly to nim-libplum or whether a compatibility layer / nat-traversal API emulation is worth implementing.

#### Deliverables
- [logos-storage/nim-libplum#15](https://github.com/logos-storage/nim-libplum/pull/15) feat: protocol filter
- [logos-storage/nim-libplum#16](https://github.com/logos-storage/nim-libplum/pull/16) chore: release 0.6.0
- [logos-storage/nim-libplum#14](https://github.com/logos-storage/nim-libplum/pull/14) chore: point libplum submodule to upstream paullouisageneau master (v0.6.0)
- [logos-storage/nim-libplum#10](https://github.com/logos-storage/nim-libplum/pull/10) Use Nim Docker  image
- [logos-storage/nim-libplum#11](https://github.com/logos-storage/nim-libplum/pull/11) Remove cmake

### Protobuf Serialization Docs

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:protobuf-serialization-docs`
* owner: Constantine
* status: done
* start-date: 2026/07/01
* end-date: 2026/08/18

#### Description
- Improve documentation for Protobuf Serialization.
- Cover usage guidance, examples, and integration notes needed by downstream teams.

#### Deliverables
- [status-im/nim-protobuf-serialization#83](https://github.com/status-im/nim-protobuf-serialization/pull/83) Add docs about serializing with type extensions

### Thread Pool Library

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:thread-pool-library`
* owner: Esteban
* status: in progress (80%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Continue improving [`nim-taskpools`](https://github.com/status-im/nim-taskpools) with fixes and missing functionality.
- Port the remaining relevant taskpool features from [`mratsim/constantine`](https://github.com/mratsim/constantine) into `nim-taskpools`.
- Keep the ported functionality covered by tests and suitable for downstream consumers.

#### Deliverables
- [status-im/nimbus-eth1#4638](https://github.com/status-im/nimbus-eth1/pull/4638) Bump nim-taskpools to v0.2.1
- [status-im/nimbus-eth2#8879](https://github.com/status-im/nimbus-eth2/pull/8879) Bump nim-taskpools to v0.2.1
- [status-im/nim-taskpools#60](https://github.com/status-im/nim-taskpools/pull/60) Bump to v0.2.1
- [status-im/nim-taskpools#63](https://github.com/status-im/nim-taskpools/pull/63) Clean up futexes_macos `XDeclaredButNotUsed`
- [status-im/nim-taskpools#61](https://github.com/status-im/nim-taskpools/pull/61) Fix schedule race cond which causes a hang
- [status-im/nim-taskpools#62](https://github.com/status-im/nim-taskpools/pull/62) Fix emscripten compile target
- [status-im/nim-taskpools#59](https://github.com/status-im/nim-taskpools/pull/59) `sync`: allow awaiting threads to sleep
- [status-im/nim-taskpools#58](https://github.com/status-im/nim-taskpools/pull/58) Set worker current task
- [status-im/nim-taskpools#56](https://github.com/status-im/nim-taskpools/pull/56) Reduce allocs: make TaskNode intrusive to the Flowvar
- [status-im/nim-taskpools#54](https://github.com/status-im/nim-taskpools/pull/54) Fixes #5; Event notifier is a bottleneck for very small tasks
- [status-im/nim-taskpools#51](https://github.com/status-im/nim-taskpools/pull/51) Fix #6; Support tasks submitted from a thread that is not managed by the threadpool
- [status-im/nim-taskpools#55](https://github.com/status-im/nim-taskpools/pull/55) Test suite based on benchs
- [status-im/nim-taskpools#52](https://github.com/status-im/nim-taskpools/pull/52) Fix TSan detected data races

### Nim Web3 Error Handling and Issue Triage

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:nim-web3`
* owner: Constantine
* status: in progress (90%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Review and improve [`nim-web3`](https://github.com/status-im/nim-web3) error handling now that `nim-json-rpc` checked-raises work is mostly done.
- Start with [status-im/nim-web3#257](https://github.com/status-im/nim-web3/issues/257) and clean up outdated or noisy exception handling where relevant.
- Review the open `nim-web3` issue backlog and close or update stale items where possible.

#### Deliverables
- [status-im/nim-web3#262](https://github.com/status-im/nim-web3/pull/262) Replace ci-install.sh with `nimble test`
- [status-im/nim-web3#263](https://github.com/status-im/nim-web3/pull/263) Cherry-pick tests for the Nim packages test suite
- [status-im/nim-web3#45](https://github.com/status-im/nim-web3/issues/45) Encoding of mixed dynamic/fixed arguments fails
- [status-im/nim-web3#215](https://github.com/status-im/nim-web3/issues/215) Nested tuple encoding produces incorrect offset calculations
- [status-im/nim-web3#220](https://github.com/status-im/nim-web3/issues/220) Objects should be transformed as tuple when generating function

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:maintenance`
* owner: Constantine
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- [status-im/nimbus-common-workflow#29](https://github.com/status-im/nimbus-common-workflow/pull/29) Add linux arm64 to matrix
- [status-im/nim-json-rpc#289](https://github.com/status-im/nim-json-rpc/pull/289) Fix #285; Do not swallow cancellations in socket client
- [status-im/nim-chronos#704](https://github.com/status-im/nim-chronos/pull/704) Docs: Improve User Guide visibility
- [status-im/nim-json-rpc#288](https://github.com/status-im/nim-json-rpc/pull/288) CI speed up
- [status-im/nim-protobuf-serialization#114](https://github.com/status-im/nim-protobuf-serialization/pull/114) Add `readFieldPackedIntoIt` without `value` param
- [status-im/nim-faststreams#91](https://github.com/status-im/nim-faststreams/pull/91) Add outputs `pos` comptime support
- [nim-lang/nimble#1818](https://github.com/nim-lang/nimble/pull/1818) Docs: Install Nimble: Simplify the PowerShell oneliner command.
- [status-im/nimbus-eth2#8818](https://github.com/status-im/nimbus-eth2/pull/8818) Feature: Use `Opt` instead of `Option` in Presto code
- [vacp2p/nim-cbor-serialization#40](https://github.com/vacp2p/nim-cbor-serialization/pull/40) Bump to v0.4.2
- [vacp2p/nim-cbor-serialization#39](https://github.com/vacp2p/nim-cbor-serialization/pull/39) Bump nph to 0.7.0
- [vacp2p/nim-cbor-serialization#38](https://github.com/vacp2p/nim-cbor-serialization/pull/38) Fix #36; Compile-time CDDL parsing fails with invalid type
- [status-im/nim-protobuf-serialization#113](https://github.com/status-im/nim-protobuf-serialization/pull/113) Bump to v0.6.1
- [status-im/nim-protobuf-serialization#112](https://github.com/status-im/nim-protobuf-serialization/pull/112) More proto editions tests
- [status-im/nim-protobuf-serialization#109](https://github.com/status-im/nim-protobuf-serialization/pull/109) Add proto editions pragma
- [Nim track-based find-references and go-to-definition announcement](https://forum.nim-lang.org/t/13904)
- [status-im/nim-stint#175](https://github.com/status-im/nim-stint/pull/175) Replace for-loops with staticFor for StInt of size 4096 and lower
- [nim-lang/nimble#1781](https://github.com/nim-lang/nimble/issues/1781) `nimble dump`: nimDir is empty a special version of Nim is required
- [nim-lang/langserver#425](https://github.com/nim-lang/langserver/pull/425) Fix SIGSEGV in writeOutput when writing after stdio teardown
- [nim-lang/langserver#426](https://github.com/nim-lang/langserver/pull/426) Prevent CancelledError escaping addProjectFileToPendingRequest killing the server
- [nim-lang/langserver#427](https://github.com/nim-lang/langserver/pull/427) Fix KeyError in removeIdleNimsuggests aborting idle project cleanup
- [nim-lang/langserver#429](https://github.com/nim-lang/langserver/pull/429) Make markFailed idempotent so one nimsuggest crash restarts once
- [nim-lang/langserver#430](https://github.com/nim-lang/langserver/pull/430) Reset failTable count when a nimsuggest starts successfully
- [status-im/nim-json-rpc#286](https://github.com/status-im/nim-json-rpc/pull/286) CI: test with ASan
- [status-im/nim-json-rpc#281](https://github.com/status-im/nim-json-rpc/pull/281) Fix #280; Result of method returning `void` fails to parse
- [status-im/nim-chronos#688](https://github.com/status-im/nim-chronos/pull/688) Fix error in `new` after replacing getAddress with getHttpAddress
- [status-im/nim-json-rpc#283](https://github.com/status-im/nim-json-rpc/pull/283) Restrict proxy server raises to `JsonRpcError`
- [status-im/nim-json-rpc#282](https://github.com/status-im/nim-json-rpc/pull/282) Restrict client raises to `JsonRpcError`
- [status-im/nim-json-rpc#279](https://github.com/status-im/nim-json-rpc/pull/279) Support notification in rpc context for non-async method
- [status-im/nim-json-rpc#263](https://github.com/status-im/nim-json-rpc/pull/263) Documentation book

### Documentation Improvement

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:docs-improvement`
* owner: Constantine
* status: in progress (25%)
* start-date: 2026/08/01
* end-date: 2026/08/31

#### Description
- Add missing documentation to IFT packages (e.g. Presto).
- Improve documentation tooling (e.g. `nim doc` as mdBook replacement).

#### Deliverables
