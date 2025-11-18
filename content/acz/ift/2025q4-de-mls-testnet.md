---
title: de-MLS testnet
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Releasing de-MLS with the multi-steward support and Ethereum authentication mechanism."

---

`vac:acz:ift:2025q4-de-mls-tesnet`

## Description
This commitment involves releasing the de-MLS poc with the multi-steward configurations.
The process includes presenting the findings, such as MLS over Waku and benchmarking,
and then achieving better iteration for the EF grant.

### Background
de-MLS is a decentralized, scalable, end-to-end encrypted (E2EE)
group messaging application with Ethereum-based authentication.
The primary goal of this project is to develop a comprehensive
and a mature RFC that outlines decentralized, secure, and scalable group key generation, 
designed to accommodate large numbers of users within a single group.
 
During 2025q3, we released the multi-steward de-MLS RFC, including consensus implementation.
The implementation plan for this quarter is to release multi-steward with a single consensus
version with Ethereum authentication factor by operating across the Waku network. 

## Task List

### Maintain de-MLS RFC with multi stewards 

* fully qualified name: `vac:acz:ift:2025q4-de-mls-tesnet:multi-steward-rfc`
* owner: Ugur
* status: in progress (70%)
* start-date: 2025/10/25
* end-date: 2025/11/25

#### Description

Maintain and develop the decentralized MLS RFC by addressing feedback.
The RFC needs to contain a concrete flow and explanation.   

#### Deliverables

* A [PR](https://github.com/vacp2p/rfc-index/pull/193) to vacp2p/rfc-index repo with related updates.


### Extract `hashgraph-like-consensus` into a standalone Rust library

* fully qualified name: `vac:acz:ift:2025q4-de-mls-testnet:extract-hashgraph-lib`
* owner: Ekaterina 
* status:  started (10%)
* start-date: 11/10/2025
* end-date: 12/10/2025

#### Description

The current hashgraph-like consensus implementation lives inside the `de-mls` codebase
and is tightly coupled to application-specific logic (Waku integration, MLS message handling, actor interfaces, UI-specific types).
This task aims to extract that logic into a clean, reusable Rust library (`hashgraph-like-consensus`),
exposing a well-defined public API and isolating the consensus engine from application concerns.

This enables:

* independent development, testing, and versioning of the consensus algorithm,
* support for reuse in other prototypes or benchmarking tools,
* cleaner integration in `de-mls`,
* better architectural separation between “consensus core” and “application layer.”

The new library should contain only the consensus logic and generic traits for persistence and callbacks,
with no dependency on Waku, Dioxus, or MLS-specific types.

#### Deliverables

* New Rust crate: https://github.com/vacp2p/hashgraph-like-consensus
* Migration of core logic from `de-mls` into the new crate:
* Public API definition & documentation:
  * rustdoc for all public types/traits,
  * `README.md` with architecture overview and simple usage example.
* Unit tests for core components,
* Integration in `de-mls`:
  * replace internal module usage with the new crate,
  * implement required traits (storage, observer) inside `de-mls`,
  * ensure the app compiles and existing tests pass.

### Multi-steward integration

* fully qualified name: `vac:acz:ift:2025q4-de-mls-tesnet:multi-steward-integration`
* owner: Ekaterina
* status: in progress (15%)
* start-date: 2025/10/01
* end-date: 2025/11/01

#### Description

The multi-steward settings allow de-MLS that multiple stewards to manage the group
changes to protect a single point of failure, better availability, and decentralization.

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
containing an update of message processing 

### de-mls maintenance

* fully qualified name: `vac:acz:ift:2025q4-de-mls-tesnet:de-mls-maintaining`
* owner: Ekaterina
* status: not started 
* start-date: 2025/06/30
* end-date: 2025/09/30

#### Description

This task encompasses all maintenance updates for de-mls, including CI updates,
testing, small issues, and the creation of future issues.

#### Deliverables

A set of PRs and issues to  [de-MLS repository](https://github.com/vacp2p/de-mls)