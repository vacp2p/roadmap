---

title: nim-libp2p IPv6 support
tags:
  - "2025q4"
  - "p2p"
  - "ift"
draft: false
description: add first-class IPv6 support across transports

---

`vac:p2p:ift:2025q4-nimlibp2p-ipv6`

Enable IPv6 support

## Description

Enable IPv6 in nim-libp2p end-to-end so users of the library can run dual-stack when needed. Scope covers transports (tcp/quic), address handling (multiaddr, identify),  and ci/test infra. 

## Task List

### Core transports (tcp/quic)

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-ipv6:transport`
* owner:
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Add IPv6 listen/dial for tcp and quic. Might require changes in chronos

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- nodes can listen on /ip6 and accept inbound requests
- dialer can dial /ip6 addresses


### addresses & identity

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-ipv6:addresses`
* owner:
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Add IPv6 support in the switch when specifying listening multiaddresses containing ip6 component. 
Ensure ip6 addresses are advertised in identify.
Implement measures to handle duplicated IPs in peerstore/addresses being listened to (i.e 192.0.2.42 vs 2001:db8::1234). 

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Identify advertises correct /ip6 addrs; observed addrs tracked per transport


### Testing, Interop & CI

* fully qualified name: `vac:p2p:ift:2025q4-nimlibp2p-ipv6:testing`
* owner:
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Ensure IPv6 support and ensure there are no regressions in IPv4 support. Add test units demonstrating the support, and check that interop against other implementations is achieved

Schedule note: Dates reflect quarter bounds; update when actual timing is known.
#### Deliverables
- Test units focusing on IPv6
- Interop tests against other implementations that support IPv6
