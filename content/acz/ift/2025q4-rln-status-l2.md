---
title: RLN Status L2
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Deploying and testing prover module in testnet and devnet,
as well as maintaining the code quality and performance"

---

`vac:acz:ift:2025q4-rln-status-l2`

## Description
This commitment entails testing deployed RLN prover module for
the gasless feature of Status L2 architecture in testnet and devnet.
Specificaly, testing that all RLN components such as prover,
verifier, deny list and RPC node in monorepo.

### Background
Status L2 is a rollup with Linea and builds a platform with the capacity to support
SocialFi and GameFi apps, governance experiments, the Status voting system,
and more all while aiming to keep transaction costs low and throughput high.
Status L2 will incorporate a gasless feature, necessitating an effective anti-spam mechanism.
Rate-Limiting Nullifier (RLN) is a potential solution that could be deployed on Status L2
to prevent spam and support the gasless functionality. 

In 2025q3, we released the RLN prover module with tracking module, tests, optimizations and benchmarks.

### Narratives
By utilizing this commitment, we will reinforce the Conduit of Expertise narrative by:
* Continue sharing the RLN knowledge with the Status L2 team.
* Testing modified RLN design to make sure all components work seaminglessly. 

We will also strengthen the Premier Research Destination narrative by:
* Offering a RLN use-case to the ecosystem that can be used for other gasless roll-up projects.  

## Task List

### Prover Module maintaining

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:maintaining`
* owner: Sylvain
* status: not started
* start-date: 2025/10/01
* end-date: 2025/02/30

#### Description
This task encompasses all maintenance updates for prover module, 
including CI updates and the creation of future issues.

#### Deliverables
* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover).

### Devnet testing 

* fully qualified name: `vac:acz:ift:2025q4-rln-status-l2:devnet-testing`
* owner: Sylvain
* status: not started (5%)
* start-date: 2025/10/15
* end-date: 2025/11/15

### Description

This task focuses on testing internal devnet. 
The findings and feedbacks will be reflected to the RLN specification.

### Deliverables

* A set of PRs and issues to [vacp2p/status-rln-prover](https://github.com/vacp2p/status-rln-prover)