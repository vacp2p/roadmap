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
* owner: moigagoo
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Continue the NAT traversal work through [`nim-libplum`](https://github.com/logos-storage/nim-libplum), using libplum as the preferred path for PCP, NAT-PMP, and UPnP support.
- Avoid expanding [`nim-nat-traversal`](https://github.com/status-im/nim-nat-traversal/issues/41) directly unless the libplum approach proves unsuitable.
- Decide whether consumers should migrate directly to nim-libplum or whether a compatibility layer / nat-traversal API emulation is worth implementing.

#### Deliverables
- PRs/Issues/Docs/Reports

### Protobuf Serialization Docs

* fully qualified name: `ift-ts:nim:ift:2026q3-nim-core-libs:protobuf-serialization-docs`
* owner: Constantine
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Improve documentation for Protobuf Serialization.
- Cover usage guidance, examples, and integration notes needed by downstream teams.

#### Deliverables
- PRs/Issues/Docs/Reports

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
* status: in progress (25%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- [status-im/nim-json-rpc#283](https://github.com/status-im/nim-json-rpc/pull/283) Restrict proxy server raises to `JsonRpcError`
- [status-im/nim-json-rpc#282](https://github.com/status-im/nim-json-rpc/pull/282) Restrict client raises to `JsonRpcError`
- [status-im/nim-json-rpc#279](https://github.com/status-im/nim-json-rpc/pull/279) Support notification in rpc context for non-async method
- [status-im/nim-json-rpc#263](https://github.com/status-im/nim-json-rpc/pull/263) Documentation book
