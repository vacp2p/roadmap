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
* status: done
* start-date: 2025/04/1
* end-date: 2025/04/14

#### Description

Dockerize the mixified gossipsub poc to be tested.  

#### Deliverables

* [A branch](https://github.com/vacp2p/dst-gossipsub-test-node/tree/dockerized-mix-gossipsub-dockerfile-1) to [vacp2p/dst-gossipsub-test-node](https://github.com/vacp2p/dst-gossipsub-test-node/) repo.

### Delivering PoC 

* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:delivering-poc`
* owner: Akshaya
* status: done 
* start-date: 2025/04/01
* end-date: 2025/04/28

#### Description

Delivering the implementation a simple gossipsub PoC over Waku the mixnet. 

#### Deliverables

* [A branch for mixified gossipsub](https://github.com/vacp2p/dst-gossipsub-test-node/tree/dockerized-mix-gossipsub)

### Updating RFC
* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:update-rfc`
* owner: Akshaya
* status: done
* start-date: 2025/04/1
* end-date: 2025/04/21

#### Description

Updating the [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) with latest findings such as
- clarifications on the pluggable components,
- introducing  the entry and exit layers,
- libp2p integrations .

#### Deliverables

* A [PR](https://github.com/vacp2p/rfc-index/pull/158) to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)

### Nomos Comparison
* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:nomos-comparison`
* owner: Akshaya
* status: done
* start-date: 2025/05/19
* end-date: 2025/06/02

#### Description

A technical comparison between Nomos Blend Network and libp2p-mix, 
aimed at identifying trade-offs in scalability, privacy, and protocol adaptability.

#### Deliverables

* A Notion page to [ACZ Notion page](https://www.notion.so/Applied-Cryptography-ZK-870520f131954b90b1837ec4749f890f?pvs=4#a9a753fd85614cca8f1ac6b7be033032)


### Implementing SURB
* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:surb-implementation`
* owner: Ben
* status: on-hold(40%)
* start-date: 2025/05/19
* end-date: 2025/06/10

#### Description

This task is currently on hold as it has been taken over by the P2P team.

Implement and integrate the single-use replay block encoding to 
[mixnet](https://github.com/vacp2p/mix) as in [Sphinx: A Compact and Provably Secure Mix Format](https://cypherpunks.ca/~iang/pubs/Sphinx_Oakland09.pdf) 
section 3.4 and 3.5. 

#### Deliverables

* A PR to [vacp2p/mix](https://github.com/vacp2p/mix)

### Solving discrepancies
* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:solve-discrepancy`
* owner: Akshaya
* status: started (85%)
* start-date: 2025/05/28
* end-date: 2025/06/10

#### Description

This task entails solving the discrepancy in mix implementation based on [issue#24](https://github.com/vacp2p/mix/issues/24). 

#### Deliverables

* A PR to [vacp2p/mix](https://github.com/vacp2p/mix)

### Consulting Waku-mix 

* fully qualified name: `vac:acz:ift:2025q2-libp2p-mix-testnet:consulting-waku-mix`
* owner: Akshaya
* status: done
* start-date: 2025/05/1
* end-date: 2025/06/30

#### Description

Consulting about mixnet to Mixnet integration to the Waku.  

#### Deliverables

* PR to [vacp2p/mix](https://github.com/vacp2p/mix) or [waku-org/nwaku](https://github.com/waku-org/nwaku/) repo.

