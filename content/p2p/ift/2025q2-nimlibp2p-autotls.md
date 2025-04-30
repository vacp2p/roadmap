---

title: nim-libp2p Auto TLS
tags:
  - "2025q2"
  - "p2p"
  - "ift"
draft: false
description: nim-libp2p Auto TLS

---

`vac:p2p:ift:2025q2-nimlibp2p-autotls`

Implement a process that automates the issuance of Let’s Encrypt wilcard TLS certificates for nim-libp2p nodes. 
This would enable reliable browser-based clients to connect to libp2p nodes, regardless of the network topology which 
improves resilience and opens up a window to more capable browser clients. 
This task is limited to the client functionality; Server functionality could be implemented on a separate commitment. 
[AutoTLS](https://blog.libp2p.io/autotls/)


## Task List

### Certificate request and authentication

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:certificate-request-auth`
* owner: gabriel
* status: 25%
* start-date: 2025-04-14
* end-date:

#### Description
Request certificate and authenticate against registration.libp2p.direct

#### Deliverables



### DNS challenge

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:dns-challenge`
* owner: gabriel
* status: 25%
* start-date: 2025-04-14
* end-date:

#### Description
Notify DNS-01 challenge completion

#### Deliverables



### Certificate Installation

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:certificate-installation`
* owner: gabriel
* status: 25%
* start-date: 2025-04-14
* end-date:

#### Description
Install generated certificate and use it in TCP/WS/WSSS/Quic/Webtransport


#### Deliverables

