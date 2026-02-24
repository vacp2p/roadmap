---
title: 2026q1 Nim Core Libraries
tags:
  - "2026q1"
  - "nim"
  - "ift"
draft: false
description: Continue evolving Nim core libraries.
---

`ift-ts:nim:ift:2026q1-nim-core-libs`

## Description
Maintain and extend the foundational Nim libraries required by IFT teams.

## Task List

### Json RPC

* fully qualified name: `ift-ts:nim:ift:2026q1-nim-core-libs:json-rpc`
* owner: Nitely
* status: in progress (70%)
* start-date: 2026/01/01
* end-date: 2025/02/14

#### Description
- Improve JSON-RPC (e.g: https://github.com/status-im/nim-json-rpc) by adding support for custom protocol flavors, 
CBOR payloads, and more comprehensive documentation. 
These enhancements will enable JSON-RPC to be used efficiently for cross-thread and cross-process (IPC) RPC protocol

#### Deliverables
- PRs
  - [vacp2p/nim-cbor-serialization#24](https://github.com/vacp2p/nim-cbor-serialization/pull/24) Bump to v0.3.0
  - [vacp2p/nim-cbor-serialization#23](https://github.com/vacp2p/nim-cbor-serialization/pull/23) Avoid DefaultFlavor ambiguity
  - [vacp2p/nim-cbor-serialization#22](https://github.com/vacp2p/nim-cbor-serialization/pull/22) Prefix error types
  - [vacp2p/nim-cbor-serialization#20](https://github.com/vacp2p/nim-cbor-serialization/pull/20) Avoid mixin ambiguity errors
  - [status-im/nim-json-rpc#259](https://github.com/status-im/nim-json-rpc/pull/259) Fix #239; allow custom JSON flavors for client code

### Integrate nim-intops into nim-bncurve and nim-stint

* fully qualified name: `ift-ts:nim:ift:2026q1-nim-core-libs:intops-integration-bncurve-stint`
* owner: Juan/Constantine
* status: in progress (99%)
* start-date: 2026/01/01
* end-date: 2026/02/14

#### Description
- Integrate [`nim-intops`](https://github.com/vacp2p/nim-intops) into both [`nim-bncurve`](https://github.com/status-im/nim-bncurve) and [`nim-stint`](https://github.com/status-im/nim-stint), ensuring compatibility, performance, and test coverage across both codebases.

#### Deliverables
- PRs
  - [vacp2p/nim-intops#11](https://github.com/vacp2p/nim-intops/pull/11) Merged the benchmarks PR
- Docs
  - [Guide on creating new benchmarks](https://vacp2p.github.io/nim-intops/contrib.html#writing-benchmarks)
  - [vacp2p/nim-intops#18](https://github.com/vacp2p/nim-intops/pull/18) Added testing against more Nim versions
- Releases
  - [nim-intops changelog](https://github.com/vacp2p/nim-intops/blob/develop/changelog.md) Released six intops versions

### Protobuf Serialization in libp2p

* fully qualified name: `ift-ts:nim:ift:2026q1-nim-core-libs:libp2p-protobuf-serialization`
* owner: Nitely
* status: in progress (5%)
* start-date: 2026/02/15
* end-date: 2026/03/31

#### Description
- Add protobuf serialization support within libp2p, aligning scope and design with the existing libp2p stack and future messaging needs.

#### Deliverables
- PRs

### Language Server and Editor Integration

* fully qualified name: `ift-ts:nim:ift:2026q1-nim-core-libs:language-server-editor-integration`
* owner: Constantine
* status: in progress (5%)
* start-date: 2026/02/14
* end-date: 2026/03/31

#### Description
- Develop language-server capabilities and editor integrations.

#### Deliverables
- [nim-lang/langserver#380](https://github.com/nim-lang/langserver/issues/380) Started researching the issue with no backticked symbols in picker
- [nim-lang/langserver#226](https://github.com/nim-lang/langserver/issues/226) Missing licence Misplaced inlay hints
- PRs

### Documentation

* fully qualified name: `ift-ts:nim:ift:2026q1-nim-core-libs:docs`
* owner: Constantine
* status: in progress (20%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
- Produce documentation for the core libs.

#### Deliverables
- Docs
  - [status-im/nim-chronos#617](https://github.com/status-im/nim-chronos/pull/617) Chronos tutorial chapters: Request and Concurrency
  - [status-im/nimbus-common-workflow#17](https://github.com/status-im/nimbus-common-workflow/pull/17) Add common workflow for docs (mdBook)
  - [status-im/nim-stint#171](https://github.com/status-im/nim-stint/pull/171) Docs updates
  - [nim-stint docs site](https://status-im.github.io/nim-stint/)
  - [status-im/nim-chronos#612](https://github.com/status-im/nim-chronos/pull/612) Optimize mdBook build time

### Maintenance

* fully qualified name: `ift-ts:nim:ift:2026q1-nim-core-libs:maintenance`
* owner: Constantine
* status: in progress (20%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
- Ongoing maintenance and fixes across Nim core libraries.

#### Deliverables
- PRs
  - [status-im/nim-stew#266](https://github.com/status-im/nim-stew/pull/266) Deprecate saturating_arith and saturation_arith
  - [status-im/nim-unittest2#65](https://github.com/status-im/nim-unittest2/pull/65) Fix print expression content
  - [M] Pinned default mdBook version in the common docs workflow: https://github.com/status-im/nimbus-common-workflow/pull/20
  - Reported that `nimble install -g foo bar` installs only `bar`: https://github.com/nim-lang/nimble/issues/1604
  - [vacp2p/nim-intops#20](https://github.com/vacp2p/nim-intops/pull/20) Improve narrowingDiv based on review comments
  - [status-im/nimbus-common-workflow#15](https://github.com/status-im/nimbus-common-workflow/pull/15/) Fix Nimbus common workflow for tests
  - [status-im/nim-stint#172](https://github.com/status-im/nim-stint/pull/172/changes) Code review PR
- Releases
  - [nim-intops 1.0.7 changelog](https://github.com/vacp2p/nim-intops/blob/develop/changelog.md#107-february-2-2026)
