---
title: Zerokit v.0.6
tags:
  - "2024q4"
  - "acz"
  - "ift"
draft: false
description: "Implementation of the next release of Zerokit"

---

`vac:acz:ift:zerokit-v0-6`

Implementation of the next release of Zerokit 
## Description

[Zerokit](https://github.com/vacp2p/zerokit) is a collection of Zero Knowledge modules that focus on RLN, 
developed in Rust, intended for integration with various system programming environments.

This commitment marks the next iteration of Zerokit addressed by the issue https://github.com/vacp2p/zerokit/issues/263, 
version 0.6.0, which introduces several new features, including arkzkey, a stateless architecture 
and Poseidon hash integration, distinguishing it from the previous version.

By utilizing the zerokit-v0-6 commitment, we will reinforce the Conduit of Expertise narrative by:
* Delivers an optimized version for IFT projects utilizing Zerokit, 
including [nwaku](https://github.com/waku-org/nwaku)and [js-rln](https://github.com/waku-org/js-rln).

We will also strengthen the Premier Research Destination narrative by:
* Offers a Rust crate that serves as a more efficient open-source development tool 
for users looking to integrate RLN into their projects. 


## Task List

### RLN Timestamp & wasm 

* fully qualified name: `vac:acz:ift:zerokit-v0-6:rln-timestamp-and-wasm`
* owner: Ekaterina
* status: not started 
* start-date: 2024/11/04
* end-date: 2024/11/18

#### Description

Including the timestamp in the RLN signal. 
Problem statement from Waku: [chore(rln): move from epoch based gap to timestamp based. waku-org/nwaku#2972](https://github.com/waku-org/nwaku/issues/2972) and 
audit the current implementation to find performance pitfalls. 
Bump dependencies of wasmer and benchmark against current implementation.
Results of the rln-wasm audit

#### Deliverables

PR to vacp2p/zerokit repo with related update for v0.6

### Poseidon Hash

* fully qualified name: `vac:acz:ift:zerokit-v0-6:poseidon-hash`
* owner: Ekaterina
* status: not started 
* start-date: 2024/11/18
* end-date: 2024/12/02

#### Description

[Generate Poseidon round parameters and constants #50](https://github.com/vacp2p/zerokit/issues/50)
Only round parameters (easy) and 
secure MDS matrices verification algorithms (hard) missing.
Ensure that known answer tests match with the result of another implementation.
Lastly solving the issue: [Docs fail to build on docs.rs](https://github.com/vacp2p/zerokit/issues/256) 

#### Deliverables

PR to vacp2p/zerokit repo with related update for v0.6

### Circom Witness rs

* fully qualified name: `vac:acz:ift:zerokit-v0-6:circom-witness-rs`
* owner: Ekaterina
* status: not started 
* start-date: 2024/12/02
* end-date: 2024/12/16

#### Description

Replace the zkey with https://github.com/philsippl/circom-witness-rs for faster witness generation. Benchmark and compare performance with the existing setup. 
Example: https://github.com/philsippl/semaphore-witness-example
rln-v2 circuits: https://github.com/Rate-Limiting-Nullifier/circom-rln

#### Deliverables

PR to vacp2p/zerokit repo with related update for v0.6


