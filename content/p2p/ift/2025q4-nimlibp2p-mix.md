---

title: Nim-libp2p Mix
tags:
  - "2025q4"
  - "p2p"
  - "ift"
draft: false
description: upstream specs for mix and reuse streams

---

`vac:p2p:ift:2025q4-nimlibp2p-mix`

Upstream spec for mix protocol and add stream reuse to reduce latency


## Description

The mix specification currently resides in [vacp2p#rfc-index](https://github.com/vacp2p/rfc-index/blob/main/vac/raw/mix.md). The goal is to upstream it into [libp2p#specs](https://github.com/libp2p/specs), ensuring adoption across libp2p implementations. Additionally, in late Q3 we identified an improvement: rather than opening and closing a new stream for each mix packet, streams can be reused, reducing lifecycle overhead and lowering end-to-end latency. Finally we found out that there's a possible metadata leakage when multiple Sphinx packets are broadcasted due to gragmentation of a large message by an upstram protocol sent in a burst.

## Task List


### Specs

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-mix:specs`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Collaborate with ACZ team into upstreaming initial mix design and rationale to 
`libp2p/spec` as proposal or draft PR. This task was originally part of Q3 but moved to
Q4 as specs update was not completed

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Draft PR merged into `libp2p/specs`


### Stream Reuse

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-mix:stream-reuse`
* owner: rramos
* status: completed
* start-date: 2025/10/13
* end-date: 2025/10/22

#### Description
Implement long-lived stream reuse between mix nodes, by establishing a persistent stream between mix peers.
Maintain a queue of outgoing Sphinx packets per peer, and dispatch them over the persistent stream. [vacp2p/mix#88](https://github.com/vacp2p/mix/issues/88)

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- [vacp2p/nim-libp2p#1753](https://github.com/vacp2p/nim-libp2p/pull/1753) feat(mix): reuse streams


### Rate limit publishing

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-mix:rate-limit`
* owner: rramos
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Introduce a randomized delay before the initiator sends each Sphinx packet to the first hop. This is important to avoid metadata leakage when multiple Sphinx packets (e.g., due to fragmentation of a large message by an upstream protocol) are sent in a burst.


Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Sender should not be able to send a burst of mix messages but instead have them rate limited with a random delay similar to the one used for hops.
