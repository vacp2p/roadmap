---
title: Nescience Consulting
tags:
  - "2025q2"
  - "acz"
  - "nes"
draft: false
description: "Creating research documents and specifications 
for Nescience architecture"

---

`vac:acz:nes:2025q2-nescience-consulting`

Creating research documents and specifications 
for Nescience architecture
## Description

ACZ offers review consulting services to Nescience, 
acting as a bridge between Nescience researchers and engineers, 
facilitating faster and more efficient communication between the two groups.

By utilizing the Nescience Consulting commitment, 

we will reinforce the Conduit of Expertise narrative by:
* The Nescience specifications will be reviewed and refined from an engineering perspective.
* Addressing any potential gaps in the architecture, whether theoretical or practical, 
if any are identified
* Improve communication between Nescience researchers and developers.

We will also strengthen the Premier Research Destination narrative by: 
* This will enable the Nescience project to be more effectively integrated 
and introduced into the ecosystem.

## Task List

### Unifying 2025q1 Documents
* fully qualified name: `vac:acz:nes:2025q2-nescience-consulting:unifying-q1-docs`
* owner: Marvin
* status: done
* start-date: 2024/05/05
* end-date: 2025/05/20

### Description
Nescience has many unstructured documents from 2025q1, this task entails creating a single document 
that covers all these new ideas by removing recurring topics. Also, it includes creating a table for each document
which topics we include or exclude. 


### Deliverables
* A [notion page](https://www.notion.so/1-Single-Unified-Doc-of-2025Q1-Research-1eb8f96fb65c808aa51bd4a9f5e11cc3) that consists of a single unified doc 
* A [table](https://www.notion.so/2-Table-that-what-we-include-or-exclude-1ec8f96fb65c805a8ba6d0221926efff) that shows which topics we include or exclude
* A [notion](https://www.notion.so/3-Recommended-research-directions-1f88f96fb65c800c80e9e4ec5f0e3cae) page that shows decisions need to be made

### SE/DE improvements
* fully qualified name: `vac:acz:nes:2025q2-nescience-consulting:SE-DE-improvements`
* owner: Marvin
* status: done
* start-date: 2024/05/21
* end-date: 2025/06/04

### Description
In Q1, shielded executions were a primary focus. In this task, we focus on improvements to deshieldedd executions. Specifically,
- Examine deshielded execution kernel circuit for optimisations.
- Design and prototype a mechanism that applies deshielded execution's results to the public state in a consistent and verifiable manner.
- For both DE and SE, design sample transactions to example edge cases (concurrent updates to same public account, ordering issues).

This directly corresponds to Nescience's [Q2-R2](https://www.notion.so/R2-Updating-public-state-with-private-execution-SE-DE-improvements-1bf8f96fb65c81a98548fff27c4d1dcc) task.

### Deliverables
* RFC style documents for SE/DE

### Light user support in NSSA
* fully qualified name: `vac:acz:nes:2025q2-nescience-consulting:light-users`
* owner: Marvin
* status: done
* start-date: 2024/06/03
* end-date: 2025/06/11

### Description
Light user support is essential for NSSA adoption. 
This ensures a wide range of users can participate within NSSA. 
It is necessary to ensure that light users can enjoy the same level of NSSA privacy guarantees as any other users. 
To this end, we will examine privacy transactions (private, SE, DE) for light users. Specific analysis should include:

- Investigate how other projects handle light user proof generation.
- Potential privacy risks relying on a third party to run zkVM.
- Investigate whether light users can practically compute portions of the proof locally to strengthen privacy.
- Design protocol or mitigations (of current circuits) for outsourcing zkVM execution.

Ties directly with NSSA’s task [Q2/R4](https://www.notion.so/R4-Lightweight-user-execution-model-1bf8f96fb65c81dc9471c6a03d2c8513?pvs=21).

### Deliverables
* [A notion Doc](https://www.notion.so/Light-user-support-in-NSSA-2108f96fb65c8031b2f8d651721f7c84) covering private, 
SE, DE transactions performed by light users with analysis on any privacy or security compromises.

### Viewing keys and elliptic curve
* fully qualified name: `nes:2025q2-nescience-consulting:view-keys`
* owner: Marvin
* status: started (0%)
* start-date: 2024/06/13
* end-date: 2025/06/19

### Description:

1. The current design of NSSA’s viewing keys is restricted to 
only permit decryption of incoming transactions. 
However, it is desirable to for regulatory entities to have the ability to 
decrypt outgoing transactions as well. 
In this task, we work on redesigning the viewing key construction to incorporate:
- incoming viewing key; decrypt transactions in which the user is the recipient.
- outgoing viewing key; decrypt transactions in which the user is the sender.
- full viewing key; used to decrypt both outgoing and incoming transactions.
    
Additionally, to increase a user’s control over their data, we will investigate mechanisms 
that can be used generate viewing keys that are only decrypt transactions 
with in a specified set of sequential blocks.
    
2. Tangentially but related subtask. Investigate alternate elliptic curves to `secp256k1`. 
NSSA uses points on `secp256k1` for public keys and Pedersen commitments in transactions. 
This curve does not support fast addition. 
Computational overhead can be reduced by selecting an elliptic curve that supports fast addition. 
Additionally, light users need to generate zk-SNARK proofs which may require pairing-friendly curve.

### Deliverables:

- Document that concisely explains:
    - Mathematical construction of viewing keys
    - Usage in NSSA
    - Feasibility of ‘period specific’ viewing keys.
- Document with elliptic curve recommendation and reason.