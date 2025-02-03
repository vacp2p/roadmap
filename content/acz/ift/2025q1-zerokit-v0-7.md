---
title: Zerokit v.0.7
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "Implementation of the next release of Zerokit"

---

`vac:acz:ift:2025q1-zerokit-v0-7`

Implementation of the next release of Zerokit 
## Description

This commitment entails achieving Zerokit v0.7.0 by advancing the next version 
through the integration of new features aimed at improving its speed and robustness, 
such as Poseidon integration, accelerated witness generation, and updates to the WASM module.

### Background

[Zerokit](https://github.com/vacp2p/zerokit) is a collection of Zero Knowledge modules that focus on RLN, 
developed in Rust, intended for integration with various system programming environments.

This commitment marks the next iteration of Zerokit addressed by the issue https://github.com/vacp2p/zerokit/issues/263, 
version 0.7.0, which introduces several new features, including arkzkey, poseidon and updated wasm that is 
distinguishing it from the previous version.

### Narratives

By utilizing the zerokit-v0-7 commitment, we will reinforce the Conduit of Expertise narrative by:
* Delivers an optimized version for IFT projects utilizing Zerokit, 
including [nwaku](https://github.com/waku-org/nwaku)and [js-rln](https://github.com/waku-org/js-rln).

We will also strengthen the Premier Research Destination narrative by:
* Offers a Rust crate that serves as a more efficient open-source development tool 
for users looking to integrate RLN into their projects. 

## Task List
 
### Poseidon Hash

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:poseidon-hash`
* owner: Aleksei
* status: started (60%) 
* start-date: 2025/01/01
* end-date: 2025/01/27

#### Description

Releasing a Rust crate that checks the security of arbitrary MDS matrix with a new method 
based on the [report](https://notes.status.im/CVMoa6EcTmS2D4VPBCsH2w#). 
This crate will be open source and can be used by any project that requires generating in-code round parameters 
with an MDS matrix and checking the matrix security efficiently.

#### Deliverables

* PR to [rust-lang/crates.io](https://github.com/rust-lang/crates.io) repo with related crate 
* [A Report](https://notes.status.im/CVMoa6EcTmS2D4VPBCsH2w#) about the MDS security checker

### Blogpost MDS

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:blogpost-mds`
* owner: Aleksei
* status: not started
* start-date: 2025/01/27
* end-date: 2025/02/03

#### Description

Writing a blog post that explains the security of MDS matrices 
and reviews existing methods for assessing their security. 
The post also introduces a new, efficient method for evaluating MDS matrix security 
and provides details about a Rust crate that automates these security checks 
based on the findings presented in the article.

#### Deliverables

A blogpost to [vac.dev/rlog/](https://vac.dev/rlog/)

### RLN wasm

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:rln-wasm`
* owner: Ekaterina
* status: not started 
* start-date: 2025/01/27
* end-date: 2025/02/03

#### Description

Regarding the [issue 271](https://github.com/vacp2p/zerokit/issues/271), 
rln wasm is revisited for performance analysis and updated by dependencies and gatherin new benchmarks.

#### Deliverables

* PR to vacp2p/zerokit repo with related update for v0.7

### Bump dependencies

* fully qualified name:  `vac:acz:ift:2025q1-zerokit-v0-7:bump_dependencies`
* owner: Ekaterina
* status: started 
* start-date: 2025/01/27
* end-date: blocked

 #### Description

zerokit fixes many dependencies and some versions are too old 
and new libraries don't support them and a conflict happened. 
One of this dependency is  `num_traits` cannot be fixed yet 
because this strict dependency came from `ark-zkey`, 
and there it in turn came from a fork on an old version of `arc-circom` where version 2.15 is fixed.

#### Deliverables 

A [PR](https://github.com/vacp2p/zerokit/pull/276) to the zerokit repository. 

### Release v0.7

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:release`
* owner: Ekaterina
* status: not started
* start-date: 2025/03/24
* end-date: 2025/03/31

#### Description

The new version of the Zerokit v0.7 based on the issue [#271](https://github.com/vacp2p/zerokit/issues/271)
that covers faster witness generation, posidon hash integration and update the RLN wasmer dependencies. 

#### Deliverables
A set of PRs to vacp2p/zerokit repository with [tag v0.7.0](https://github.com/vacp2p/zerokit/releases/tag/v0.7.0)