---

title: Logos Core Custom Protocol Support
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Support custom libp2p protocols from external Logos Core modules

---

`ift-ts:p2p:ift:2026q3-logos-core-custom-protocol-support`

Support custom libp2p protocols created by external Logos Core modules,
including modules that may not run in the same process or on the same machine
as the libp2p node.

## Description

Logos Core needs a way for external modules to define and handle custom libp2p
protocols without embedding all protocol logic inside the Logos libp2p module.
This work depends on the Logos Core exposing functionality to be able to
implement such functionality because custom protocol stream events need to be 
routed to module code and responses need to flow back to the libp2p node.

Once this functionality is available in logos core, this becomes the 
highest-priority Q3 commitment.

## Task List

### Custom Protocol Registration

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-custom-protocol-support:registration`
* owner: gabe
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Expose an API that lets external modules register libp2p protocol identifiers
and handlers through Logos Core. The API should support modules that are
separate from the libp2p node process while preserving nim-libp2p stream
semantics.

#### Deliverables
- Logos Core API for registering custom protocol handlers
- Wiring from Logos Core registration to nim-libp2p protocol mounting


### Remote Stream Handling

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core-custom-protocol-support:remote-stream-handling`
* owner: gabe
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Implement the stream event path that lets an external module handle inbound and
outbound custom protocol streams. The design should account for timeouts, 
stream reset, node shutdown, and remote module failure.

#### Deliverables
- Inbound stream events delivered to external modules
- Stream read, write, close, and reset operations exposed through Logos Core
- Tests or examples covering custom protocol registration and remote stream handling
