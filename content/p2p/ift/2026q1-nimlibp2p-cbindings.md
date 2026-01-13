---

title: nim-libp2p c-bindings  
tags:  
  - "2026q1"  
  - "p2p"  
  - "ift"  
draft: false  
description: Provide c-bindings for nim-libp2p  

---

`ift-ts:p2p:ift:2026q1-nimlibp2p-cbindings`

Continue exposing key nim-libp2p functionality via c-bindings to enables downstream projects like logoscore to embed libp2p functionality directly. 

## Description
Continue the work started in `ift-ts:p2p:ift:2026q1-nimlibp2p-cbindings` by exposing nim-libp2p functionality via a c static library, enabling external projects to integrate without depending on nim toolchains. Develop a logos core module that uses these bindings

## Task List

TODO: move tasks that were not completed in 2026q1 here

### Core c-bindings

* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-cbindings:core`  
* owner: Richard
* status: in progress (15%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Expose core nim-libp2p functionality via c-bindings, including stream read/write support and basic node/kademlia configuration.

#### Deliverables
- [vacp2p/nim-libp2p#2009](https://github.com/vacp2p/nim-libp2p/pull/2009) feat(cbind): config parameters
- [vacp2p/nim-libp2p#1976](https://github.com/vacp2p/nim-libp2p/pull/1976) feat(cbind): stream read / write


### mix

* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-cbindings:mix`  
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Extend c-bindings to expose Mix functionality. 
Exported functions must include:  
- Setting up nodes to be used for the Mix Path
- Choose whether exit node is destination or not
This task depends on `ift-ts:p2p:ift:2026q1-nimlibp2p-cbindings:core` being implemented (interaction with streams)

#### Deliverables
- Updated c header + library with mix api  
- Tests verifying mix behavior via ffi
- Documentation
