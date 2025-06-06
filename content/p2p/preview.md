---
title: P2P Roadmap Preview
tags:
- p2p
- vac
---

## Roadmap Preview

### 2025Q3
- Webtransport (HTTP3)
    - Continue implementation; may defer remaining work to Q4 depending on bandwidth.
    - HTTP3 Finalized
    - HTTP3 demands a complete working stack before anything functions - no partial implementation,
      this makes it non trivial and time consuming
- Gossipsub 2.0
    - May continue depending on remaining gaps contingent on prior quarter’s outcomes.
- Kad-DHT 
    - Continue implementation; may defer remaining work to Q4 depending on bandwidth.
- Autonat V2
    - Implement according to [specs](https://github.com/libp2p/specs/blob/master/autonat/autonat-v2.md)
- Maintenance
    - Debug and fix flaky QA tests as well as continue giving support to QA team
    - Remove go-libp2p-daemon usage in examples/tests
    - (This is in addition to other maintenance tasks).
- Mix-core in nim-libp2p as Prototype / Unstable state
    - Usable in PoCs or experiments
    - Rough edges and minor issues expected, not recommended for production
    - API and internal structure subject to changes
- Mix specs in libp2p/specs
    - Upstream initial mix design and rationale to libp2p/spec as proposal or draft PR

### 2025Q4
- WebTransport (finalized)
    - Complete implementation of WebTransport protocol
    - Support WebTransport as a transport option within nim-libp2p
- Kad-DHT
    - May continue depending on remaining gaps contingent on prior quarter’s outcomes.
- Cross-compilation for mobile
    - Enable nim-libp2p builds for arm64/aarch64 targeting Android/iOS
    - Needed for integration into Status App.
- C-bindings
    - Expose stable C API surface for LogosCore and other external consumers. 
- Connection abstraction refactor
    - The current implementation of nim-libp2p includes abstractions that are difficult to understand, 
      which makes development and collaboration more challenging. 
      Refactoring the codebase would improve clarity, allowing contributors to grasp the code more easily. 
      Additionally, a more streamlined implementation would enhance maintainability, 
      leading to more efficient troubleshooting and debugging.
- IPv6 support
    - Full handling of /ip6/... multiaddresses
- Mix-core in nim-libp2p as Done state
    - core protocol logic stable; 
    - no blocking issues
    - Issues (if any) are around API polish
- Maintenance
    - evaluate whether to keep using nim-protobuf-serialization or migrate to minprotobuf
    - (This is in addition to other maintenance tasks).

### 2026Q1 and beyond
- Unix Domain Socket transport (`/unix//tmp/foo`)
- Performance & scale
    - Profiling and memory audit: guide future optimizations by identifying bottlenecks and alloc hotspots
    - Implement zero-copy buffers between layes (transport / protocol / muxer / network libraries)
- Connection management
    - enforce upper bounds on total open connections to prevent fd exhaustion, trim connections to a lower bound
    - tag connections with metadata
    - support protected connections (don’t trim them under pressure)
    - implement exponential dial backoff to avoid peer hammering
- Modular Gossipsub
    - Pluggable GossipSub scoring
    - TODO

#### Uncategorized
The following items are not part of our current roadmap. They haven't been requested by any consumer of nim-libp2p, so they do not have any prioritization status. Still, they are recorded here potential future consideration.

- bluetooth transport
    - [ble exploration by berty](https://berty.tech/fr/blog/bluetooth-low-energy/).
    - Low-power proximity-based connections over BLE, mostly relevant in mobile/offline-first contexts.
    - Not part of libp2p spec rn but has been explored in the ecosystem.
- tls secure transport
    - [spec](https://github.com/libp2p/specs/blob/master/secure-channels/tls.md). 
    - Reuse standard TLS instead of Noise for encryption/auth.
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