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

### PoC over Waku 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:poc-over-waku`
* owner: Akshaya
* status: started (20%)
* start-date: 2025/01/06
* end-date: 2025/02/03

#### Description

Implementation the second PoC over Waku network by integrating the mixnet.

#### Deliverables

* PR to vacp2p/mix repo 

### RFC Update

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:rfc-update`
* owner: Akshaya
* status: not started
* start-date: 2025/02/03
* end-date: 2025/02/17

#### Description

Revise the RFC to incorporate a transport adapter transitioning from a custom protocol.

#### Deliverables

* A notion document as the new version of the RFC

### Testing and Documentation 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:test-and-doc`
* owner: Akshaya
* status: not started
* start-date: 2025/02/17
* end-date: 2025/03/03

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
* start-date: 2025/03/03
* end-date: 2025/03/10

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
* start-date: 2025/03/10
* end-date: 2025/03/31

#### Description

This application involves two steps: 
first, compiling the proof-of-concept details, focusing on latency and incentivization requirements, 
and then initiating the EF grant process.

#### Deliverables

* A report document to Notion contains information of application details and updates

### Publishing a Paper 

* fully qualified name: `vac:acz:ift:2025q1-libp2p-mix-poc:publish-a-paper`
* owner: Akshaya
* status: not started
* start-date: 2025/03/10
* end-date: 2025/03/24

#### Description

Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance (product-market fit), 
offering improvements over Tor push. 

#### Deliverables

* A paper on arxiv.com
