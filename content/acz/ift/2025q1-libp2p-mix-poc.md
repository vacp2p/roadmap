---
title: LibP2P mix protocol
tags:
  - "2025q1"
  - "acz"
  - "ift"
draft: false
description: "Updating a raw RFC specifying libp2p mixnet protocol and implementing a PoC over Waku"

---

`vac:acz:ift:2025q1-libp2p-mix-poc`

Updating the raw RFC specifying libp2p mixnet protocol and implementing a PoC over Waku
## Description

This commitment entails designing an anonymization layer for gossipsub, and by extension, IFT projects.
The primary objective of this anonymization layer is to serve as a cohesive anonymization solution for gossip-based projects,
with a specific focus on integrating it with the IFT projects Waku and Codex.


Our initial exploration will revolve around extending our [Tor push proposal](https://rfc.vac.dev/spec/46/).
In this approach, messages will traverse through an anonymization network before being disseminated via gossip protocols upon exiting the anonymization network.
Additionally, we aim to investigate the concept of embedding anonymization capabilities directly into gossipsub,
rather than routing messages through a separate anonymization network before entering a standard gossipsub network operation.

Currently we view this anonymization solution as a P2P base layer, which the Vac P2P team will offer as part of libp2p.
This effort could potentially spawn an incubation project.
This effort would act as a basis for the Validator Privacy Network incubation project.


By utilizing this commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Create a document describing the benefits of mixnet protocol for each of Waku, Status, Codex, and Nimbus
* Implement a gossibsub over Waku PoC shows the base functionality 

We will also strengthen the Premier Research Destination narrative by:
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the mixnet PoC and 
gain support from the Ethereum ecosystem.
* Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance(product-market fit), 
offering improvements over Tor push. 
* Publish two blogpost on [vac.dev/rlog](https://vac.dev/rlog) that includes update on transport layer of mixnet and 
Waku integration. 

## Task List

### RFC Update

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:rfc-update`
* owner: Akshaya
* status: not started
* start-date: 
* end-date: 

#### Description

Revise the RFC to incorporate a transport adapter transitioning from a custom protocol.

#### Deliverables

* A notion document as the new version of the RFC

### Gossibsub over Waku 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:gossipsub-over-waku`
* owner: Akshaya
* status: not started
* start-date: 
* end-date: 

#### Description

Implementation the second PoC, a gossibsub protocol over Waku network by integrating the mixnet.

#### Deliverables

* PR to vacp2p/mix repo 

### Testing and Documentation 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:test-and-doc`
* owner: Akshaya
* status: not started
* start-date: 
* end-date: 

#### Description

Implement logging for debugging and demonstration and test module including 
functional tests for mix handlers, integration tests for libp2p protocol adapter, and
End-to-end test of the mix network.

Developing documentation for individuals looking to integrate a mixnet into their projects. 

#### Deliverables

* PR to vacp2p/mix repo with test module
* PR to vacp2p/mix repo with documentation.md  

### Blogposts

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:blogposts`
* owner: Akshaya
* status: not started
* start-date: 
* end-date: 

#### Description

Two blog posts: one delves into the challenges of integrating mixnet to Waku, 
emphasizing receiver anonymity and featuring practical examples, 
while the other discusses updates to the RFC through the incorporation of a transport adapter.

#### Deliverables

* Two blogposts to [vac.dev/rlog](https://vac.dev/rlog)

### EF Grant Applications

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:ef-grant-app`
* owner: Akshaya
* status: not started
* start-date: 
* end-date: 

#### Description

This application involves two steps: 
first, compiling the proof-of-concept details, focusing on latency and incentivization requirements, 
and then initiating the EF grant process.

#### Deliverables

* A report document to Notion contains information of application details and updates
