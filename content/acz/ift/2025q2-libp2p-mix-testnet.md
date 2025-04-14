---
title: LibP2P mix testnet
tags:
  - "2025q2"
  - "acz"
  - "ift"
draft: false
description: "Publishing the findings with a blog post and a paper, maintaining the Waku PoC over mixnet, 
and also maintaining EF grant application with a privacy project that introduces sender anonymity 
to Ethereum nodes for censorship resistanceness"

---

`vac:acz:ift:2025q2-libp2p-mix-testnet`

Publishing the findings with a blog post and a paper, maintaining the Waku PoC over mixnet, 
and also maintaining EF grant application with a privacy project that introduces sender anonymity 
to Ethereum nodes for censorship resistanceness
## Description
This commitment entails publishing the findings with a blogpost and a paper with extensive benchmark and
privacy analysis, also maintaining the Waku PoC over the mixnet and finally maintaining the EF grant application. 
 
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

In 2025q1, we developed the extended functionality of mixnet and its integration with libp2p such as transport protocol. 
Also, we released a simple gossipsub poc over the mixnet. 

### Narratives
By utilizing this commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Implement a poc over Waku PoC shows the base functionality on Waku network. 

We will also strengthen the Premier Research Destination narrative by:
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the mixnet PoC and 
gain support from the Ethereum ecosystem.
* Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance(product-market fit), 
offering improvements over Tor push. 
* Publish a blogpost on [vac.dev/rlog](https://vac.dev/rlog) that includes update on transport layer of mixnet and 
Waku integration. 

## Task List

### Dockerize GossipSub 

* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:dockerize`
* owner: Akshaya
* status: started (40%)
* start-date: 2025/04/1
* end-date: 2025/04/14

#### Description

Dockerize the mixified gossipsub poc to be tested.  

#### Deliverables

* PR to [vacp2p/mix](https://github.com/vacp2p/mix) repo.

### Delivering PoC 

* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:delivering-poc`
* owner: Akshaya
* status: started (50%)
* start-date: 2025/04/01
* end-date: 2025/04/28

#### Description

Delivering the implementation a simple gossipsub PoC over Waku the mixnet. 

#### Deliverables

* [A branch for mixified gossipsub](https://github.com/vacp2p/dst-gossipsub-test-node/tree/dockerized-mix-gossipsub)

### Updating RFC
* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:update-rfc`
* owner: Akshaya
* status: started (0%)
* start-date: 2025/04/1
* end-date: 2025/04/21

#### Description

Updating the [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) with latest findings such as
- clarifications on the pluggable components,
- introducing  the entry and exit layers,
- libp2p integrations .

#### Deliverables

* A PR to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)

