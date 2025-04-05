---
title: Zerokit
tags:
  - "2025q2"
  - "acz"
  - "ift"
draft: false
description: "Maintaining and improving Zerokit, including the release of its next version"

---

`vac:acz:ift:2025q2-zerokit`

Maintaining and improving Zerokit, including the release of its next version 
## Description

This commitment entails developing and maintaining Zerokit including Zerokit v0.8.0 release 
by advancing the next version through the integration of new features such as updated WASM component 
based on the [issue #289](https://github.com/vacp2p/zerokit/issues/289). 

### Background

[Zerokit](https://github.com/vacp2p/zerokit) is a collection of Zero Knowledge modules that focus on RLN, 
developed in Rust, intended for integration with various system programming environments.


### Narratives

By utilizing the zerokit commitment, we will reinforce the Conduit of Expertise narrative by:
* Delivers an optimized version for IFT projects utilizing Zerokit, 
including [nwaku](https://github.com/waku-org/nwaku)and [js-rln](https://github.com/waku-org/js-rln).

We will also strengthen the Premier Research Destination narrative by:
* Offers a Rust crate that serves as a more efficient open-source development tool 
for users looking to integrate RLN into their projects. 

## Task List

### Iden3 Witness Calculator Integration Review
* fully qualified name: `vac:acz:ift:2025q2-zerokit:iden3-witness-review`
* owner: Sylvain
* status: not started
* start-date: 2025/04/01
* end-date: 2025/04/07

#### Description

The current implementation includes a modified version of the Iden3 witness calculator, 
with changes specifically related to data types. This task involves:
1. Verifying whether these modifications are truly necessary.
2. Exploring the feasibility of using the original Iden3 repository as a submodule 
instead of maintaining a separate modified version.
3. Benchmarking both solutions to compare their performance and potential impact.

#### Deliverables

A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) to cover as follows:

- Analysis of the differences between the current implementation and the original Iden3 witness calculator.
- Justification (or refutation) of the necessity of data type modifications.
- A benchmark comparing the performance of both implementations.
- Recommendation on whether to keep the modified version or use Iden3 as a submodule.

### RLN Execution Bottleneck Analysis
* fully qualified name: `vac:acz:ift:2025q2-zerokit:rln-execution-bottleneck`
* owner: Sylvain
* status: not started
* start-date: 2025/04/07
* end-date: 2025/04/14

#### Description 

There is an issue with the execution time of RLN operations. 
The problem may stem from two potential sources:

- Inefficient tree operations within Zerokit, particularly in the function located here. 
The method of reading and parsing input data might be suboptimal.
- Inefficiencies within the membership contract itself.

The issue became apparent when the membership contract reached `270,000` memberships, 
causing extreme slowdowns in processing. 
Specifically, the `atomic_write` function from `librln` is a major bottleneck, taking `11 to 30 seconds` per call. 
Since this function is called within a loop, processing large batches 
(e.g., 1752 events per RPC call) results in multi-hour delays. 
This makes syncing infeasible and exposes scalability issues with the current approach.

This task involves identifying the actual bottleneck and 
making at least initial improvements to Zerokit’s tree structure performance. 
We need to Investigate why `atomic_write` takes so long and whether it can be optimized.

#### Deliverables

A PR to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) incorporating the improvements:

- Adding measurements to atomic operations in the existing benchmark
- Analysis of the tree operations in Zerokit to identify inefficiencies.
- If applicable, improvements to the tree structure in Zerokit to enhance performance.

### Zerokit Wasm Implementation  
* Fully qualified name: `vac:acz:ift:2025q2-zerokit:wasm-implementation`  
* Owner: Vinh  
* Status: started (0%) 
* Start date: 2025/03/31  
* End date: 2025/04/14  

#### Description  
The zerokit RLN-Wasm module was originally built using Wasmer, 
but it has proven difficult to maintain, slow, and inefficient for parallel computations. 
This task focuses on comparing the existing Wasmer-based approach 
with an alternative implementation based on Iden3’s Wasm solution. 
The goal is to evaluate their performance, compatibility, and maintainability 
to determine the best approach for zerokit.

#### Deliverables  
A working implementation of the selected Wasm solution integrated into `zerokit`, 
ensuring improved performance and maintainability. 
The implementation should be submitted as a pull request to `zerokit` 
and linked to the issue related to release v0.8.0.

### Zerokit maintaining

* fully qualified name: `vac:acz:ift:2025q2-zerokit:zerokit-maintaining`
* owner: Ekaterina
* status: not started
* start-date: 2025/04/01
* end-date: 2025/05/30

#### Description
This task encompasses all maintenance updates for Zerokit, including CI updates and the creation of future issues.

#### Deliverables
A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/). 

### Release v0.8
* fully qualified name: `vac:acz:ift:2025q2-zerokit:release`
* owner: Ekaterina
* status: not started
* start-date: 2025/05/12
* end-date: 2025/05/26

#### Description
The new version of the Zerokit v0.8.  

#### Deliverables
A set of PRs to vacp2p/zerokit repository with [tag v0.8.0](https://github.com/vacp2p/zerokit/releases/tag/v0.8.0)
