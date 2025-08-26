---

title: Zerokit
tags:

- "2025q3"
- "acz"
- "ift"
draft: false
description: "Maintaining and improving Zerokit, including the release of its next version"

---

`vac:acz:ift:2025q3-zerokit`

Maintaining and improving Zerokit, including the release of its next version
## Description

This commitment entails developing and maintaining Zerokit, including Zerokit v0.9.0 release by advancing the next version.

### Background

[Zerokit](https://github.com/vacp2p/zerokit) is a collection of Zero Knowledge modules 
that focus on RLN, developed in Rust, intended for integration with various system programming environments.

During 2025q2, we release Zerokit v0.8.0 which is wasm integration and tree optimization with better performance. 

### Narratives

By utilizing the zerokit commitment, we will reinforce the Conduit of Expertise narrative by:

- Delivers an optimized version for IFT projects utilizing Zerokit, 
including [nwaku](https://github.com/waku-org/nwaku)and [js-rln](https://github.com/waku-org/js-rln) and [Status L2](https://docs.status.network/).

We will also strengthen the Premier Research Destination narrative by:

- Offers a Rust crate that serves as a more efficient open-source development tool for users 
looking to integrate RLN into their projects.

## Task List

### Big Endian Support

- fully qualified name: `vac:acz:ift:2025q3-zerokit:big-endian-support`
- owner: Sylvain
- status: started (65%)
- start-date: 2025/06/20
- end-date: 2025/09/20

#### Description

This task addresses a request from the nwaku team to add **Big Endian support**
for Zerokit's stateless feature.
This is critical because data on the smart contract side is processed in Big Endian format.
Specifically, we need to ensure all relevant key generation and
hash functions within Zerokit correctly handle Big Endian data.

#### Deliverables

- A Pull Request to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) that includes new functions
for working with Big Endian data and updates the public API to expose this functionality.

### CI and Feature Revising

- fully qualified name: `vac:acz:ift:2025q3-zerokit:ci-revising`
- owner: Vinh
- status: done
- start-date: 2025/07/07
- end-date: 2025/07/26

#### Description

This task focuses on improving Zerokit's Continuous Integration (CI) 
and build setup to enable more flexible and accurate binary generation. Key objectives include:

- **Integrating missing options for generating feature-specific binaries**,
and **making `arkzkey` the default feature** for improved consistency.
This will also require creating a script to convert `arkzkey` from `zkey`.
- **Addressing the current default enablement of the `parallel` feature** within the `rln` module.
This was a temporary workaround for a macro expansion issue in `graph.rs` affecting WASM multithreading.
The goal is to **refactor the feature flags** across Zerokit
and its internal dependencies to allow `parallel` to be optional.
This cleanup will require a thorough review of all dependent crates
that internally utilize the `parallel` flag.

#### Deliverables

* [A Pull Request](https://github.com/vacp2p/zerokit/pull/326) to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) with updated CI configurations.

### Consistent Naming and Docs for Merkle Trees

- fully qualified name: `vac:acz:ift:2025q3-zerokit:merkle-tree-revising`
- owner: 
- status: started (85%)
- start-date: 2025/07/14
- end-date: 2025/08/30

#### Description

Based on this [GitHub comment](https://github.com/vacp2p/zerokit/pull/306),
this task aims to improve consistency and clarity within Zerokit's Merkle tree implementation.
We'll **rename `TEST_TREE_HEIGHT` to `TEST_TREE_DEPTH`** for better conceptual alignment.
Additionally, we'll **enhance documentation and the `Cargo.toml` file**
to clearly explain which Merkle tree implementation to use and when.

#### Deliverables

A Pull Request to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) containing 
the renamed variables and updated, more detailed documentation.
    * [chore: consistent naming and update docs for merkle trees PR#333](https://github.com/vacp2p/zerokit/pull/333)

### Implement PmTreeConfig Builder

- fully qualified name: `vac:acz:ift:2025q3-zerokit:pmtree-config-builder`
- owner: Vinh
- status: started (85%)
- start-date: 2025/08/11
- end-date: 2025/09/08

#### Description

Currently, initializing a `PmTreeConfig` struct for `PmTree` in Rust requires either
providing a JSON-formatted string or using the default configuration.
This approach lacks type safety and compile-time validation,
making configuration less ergonomic and more prone to runtime errors.

This task aims to improve the `PmTreeConfig` initialization process by **implementing a builder pattern**.
This will allow developers to construct `PmTreeConfig` instances programmatically with clear,
chained method calls, enhancing readability, type safety, and ease of use,
rather than solely relying on string-based JSON parsing.

#### Deliverables

A Pull Request to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) containing:

- A new `PmTreeConfigBuilder` implementation.
- Updated documentation and examples demonstrating the new builder pattern usage.

    * [feat(rln): improve the PmTreeConfig initialization process with builder pattern PR#334](https://github.com/vacp2p/zerokit/pull/334)

### RLN-WASM Maintenance

- fully qualified name: `vac:acz:ift:2025q3-zerokit:rln-wasm-maintaining`
- owner: Vinh
- status: done
- start-date: 2025/07/01
- end-date: 2025/09/30

#### Description

This task consolidates several outstanding issues related to `rln-wasm` following the last release.
The key objectives are:

- **Standardize `stateless` feature enablement**: 
The current `rln-wasm` build always works with the `stateless` feature enabled.
We should make this the **default**, as `rln-wasm` does not support instances 
where the tree is part of the instance itself.
- **Add a local Node.js test**:
Implement a local Node.js test for the multithreaded `rln-wasm` feature to ensure its correct functionality.
- **Address `wasm-bindgen-rayon` issue**:
Follow up on the open issue [here](https://github.com/RReverser/wasm-bindgen-rayon/issues/26) and,
if necessary, update the `rln-wasm` module based on the resolution.

#### Deliverables

* A set of PRs to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/) addressing the outlined `rln-wasm` maintenance items.
    * [feat: add wasm parallel testcase and simplify the witness_calculator PR 328](https://github.com/vacp2p/zerokit/pull/328)

### Zerokit maintaining

- fully qualified name: `vac:acz:ift:2025q3-zerokit:zerokit-maintaining`
- owner: Ekaterina
- status: started (50%)
- start-date: 2025/07/01
- end-date: 2025/09/30

### Description

This task encompasses all maintenance updates for Zerokit, including CI updates and the creation of future issues.

### Deliverables

A set of PRs and issues to [vacp2p/zerokit](https://github.com/vacp2p/zerokit/).

### Release v0.9.0

- fully qualified name: `vac:acz:ift:2025q3-zerokit:release`
- owner: Ekaterina
- status: not started
- start-date: 2025/09/01
- end-date: 2025/09/30

### Description

The new version of the Zerokit v0.9.0

### Deliverables

A set of PRs to vacp2p/zerokit repository with [tag v0.9.0](https://github.com/vacp2p/zerokit/releases/tag/v0.9.0)