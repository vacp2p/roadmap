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

### ACME registration

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:acme-registration`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-06-06

#### Description
Register new account on ACME server 

#### Deliverables
- Generate key
- Register to ACME server using generated key

### Challenge request

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:certificate-request-challenge`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-06-06

#### Description
Request challenge from the ACME server (typically Let's Encrypt)

#### Deliverables
- Base36 encode our peerId
- Send certificate request for `*.{base36PeerId}.libp2p.direct` domain

### Notify AutoTLS broker

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:notify-autotls-broker`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-06-29

#### Description
Send DNS-01 challenge received from ACME server to the AutoTLS broker (registration.libp2p.direct)

#### Deliverables
- Authenticate with AutoTLS broker using PeerId Auth
- Send DNS-01 challenge to AutoTLS broker
- Successfully receive and respond to a dial from AutoTLS broker
- Query the broker's DNS registry until the `TXT` `_acme-challenge.{peerID}.libp2p.direct` record is set

### Notify challenge completion

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:notify-challenge-completion`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-06-29

#### Description
Notify the ACME server that we're done with DNS-01 challenge

#### Deliverables
- Send message to ACME server notifying that we're ready to be test
- Query the ACME server until it responds saying the challenge was fulfilled

### Finalize certificate

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:finalize-cert`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-06-29

#### Description
Finalize certificate issuance with CSR

#### Deliverables
- Generate CSR
- Send finalize message with CSR to ACME server
- Download certificate from ACME server

### Certificate installation

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:cert-installation`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-07-22

#### Description
Install generated certificate and use it in TCP/WS/WSSS/Quic/Webtransport

#### Deliverables
- Install certificate

### Certificate renewal

* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-autotls:cert-renewal`
* owner: gabriel
* status: 100%
* start-date: 2025-04-14
* end-date: 2025-06-29

#### Description
Renew certificate before it expires

#### Deliverables
- Send a request for the same certificate to the ACME server 

