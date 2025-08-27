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

### Updating RFC
* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:update-rfc`
* owner: Akshaya
* status: started (70%)
* start-date: 2025/07/01
* end-date: 2025/08/18

#### Description
This task entails completing updating the [mixnet RFC](https://rfc.vac.dev/vac/raw/mix) 
with latest findings such as clarifications on the pluggable components, 
introducing  the entry and exit layers and libp2p integrations.

#### Deliverables

* A [PR](https://github.com/vacp2p/rfc-index/pull/158) to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)
* [RFC Refactor: Sphinx Packet Format PR ](https://github.com/vacp2p/rfc-index/pull/173)

### libp2p-mix Relay RFC  
* fully qualified name: `vac:acz:ift:2025q?-gossipsub-relay-rfc:relay-rfc`  
* owner: Akshaya
* status: not started  
* start-date: 2025/09/01
* end-date: 2025/09/15

#### Description  
Draft an RFC for `/gossipsub-relay/1.0.0`, a minimal protocol that allows external clients
to inject raw GossipSub messages into a full node’s relay logic.
This makes Mix integration cleaner without requiring the exit nodes to participate in mesh or support GossipSub.  

#### Deliverables  
* A PR to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index) containing the RFC.  

### Investigate Unexpected Mixnet Latency
* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:unexpected-latency`
* owner: Akshaya
* status: on-hold (%70)
* start-date: 2025/07/01
* end-date: 2025/07/15

#### Description

This task is on hold since the solution is waiting to be confirmed.

This task entails investigating to find root cause of unexpected latency.
Observed latency with 3 mix hops and 100ms delays is ~1100–1600ms, 
far exceeding the expected ~300ms. 
Prior Lightpush tests showed much lower overhead. 


#### Deliverables

* A PR to [vacp2p/mix](https://github.com/vacp2p/mix)

### Fix Premature Handler Invocation
* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:premature-handler`
* owner: Akshaya
* status: done
* start-date: 2025/07/01
* end-date: 2025/07/15

#### Description
This task entails solving the issue that: in some runs, 
handlers are triggered before any exit receives the message. 
Likely due to publisher advertising the message via IHAVE 
from its mcache while the mix path is still active. 
Requires investigation and fix.


#### Deliverables

* A PR to [vacp2p/mix](https://github.com/vacp2p/mix)

### Consulting Waku-mix 

* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:consulting-waku-mix`
* owner: Akshaya
* status: started (50%)
* start-date: 2025/07/01
* end-date: 2025/09/20

#### Description

Consulting about mixnet to Mixnet integration to the Waku.  

#### Deliverables

* PR to [vacp2p/mix](https://github.com/vacp2p/mix) or [waku-org/nwaku](https://github.com/waku-org/nwaku/) repo.

### Multi SURB Design
* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:multi-surb-design`
* owner: Akshaya
* status: started (85%)
* start-date: 2025/07/01
* end-date: 2025/08/17

#### Description
This task focuses on developing a multi-SURB scheme 
capable of resolving inconsistencies that occur 
when multiple SURBs are concurrently active.

#### Deliverables

* A [PR] to [vacp2p/rfc-index](https://github.com/vacp2p/rfc-index)

### Mix benchmarking
* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:mix-benchmarking`
* owner: Ben
* status: cancelled
* start-date: 
* end-date: 

#### Description

This task is cancelled since the P2P team has taken it over.

This task involves running the next set of benchmarks after resolving the outstanding issues.

#### Deliverables

* A [PR] to [vacp2p/nim-libp2p](https://github.com/vacp2p/rfc-index)

### nimlibp2p integration
* fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:nimlibp2p-integration`
* owner: Ben
* status: cancelled
* start-date: 
* end-date: 

#### Description

This task is cancelled since the P2P team has taken it over. 

This task focuses on integration the mix into the [vacp2p/nim-libp2p repo](https://github.com/vacp2p/nim-libp2p)

#### Deliverables

* A [PR] to [vacp2p/nim-libp2p](https://github.com/vacp2p/rfc-index)


### libp2p-mix Repository 

- fully qualified name: `vac:acz:ift:2025q3-libp2p-mix-testnet:libp2p-mix-repo`
- owner: Akshaya
- status: started (60%)
- start-date: 2025/07/01
- end-date: 2025/09/30

### Description

This task encompasses all maintenance updates for [vacp2p/nim-libp2p repo](https://github.com/vacp2p/nim-libp2p) repo, including PR reviews.

### Deliverables

* A set of PRs and issues to [vacp2p/nim-libp2p repo](https://github.com/vacp2p/nim-libp2p).