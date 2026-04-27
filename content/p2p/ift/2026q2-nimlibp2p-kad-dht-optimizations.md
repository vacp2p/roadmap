---

title: nim-libp2p Kad-DHT Optimizations
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Improve Kad-DHT privacy and provider record advertisement behavior

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-kad-dht-optimizations`

Improve nim-libp2p Kad-DHT privacy and provider record advertisement behavior.

## Description

This commitment covers two related Kad-DHT improvements. First, Kad-DHT response
messages should avoid disclosing peer connection type because it can reveal
network topology and increase eclipse-attack risk. This follows
[vacp2p/nim-libp2p#2050](https://github.com/vacp2p/nim-libp2p/issues/2050)
and the Logos extended Kad discovery privacy requirement that every Kad-DHT
`Peer.connection` field be encoded as `NOT_CONNECTED`.

Second, provider record advertisement traffic can overload nodes close to
popular content. The libp2p community has discussed Coral-style rejection,
spillover, and backtracking for provider records in
[libp2p/specs#163](https://github.com/libp2p/specs/issues/163), and
[go-libp2p-kad-dht#345](https://github.com/libp2p/go-libp2p-kad-dht/issues/345)
tracks these as part of the critical path toward DHT efficiency and
performance. This commitment brings equivalent optimization work to the
nim-libp2p Kad-DHT implementation.

## Task List

### Kad-DHT Connection Field Privacy

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-kad-dht-optimizations:connection-field-privacy`
* owner: not assigned yet
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description
Ensure Kad-DHT response messages can optionally not disclose local connection information.
When encoding Kad-DHT `Peer` records, set the `connection` field to
`NOT_CONNECTED`. Maintain backward compatibility by continuing to parse peers
that send other `ConnectionType` values.

#### Deliverables
- Kad-DHT encoder always emits `NOT_CONNECTED` for peer connection type depending on kademlia setup option
- Receive-side compatibility for non-compliant peers
- Tests covering encoding and parsing of `ConnectionType` values
- Documentation of the privacy behavior and compatibility policy


### Provider Record Spillover

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-kad-dht-optimizations:provider-record-spillover`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Add provider record overload protection and advertisement spillover behavior.
Provider records should have local limits and throttling, and rejected
advertisements should be able to spill over by backtracking through the lookup
path rather than repeatedly targeting only the closest nodes to a popular key.

#### Deliverables
- Configurable provider record limits and throttling policy
- Rejection response handling for provider advertisements
- Spillover/backtracking behavior for popular provider records
- Metrics or simulation coverage showing advertisement load distribution
- Tests for provider record limits, rejection, spillover, and lookup behavior
