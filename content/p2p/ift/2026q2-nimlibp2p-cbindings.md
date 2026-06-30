---

title: nim-libp2p c-bindings
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Provide C bindings for nim-libp2p

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings`

Continue exposing key nim-libp2p functionality via C bindings to enable
downstream projects to embed libp2p functionality directly.

## Description
Continue the work started in `ift-ts:p2p:ift:2026q1-nimlibp2p-cbindings` by
exposing nim-libp2p functionality through a C static library, enabling
external projects to integrate without depending on Nim toolchains.

## Task List

### Peerstore

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:peerstore`  
* owner: gabe
* status: done
* start-date: 2026/05/08
* end-date: 2026/05/05

#### Description
Expose nim-libp2p peerstore functionality through C bindings so downstream
projects can access the different peerstore books and add, remove, or update
entries.

#### Deliverables
- C API for reading peerstore data
- C API for adding, removing, and updating peerstore entries
- Tests covering peerstore access through the bindings
- [vacp2p/nim-libp2p#2346](https://github.com/vacp2p/nim-libp2p/pull/2346) feat(cbind): add peerstore


### Protocol Handlers

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:handlers`  
* owner: rramos
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/28

#### Description
Create a set of C functions that allows a user of the bindings to register
custom protocol handlers and read from or write to streams.

#### Deliverables
- C API for registering custom protocol handlers
- Stream read/write support exposed through the bindings
- Tests covering protocol handler registration and stream I/O
- [vacp2p/nim-libp2p#2314](https://github.com/vacp2p/nim-libp2p/pull/2314) feat(cbind): register custom protocol handlers


### Capability Discovery

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:capability-discovery`  
* owner: gabe
* status: done
* start-date: 2026/04/17
* end-date: 2026/04/28

#### Description
Create a set of C functions that allows a user of the bindings to use
capability discovery.
This task depends on `ift-ts:p2p:ift:2026q2-anoncomms-consulting:capability-discovery` being delivered.

#### Deliverables
- C API for capability discovery
- Example or test coverage for capability discovery through the bindings
- [vacp2p/nim-libp2p#2324](https://github.com/vacp2p/nim-libp2p/pull/2324) chore(cbind): add service discovery



### nim-ffi

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:nim-ffi`  
* owner: gabe
* status: in progress (98%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Logos Delivery has an initiative to evolve the Nim C bindings API to use
Protocol Buffers instead of custom structs, while ensuring callbacks are
executed in separate worker threads. Once that work is available, refactor the
existing bindings to take advantage of it.

#### Deliverables
- [vacp2p/nim-libp2p#2668](https://github.com/vacp2p/nim-libp2p/pull/2668) feat(cbind): user-provided XPRs
- [vacp2p/nim-libp2p#2625](https://github.com/vacp2p/nim-libp2p/pull/2625) feat(cbind): expose metrics via libp2p_collect_metrics
- [logos-messaging/nim-ffi#100](https://github.com/logos-messaging/nim-ffi/pull/100) chore: bump Nim to 2.2.6
- [logos-messaging/nim-ffi#99](https://github.com/logos-messaging/nim-ffi/pull/99) feat(ffi): scalar type mappings + seq[byte] byte-string codec
- [logos-messaging/nim-ffi#97](https://github.com/logos-messaging/nim-ffi/pull/97) test(bench): submit-throughput scaling gate for sendRequestToFFIThread (issue #90)
- [logos-messaging/nim-ffi#88](https://github.com/logos-messaging/nim-ffi/pull/88) feat(ffi): cwire codec composite fields
- [logos-messaging/nim-ffi#87](https://github.com/logos-messaging/nim-ffi/pull/87) feat(ffi): cwire codec core (flat scalars + strings)
- [logos-messaging/nim-ffi#86](https://github.com/logos-messaging/nim-ffi/pull/86) test(bench): cbor vs c (cwire) codec microbenchmark
- [logos-messaging/nim-ffi#85](https://github.com/logos-messaging/nim-ffi/pull/85) feat(ffi): per-interaction ABI-format annotations + c codec (ffiRaw)
- Existing bindings refactored to use the new FFI approach
- Callback execution aligned with the worker-thread model
- [logos-messaging/nim-ffi#20](https://github.com/logos-messaging/nim-ffi/pull/20) chore: run tests with refc
- [logos-messaging/nim-ffi#19](https://github.com/logos-messaging/nim-ffi/pull/19) chore: remove CatchableError
- [logos-messaging/nim-ffi#21](https://github.com/logos-messaging/nim-ffi/pull/21) fix: context buffer overflow
- [logos-messaging/nim-ffi#26](https://github.com/logos-messaging/nim-ffi/pull/26) chore(ci): run tests in parallel
- [logos-messaging/nim-ffi#38](https://github.com/logos-messaging/nim-ffi/pull/38) chore(ci): extend cpp-e2e to OS matrix
- [logos-messaging/nim-ffi#34](https://github.com/logos-messaging/nim-ffi/pull/34) chore(ci): fsanitize tests
- [logos-messaging/nim-ffi#46](https://github.com/logos-messaging/nim-ffi/pull/46) chore: avoid throwing exceptions in C++ bindings
- [logos-messaging/nim-ffi#41](https://github.com/logos-messaging/nim-ffi/pull/41) tests: cover gaps in CBOR type coverage
- [logos-messaging/nim-ffi#42](https://github.com/logos-messaging/nim-ffi/pull/42) test(cpp-e2e): add multi-context, cross-library, pipeline, stress tests
- [logos-messaging/nim-ffi#71](https://github.com/logos-messaging/nim-ffi/pull/71) Add event-thread scaffolding and split `FFIContext` lifecycle work
- [logos-messaging/nim-ffi#69](https://github.com/logos-messaging/nim-ffi/pull/69) feat: move user event code to a dedicated event thread
- [logos-messaging/nim-ffi#77](https://github.com/logos-messaging/nim-ffi/pull/77) chore(ci): add nph linting
