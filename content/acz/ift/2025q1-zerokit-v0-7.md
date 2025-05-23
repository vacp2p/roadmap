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

### RLN wasm

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:rln-wasm`
* owner: Ekaterina
* status: on-hold
* start-date: 2025/01/27
* end-date: 2025/02/03

#### Description

This task was initially scheduled to be on hold for 2025q1. 
However, due to evolving requirements, 
we proceeded with and completed the Zerokit Wasm Research task. 

Regarding the [issue 271](https://github.com/vacp2p/zerokit/issues/271), 
rln wasm is revisited for performance analysis and updated by dependencies and gatherin new benchmarks.

#### Deliverables

* PR to vacp2p/zerokit repo with related update for v0.7

### Bump dependencies

* fully qualified name:  `vac:acz:ift:2025q1-zerokit-v0-7:bump_dependencies`
* owner: Ekaterina
* status: done
* start-date: 2025/01/27
* end-date: 2025/02/07

 #### Description

zerokit fixes many dependencies and some versions are too old 
and new libraries don't support them and a conflict happened. 
One of this dependency is  `num_traits` cannot be fixed yet 
because this strict dependency came from `ark-zkey`, 
and there it in turn came from a fork on an old version of `arc-circom` where version 2.15 is fixed.

#### Deliverables 

A [PR](https://github.com/vacp2p/zerokit/pull/276) to the zerokit repository. 

### RLN-cli

* fully qualified name:  `vac:acz:ift:2025q1-zerokit-v0-7:rln-cli`
* owner: Vinh
* status: done
* start-date: 2025/02/11
* end-date: 2025/02/24

 #### Description

The [rln-cli](https://github.com/vacp2p/zerokit/tree/master/rln-cli) is a command-line utility 
designed to help developers integrate Rate-Limiting Nullifier (RLN) into their applications. 
However, it is currently unusable due to a missing configuration file. 
To enable its functionality, the codebase needs to be improved to properly handle the required configuration.

Additionally, the RLN-cli task contains implementing an example demonstrating RLN’s stateless mode. 
This involves creating the Merkle tree outside of RLN, 
similar to the approach used [here](https://github.com/vacp2p/zerokit/blob/8a3e33be418ca6f66fa041c3fda475e24bb82268/rln/src/public_api_tests.rs#L993). 
The example should then provide the necessary roots from tree to RLN functions. 
This will help developers better understand RLN’s functionality and how to integrate it in a stateless manner.

#### Deliverables 

A [PR](https://github.com/vacp2p/zerokit/pull/280) to the [Zerokit]((https://github.com/vacp2p/zerokit)) repository that contains as follows:
- **Fix Configuration Handling:**  
  - Document the expected format of the configuration file.  
  - **Provide an example configuration file** in `rln-cli` to guide users.  
  - Ensure that the CLI provides useful error messages if the configuration is missing or incorrect.  

- **Implement Stateless RLN Example:**  
  - Create an example where the Merkle tree is constructed **outside** of RLN (similar to [this test](https://github.com/vacp2p/zerokit/blob/8a3e33be418ca6f66fa041c3fda475e24bb82268/rln/src/public_api_tests.rs#L993)).  
  - Use this external tree to generate **path and roots**, then pass them into RLN functions.  

- **Testing & Documentation:**  
  - Add tests to verify the CLI works correctly with the new configuration handling.  
  - Ensure the new stateless example is well-documented so that developers can easily follow it

### Zerokit maintaining

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:zerokit-maintaining`
* owner: Ekaterina
* status: done
* start-date: 2025/02/17
* end-date: 2025/03/31

#### Description

This task encompasses all maintenance updates for Zerokit, including CI updates and the creation of future issues.

#### Deliverables
A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/). 
- [Resolve circuit parameter mismatch PR](https://github.com/vacp2p/zerokit/pull/288)
- [Add custom iden3 graph PR](https://github.com/vacp2p/zerokit/pull/286)
- [pin ark-circom version and solve local building PR](https://github.com/vacp2p/zerokit/pull/285)
- [prepare Readme PR ](https://github.com/vacp2p/zerokit/pull/284)

### Reviewing utility functions

* fully qualified name:  `vac:acz:ift:2025q1-zerokit-v0-7:review-util-func`
* owner: Vinh
* status: done
* start-date: 2025/02/26
* end-date: 2025/03/07

 #### Description

Reviewing the utility functions in rln/src/utils.rs based on the [issue #279](https://github.com/vacp2p/zerokit/issues/279), 
which are used across various serialization functions and tested in rln/tests/protocol.rs. 
Assess whether all of these functions are necessary and identify any that may be redundant or obsolete.

#### Deliverables 

A [PR](https://github.com/vacp2p/zerokit/pull/287) to the [Zerokit]((https://github.com/vacp2p/zerokit)) repository that contains as follows:

- Analyze the usage of each function in `utils.rs` to determine if they are all needed.  
- Check if any functionality is redundant or can be optimized.  
- Consider simplifying or removing unused functions if possible.  


### Zerokit Wasm Research
* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:zerokit-wasm-research`
* owner: Vinh
* status: done
* start-date: 2025/03/12
* end-date: 2025/03/21

#### Description
In zerokit rln-wasm module was built with wasmer, 
but the big problem with it is that it is difficult to support, 
very slow and problems with running calculations in parallel. 
The bottom line is to investigate other existing web support solutions 
and understand what can be used to deliver high performance on the web 

#### Deliverables
As a result, a comparative characterization of the possible solutions and a final selection is made. 
Comment in zerokit issue related to release v0.8.0
- [Research report](https://github.com/vacp2p/zerokit/issues/289#issuecomment-2755917797)
- [Benchmark comparison report](https://github.com/vacp2p/zerokit/issues/289#issuecomment-2763285858) 

### Release v0.7

* fully qualified name: `vac:acz:ift:2025q1-zerokit-v0-7:release`
* owner: Ekaterina
* status: done
* start-date: 2025/03/24
* end-date: 2025/03/31

#### Description

The new version of the Zerokit v0.7 based on the issue [#271](https://github.com/vacp2p/zerokit/issues/271)
that covers faster witness generation, posidon hash integration and update the RLN wasmer dependencies. 

#### Deliverables
A set of PRs to vacp2p/zerokit repository with [tag v0.7.0](https://github.com/vacp2p/zerokit/releases/tag/v0.7.0)


