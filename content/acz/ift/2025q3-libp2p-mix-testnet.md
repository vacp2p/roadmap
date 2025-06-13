---

title: LibP2P mix testnet
tags:

- "2025q3"
- "acz"
- "ift"
draft: false
description: "Publishing the findings with a blog post and a paper, and consulting the Waku PoC over mixnet"

---

`vac:acz:ift:2025q3-libp2p-mix-testnet`

Publishing the findings with a blog post and a paper, and consulting the Waku PoC over mixnet

## Description

This commitment entails publishing the findings with a blog post and a paper with an extensive benchmark and
privacy analysis, also maintaining the Waku PoC over the mixnet. 
Lastly, review and modify the codebase for better compatibility. 

### Background

The primary objective of this anonymization layer is to serve as a cohesive anonymization solution
for gossip-based projects, with a specific focus on integrating it with the IFT projects Waku and Codex.

Our initial exploration will revolve around extending our [Tor push proposal](https://rfc.vac.dev/spec/46/). 
In this approach, messages will traverse through an anonymization network before being disseminated 
via gossip protocols upon exiting the anonymization network. 
Additionally, we aim to investigate the concept of embedding anonymization capabilities directly into gossipsub, 
rather than routing messages through a separate anonymization network before entering a standard gossipsub network operation.

In 2025q3, we delivered mixnet gossipsub to be benchmarked in large scale, 
updated the RFC with latest changes, and SURB implementationm lastly obtain 
the comparison between Nomos blend network and P2P mixnet.

### Narratives

By utilizing this commitment,
we will reinforce the Conduit of Expertise narrative by:

- Deploy the mixnet implementation as standard mixnet to the [nimlibp2p](https://github.com/vacp2p/nim-libp2p) repo.

We will also strengthen the Premier Research Destination narrative by:

- Publish a paper on [arxiv.com](http://arxiv.com/) that includes security/privacy analysis 
with applicability and revelance(product-market fit), offering improvements over Tor push.
- Publish a blogpost on [vac.dev/rlog](https://vac.dev/rlog) that includes update on transport layer of mixnet and
Waku integration.

## Task List