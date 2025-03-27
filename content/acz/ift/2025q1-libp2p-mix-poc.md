---
title: LibP2P mix protocol
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "Achieving mixnet's PoC on Waku network, updating the RFC for libp2p compatibility, 
sharing results, and also submitting to the EF grant program with a privacy project 
that introduces sender anonymity to Ethereum nodes for censorship resistanceness"

---

`vac:acz:ift:2025q1-libp2p-mix-poc`

Achieving mixnet's PoC on Waku network, updating the RFC for libp2p compatibility, 
sharing results, and also submitting to the EF grant program with a privacy project 
that introduces sender anonymity to Ethereum nodes for censorship resistanceness.
## Description

This commitment entails achieving proof of concept (PoC) 
for the base functionality of mixnet (Waku over mix). 
Additionally, it includes updating the RFC by replacing the custom transport protocol 
with a new TCP-based transport protocol, enhancing mixnet's compatibility with libp2p. 
The results will then be shared through a blogpost and a research paper, 
followed by researching the use case, features and further research topics to apply for EF grants. 

### Background

The primary objective of this anonymization layer is to serve as a cohesive anonymization solution 
for gossip-based projects, with a specific focus on integrating it with the IFT projects Waku and Codex.

Our initial exploration will revolve around extending our [Tor push proposal](https://rfc.vac.dev/spec/46/).
In this approach, messages will traverse through an anonymization network before being disseminated 
via gossip protocols upon exiting the anonymization network.
Additionally, we aim to investigate the concept of embedding anonymization capabilities 
directly into gossipsub, rather than routing messages through a separate anonymization network 
before entering a standard gossipsub network operation.

Currently we view this anonymization solution as a P2P base layer, 
which the Vac P2P team will offer as part of libp2p.
This effort could potentially spawn an incubation project.
This effort would act as a basis for the Validator Privacy Network incubation project.

In 2024q4, we developed the core functionality of mixnet and integrated it with libp2p. 
To enhance compatibility, we saw fit to replace the custom transport protocol with a TCP-based one. 
Additionally, we implemented two proofs of concept: 
anonymized ping and anonymized plain gossipsub with new transport protocol. 

### Narratives

By utilizing this commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Implement a poc over Waku PoC shows the base functionality on Waku network. 

We will also strengthen the Premier Research Destination narrative by:
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the mixnet PoC and 
gain support from the Ethereum ecosystem.
* Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance(product-market fit), 
offering improvements over Tor push. 
* Publish two blogpost on [vac.dev/rlog](https://vac.dev/rlog) that includes update on transport layer of mixnet and 
Waku integration. 

### Additional Info

This commitment has been rescheduled from 2024q4 to 2025q1
due to the lack of engineering resource. For this, budget is requested for 2025q1, 
hiring process started. 

## Task List

### Entry and Exit Abstraction

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:entry-exit-abstraction`
* owner: Akshaya
* status: done
* start-date: 2025/02/03
* end-date: 2025/02/10

#### Description

Implementation of the MixEntry and MixExit abstractions for the Mixnet. 

#### Deliverables

* [Mix-interface branch](https://github.com/vacp2p/mix/tree/feature/mix-interface) in [vacp2p/mix](https://github.com/vacp2p/mix/) repo 

### Simple GossipSub PoC 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:simple-gossipsub-poc`
* owner: Akshaya
* status: started (90%)
* start-date: 2025/02/10
* end-date: 2025/02/24

#### Description

Implementation a simple gossipsub PoC over Waku the mixnet.

#### Deliverables

* PR to vacp2p/mix repo 

### IFT Research Call Preparation

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:ift-research-call-prep`
* owner: Akshaya
* status: started (80%)
* start-date: 2025/02/17
* end-date: 2025/02/28

#### Description
Preparation for the IFT research call on 26th of February. 

#### Deliverables

* A presentation that describes the mixnet RFC and implementation point of view in 
[notion](https://www.notion.so/Applied-Cryptography-ZK-870520f131954b90b1837ec4749f890f?pvs=4#12d8f96fb65c80f49f11e8e6fe7fc974)


### Updating RFC
* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:update-rfc`
* owner: Akshaya
* status: started (0%)
* start-date: 2025/03/12
* end-date: 2025/03/24

#### Description
Updating the [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) with latest findings such as
- clarifications on the pluggable components,
- introducing  the entry and exit layers,
- libp2p integrations .

#### Deliverables

* A paper on arxiv.com

### Blogposts

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:blogposts`
* owner: Akshaya
* status: on-hold
* start-date: 2025/03/17
* end-date: 2025/03/28

#### Description

Writing a blogpost about the mixnet with PoC details. 

This task is postponed to the 2025q2 by replacing the updating RFC task since 
there were changes in [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) and the RFC must be updated first. 

#### Deliverables

* Two blogposts to [vac.dev/rlog](https://vac.dev/rlog)

### Publishing a Paper 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:publish-a-paper`
* owner: Akshaya
* status: on-hold
* start-date: 2025/03/03
* end-date: 2025/03/17

#### Description

Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance (product-market fit), 
offering improvements over Tor push. 

This task is postponed to the 2025q2 by replacing the updating RFC task since 
there were changes in [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) and the RFC must be updated first. 

#### Deliverables

* A paper on arxiv.com