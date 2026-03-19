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
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Expose nim-libp2p peerstore functionality through C bindings so downstream
projects can access the different peerstore books and add, remove, or update
entries.

#### Deliverables
- C API for reading peerstore data
- C API for adding, removing, and updating peerstore entries
- Tests covering peerstore access through the bindings


### Protocol Handlers

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:handlers`  
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Create a set of C functions that allows a user of the bindings to register
custom protocol handlers and read from or write to streams.

#### Deliverables
- C API for registering custom protocol handlers
- Stream read/write support exposed through the bindings
- Tests covering protocol handler registration and stream I/O


### Capability Discovery

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:capability-discovery`  
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Create a set of C functions that allows a user of the bindings to use
capability discovery.
This task depends on `vac:p2p:acz:2026q2-anoncomms-consulting:capability-discovery` being delivered.

#### Deliverables
- C API for capability discovery
- Example or test coverage for capability discovery through the bindings



### nim-ffi

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-cbindings:nim-ffi`  
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Logos Delivery has an initiative to evolve the Nim C bindings API to use
Protocol Buffers instead of custom structs, while ensuring callbacks are
executed in separate worker threads. Once that work is available, refactor the
existing bindings to take advantage of it.

#### Deliverables
- Existing bindings refactored to use the new FFI approach
- Callback execution aligned with the worker-thread model
