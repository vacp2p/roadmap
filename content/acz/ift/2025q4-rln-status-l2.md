---
title: RLN Status L2
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Deploying and testing the prover module in testnet and devnet,
releasing the prover module with shared DB support,
as well as maintaining the code quality and performance"

---

`vac:acz:ift:2025q4-rln-status-l2`

## Description
This commitment entails testing the deployed RLN prover module for
the gasless feature of Status L2 architecture in testnet and devnet.
Specificaly, testing that all RLN components such as prover,
verifier, deny list and RPC node in monorepo.

### Background
Status L2 is a rollup with Linea and builds a platform with the capacity to support
SocialFi and GameFi apps, governance experiments, the Status voting system,
and more, all while aiming to keep transaction costs low and throughput high.
Status L2 will incorporate a gasless feature, necessitating an effective anti-spam mechanism.
Rate-Limiting Nullifier (RLN) is a potential solution that could be deployed on Status L2
to prevent spam and support the gasless functionality. 

In 2025q3, we released the RLN prover module with tracking module, tests, optimizations and benchmarks.

## Task List

### Finalizing the RLN deployment spec

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:rln-spec-final`
* owner: Sylvain
* status: in progress (40%)
* start-date: 2025/10/22
* end-date: 2025/11/03

#### Description
This task encompasses finalizing the RLN deployment spec with all its edge cases
and ready to the final implementation.

#### Deliverables
* [A notion document](https://www.notion.so/RLN-Deployment-Specs-1f98f96fb65c806c8737d94851b4d14d)

### Prover Module maintaining

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:maintaining`
* owner: Sylvain
* status: in progress (10%)
* start-date: 2025/10/01
* end-date: 2025/02/30

#### Description
This task encompasses all maintenance updates for prover module, 
including CI updates and the creation of future issues.

#### Deliverables
* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Multi Tree Support

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:multi-tree`
* owner: Sylvain
* status: done
* start-date: 2025/10/01
* end-date: 2025/10/15

### Description

This task entails extending the Prover module to scale from supporting a single tree
with up to 1M users to a multi-tree architecture capable of handling
up to 32M users without compromising performance.
The current design, limited to a single tree, cannot efficiently manage larger user sets.
While an initial approach based on consistent hashing was considered,
it was ultimately discarded due to performance drawbacks.
The new approach introduces a dual-identifier database structure
using both tree_id and rln_identifier_id to efficiently
distribute and manage user commitments across multiple trees.
When one tree reaches its capacity, the system will automatically allocate
new users to the next available tree, ensuring seamless scalability and high performance.
This task is complete when the Prover module can reliably
handle up to 32M users across multiple trees with proper data management and performance validation.

### Deliverables

* A set of [PRs](https://github.com/vacp2p/status-rln-prover/pull/49) and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Gas checking support

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:gascheck`
* owner: Sylvain
* status: done 
* start-date: 2025/10/15
* end-date: 2025/10/20

### Description

This task entails updating the Prover module to handle cases where
a single transaction exceeds the maximum quota and therefore requires burning multiple message IDs.
Currently, the module generates one RLN proof per transaction,
without accounting for transactions that surpass the allowed quota.

The updated implementation must ensure that the gas information associated
with each incoming transaction is received alongside the transaction data.
Using both the max quota value and the transaction’s gas amount,
the module should calculate the exact number of message IDs to be burned
and deduct them from the user’s remaining tier limit accordingly.
This task is complete when the Prover module computes and applies 
the required number of message ID burns based on transaction gas
and quota values, ensuring accurate user limit tracking.

### Deliverables

* A set of [PRs](https://github.com/vacp2p/status-rln-prover/pull/51) and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Monorepo Review

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:monorepo-review`
* owner: Sylvain
* status: done
* start-date: 2025/10/01
* end-date: 2025/11/01

### Description

This task entails getting familiar with and testing the
[monorepo](https://github.com/status-im/status-network-monorepo)in preparation for the prover integration. 
In addition to basic exploration and setup, it includes a brief review of the implementation
of the sequencer, prover, and smart contracts, as well as a review of the deployment process
to identify and fix existing platform-specific bugs.
The task also involves testing newly added features to ensure
compatibility, stability, and readiness for prover integration. 
This task is complete when the monorepo environment is fully reviewed, 
deployment issues are resolved, and new features have been successfully tested and validated.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Decentralized slashing

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:monorepo-review`
* owner: Sylvain
* status: done
* start-date: 2025/10/01
* end-date: 2025/11/01

### Description

This task entails updating the Prover module to listen for slashing events emitted by the `karma.sol` smart contract
and to handle the corresponding user data accordingly.
When a slashing occurs, the Prover must identify the affected user through the event data and remove
that user’s commitment from the local database to maintain consistency between on-chain and off-chain states.
This task is complete when the Prover module successfully detects slashing events from `karma.sol`,
correctly identifies the corresponding user, and reliably removes their commitment from the local database.

### Deliverables

* A set of [PRs](https://github.com/vacp2p/status-rln-prover/pull/52) and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Multi-prover with shared Database

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:shared-db`
* owner: Sylvain
* status: in progress (10%) 
* start-date: 2025/11/03
* end-date: 2025/11/30

### Description

This task entails modifying the prover instance to release the multi-prover that each prover module
can write to the shared DB for having a prover cluster based on the pre-research in 2025q3.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Devnet testing 

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:devnet-testing`
* owner: Sylvain
* status: in progress (5%)
* start-date: 2025/10/15
* end-date: 2025/11/15

### Description

This task focuses on testing the internal devnet. 
The findings and feedback will be reflected in the RLN specification.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover)

### RLN public website

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:rln-public-website`
* owner: Ugur
* status: in progress (60%) 
* start-date: 2025/10/13
* end-date: 2025/11/03

### Description

This task entails preparing a comprehensive and publicly shareable Notion document
that consolidates the latest and most accurate notes on RLN (Rate Limiting Nullifier).
The document should explain in technical detail how RLN enables the gasless feature in the Gasless L2, 
including the underlying cryptographic mechanisms that make gasless operations possible.
This task is complete when the Notion document accurately compiles the most recent RLN insights,
clearly articulates the technical reasoning behind the Gasless L2’s gasless functionality,
and is structured in a manner suitable for public presentation.

### Deliverables

* A doc on [Status Notion](https://www.notion.so/Status-Program-f6eef7b91ad94539babf66c26ea1cf02).


### SN RLN whitepaper

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:whitepaper`
* owner: Ugur
* status: not started 
* start-date: 2025/11/03
* end-date: 2025/12/03

### Description

This task entails writing the Prover module section of the IEEE-format whitepaper,
providing a detailed and technically rigorous explanation of RLN as implemented in the system.
The section should build upon the existing RLN specification,
expanding it with clear descriptions of the Prover’s responsibilities,
data flow, and interactions with other components.
It should also illustrate the key mechanisms and cryptographic processes that enable
the Prover to function correctly within the RLN framework.
This task is complete when the whitepaper section presents a comprehensive,
technically accurate, and publication-ready explanation of the Prover module and its integration with RLN.

### Deliverables

* A doc on [Status Notion](https://www.notion.so/Status-Program-f6eef7b91ad94539babf66c26ea1cf02).
