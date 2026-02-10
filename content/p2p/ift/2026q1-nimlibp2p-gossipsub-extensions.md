---

title: GossipSub Extensions and Partial Messages
tags:
  - "2026q1"
  - "p2p"
  - "ift"
draft: false
description: GossipSub Extensions and Partial Messages

---

`ift-ts:p2p:ift:2026q1-nimlibp2p-gossipsub-extensions`

## Description

This commitment focuses on implementing [Gossipsub v1.3 - Extensions control message](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/gossipsub-v1.3.md), a set of features that would allow gossipsub peers to describe characteristics to each other without requiring a new protocol ID per extension, and creating the partial messages extension, which would allow users to transmit only a small part of a message rather than a full message.

## Task List

### Implement Gossipsub Extensions support
* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-gossipsub-extensions:extensions`
* owner: Vlado
* status: done
* start-date: 2026/01/01
* end-date: 2026/01/20

#### Description
* Modify RPC protobuffer to be aware of the existence of `ControlExtensions` control message
* Send extensions message as the first message on a stream
* Test interoperability by implementing [Test Extension](https://github.com/libp2p/specs/blob/master/pubsub/gossipsub/extensions/experimental/test-extension.md)

#### Deliverables
- [vacp2p/nim-libp2p#2000](https://github.com/vacp2p/nim-libp2p/pull/2000) feat(gossipsub): extensions control message
- Gossipsub extensions supported
- Test Extension implemented (optionally enabled via compile time flag)

### Implement Gossipsub Partial Messages Extension
* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-gossipsub-extensions:partial-messages`
* owner: Vlado
* status: in progress (85%)
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
* [Partial Messages Extensions](https://github.com/libp2p/specs/blob/marco/partial-messages/pubsub/gossipsub/partial-messages.md) allow users to transmit only a small part of a message rather than a full message. 
* This is especially useful in cases where there is a large messages and a peer is missing only a small part of the message.

#### Deliverables
- [vacp2p/nim-libp2p#2076](https://github.com/vacp2p/nim-libp2p/pull/2076) test(extensions): adding tests for partial message
- [vacp2p/nim-libp2p#2074](https://github.com/vacp2p/nim-libp2p/pull/2074) test(extensions): improving tests
- [vacp2p/nim-libp2p#2040](https://github.com/vacp2p/nim-libp2p/pull/2040) feat(gossipsub): partial message extension
- Partial messages extension implemented
- Set of unit tests to test this extension


### Change Gossipsub 1.4 to an extension
* fully qualified name: `ift-ts:p2p:ift:2026q1-nimlibp2p-gossipsub-extensions:1-4-extension`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Modify gossipsub 1.4 so it uses extensions instead of a new protocol Id. This task has low priority and should only be implemented if time allows it.

#### Deliverables
- Gossipsub 1.4 implemented as a gossipsub extension
