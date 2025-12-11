---

title: nim-libp2p c-bindings  
tags:  
  - "2026q1"  
  - "p2p"  
  - "ift"  
draft: false  
description: Provide c-bindings for nim-libp2p  

---

`vac:p2p:ift:2026q1-nimlibp2p-cbindings`

Continue exposing key nim-libp2p functionality via c-bindings to enables downstream projects like logoscore to embed libp2p functionality directly. 

## Description
Continue the work started in `vac:p2p:ift:2026q1-nimlibp2p-cbindings` to continue exposing nim-libp2p functionality via a c static library, enabling external projects to integrate without depending on nim toolchains. Develop a logos core module that uses these bindings

## Task List

TODO: move tasks that were not completed in 2026q1 here


### mix

* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-cbindings:mix`  
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### description
Extend c-bindings to expose Mix functionality. 
Exported functions must include:  
- Setting up nodes to be used for the Mix Path
- Choose whether exit node is destination or not
This task depends on `vac:p2p:ift:2026q1-nimlibp2p-cbindings:core` being implemented (interaction with streams)

#### deliverables
- Updated c header + library with mix api  
- Tests verifying mix behavior via ffi
- Documentation
