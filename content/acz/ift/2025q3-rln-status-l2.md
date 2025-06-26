---

title: RLN Status L2
tags:

- "2025q3"
- "acz"
- "ift"
draft: false
description: "Testing deployed RLN for the Status L2 architecture, including prover, verifier, deny list and RPC node"

---

`vac:acz:ift:2025q3-rln-status-l2`

## Description

This commitment entails testing and fine-tuning deployed RLN components 
for the gasless feature of the Status L2 architecture. 
Specifically, testing that all RLN components, such as prover, verifier, deny list, 
and RPC node, work fine with the Linea codebase securely and efficiently.

### Background

Status L2 is a rollup with Linea and builds a platform with the capacity 
to support SocialFi and GameFi apps, governance experiments, the Status voting system, 
and more, all while aiming to keep transaction costs low and throughput high. 
Status L2 will incorporate a gasless feature, necessitating an effective anti-spam mechanism. 
Rate-Limiting Nullifier (RLN) is a potential solution that could be deployed on 
Status L2 to prevent spam and support the gasless functionality.

In 2025q2, we released the RLN components such as prover, verifier, deny list, and RPC node.

### Narratives

By utilizing this commitment, we will reinforce the Conduit of Expertise narrative by:

- Continue sharing the RLN knowledge with the Status L2 team.
- Testing modified RLN design to make sure all components work seaminglessly.

We will also strengthen the Premier Research Destination narrative by:

- Offering a RLN use-case to the ecosystem that can be used for other gasless roll-up projects.

## Task List

### Maintain RLN Specification

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:rln-spec-maintain`
* owner: Ugur
* status: not started
* start-date: 
* end-date: 

### Description

This task focuses on maintainin a specification of RLN deployment to the Status L2 network, 
based in the feedbacks and changes during testnet.

### Deliverables

* A Notion doc document that has implementation details. 

### Researching decentralized architecture

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:research-decentralized`
* owner: Ugur
* status: not started
* start-date: 
* end-date: 

### Description

This task focuses on researching more decentralized and applicable solutions to the Status L2 network, 
by minimize the prover and RLN centralization. 

### Deliverables

* A Notion doc document that has implementation details.

### E2E Prover module testing 

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:e2e-prover-testing`
* owner: Sylvain
* status: not started
* start-date: 2025/07/01
* end-date: 2025/07/15

### Description

This task focuses on testing prover module with its edge cases before the testnet. 
The findings and feedbacks will be reflected to the RLN specification.

### Deliverables

* A Notion doc document that has implementation details.

### Devnet testing 

* fully qualified name: `vac:acz:ift:2025q3-rln-status-l2:devnet-testing`
* owner: Sylvain
* status: not started
* start-date: 2025/07/15
* end-date: 2025/09/15

### Description

This task focuses on testing internal devnet. 
The findings and feedbacks will be reflected to the RLN specification.

### Deliverables

* A Notion doc document that has implementation details.