---

title: Nim-libp2p maintenance
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users, Nimbus and Waku, as their needs evolve.

## Task List

### Maintenance

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-maintenance:maintenance`
* owner: rramos/vlado/gabe
* status: in progress (51%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Maintain the [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors, and bug fixes.

#### Deliverables
- [vacp2p/nim-libp2p#2941](https://github.com/vacp2p/nim-libp2p/pull/2941) fix(pubsub): initialize RPC handlers before connecting
- [vacp2p/nim-lsquic#153](https://github.com/vacp2p/nim-lsquic/pull/153) fix(connection): report current remote address
- [vacp2p/nim-lsquic#149](https://github.com/vacp2p/nim-lsquic/pull/149) feat(client): pass server name when dialing
- [vacp2p/nim-lsquic#147](https://github.com/vacp2p/nim-lsquic/pull/147) fix(tlsconfig): validate ALPN protocol lengths
- [vacp2p/nim-lsquic#152](https://github.com/vacp2p/nim-lsquic/pull/152) fix(stream): handle peer unidirectional streams
- [vacp2p/nim-libp2p#2925](https://github.com/vacp2p/nim-libp2p/pull/2925) test(quic): pin nim-lsquic close fix
- [vacp2p/nim-lsquic#144](https://github.com/vacp2p/nim-lsquic/pull/144) fix(connection): preserve queued streams after peer close
- [vacp2p/nim-lsquic#129](https://github.com/vacp2p/nim-lsquic/pull/129) feat(benchmarks): error handling, resource-usage capture, refreshed docs
- [vacp2p/nim-libp2p#2923](https://github.com/vacp2p/nim-libp2p/pull/2923) feat: v2.3.0
- [vacp2p/nim-libp2p#2926](https://github.com/vacp2p/nim-libp2p/pull/2926) ci: change log lvl
- [logos-storage/nim-libplum#18](https://github.com/logos-storage/nim-libplum/pull/18) fix: add missing libplum_units.c
- [vacp2p/nim-libp2p#2932](https://github.com/vacp2p/nim-libp2p/pull/2932) chore(nat): bump libplum to v0.6.2
- [vacp2p/nim-libp2p#2940](https://github.com/vacp2p/nim-libp2p/pull/2940) fix(peerstore): bound the identify stream close
- [vacp2p/nim-libp2p#2929](https://github.com/vacp2p/nim-libp2p/pull/2929) fix(dialer): bound outbound dials so one stuck peer cannot stall the node
- [logos-co/logos-libp2p-module#101](https://github.com/logos-co/logos-libp2p-module/pull/101) fix(gossipsub): bound the per-topic message queue and expose the ingress limits
- [logos-co/logos-libp2p-module#99](https://github.com/logos-co/logos-libp2p-module/pull/99) fix(service-disco): advertise a caller-supplied XPR
- [vacp2p/nim-libp2p#2919](https://github.com/vacp2p/nim-libp2p/pull/2919) feat(cbind): expose the GossipSub ingress limits in Libp2pConfig
- [vacp2p/nim-libp2p#2917](https://github.com/vacp2p/nim-libp2p/pull/2917) fix(service-disco): let a caller advertise a full XPR
- [vacp2p/nim-libp2p#2913](https://github.com/vacp2p/nim-libp2p/pull/2913) chore(cbind): change procs to static
- [vacp2p/nim-libp2p#2915](https://github.com/vacp2p/nim-libp2p/pull/2915) refactor(nat): a ReachabilityObservers store for reachability subscribers
- [status-im/nimbus-eth2#8836](https://github.com/status-im/nimbus-eth2/pull/8836) feat: bump lsquic to v0.8.0
- [vacp2p/nim-lsquic#132](https://github.com/vacp2p/nim-lsquic/pull/132) perf: reuse a stack WSABUF and heap-fall-back on the Windows send path
- [vacp2p/nim-lsquic#131](https://github.com/vacp2p/nim-lsquic/pull/131) perf: compare address families directly in prepareDestAddr
- [vacp2p/nim-lsquic#133](https://github.com/vacp2p/nim-lsquic/pull/133) perf: skip CID routing and the sockaddr bounce buffer on the packet-in path
- [vacp2p/nim-lsquic#125](https://github.com/vacp2p/nim-lsquic/pull/125) perf: settle pending stream operations on close instead of racing
- [vacp2p/nim-lsquic#124](https://github.com/vacp2p/nim-lsquic/pull/124) perf: add a pointer overload for stream writes
- [vacp2p/nim-lsquic#123](https://github.com/vacp2p/nim-lsquic/pull/123) perf: take stream write payloads as sink
- [vacp2p/nim-lsquic#121](https://github.com/vacp2p/nim-lsquic/pull/121) perf: coalesce engine ticks, gated on write size
- [vacp2p/nim-lsquic#120](https://github.com/vacp2p/nim-lsquic/pull/120) perf: stop copying 64KB per receive wakeup under arc/orc
- [status-im/nimbus-eth2#8811](https://github.com/status-im/nimbus-eth2/pull/8811) chore: bump lsquic and boringssl
- [vacp2p/nim-lsquic#117](https://github.com/vacp2p/nim-lsquic/pull/117) perf: drain the UDP socket per wakeup instead of ticking per datagram
- [vacp2p/nim-libp2p#2889](https://github.com/vacp2p/nim-libp2p/pull/2889) chore: bump lsquic
- [vacp2p/nim-lsquic#111](https://github.com/vacp2p/nim-lsquic/pull/111) feat: configure UDP receive buffer size
- [vacp2p/nim-lsquic#110](https://github.com/vacp2p/nim-lsquic/pull/110) feat: add back `sendmmsg`
- [vacp2p/nim-lsquic#109](https://github.com/vacp2p/nim-lsquic/pull/109) fix: avoid copying inbound UDP datagrams
- [litespeedtech/lsquic#670](https://github.com/litespeedtech/lsquic/pull/670) fix: MinGW build compatibility
- [vacp2p/nim-libp2p#2900](https://github.com/vacp2p/nim-libp2p/pull/2900) refactor(pubsub): use protobuf proto editions
- [vacp2p/nim-libp2p#2884](https://github.com/vacp2p/nim-libp2p/pull/2884) feat(cbind): nat config
- [vacp2p/nim-libp2p#2892](https://github.com/vacp2p/nim-libp2p/pull/2892) ci: cache improvements
- [vacp2p/nim-libp2p#2894](https://github.com/vacp2p/nim-libp2p/pull/2894) chore(make): format .nimble files
- [vacp2p/nim-libp2p#2895](https://github.com/vacp2p/nim-libp2p/pull/2895) chore(.gitignore): cleanup
- [vacp2p/nim-libp2p#2905](https://github.com/vacp2p/nim-libp2p/pull/2905) fix(test): guard the logging test on a dynamic chronicles sink
- [libp2p/py-libp2p#1407](https://github.com/libp2p/py-libp2p/pull/1407) fix(pubsub): disconnect hygiene and once-per-subscription mcache replay
- [vacp2p/nim-libp2p#2897](https://github.com/vacp2p/nim-libp2p/pull/2897) test(kad): import tables in the find test
- [vacp2p/nim-libp2p#2883](https://github.com/vacp2p/nim-libp2p/pull/2883) feat(cbind): dial with addrs
- [vacp2p/nim-libp2p#2881](https://github.com/vacp2p/nim-libp2p/pull/2881) ci: harden workflow permissions
- [logos-co/logos-libp2p-module#88](https://github.com/logos-co/logos-libp2p-module/pull/88) chore: harden CI workflow permissions
- [vacp2p/nim-libp2p#2876](https://github.com/vacp2p/nim-libp2p/pull/2876) ci: composite actions for dependencies
- [vacp2p/nim-libp2p#2874](https://github.com/vacp2p/nim-libp2p/pull/2874) ci: fix dependnecies cache keys
- [vacp2p/nim-libp2p#2873](https://github.com/vacp2p/nim-libp2p/pull/2873) chore(deps): bump nimble to v0.24.1
- [vacp2p/nim-libp2p#2867](https://github.com/vacp2p/nim-libp2p/pull/2867) chore(tests): use `await` insted of `waitFor`
- [vacp2p/nim-libp2p#2844](https://github.com/vacp2p/nim-libp2p/pull/2844) fix(kad): avoid advertising ephemeral peer addresses
- [vacp2p/nim-libp2p#2843](https://github.com/vacp2p/nim-libp2p/pull/2843) chore: print selected platform in test_multiformat_exts
- [vacp2p/nim-libp2p#2838](https://github.com/vacp2p/nim-libp2p/pull/2838) fix(dcutr): preserve QUIC server role during hole punching
- [vacp2p/nim-libp2p#2837](https://github.com/vacp2p/nim-libp2p/pull/2837) fix(quic): propagate accept errors instead of nil
- [vacp2p/nim-libp2p#2830](https://github.com/vacp2p/nim-libp2p/pull/2830) fix: avoid unused allFinished copies
- [vacp2p/nim-libp2p#2836](https://github.com/vacp2p/nim-libp2p/pull/2836) fix(ci): daily workflow job names
- [vacp2p/nim-boringssl#13](https://github.com/vacp2p/nim-boringssl/pull/13) chore: remove natlibs
- [vacp2p/nim-libp2p#2828](https://github.com/vacp2p/nim-libp2p/pull/2828) fix(dialer): reset streams after failed protocol negotiation
- [vacp2p/nim-lsquic#99](https://github.com/vacp2p/nim-lsquic/pull/99) fix: close QUIC streams after receiving FIN
- [status-im/nimbus-eth2#8756](https://github.com/status-im/nimbus-eth2/pull/8756) chore: bump libp2p to 2.1.5
- [vacp2p/nim-libp2p#2823](https://github.com/vacp2p/nim-libp2p/pull/2823) fix(service-discovery): drain bootstrap futures on shutdown
- [vacp2p/nim-libp2p#2819](https://github.com/vacp2p/nim-libp2p/pull/2819) chore(builders): disable IdentifyPusher by default
- [vacp2p/nim-libp2p#2815](https://github.com/vacp2p/nim-libp2p/pull/2815) fix(gossipsub): concurrent peers table access during topic unsubscribe
- [vacp2p/nim-libp2p#2829](https://github.com/vacp2p/nim-libp2p/pull/2829) fix(ci): ignore missing sources in coverage genhtml
- [vacp2p/nim-libp2p#2605](https://github.com/vacp2p/nim-libp2p/pull/2605) fix: track and cancel asyncSpawn-ed futures on teardown
- [vacp2p/nim-libp2p#2803](https://github.com/vacp2p/nim-libp2p/pull/2803) ci: drop i386_temp workflow
- [vacp2p/nim-libp2p#2808](https://github.com/vacp2p/nim-libp2p/pull/2808) fix(ci): stop dcutr test leaking a channel; run full daily CI on label
- [vacp2p/nim-libp2p#2770](https://github.com/vacp2p/nim-libp2p/pull/2770) chore: add issue and feature templates
- [vacp2p/nim-libp2p#2807](https://github.com/vacp2p/nim-libp2p/pull/2807) fix(routing-record): use proto3 peer record encoding
- [vacp2p/nim-libp2p#2789](https://github.com/vacp2p/nim-libp2p/pull/2789) fix(protobuf): tolerate empty custom fields
- [vacp2p/nim-libp2p#2790](https://github.com/vacp2p/nim-libp2p/pull/2790) fix(autonat): optional msgType and status fields
- [vacp2p/nim-libp2p#2785](https://github.com/vacp2p/nim-libp2p/pull/2785) chore(relay)!: make v1 hop opt-in
- [vacp2p/nim-libp2p#2801](https://github.com/vacp2p/nim-libp2p/pull/2801) test: fix flakines with "client-mode node successfully completes lookup against server-mode registrars"
- [vacp2p/nim-libp2p#2795](https://github.com/vacp2p/nim-libp2p/pull/2795) ci: single file for daily test_all workflow
- [vacp2p/nim-libp2p#2794](https://github.com/vacp2p/nim-libp2p/pull/2794) feat(tests): tests as subproject of repo
- [vacp2p/nim-libp2p#2804](https://github.com/vacp2p/nim-libp2p/pull/2804) chore(cbind): change dep commit
- [vacp2p/nim-libp2p#2797](https://github.com/vacp2p/nim-libp2p/pull/2797) ci: dropping i386 orc from tests
- [vacp2p/nim-libp2p#2792](https://github.com/vacp2p/nim-libp2p/pull/2792) chore(makefile): simplify code
- [vacp2p/nim-libp2p#2791](https://github.com/vacp2p/nim-libp2p/pull/2791) ci: save build cache when in merge queue
- [vacp2p/nim-libp2p#2788](https://github.com/vacp2p/nim-libp2p/pull/2788) fix(kademlia): align DHT message and provider limits for interop
- [vacp2p/nim-libp2p#2787](https://github.com/vacp2p/nim-libp2p/pull/2787) fix(yamux): align default window with spec and reject invalid versions
- [vacp2p/nim-libp2p#2765](https://github.com/vacp2p/nim-libp2p/pull/2765) fix(memory-transport): serialize concurrent writes
- [vacp2p/nim-libp2p#2761](https://github.com/vacp2p/nim-libp2p/pull/2761) test(mplex): make tests teardown more robust
- [vacp2p/nim-libp2p#2764](https://github.com/vacp2p/nim-libp2p/pull/2764) test(autonat): fix flaky test "Peer must be not reachable and then reachable"
- [vacp2p/nim-libp2p#2767](https://github.com/vacp2p/nim-libp2p/pull/2767) ci(daily-report): add runnable examples to report
- [vacp2p/nim-libp2p#2762](https://github.com/vacp2p/nim-libp2p/pull/2762) test(dcutr): better synchronisation and assertion for "DCUtR establishes a new QUIC connection"
- [vacp2p/nim-libp2p#2766](https://github.com/vacp2p/nim-libp2p/pull/2766) ci: use macos for "Daily without feature flags" workflow
- [vacp2p/nim-libp2p#2769](https://github.com/vacp2p/nim-libp2p/pull/2769) ci: add merge_group
- [logos-co/nim-libp2p-mix#25](https://github.com/logos-co/nim-libp2p-mix/pull/25) fix(mix): limit replay cache and defer tag insertion
- [vacp2p/nim-libp2p#2752](https://github.com/vacp2p/nim-libp2p/pull/2752) ci: dropping daily pinned
- [vacp2p/nim-libp2p#2754](https://github.com/vacp2p/nim-libp2p/pull/2754) test: remove unnecessary test that takes too much time
- [status-im/nimbus-eth2#8701](https://github.com/status-im/nimbus-eth2/pull/8701) chore: bump libp2p to 2.1.4
- [vacp2p/nim-libp2p#2751](https://github.com/vacp2p/nim-libp2p/pull/2751) fix: avoid deadlock when dropping peers from stream handler
- [status-im/nimbus-eth2#8699](https://github.com/status-im/nimbus-eth2/pull/8699) chore: bump libp2p to 2.1.3
- [vacp2p/nim-libp2p#2745](https://github.com/vacp2p/nim-libp2p/pull/2745) test(pubsub): cover stale peer cleanup after dropped connection
- [vacp2p/nim-boringssl#11](https://github.com/vacp2p/nim-boringssl/pull/11) chore(ci): test PR against nim-libp2p and nim-lsquic
- [vacp2p/nim-libp2p#2737](https://github.com/vacp2p/nim-libp2p/pull/2737) fix(connmanager): avoid late Joined after peer drop
- [vacp2p/nim-libp2p#2734](https://github.com/vacp2p/nim-libp2p/pull/2734) fix(peerstore): keep connected peer addresses from expiring
- [vacp2p/nim-libp2p#2729](https://github.com/vacp2p/nim-libp2p/pull/2729) fix(pubsub): avoid sink params for small RPC fields
- [vacp2p/nim-libp2p#2716](https://github.com/vacp2p/nim-libp2p/pull/2716) feat(ci): allow selecting nim-libp2p ref for dependency bumps and disabling scheduled run
- [vacp2p/nim-libp2p#2719](https://github.com/vacp2p/nim-libp2p/pull/2719) fix(autotls): decouple ACME RSA keys from libp2p identity schemes
- [status-im/nimbus-eth2#8536](https://github.com/status-im/nimbus-eth2/pull/8536) chore: bump libp2p to 2.1.2
- [vacp2p/nim-libp2p#2699](https://github.com/vacp2p/nim-libp2p/pull/2699) fix(autotls): release certificate keys after CSR generation
- [vacp2p/boringssl#6](https://github.com/vacp2p/boringssl/pull/6) chore: sync BoringSSL upstream
- [vacp2p/nim-lsquic#96](https://github.com/vacp2p/nim-lsquic/pull/96) fix: leaks
- [vacp2p/nim-libp2p#2687](https://github.com/vacp2p/nim-libp2p/pull/2687) fix(tests): remove chronicles import hacks
- [vacp2p/nim-libp2p#2693](https://github.com/vacp2p/nim-libp2p/pull/2693) chore(ci): add mm to the job names
- [vacp2p/nim-libp2p#2647](https://github.com/vacp2p/nim-libp2p/pull/2647) chore(pubsub): adjust incoming message validation order
- [vacp2p/nim-libp2p#2670](https://github.com/vacp2p/nim-libp2p/pull/2670) fix(connmanager): emit Joined before trimming new peers
- [vacp2p/nim-libp2p#2742](https://github.com/vacp2p/nim-libp2p/pull/2742) test: utilize new switch builder with multiple addresses
- [vacp2p/nim-libp2p#2740](https://github.com/vacp2p/nim-libp2p/pull/2740) fix(test): use captured variable for closure
- [vacp2p/nim-libp2p#2724](https://github.com/vacp2p/nim-libp2p/pull/2724) fix(gossipsub): sending duplicate IHAVE
- [vacp2p/nim-libp2p#2739](https://github.com/vacp2p/nim-libp2p/pull/2739) ci(daily): remove concurrent test job
- [vacp2p/nim-libp2p#2728](https://github.com/vacp2p/nim-libp2p/pull/2728) ci: avoiding cache for trivial jobs
- [vacp2p/nim-libp2p#2730](https://github.com/vacp2p/nim-libp2p/pull/2730) ci: only save build cache on master
- [vacp2p/nim-libp2p#2721](https://github.com/vacp2p/nim-libp2p/pull/2721) ci: force save build cache
- [vacp2p/nim-libp2p#2707](https://github.com/vacp2p/nim-libp2p/pull/2707) ci: add line trace
- [vacp2p/nim-libp2p#2715](https://github.com/vacp2p/nim-libp2p/pull/2715) ci: add build cache to workflows
- [vacp2p/nim-libp2p#2709](https://github.com/vacp2p/nim-libp2p/pull/2709) ci: rework test workflow
- [vacp2p/nim-libp2p#2747](https://github.com/vacp2p/nim-libp2p/pull/2747) chore(readme): update badge link of test workflow
- [vacp2p/nim-libp2p#2743](https://github.com/vacp2p/nim-libp2p/pull/2743) ci: add build prerequisites to daily with no flags
- [vacp2p/nim-libp2p#2738](https://github.com/vacp2p/nim-libp2p/pull/2738) ci: force save cache
- [vacp2p/nim-libp2p#2701](https://github.com/vacp2p/nim-libp2p/pull/2701) ci: i386 temp workflow
