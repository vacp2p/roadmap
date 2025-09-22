---

title: AutoNAT v2
tags:
  - "2025q3"
  - "p2p"
  - "ift"
draft: false
description: Implement AutoNAT v2

---

`vac:p2p:ift:2025q3-nimlibp2p-autonat-v2`

Implement AutoNAT V2 based on the [libp2p specification](https://github.com/libp2p/specs/blob/master/autonat/autonat-v2.md).

## Task List

### Client

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autonat-v2t:client`
* owner: gabe
* status: 100%
* start-date: 2025-07-01
* end-date: 2025-09-10

#### Description
Implement client side, constructing and sending `DialRequest`, handling `DialDataRequest`/`DialDataResponse` exchange,
validate nonce on `DialBack` and parse `DialResponse`.
Ensure interop against other implementations

#### Deliverables
- PR:
  - [nim-libp2p#1659](https://github.com/vacp2p/nim-libp2p/pull/1659) feat: add client and tests
  - [nim-libp2p#1657](https://github.com/vacp2p/nim-libp2p/pull/1657) chore: add utils
  - [nim-libp2p#1654](https://github.com/vacp2p/nim-libp2p/pull/1654) chore: pass localAddr in noise, mplex and yamux
  - [nim-libp2p#1651](https://github.com/vacp2p/nim-libp2p/pull/1651) chore: add localAddr to Connection
  - [nim-libp2p#1637](https://github.com/vacp2p/nim-libp2p/pull/1637) chore: add message types

### Server

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autonat-v2:server`
* owner: gabe
* status: 100%
* start-date: 2025-07-01
* end-date: 2025-09-10

#### Description
Address selection, dial address, send `DialBack`, handle nonce and do amplification check.
Ensure interop against other implementations

#### Deliverables
- PR
  - [nim-libp2p#1680](https://github.com/vacp2p/nim-libp2p/pull/1680) chore: rename withAutonatV2 to withAutonatV2S
  - [nim-libp2p#1669](https://github.com/vacp2p/nim-libp2p/pull/1669) chore: add server config
  - [nim-libp2p#1658](https://github.com/vacp2p/nim-libp2p/pull/1658) feat: add server

### Service

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autonat-v2:service`
* owner: gabe
* status: 100%
* start-date: 2025-09-10
* end-date: 2025-09-12

#### Description
Create a service that determines if the node is reachable behind NAT by asking connected peers 
to dial it back, maintains a sliding-window confidence, and periodically reschedules checks, 
and (when reachable) rewrites listen addrs to dialable ones

#### Deliverables
- PR
  - [nim-libp2p#1684](https://github.com/vacp2p/nim-libp2p/pull/1684) feat: add autonatv2 service
  - [nim-libp2p#1686](https://github.com/vacp2p/nim-libp2p/pull/1686) chore: add autonatv2 service to builder

### Interop

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autonat-v2:interop`
* owner: gabe
* status: 20%
* start-date: 2025-09-15
* end-date:

#### Description
Ensure there's interop in both client and server of AutonatV2 against other libp2p implementations 

#### Deliverables
