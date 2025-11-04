---

title: nim-libp2p c-bindings  
tags:  
  - "2025q4"  
  - "p2p"  
  - "ift"  
draft: false  
description: Provide c-bindings for nim-libp2p  

---

`vac:p2p:ift:2025q4-nimlibp2p-cbindings`

Expose nim-libp2p functionality via a c static library, enabling external projects (e.g. logoscore) to integrate without depending on nim toolchains. Implementation may leverage [nim-ffi](https://github.com/waku-org/nim-ffi) and/or [nim-library-template](https://github.com/logos-co/nim-library-template/) as well as previous learnings from building libwaku to simplify binding generation and library packaging.

## Description

Deliver a minimal set of c-bindings around nim-libp2p core. The bindings should cover basic node lifecycle, peer connectivity, and stream i/o. This enables downstream projects like logoscore to embed libp2p functionality directly. Stretch goals include exposing Gossipsub and custom protocol support, which may be deferred to 2026q1.

## Task List

### Core Bindings

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-cbindings:core`  
* owner: rramos
* status: in progress (15%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### description
Implement and test c-bindings for core nim-libp2p functionality. Exported functions must include:  
- switch builder  
- start/stop node 
- access node peer's information (addresses, peerId) 
- connect/disconnect peer  
- dial peer on protocol  
- read/write stream  
- close stream  

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Static c library build artifact  
- Header file exposing ffi-safe api  
- Integration tests demonstrating basic usage
- Documentation

---

### kademlia

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-cbindings:kademlia`  
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### description
Extend c-bindings to expose Kademlia functionality. This task depends on `vac:p2p:ift:2025q4-nimlibp2p-kad-dht`.
Exported functions must include:  
- Bootstrap
- Find Node / Put Value / Get Value / Set Providers / Get Providers 
- Discovery

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### deliverables
- Updated c header + library with kademlia api  
- Tests verifying kademlia behavior via ffi
- Documentation

---

### gossipsub

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-cbindings:gossipsub`  
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### description
Extend c-bindings to expose Gossipsub Functionality. Exported functions must include:  
- start/stop gossipsub  
- publish/subscribe  
- add/remove validators  

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### deliverables
- Updated c header + library with gossipsub api  
- Tests verifying pub/sub behavior via ffi
- Documentation


### Custom Protocols

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-cbindings:custom-protocols`  
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Provide FFI to register and handle custom protocols from c, enabling downstream applications to define custom behaviors.

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- FFI API for custom protocol registration  
- Example implementation + tests
- Documentation
