---

title: nim-libp2p Webtransport
tags:
  - "2026q1"
  - "p2p"
  - "ift"
draft: false
description: Add webtransport support to nim-libp2p

---

`vac:p2p:ift:2026q1-nimlibp2p-webtransport`

Implement WebTransport support in nim-libp2p, enabling browser/server bidirectional streams via h3+quic. built atop nim-lsquic, extending its current quic-only integration.

## Description

Extend the number of transports supported by nim-libp2p via the development of Webtransport,
which would allow browsers to establish bidirectional stream connections to nim-libp2p servers
This is done by using ls-quic which nim-libp2p already uses for quic transport

## Task List

### Http3 engine
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-webtransport:http3-engine`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Extend nim-lsquic bindings to support acting as a proper http3 engine. enable configuration flags for h3 mode vs raw-quic mode, implement the callback plumbing for headers, datagrams, and stream events required by webtransport.

#### Deliverables
- New h3-capable initialization api in nim-lsquic.

### Client
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-webtransport:client`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Implement client-side webtransport session establishment

#### Deliverables
Client side functionality that allows establishing a connection via webtransport

### Server
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-webtransport:server`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Server acceptance of webtransport sessions

#### Deliverables
Server side functionality that allows accepting connections via webtransport


### Transport
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-webtransport:transport`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Introduce a new libp2p transport that spins up a dedicated nim-lsquic instance with http3 enabled 
on a separate UDP port from raw quic transport. Map libp2p connection and stream abstractions to 
webtransport sessions and streams.

#### Deliverables
A libp2p transport that allows web clients to communicate with nim-libp2p nodes via WebTransport

### Interop
* fully qualified name: `vac:p2p:ift:2026q1-nimlibp2p-webtransport:interop`
* owner: not assigned yet
* status: not started
* start-date: 2026/01/01
* end-date: 2026/03/31

#### Description
Ensure interoperability with other libp2p implementations, with focus on js-libp2p

#### Deliverables
- Interop test suite runnable in CI