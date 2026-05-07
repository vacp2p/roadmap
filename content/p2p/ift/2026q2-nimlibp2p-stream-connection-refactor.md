---

title: nim-libp2p Stream and Connection Refactor
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Refactor nim-libp2p stream and connection abstractions

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-stream-connection-refactor`

Refactor nim-libp2p stream and connection abstractions so peer connections and protocol streams are represented by distinct types.

## Description

The current nim-libp2p implementation uses `Connection` both for actual peer
connections and for streams opened over multiplexed connections. In the current
code shape `Connection` inherits from `LPStream`, muxers return `Connection`
from `newStream`, and protocol handlers receive `Connection` even when they are
handling a single protocol stream. This makes the abstraction harder to
understand, increases the cost of onboarding contributors, and complicates
resource lifecycle work such as close/reset behavior and stream ownership.

This commitment separates the concepts so `Connection` refers to peer-level
connections and a new stream abstraction is used for protocol streams. The
refactor should preserve downstream compatibility during the migration and
reduce ambiguity in code, tests, metrics, and documentation.

## Task List

### Stream and Connection Abstractions

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-stream-connection-refactor:abstractions`
* owner: not assigned yet
* status: not started
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description
Introduce a clear stream abstraction for protocol streams and narrow
`Connection` to represent actual peer connections. Update muxer and connection
manager interfaces so opening a stream returns the stream type, while peer-level
connection state remains on connection objects.


#### Deliverables
- New stream-level abstraction used by muxers and protocol handlers
- `Connection` narrowed to peer-level connection state and behavior
- Compatibility shims or migration aliases for existing downstream users
- Updated close/reset lifecycle behavior for streams and connections
- Tests covering stream creation, close/reset semantics, and protocol handler usage
- Documentation and examples using the new names consistently
