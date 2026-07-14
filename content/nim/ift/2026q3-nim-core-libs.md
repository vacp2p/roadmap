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
* status: in progress (50%)
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
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Improve documentation for Protobuf Serialization.
- Cover usage guidance, examples, and integration notes needed by downstream teams.

#### Deliverables
- [status-im/nim-protobuf-serialization#83](https://github.com/status-im/nim-protobuf-serialization/pull/83) Add docs about serializing with type extensions

### Thread Pool Library

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:thread-pool-library`
* owner: Esteban
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Continue improving [`nim-taskpools`](https://github.com/status-im/nim-taskpools) with fixes and missing functionality.
- Port the remaining relevant taskpool features from [`mratsim/constantine`](https://github.com/mratsim/constantine) into `nim-taskpools`.
- Keep the ported functionality covered by tests and suitable for downstream consumers.

#### Deliverables
- [status-im/nim-taskpools#52](https://github.com/status-im/nim-taskpools/pull/52) Fix TSan detected data races

### Nim Web3 Error Handling and Issue Triage

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:nim-web3`
* owner: Constantine
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Review and improve [`nim-web3`](https://github.com/status-im/nim-web3) error handling now that `nim-json-rpc` checked-raises work is mostly done.
- Start with [status-im/nim-web3#257](https://github.com/status-im/nim-web3/issues/257) and clean up outdated or noisy exception handling where relevant.
- Review the open `nim-web3` issue backlog and close or update stale items where possible.

#### Deliverables
- PRs/Issues/Docs/Reports

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:maintenance`
* owner: Constantine
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- [status-im/nim-json-rpc#286](https://github.com/status-im/nim-json-rpc/pull/286) CI: test with ASan
- [status-im/nim-json-rpc#281](https://github.com/status-im/nim-json-rpc/pull/281) Fix #280; Result of method returning `void` fails to parse
- [status-im/nim-chronos#688](https://github.com/status-im/nim-chronos/pull/688) Fix error in `new` after replacing getAddress with getHttpAddress
- [status-im/nim-json-rpc#283](https://github.com/status-im/nim-json-rpc/pull/283) Restrict proxy server raises to `JsonRpcError`
- [status-im/nim-json-rpc#282](https://github.com/status-im/nim-json-rpc/pull/282) Restrict client raises to `JsonRpcError`
- [status-im/nim-json-rpc#279](https://github.com/status-im/nim-json-rpc/pull/279) Support notification in rpc context for non-async method
- [status-im/nim-json-rpc#263](https://github.com/status-im/nim-json-rpc/pull/263) Documentation book
