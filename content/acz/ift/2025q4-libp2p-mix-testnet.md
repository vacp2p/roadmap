---
title: LibP2P mix testnet
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Publishing the findings with a blog post and a paper, investigating incentivization and consulting the Waku PoC over mixnet, and having next iteration of EF grant application with a privacy project that introduces sender anonymity for Ethereum nodes"


---

`vac:acz:ift:2025q4-libp2p-mix-testnet`

## Description
This commitment entails publishing the findings with a blogpost and a paper with extensive benchmark and
privacy analysis, also maintaining the Waku PoC over the mixnet and finally maintaining the EF grant application. 
 
### Background
The primary objective of this anonymization layer is to serve as a cohesive anonymization solution 
for gossip-based projects, with a specific focus on integrating it with the IFT projects Waku and Codex.

Our initial exploration will revolve around extending our [Tor push proposal](https://rfc.vac.dev/spec/46/).
In this approach, messages will traverse through an anonymization network before being disseminated via gossip protocols upon exiting the anonymization network. Additionally, we aim to investigate the concept of embedding anonymization capabilities directly into gossipsub,
rather than routing messages through a separate anonymization network  before entering a standard gossipsub network operation.

In 2025q3, we delivered mixnet gossipsub to be benchmarked in large scale, 
updated the RFC with latest changes, SURB specifications, and security section, 
lastly obtain the comparison between Nomos blend network and P2P mixnet.

### Narratives
By utilizing this commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Deploy the mixnet implementation as standard mixnet to the [nimlibp2p](https://github.com/vacp2p/nim-libp2p) repo. 

We will also strengthen the Premier Research Destination narrative by:
* Create a proposal for the Ethereum Foundation (EF) to apply for EF grants to promote the mixnet PoC and gain support from the Ethereum ecosystem.
* Publish a paper on arxiv.com that includes security/privacy analysis with applicability and revelance(product-market fit), offering improvements over Tor push. 
* Publish a blogpost on [vac.dev/rlog](https://vac.dev/rlog) that includes update on transport layer of mixnet and 
Waku integration. 

## Task List

### Updating RFC
* fully qualified name: `vac:acz:ift:2025q4-libp2p-mix-testnet:update-rfc`
* owner: Akshaya
* status: not started
* start-date: 2025/10/01
* end-date: 2025/11/10

#### Description
This task entails completing updating the [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) 
with latest findings such as clarifications on the pluggable components and adressing feedback. 

#### Deliverables

* A PR to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)

### Consulting Waku-mix 

* fully qualified name: `vac:acz:ift:2025q4-libp2p-mix-testnet:consulting-waku-mix`
* owner: Akshaya
* status: not started 
* start-date: 22025/10/01
* end-date: 2025/12/20

#### Description

Consulting about mixnet to Mixnet integration to the Waku.  

#### Deliverables

* PR to [vacp2p/mix](https://github.com/vacp2p/mix) or [waku-org/nwaku](https://github.com/waku-org/nwaku/) repo.