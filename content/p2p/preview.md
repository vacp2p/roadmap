---
title: P2P Roadmap Preview
tags:
- p2p
- vac
---

## Roadmap Preview


### 2026Q3 and beyond
- Cross-compilation for mobile
    - Enable nim-libp2p builds for arm64/aarch64 targeting Android/iOS
    - Needed for integration into Status App.
- Connection abstraction refactor
    - The current implementation of nim-libp2p includes abstractions that are difficult to understand, 
      which makes development and collaboration more challenging. 
      Refactoring the codebase would improve clarity, allowing contributors to grasp the code more easily. 
      Additionally, a more streamlined implementation would enhance maintainability, 
      leading to more efficient troubleshooting and debugging.
- Unix Domain Socket transport (`/unix//tmp/foo`)
- Performance & scale
    - Profiling and memory audit: guide future optimizations by identifying bottlenecks and alloc hotspots

#### Uncategorized
The following items are not part of our current roadmap. They haven't been requested by any consumer of nim-libp2p, so they do not have any prioritization status. Still, they are recorded here potential future consideration.

- bluetooth transport
    - [ble exploration by berty](https://berty.tech/fr/blog/bluetooth-low-energy/).
    - Low-power proximity-based connections over BLE, mostly relevant in mobile/offline-first contexts.
    - Not part of libp2p spec rn but has been explored in the ecosystem.
- tls secure transport
    - [spec](https://github.com/libp2p/specs/blob/master/secure-channels/tls.md). 
    - Reuse standard TLS instead of Noise for encryption/auth.
- tls/sni multiaddress support
- webrtc-direct
    - [spec](https://github.com/libp2p/specs/blob/master/webrtc/direct.md). 
    - Connects peers via WebRTC datachannels without signaling servers. 
    - Useful for browser-to-native or p2p-web setups.
    - Available in js/go.
- mdns discovery
    - [spec](https://github.com/libp2p/specs/blob/master/discovery/mdns.md)
    - local network peer discovery using multicast DNS. 
    - Simplifies peer bootstrapping in LANs. 
    - Trivial in theory, might depend on whether there are multicast DNS libraries in nim or having to implement one
- wasm support
    - compile nim-libp2p to a wasm library for embedding in browser environments. 
    - no spec, but precedent exists in js-libp2p and rust efforts.
- native nim impl of Quic
