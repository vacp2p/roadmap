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
* status: in progress (90%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Using the c-bindings module from nim-libp2p, develop a logos module that would allow nim-libp2p
to be used in logos.

#### Deliverables
- [vacp2p/nim-libp2p#2123](https://github.com/vacp2p/nim-libp2p/pull/2123) fix(cbind): various
- [logos-co/logos-libp2p-module#19](https://github.com/logos-co/logos-libp2p-module/pull/19) fix: macos CI
- [logos-co/logos-libp2p-module#20](https://github.com/logos-co/logos-libp2p-module/pull/20) fix: increase timeout for failing sync op in linux aarch64
- [logos-co/logos-libp2p-module#21](https://github.com/logos-co/logos-libp2p-module/pull/21) fix: ci.yml
- [logos-co/logos-libp2p-module#17](https://github.com/logos-co/logos-libp2p-module/pull/17) docs: README and kad example
- [logos-co/logos-libp2p-module#16](https://github.com/logos-co/logos-libp2p-module/pull/16) feat(sync): result-like return types
- [logos-co/logos-libp2p-module#15](https://github.com/logos-co/logos-libp2p-module/pull/15) feat: stream functions
- [logos-co/logos-libp2p-module#13](https://github.com/logos-co/logos-libp2p-module/pull/13) feat(kad): add integration tests
- [logos-co/logos-libp2p-module#12](https://github.com/logos-co/logos-libp2p-module/pull/12) chore(kad): sync functions
- Fixed diff bugs that could cause mem corruption, leaks, and usage after free
- Fixed CI to get macos and linux arm64 builds to complete, as well as making sure the latter does not take too much time to complete
- [logos-co/logos-libp2p-module#9](https://github.com/logos-co/logos-libp2p-module/pull/9) feat(kad): add kademlia functions
- [logos-co/logos-libp2p-module#8](https://github.com/logos-co/logos-libp2p-module/pull/8) feat(kad): add provider tests
- [logos-co/logos-libp2p-module#6](https://github.com/logos-co/logos-libp2p-module/pull/6) chore(test): add nix check and ci tests
- [vacp2p/nim-libp2p#2065](https://github.com/vacp2p/nim-libp2p/pull/2065) chore(cbind): add private key
- [logos-co/logos-libp2p-module#3](https://github.com/logos-co/logos-libp2p-module/pull/3) feat: minimal module
- [vacp2p/nim-libp2p#2026](https://github.com/vacp2p/nim-libp2p/pull/2026) feat(nix): build cbindings
- [logos-co/logos-libp2p-module#2](https://github.com/logos-co/logos-libp2p-module/pull/2) feat(nix): build from libp2p's nix file
- [logos-co/logos-libp2p-module#1](https://github.com/logos-co/logos-libp2p-module/pull/1) chore: add initial libp2p lib and wrappers
- Logos core module 
- Created `logos-co/logos-libp2p-module` repo
