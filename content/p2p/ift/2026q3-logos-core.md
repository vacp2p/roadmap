---
title: Logos Core
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Maintain the Logos Core libp2p integration and its networking dependency stack
---

`ift-ts:p2p:ift:2026q3-logos-core`

Maintain the Logos Core libp2p integration and its networking dependency stack.

## Description

Continue supporting the Logos Core libp2p module through compatibility fixes,
dependency updates, release coordination, and integration maintenance. This
includes the nim-libp2p, nim-lsquic, BoringSSL, and libplum changes required to
keep Logos modules building and operating reliably.

## Task List

### Maintenance

- fully qualified name: `ift-ts:p2p:ift:2026q3-logos-core:maintenance`
- owner: rramos/gabe
- status: in progress (66%)
- start-date: 2026/07/01
- end-date: 2026/09/30

#### Description

Maintain the Logos Core libp2p integration, coordinate compatible dependency
releases, and resolve build, runtime, and integration defects across the
networking stack.

#### Deliverables

- [vacp2p/nim-libp2p#2998](https://github.com/vacp2p/nim-libp2p/pull/2998) fix(bufferstream): avoid stranding pushes on close
- [logos-messaging/logos-delivery#4161](https://github.com/logos-messaging/logos-delivery/pull/4161) chore: bump nim-libp2p to v2.3.1
- [vacp2p/nim-libp2p#3002](https://github.com/vacp2p/nim-libp2p/pull/3002) chore(release): prepare v2.3.1 with libplum v0.6.3
- [logos-storage/nim-libplum#24](https://github.com/logos-storage/nim-libplum/pull/24) chore: bump version to 0.6.3
- [logos-storage/nim-libplum#23](https://github.com/logos-storage/nim-libplum/pull/23) fix(android): avoid linking libpthread
- [status-im/nimbus-eth2#8936](https://github.com/status-im/nimbus-eth2/pull/8936) chore: bump nim-libp2p
- [vacp2p/nim-lsquic#164](https://github.com/vacp2p/nim-lsquic/pull/164) fix(connection): notify dialers when accepted connections close
- [vacp2p/nim-lsquic#161](https://github.com/vacp2p/nim-lsquic/pull/161) fix(endpoint): honor QUIC stateless resets
- [vacp2p/nim-lsquic#157](https://github.com/vacp2p/nim-lsquic/pull/157) fix(tlsconfig): preserve ALPN preference order
- [vacp2p/nim-lsquic#158](https://github.com/vacp2p/nim-lsquic/pull/158) fix(build): support disabling BoringSSL assembly
- [vacp2p/nim-lsquic#159](https://github.com/vacp2p/nim-lsquic/pull/159) fix(context): pin transport defaults
- [vacp2p/nim-boringssl#10](https://github.com/vacp2p/nim-boringssl/pull/10) chore: update BoringSSL submodule and bindings
- [vacp2p/boringssl#8](https://github.com/vacp2p/boringssl/pull/8) chore: sync BoringSSL upstream
- [litespeedtech/lsquic#675](https://github.com/litespeedtech/lsquic/issues/675) `lsquic_conn_close()` on an idle server-side IETF QUIC connection does not notify the peer?
- [logos-co/logos-libp2p-module#106](https://github.com/logos-co/logos-libp2p-module/pull/106) fix(tests): find liblibp2p.so, so the integration tests build again
- [logos-co/logos-libp2p-module#107](https://github.com/logos-co/logos-libp2p-module/pull/107) fix(ctx): guard the libp2p context pointer against a concurrent destroy
