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
* status:
* start-date: 2025-07-01
* end-date:

#### Description
Implement client side, constructing and sending `DialRequest`, handling `DialDataRequest`/`DialDataResponse` exchange,
validate nonce on `DialBack` and parse `DialResponse`.
Ensure interop against other implementations

#### Deliverables



### Server

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autonat-v2:server`
* owner: gabe
* status:
* start-date: 2025-07-01
* end-date:

#### Description
Address selection, dial address, send `DialBack`, handle nonce and do amplification check.
Ensure interop against other implementations

#### Deliverables

