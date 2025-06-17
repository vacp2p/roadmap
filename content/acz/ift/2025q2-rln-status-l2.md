---
title: RLN Status L2
tags:
  - "2025q2"
  - "acz"
  - "ift"
draft: false
description: "Researching the implementation and deployment of RLN 
for the Status L2 architecture, including RLN proof provider and membership topics"

---

`vac:acz:ift:2025q2-rln-status-l2`

Researching the implementation and deployment of RLN 
for the Status L2 architecture, including RLN proof provider and membership topics
## Description
This commitment entails researching and implementing of deployment of RLN 
for the gasless feature of Status L2 architecture. 
Currently, we have only the RLN backend, but before proceeding, 
we need to explore how RLN can be deployed alongside auxiliary components 
to ensure integrity and scalability. 
This commitment will include considerations for integrating an RLN-proof provider, 
verifier, and membership topics while optimizing the overall architecture for efficiency and performance. 

### Background
Status L2 is a rollup with Linea and builds a platform with the capacity 
to support SocialFi and GameFi apps, governance experiments, the Status voting system, and more
 – all while aiming to keep transaction costs low and throughput high. 
Status L2 will incorporate a gasless feature, necessitating an effective anti-spam mechanism. 
Rate-Limiting Nullifier (RLN) is a potential solution that could be deployed on Status L2 
to prevent spam and support the gasless functionality. 

In 2025q1, we explore the Status L2 infrastructure to 
identify the best approach for deploying the RLN. 

### Narratives
 By utilizing this commitment, we will reinforce the Conduit of Expertise narrative by:
* Sharing the RLN knowledge with the Status L2 team.
* Delivering the modified RLN design to make Status L2 gasless. 

We will also strengthen the Premier Research Destination narrative by:
* Offering a use-case to the ecosystem that can be used for other gasless roll-up projects.  

## Task List

### Maintain RLN Deployment

* fully qualified name: `vac:acz:ift:2025q2-rln-status-l2:maintain`
* owner: Ugur
* status: started (85%)
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description 

This task entails the deployment of RLN (Rate-Limiting Nullifier) into the Status L2 architecture, 
actively participating in architectural discussions and integration meetings. 
Responsible for maintaining the deployment process, aligning RLN functionality 
with the target system's design requirements, and ensuring compatibility 
with the existing infrastructure. 

#### Deliverables 

* A document to ACZ notion page

### Prover Service Development

* fully qualified name: `vac:acz:ift:2025q2-rln-status-l2:prover-service`
* owner: Sylvain
* status: started (70%)
* start-date: 2025/04/16
* end-date: 2025/06/30

### Description

This task involves integrating RLN (Rate-Limiting Nullifier) into the Status L2 architecture, 
with a focus on the prover component within the Linea network. 
The goal is to ensure seamless deployment while aligning RLN functionality with the design requirements 
of the target system and maintaining compatibility with the existing infrastructure.

Key responsibilities include:
- Managing the RLN deployment process within the Linea-based prover stack.
- Implementing credential issuance and proof generation using the existing zerokit library.
- Handling secret values securely and ensuring proper interaction with the RLN Membership Contract.
- Provide information required to develop the Linea Sequencer plugin (performance & throughput).

* A PR to the appropriate repository, including the RLN integration and all related components.

### RPC Node Modification

* fully qualified name: `vac:acz:ift:2025q2-rln-status-l2:rpc-node-modification`

* owner: Vinh
* status: started (60%)
* start-date: 2025/04/16
* end-date: 2025/06/30

### Description

This task focuses on enhancing the interaction between RPC nodes and the Prover within the Linea network by:
- Developing plugins for RPC nodes to forward transaction data directly to the Prover, 
enabling more efficient proof generation.

### Deliverables

* A PR to the appropriate repository, implementing the RPC plugins and the modified `linea_estimateGas` logic.

### Gas estimation RPC Modification

* fully qualified name: `vac:acz:ift:2025q2-rln-status-l2:gas-estimate-rpc-modification`
* owner: Sylvain
* status: started (0%)
* start-date: 2025/04/16
* end-date: 2025/06/30

### Description

This task focuses on enhancing the interaction between RPC nodes and the Prover within the Linea network by:
- Modifying the `linea_estimateGas` method to dynamically adjust gas estimation based on Deny List queries,
  improving accuracy and system responsiveness.

### Deliverables

* A PR to the appropriate repository, implementing the modified `linea_estimateGas` logic.

### RLN Specification

* fully qualified name: `vac:acz:ift:2025q2-rln-status-l2:rln-spec`
* owner: Ugur
* status: started (50%)
* start-date: 2025/05/20
* end-date: 2025/06/10

### Description

This task focuses on creating a specification of RLN deployment to the Status L2 network, 
including prover, verifier, contracts, and deny list implementation specification.

### Deliverables

* A Notion doc document that has implementation details.   
