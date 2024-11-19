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
version 0.6.0, which introduces several new features, including arkzkey, a stateless architecture, 
distinguishing it from the previous version.

By utilizing the zerokit-v0-6 commitment, we will reinforce the Conduit of Expertise narrative by:
* Delivers an optimized version for IFT projects utilizing Zerokit, 
including [nwaku](https://github.com/waku-org/nwaku)and [js-rln](https://github.com/waku-org/js-rln).

We will also strengthen the Premier Research Destination narrative by:
* Offers a Rust crate that serves as a more efficient open-source development tool 
for users looking to integrate RLN into their projects. 


## Task List

### Release v0.6

* fully qualified name: `vac:acz:ift:zerokit-v0-6:release`
* owner: Ekaterina
* status: done
* start-date: 2024/10/07
* end-date: 2024/11/18

#### Description

The new version of the Zerokit v0.6 based on the issue [#263](https://github.com/vacp2p/zerokit/issues/263)
that covers stateless feature and uncompressed key and its benchmarks. 

#### Deliverables
A set of PRs to vacp2p/zerokit repository with [tag v0.6.0](https://github.com/vacp2p/zerokit/releases/tag/v0.6.0) 

* chore(rln): add verifying key deser benchmark by @rymnc in https://github.com/vacp2p/zerokit/pull/258
* chore(rln): use ark serialized verification key for faster serde by @rymnc in https://github.com/vacp2p/zerokit/pull/259
* chore(rln): refactor resource initialization by @rymnc in https://github.com/vacp2p/zerokit/pull/260
* chore(rln): further refactoring of interface by @rymnc in https://github.com/vacp2p/zerokit/pull/261
* chore(release): v0.5.1 by @rymnc in https://github.com/vacp2p/zerokit/pull/262
* fix(rln-wasm): run tests again by @rymnc in https://github.com/vacp2p/zerokit/pull/264
* Stateless Feature by @seemenkina in https://github.com/vacp2p/zerokit/pull/265
* fix(CI): add condition for stateless feature by @seemenkina in https://github.com/vacp2p/zerokit/pull/267
* chore(rln-wasm): Make rln-wasm stateless by @seemenkina in https://github.com/vacp2p/zerokit/pull/266
* fix(CI): update actions version by @seemenkina in https://github.com/vacp2p/zerokit/pull/268
* fix(CI): add test for all features by @seemenkina in https://github.com/vacp2p/zerokit/pull/270
* chore(rln): add uncompressed key and benches by @seemenkina in https://github.com/vacp2p/zerokit/pull/269


**Full Changelog**: https://github.com/vacp2p/zerokit/compare/v0.5.1...v0.6.0


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


