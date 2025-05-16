---
title: de-MLS testnet
tags:
  - "2025q2"
  - "acz"
  - "ift"
draft: false
description: "Finalizing the de-MLS RFC with consensus integration 
with the multi-admin support and implementing the last version RFC"

---

`vac:acz:ift:2025q2-de-mls-tesnet`

finalizing the de-MLS RFC with consensus integration 
with the multi-admin support and implementing the last version RFC
## Description
This commitment involves completing the de-MLS RFC by incorporating 
multi-administrator configurations with decentralized consensus and implementing it 
with a multi-admin setup over the Waku network. 
The process includes presenting the findings such as MLS over Waku and benchmarking, 
then applying for the EF grant.

### Background
de-MLS is a decentralized, scalable, end-to-end encrypted (E2EE) group messaging application 
with Ethereum-based authentication. 
The primary goal of this project is to develop a comprehensive and mature RFC that outlines 
decentralized, secure, and scalable group key generation, 
designed to accommodate large numbers of users within a single group.

During 2025q1, we removed centralized aspects of the RFC by integrating the 
consensus mechanism among the users for achieving true decentralization. 
Also, we relese the extended implementation that multi-waku node can cooperate.
The implementation plan for this quarter is to extend the initial single admin approach 
to a multi-admin configuration with consensus operating across the Waku network. 

### Narratives
we will reinforce the Conduit of Expertise narrative by:
* Develop the foundational framework for a decentralized, scalable messaging application 
* Research and implement the scalable and decentralized consensus mechanism.

We will also strengthen the Premier Research Destination narrative by:
* Develop a standardized decentralized messaging application over the Waku network,
by providing a well-structured RFC and a proof of concept (PoC) that demonstrates 
its base functionality within the ecosystem. 
This will allow teams and organizations to build their own messaging applications while 
benefiting from these features.
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the project and 
gain support from the Ethereum ecosystem.

## Task List

### Test Deployment

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:test-deployment`
* owner: Ekaterina
* status: started (0%)
* start-date: 2025/05/01
* end-date: 2025/06/30

#### Description

Set up test deployment for the [de-MLS](https://github.com/vacp2p/de-mls) repository.

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository with 
* Docker configurations for deployment and testing.
* Documentation for test deployment setup.

### Blogpost de-mls over Waku

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:blogpost-de-mls-over-waku`
* owner: Ekaterina
* status: started (70%)
* start-date: 2025/04/01
* end-date: 2025/05/30

#### Description

Writing a blog post about implementation details of single admin de-MLS with Waku node 
as delivery service based on [this PR](https://github.com/vacp2p/de-mls/pull/29)     

#### Deliverables

A blogpost to [vac.dev/rlog/](https://vac.dev/rlog/)

### Consensus RFC

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:consensus-rfc`
* owner: Ugur
* status: started (50%)
* start-date: 2025/04/01
* end-date: 2025/04/14

#### Description

This task entails delivering the decentralized consensus 
RFC which is fast and efficient for p2p networks.  
   
#### Deliverables

- A PR to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index) repo. 

### Update de-MLS RFC with multi admins 

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:multi-admin-rfc`
* owner: Ugur
* status: not started
* start-date: 2025/05/04
* end-date: 2025/05/26

#### Description

Update and reorganize the decetnralized MLS RFC with the single and multi admin options. 
This task also contains the integrating the consensus RFC.   

#### Deliverables

* PR to vacp2p/rfc-index repo with related updates. 

### CI Setup

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:ci-setup`
* owner: Ekaterina
* status: not started
* start-date: 2025/06/01
* end-date: 2025/06/30

#### Description

Set up continuous integration for the [de-MLS](https://github.com/vacp2p/de-mls) repository, 
including automated testing and code validation. 

#### Deliverables
A PR to the [de-MLS](https://github.com/vacp2p/de-mls) repository 
with a new CI pipeline for the repository that includes the waku node.

### Implement consesus layer

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:consensus-layer`
* owner: Ekaterina
* status: not started 
* start-date: 
* end-date: 

#### Description

Implement a consensus mechanism for one admin based on RFC, i.e. 
in the end we want to see a separate module 
that will process all incoming proposals for group state changes 
and receive a commit message as an output.

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
containing new consensus layer as separate module with tests.

### Separate commit and proposal messages inside app

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:commit-and-proposal`
* owner: Ekaterina
* status: started (5%)
* start-date: 2025/05/05
* end-date: 2025/05/23

#### Description

Before integrating the consensus, it is necessary to split the process of applying new commits 
into the corresponding proposal and commits for applying the group state update.  

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
updating the API for separate commit and proposal messages.

### Put all proposall message in one queue

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:global-message-queue`
* owner: Ekaterina
* status: not started
* start-date: 2025/05/19
* end-date: 2025/05/30

#### Description

At the first stage of implementation we separated adding and messages
 to a group and deleting from a group into different threads, 
 we need one message queue to work with consensus.

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
containing update of message processing  


### Update frontend 

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:frontend-updating`
* owner: Ekaterina
* status: started (5%)
* start-date: 2025/05/01
* end-date: 2025/06/30

#### Description

The current frontend is difficult to maintain and besides adding new functionality 
for testing now requires a lot of effort.
In addition, communication via websockets needs to be reconsidered in terms of efficiency 

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
containing new frontend.

### Integrate wallet based registration 

* fully qualified name: `vac:acz:ift:2025q2-de-mls-tesnet:wallet-based-register`
* owner: Ekaterina
* status: not started
* start-date: 2025/06/01
* end-date: 2025/06/30

#### Description

For the first version de-mls used a mock version for online registration, 
now it makes sense to add wallet support for user authentication

#### Deliverables

* A PR to the [de-MLS repository](https://github.com/vacp2p/de-mls) 
containing support of wallet as authentication part.