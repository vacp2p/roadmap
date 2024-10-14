---
title: LibP2P mix protocol
tags:
  - "2024q4"
  - "acz"
  - "ift"
draft: false
description: "Publishing a raw RFC specifying libp2p mixnet protocol and implementing a PoC"

---

`vac:acz:ift:libp2p-mix-poc`

Publishing a raw RFC specifying libp2p mixnet protocol and implementing a PoC
## Description

This commitment entails designing an anonymization layer for gossipsub, and by extension, IFT projects.
The primary objective of this anonymization layer is to serve as a cohesive anonymization solution for gossip-based projects,
with a specific focus on integrating it with the Logos projects Waku and Codex.


The Nomos team is crafting their own anonymization solution due to their unique requirements and their ability to leverage specific traffic patterns to enhance efficiency.
Nonetheless, the overarching objective for our anonymization network is to render our solution modular, enabling the inclusion of traffic pattern plugins that Nomos can define.

Our initial exploration will revolve around extending our [Tor push proposal](https://rfc.vac.dev/spec/46/).
In this approach, messages will traverse through an anonymization network before being disseminated via gossip protocols upon exiting the anonymization network.
Additionally, we aim to investigate the concept of embedding anonymization capabilities directly into gossipsub,
rather than routing messages through a separate anonymization network before entering a standard gossipsub network operation.

Currently we view this anonymization solution as a P2P base layer, which the Vac P2P team will offer as part of libp2p.
This effort could potentially spawn an incubation project.
This effort would act as a basis for the Validator Privacy Network incubation project.


By utilizing the de-mls-poc commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Create a document describing the benefits of mixnet protocol for each of Waku, Status, Codex, and Nimbus
* Implement a PoC shows the base functionality

We will also strengthen the Premier Research Destination narrative by:
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the mixnet PoC and 
gain support from the Ethereum ecosystem.
* Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance(product-market fit), 
offering improvements over Tor push. 

## Task List

### Libp2p Integration

* fully qualified name: `vac:acz:ift:libp2p-mix-poc:libp2p-integration`
* owner: Akshaya
* status: in progress (70%)
* start-date: 2024/10/07
* end-date: 2024/10/21

#### Description

Implement protocol handler logic for sender nodes including packet creation and wrapping. 

#### Deliverables

* PR to vacp2p/mix repos with related implementation

### Simulate Anonymized Ping

* fully qualified name: `vac:acz:ift:libp2p-mix-poc:sim-anon-ping`
* owner: Akshaya
* status: not started
* start-date: 2024/10/21
* end-date: 2024/11/04

#### Description

Develop a network simulation framework and simulate the anonymized ping protocol with
node configurations as the first PoC. 

#### Deliverables

* PR to vacp2p/mix repos with related implementation as follows
	* Procedures for node setup and teardown
	* Basic routing and message passing
	* Define node roles (mix, sender, receiver)
	* Integrate libp2p ping on designated nodes
	* Enable sender nodes to route Ping through local mix
	* Forward messages through the mix network
	* Final delivery at the exit node.

### Comparison and Benefits 

* fully qualified name: `vac:acz:ift:libp2p-mix-poc:comp-and-benefits`
* owner: Akshaya
* status: not started
* start-date: 2024/11/04
* end-date: 2024/11/18

#### Description

Comparison mixnets between Nomos and our mixnet. 

#### Deliverables

* Report the result of comparison similarities and differences in terms of 
privacy and effiency
* Report the possible benefits of the mixent for Waku and Codex 

### Gossibsub over Waku 

* fully qualified name: `vac:acz:ift:libp2p-mix-poc:gossipsub-over-waku`
* owner: Akshaya
* status: not started
* start-date: 2024/11/18
* end-date: 2024/12/2

#### Description

Implementation the second PoC which is a basic gossibsub protocol with our mixnet over Waku nodes. 

#### Deliverables

* PR to vacp2p/mix repos with related implementation as follows
	* TBD

### Testing and Documentation 

* fully qualified name: `vac:acz:ift:libp2p-mix-poc:test-and-doc`
* owner: Akshaya
* status: not started
* start-date: 2024/12/2
* end-date: 2024/12/9

#### Description

Implement logging for debugging and demonstration and test module including 
functional tests for mix handlers, integration tests for libp2p protocol adapter, and
End-to-end test of the mix network.

#### Deliverables

* PR to vacp2p/mix repos with test module
* PR to vacp2p/mix repos with documentation.md 

### Publishing a Paper 

* fully qualified name: `vac:acz:ift:libp2p-mix-poc:publish-a-paper`
* owner: Akshaya
* status: not started
* start-date: 2024/12/9
* end-date: 2024/12/16

#### Description

Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance(product-market fit), 
offering improvements over Tor push. 

#### Deliverables

* A paper on arxiv.com





