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

TODO

## Task List


### GossipSub Performance Improvements

* fully qualified name: `vac:p2p:ift:2025q2-gossipsub-perf-improvements`
* owner: farooq
* status: not started
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description

- Benchmark shadow experiments with DST experiments. This also includes:
	- Deliberating experiments focused on ethereum and other generalized usecases
	- QUIC allows stream prioritization. Experment with different message prioritization/rotation techniques. Can be helpful in peak loads
- Theoratically, average link latency can have noticeable impact on message dissemination latency. 
	- At first we will use psuedo-random peers to experiment the impact of optimal peer selection on the protocol performance. 
	- Evaluate the peering quality under the current arrangement
	- Use these findings to achieve improvements in the peering algorithm. 
- Follow up GossipSub related discussions on forums like Ethresearch, libp2p specs, and other related repos.
- Carry-out detailed performance comparisons of nim-libp2p, go-libp2p and rust-libp2p. This includes
	- Checking for latency and bandwidth utilization
	- Identifying any potential improvements available to go, rust libp2p
	- Create testcases and relevant simulation scripts for the ethereum usecase
- GossipSub 1.4 implementation

#### Deliverables
