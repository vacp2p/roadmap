---
title: LibP2P mix testnet
tags:
  - "2025q4"
  - "acz"
  - "ift"
draft: false
description: "Finalizing the specification of libp2p-mix RFC and
applying the EF grant that introduces sender anonymity for Ethereum nodes"


---

`vac:acz:ift:2025q4-libp2p-mix-testnet`

## Description
This commitment entails finalizing the [libp2p-mix RFC](https://rfc.vac.dev/vac/raw/mix) and
applying EF grant that introduces sender anonymity for Ethereum nodes. 
 
### Background
The primary objective of this anonymization layer is to serve as a cohesive anonymization solution 
for gossip-based projects, with a specific focus on integrating it with the IFT projects Waku and Codex.

Our initial exploration will revolve around extending our [Tor push proposal](https://rfc.vac.dev/spec/46/).
In this approach, messages will traverse through an anonymization network before being disseminated
via gossip protocols upon exiting the anonymization network.
Additionally, we aim to investigate the concept of embedding anonymization capabilities directly into gossipsub,
rather than routing messages through a separate anonymization network before entering a standard gossipsub network operation.

In 2025q3, we delivered libp2p-mixnet gossipsub to be benchmarked on a large scale, 
updated the RFC with the latest changes, SURB specifications, and the security section, 
lastly obtain the comparison between Nomos blend network and P2P mixnet.

### Narratives
By utilizing this commitment, 
we will reinforce the Conduit of Expertise narrative by:
* Releasing the final RFC for a standard mixnet to the [nimlibp2p](https://github.com/vacp2p/nim-libp2p) repo. 

We will also strengthen the Premier Research Destination narrative by:
* Finalize the existing proposal by refining it for the Ethereum Foundation (EF) to apply for EF grants
to promote the mixnet PoC and gain support from the Ethereum ecosystem.

## Task List

### Maintaining RFC
* fully qualified name: `vac:acz:ift:2025q4-libp2p-mix-testnet:update-rfc`
* owner: Ugur
* status: not started
* start-date: 2025/10/15
* end-date: 2025/11/15

#### Description
This task entails maintaining [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) 
with the latest findings, such as clarifications on exit =! destination, SURB design and solving current issues. 

#### Deliverables

* A PR to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)
