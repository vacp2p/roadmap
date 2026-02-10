---

title: nim-libp2p logos-core
tags:  
  - "2026q1"  
  - "p2p"  
  - "ift"  
draft: false  
description: Logos Core module for libp2p

---

`ift-ts:p2p:ift:2026q1-nimlibp2p-logos-core`

Continue exposing key nim-libp2p functionality via c-bindings to enables downstream projects like logoscore to embed libp2p functionality directly. 

## Description
Using nim-libp2p's c-bindings develop logos-core modules that would let libp2p features to be consumed from within Logos

## Task List

### logos module

* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-logos-core:core`  
* owner: Gabe
* status: in progress (60%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Using the c-bindings module from nim-libp2p, develop a logos module that would allow nim-libp2p
to be used in logos.

#### Deliverables
- [logos-co/logos-libp2p-module#6](https://github.com/logos-co/logos-libp2p-module/pull/6) chore(test): add nix check and ci tests
- [vacp2p/nim-libp2p#2065](https://github.com/vacp2p/nim-libp2p/pull/2065) chore(cbind): add private key
- [logos-co/logos-libp2p-module#3](https://github.com/logos-co/logos-libp2p-module/pull/3) feat: minimal module
- [vacp2p/nim-libp2p#2026](https://github.com/vacp2p/nim-libp2p/pull/2026) feat(nix): build cbindings
- [logos-co/logos-libp2p-module#2](https://github.com/logos-co/logos-libp2p-module/pull/2) feat(nix): build from libp2p's nix file
- [logos-co/logos-libp2p-module#1](https://github.com/logos-co/logos-libp2p-module/pull/1) chore: add initial libp2p lib and wrappers
- Logos core module 
- Created `logos-co/logos-libp2p-module` repo
