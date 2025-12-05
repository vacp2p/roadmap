---

title: GossipSub Extensions
tags:
  - "2026q1"
  - "p2p"
  - "ift"
draft: false
description: GossipSub Extensions

---

`vac:p2p:ift:2026q1-gossipsub-extensions`

## Description

This commitment focuses on implementing [Gossipsub v1.3 - Extensions control message](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/gossipsub-v1.3.md), a set of features that would allow gossipsub peers to describe characteristics to each other without requiring a new protocol ID per extension. 

## Task List

### Implement Gossipsub Extensions support

* fully qualified name: `vac:p2p:ift:2026q1-gossipsub-extensions:extensions`
* owner: 
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
* Modify RPC protobuffer to be aware of the existence of `ControlExtensions` control message
* Send extensions message as the first message on a stream
* Test interoperability by implementing [Test Extension](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/extensions/experimental/test-extension.md)
* Modify gossipsub 1.4 so it uses extensions instead of a new protocol Id

#### Deliverables
- Test extension support (optionally enabled via compile time flag)
- Gossipsub 1.4 implemented as a gossipsub extension
