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
* status: on-hold (70%)
* start-date: 2025/04/01
* end-date: 2025/04/07

#### Description

This task is on hold due to a blocker from Iden3. 
Although we can move forward, the effort required doesn't justify it, 
given the current low priority.

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
* status: done
* start-date: 2025/04/07
* end-date: 2025/05/16

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

A PR to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/pull/295) incorporating the improvements:

- Adding measurements to atomic operations in the existing benchmark
- Analysis of the tree operations in Zerokit to identify inefficiencies.
- If applicable, improvements to the tree structure in Zerokit to enhance performance.

### Zerokit Wasm Implementation  

* Fully qualified name: `vac:acz:ift:2025q2-zerokit:wasm-implementation`  
* Owner: Vinh  
* Status: done
* Start date: 2025/03/31  
* End date: 2025/05/16  

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

### Parallelization Feasibility Study For rln-wasm

* fully qualified name: `vac:acz:ift:2025q2-zerokit:parallel-computation-study`
* owner: Vinh
* status: done
* start-date: 2025/04/07
* end-date: 2025/04/21

#### Description

After returning the rln-wasm module, it is necessary to investigate 
the possibility and necessity to use parallel computation. 

#### Deliverables

* [A PR](https://github.com/vacp2p/zerokit/pull/296) to `zerokit` and linked to the issue related to release v0.8.0.

### Improve Computation In Merkle Tree  

* fully qualified name: `vac:acz:ift:2025q2-zerokit:merkle-tree-improvement`
* owner: Vinh
* status: done
* start-date: 2025/04/21
* end-date: 2025/05/09

#### Description

While working on `vac:acz:ift:2025q2-zerokit:rln-execution-bottleneck`, 
we identified an inefficient algorithm used for updating the tree structure. 
Although improvements were made, there's still potential for further optimization.

One promising approach is to update the hashes incrementally during tree updates, 
which could reduce redundant computations. 
Additionally, refactoring the current algorithm to leverage the rayon crate for parallelism 
may significantly boost performance—potentially by 20% or more. 
This task involves analyzing the current implementation, applying targeted refactors, 
and introducing parallel processing where appropriate.

#### Deliverables

* [A PR](https://github.com/vacp2p/zerokit/pull/306) to `zerokit` and linked to the issue related to release v0.8.0

### Investigate Semaphore

* fully qualified name: `vac:acz:ift:2025q2-zerokit:semaphore-parts-bench`
* owner: Ben
* status: done
* start-date: 2025/04/30
* end-date: 2025/05/16

### Description

[Semaphore](https://github.com/semaphore-protocol/semaphore-rs/tree/main) is a zero-knowledge protocol 
that allows users to prove membership in a group without revealing their identity. 
This enables anonymous messaging, voting, and other privacy-preserving applications.
In this task, we aim to evaluate whether replacing the current zero-knowledge proof system makes sense. 
To begin, we will focus on two areas of research:

1. Compare the [light-poseidon](https://crates.io/crates/light-poseidon) library 
with our current Poseidon hash implementation
   - Verify whether the parameters used are the same  
   - Prepare performance benchmarks

2. Evaluate the efficiency of the [lean-imt Merkle tree](https://github.com/brech1/zk-kit.rust/tree/main/crates/lean-imt) 
versus our current Merkle tree implementation
   - Focus on tree initialization, leaf insertion, proof generation, and proof verification

3. Compare the zero-knowledge proof systems themselves
- Once we understand the relative performance of Poseidon and Merkle tree implementations, 
evaluate the zk-proof construction step
- Assess the performance and complexity of generating and verifying proofs 
using the current system versus potential alternatives

For context, see our previous investigation into Semaphore usage in Zerokit:  
[Semaphore README in Zerokit branch](https://github.com/vacp2p/zerokit/blob/semaphore-update/semaphore/README.md)

### Deliverables

Submit either a pull request or a comment on [this issue](https://github.com/vacp2p/zerokit/issues/17) 
in the Zerokit repository that includes:

- [Benchmark results](https://github.com/vacp2p/zerokit/issues/17#issuecomment-2884697352) for both the Poseidon hash and the Merkle tree implementations
- A summary of findings, including whether it makes sense to proceed 
with evaluating alternative zk-proof systems based on the current efficiency data

### Abstract Error Handling in Zerokit

* fully qualified name: `vac:acz:ift:2025q2-zerokit:error-abstraction`
* owner: Sylvain
* status: done
* start-date: 2025/05/19
* end-date: 2025/06/06

#### Description

Evaluate and potentially refactor the error handling in Zerokit to improve composability with other crates.
The current use of `eyre` for error handling might not align with the preferences orinfrastructure of downstream users.
As `zerokit` is designed to be a reusable crate,
relying on a specific error type like `eyre::Report` may limit flexibility for consumers who prefer using `anyhow`,
custom error types, or other error frameworks.

#### Deliverables

A [PR](https://github.com/vacp2p/zerokit/pull/311) to `zerokit` and linked to the issue related to release v0.8.0.

### Blogpost about improvements in incoming release

* fully qualified name: `vac:acz:ift:2025q2-zerokit:perfomance-updates-blogpost`
* owner: Ben
* status: started (0%)
* start-date: 2025/05/26
* end-date: 2025/06/30

#### Description

Create a blog post comparing the tree implementation in zerokit v0.7.0 and the upcoming release.
The goal is to highlight and explain the motivation, architectural changes, performance impacts,
and developer-facing differences introduced during the refactor.
This post will help the community understand the rationale and value of the new approach.

The blog post should be informed by the discussion and comments from Vinh and Sylvain in zerokit issue [#289.](https://github.com/vacp2p/zerokit/issues/289)
It should make technical concepts accessible and provide examples or diagrams where appropriate to illustrate key points.

#### Deliverables

- Outline of blog post structure (sections, key topics).
- Analysis of changes between v0.7.0 and the upcoming version, focused on tree implementations.
- Integration of relevant insights and explanations from Vinh and Sylvain’s comments in issue [#289.](https://github.com/vacp2p/zerokit/issues/289)
- Complete draft of the blog post.
- Final review and publication on the VAC or Waku blog.

### Zerokit maintaining

* fully qualified name: `vac:acz:ift:2025q2-zerokit:zerokit-maintaining`
* owner: Ekaterina
* status: started (40%)
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
This task encompasses all maintenance updates for Zerokit, including CI updates and the creation of future issues.

#### Deliverables
A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/).

### Release v0.8.0

* fully qualified name: `vac:acz:ift:2025q2-zerokit:release`
* owner: Ekaterina
* status: done
* start-date: 2025/05/12
* end-date: 2025/06/26

#### Description
The new version of the Zerokit v0.8.0

#### Deliverables
A set of PRs to vacp2p/zerokit repository with [tag v0.8.0](https://github.com/vacp2p/zerokit/releases/tag/v0.8.0)
