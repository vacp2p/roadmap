---

title: GossipSub Performance Improvements
tags:
  - "2025q2"
  - "p2p"
  - "ift"
draft: false
description: GossipSub Performance Improvements

---

`vac:p2p:ift:2025q2-gossipsub-perf-improvements`

## Description

It is a continuous task to improve GossipSub performance by lowering bandwidth consumption and network-wide message dissemination time. These improvements also indirectly support scalability by allowing for a larger supported network size, higher message counts, and increased message volumes. This work contributes to the development of GossipSub specification proposal(s) and publishing findings in articles and blog posts.

During this quarter, we focus on a detailed evaluation of upcoming GossipSub proposals, including GossipSub v2.0, Push-pull transition for DAS, and GossipSub v1.4 for suitability under various conditions, including the Ethereum use case.

## Task List


### GossipSub Performance Comparison

* fully qualified name: `vac:p2p:ift:2025q2-gossipsub-perf-improvements:perf-comparison`
* owner: farooq
* status: 90%
* start-date: 2025/04/01
* end-date: 2025/05/15

#### Description

Nim, go, and rust libp2p test nodes are already implemented for the shadow simulator (including support for gossipsub v1.4, v2.0), and basic evaluations are done using the shadow simulator. This task aims to achieve a detailed performance evaluation of upcoming specification proposals (including GossipSub v2.0, v1.4, v1.4 with stagger send, push-pull phase transition for DAS) for different test scenarios (including the Ethereum use case) to identify rationales behind any performance gains. This can also help identify any potential performance improvements.

#### Deliverables
- Blog/forum post Comparing libp2p GossipSub performance across nim, go and rust libp2p
- Blog/forum post comparing libp2p GossipSub performance across GossipSub 1.2, 1.4, 2.0, PPPT



### GossipSub 1.4 Implementation

* fully qualified name: `vac:p2p:ift:2025q2-gossipsub-perf-improvements:gossipsub-1_4-impl`
* owner: farooq
* status: 90%
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description

The PoC implementation for GossipSubv1.4 is already complete. This work focuses on the full implementation of GossipSub v1.4

#### Deliverables
- Complete GossipSub v1.4 implementation
- QUIC evaluation of 1.4 (short blogpost)



### Community Engagement

* fully qualified name: `vac:p2p:ift:2025q2-gossipsub-perf-improvements:community-engangement`
* owner: farooq
* status: 25%
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description

Follow up GossipSub-related discussions on forums like Ethresearch, libp2p specs, and other related places.

#### Deliverables
- Follow-up for GossipSub v1.4 proposal approval
- libp2p specs/community meetings
- blogs, posts, and engagements in discussions relating to GossipSub



### Using Nimbus in Ethshadow

* fully qualified name: `vac:p2p:ift:2025q2-gossipsub-perf-improvements:nimbus-eth-shadow`
* owner: farooq
* status: 70%
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description

Running Nimbus in eathshadow can allow running Ethereum experiments on custom GossipSub protocols in nim-libp2p.
Nimbus support has already been added to the Ethshadow simulator, but Nimbus nodes terminate due to the unsupported 
system calls. It is worth exploring potential workarounds to the unsupported system calls (for instance, adding 
unsupported system calls in the shadow simulator) or any other issues.

#### Deliverables
- Add unsupported system calls in the shadow simulator.
- Add Prometheus support for Nimbus in Ethshadow.



### Stream prioritization/ Message rotation

* fully qualified name: `vac:p2p:ift:2025q2-gossipsub-perf-improvements:stream-prioritization`
* owner: farooq
* status: 25%
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description

QUIC allows stream prioritization. Experimenting with different message prioritization/rotation techniques can be helpful in peak loads.
We’ll prioritize this task after Task 1 completes.

#### Deliverables
- Forum/blog post on findings
