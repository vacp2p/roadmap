---

title: nim-libp2p Universal Connectivity App
tags:
  - "2025q3"
  - "p2p"
  - "ift"
draft: false
description: Add webtransport support to nim-libp2p

---

`vac:p2p:ift:2025q3-nimlibp2p-universal-connectivity-app`

Realtime highly decentralised chat app.

## Description

Create an example chat application that demonstrates libp2p features using gossipsub for messaging, 
and WSS, Quic, and TCP transports. 
This app should be published at the [libp2p/universal-connectivity](https://github.com/libp2p/universal-connectivity) repository.
A future commitment might add support of Kad-DHT to discover nodes, 
and additional transports like WebTransport/WebRTC/WebRTC-direct as transports (once they're available in nim-libp2p). 

## Task List

### Chat
* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-universal-connectivity-app:chat`
* owner: gabe
* status: 100%
* start-date: 2025-07-12
* end-date: 2025-08-22

#### Description
Using either [directchat.nim](https://github.com/vacp2p/nim-libp2p/blob/master/examples/directchat.nim) or [chat2](https://github.com/waku-org/nwaku/tree/master/apps/chat2),
implement a chat application that can interop successfully with other implementations available at [libp2p/universal-connectivity](https://github.com/libp2p/universal-connectivity/tree/main).

#### Deliverables
- [vacp2p/universal-connectivity#1](https://github.com/vacp2p/universal-connectivity/pull/1) feat: add nim peer
- [libp2p/universal-connectivity#306](https://github.com/libp2p/universal-connectivity/pull/306) feat: add nim peer



### File Exchange
* fully qualified name: `vac:p2p:ift:2025q2-nimlibp2p-universal-connectivity-app:file-exchange`
* owner: gabe
* status: out of scope
* start-date: ----
* end-date: ----

#### Description
Allow sending/receiving files. Must react to messages sent of the file exchange topic. 

#### Deliverables
- ~~Basic UI - Receive file message~~
- ~~Allow sending file  (maybe with a chat command `/file path/to/file`)~~
- ~~Interop~~
- None of the other implementations send/receive files and/or their code remains incomplete.
  Changing this task to Out of Scope until universal connectivity app specs indicate that file support is to be implemented

