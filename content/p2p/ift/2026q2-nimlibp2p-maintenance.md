---

title: Nim-libp2p maintenance
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users, Nimbus and Waku, as their needs evolve.

## Task List

### Maintenance

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:maintenance`
* owner: rramos
* status: in progress (82%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Maintain the [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors, and bug fixes.

#### Deliverables
- [vacp2p/nim-libp2p#2307](https://github.com/vacp2p/nim-libp2p/pull/2307) chore(copilot): add more instructions
- [vacp2p/nim-libp2p#2331](https://github.com/vacp2p/nim-libp2p/pull/2331) fix(floodsub): increase timeout for large message transfer in FloodSub message size validation 2
- [vacp2p/nim-lsquic#83](https://github.com/vacp2p/nim-lsquic/pull/83) fix: shutdown and stream lifecycle handling
- [vacp2p/nim-libp2p#2312](https://github.com/vacp2p/nim-libp2p/pull/2312) chore: bump deps
- [vacp2p/nim-libp2p#2309](https://github.com/vacp2p/nim-libp2p/pull/2309) chore: use latest deps used on projects instead of just the latest deps
- [vacp2p/nim-lsquic#81](https://github.com/vacp2p/nim-lsquic/pull/81) feat: StreamReset
- [vacp2p/nim-libp2p#2304](https://github.com/vacp2p/nim-libp2p/pull/2304) fix(ci): new delete action cache job
- [vacp2p/nim-lsquic#79](https://github.com/vacp2p/nim-lsquic/pull/79) feat: benchmarks
- [vacp2p/nim-lsquic#78](https://github.com/vacp2p/nim-lsquic/pull/78) fix: call engine_process synchronously if possible, otherwise defer to ticker event loop
- [vacp2p/nim-libp2p#2244](https://github.com/vacp2p/nim-libp2p/pull/2244) chore: remove unused ngtcp2 dependency from pinned list
- [vacp2p/nim-libp2p#2235](https://github.com/vacp2p/nim-libp2p/pull/2235) chore: update CI timeouts
- [vacp2p/nim-libp2p#2228](https://github.com/vacp2p/nim-libp2p/pull/2228) fix(mix): avoid creation of random
- [vacp2p/nim-libp2p#2227](https://github.com/vacp2p/nim-libp2p/pull/2227) chore: change the run schedule of Daily i386 job
- [vacp2p/nim-libp2p#2226](https://github.com/vacp2p/nim-libp2p/pull/2226) refactor(mix): add `Delay` type
- [vacp2p/nim-libp2p#2221](https://github.com/vacp2p/nim-libp2p/pull/2221) chore(ai): add copilot instructions to avoid sleepAsync
- [vacp2p/nim-libp2p#2219](https://github.com/vacp2p/nim-libp2p/pull/2219) chore(ci): remove discord notify
- [vacp2p/nim-libp2p#2216](https://github.com/vacp2p/nim-libp2p/pull/2216) fix: nil pointer dereference issues caused when sha256 is used in ref object
- [vacp2p/nim-libp2p#2214](https://github.com/vacp2p/nim-libp2p/pull/2214) fix(ci): make daily jobs setup consistent with ci.yml
- [vacp2p/nim-libp2p#2211](https://github.com/vacp2p/nim-libp2p/pull/2211) chore(test): utilize rng() template
- [vacp2p/nim-libp2p#2197](https://github.com/vacp2p/nim-libp2p/pull/2197) chore: reduce log level for noisy "too many channels created" log
- [vacp2p/nim-libp2p#2056](https://github.com/vacp2p/nim-libp2p/pull/2056) chore: remove semaphore
- [vacp2p/nim-libp2p#2294](https://github.com/vacp2p/nim-libp2p/pull/2294) feat: network simulation
- [vacp2p/nim-libp2p#2286](https://github.com/vacp2p/nim-libp2p/pull/2286) feat(builder): `withPrivateAddressFilter`
- [vacp2p/nim-libp2p#2279](https://github.com/vacp2p/nim-libp2p/pull/2279) chore(deps): use lsquic nimble package
- [nim-lang/packages#3326](https://github.com/nim-lang/packages/pull/3326) Add lsquic package to `packages.json`
- [vacp2p/nim-libp2p#2298](https://github.com/vacp2p/nim-libp2p/pull/2298) chore: add code formatting guidelines to instructions
- [vacp2p/nim-libp2p#2277](https://github.com/vacp2p/nim-libp2p/pull/2277) chore: update API stability and experimental extensions section
- [vacp2p/nim-libp2p#2272](https://github.com/vacp2p/nim-libp2p/pull/2272) fix(mix): track and cancel handleMixMessages futures
- [vacp2p/nim-libp2p#2255](https://github.com/vacp2p/nim-libp2p/pull/2255) test(mix): fix flaky test "rate limit exceeded - message rejected at intermediate node"
- [vacp2p/nim-libp2p#2259](https://github.com/vacp2p/nim-libp2p/pull/2259) test(gossipsub): fix flaky test when peers should be dropped in same heartbeat as publish
- [vacp2p/nim-libp2p#2263](https://github.com/vacp2p/nim-libp2p/pull/2263) test(transports): fix flaky test "server writes after EOF"
- [vacp2p/nim-libp2p#2271](https://github.com/vacp2p/nim-libp2p/pull/2271) fix: add asyncSleep before dial in "mount unstarted protocol" test to fix Windows flakiness
- [vacp2p/nim-libp2p#2273](https://github.com/vacp2p/nim-libp2p/pull/2273) test(transports): replace sleepAsync with write loop in "server writes after EOF"
- [vacp2p/nim-libp2p#2289](https://github.com/vacp2p/nim-libp2p/pull/2289) fix(gossipsub): flaky scoring test
- [vacp2p/nim-libp2p#2262](https://github.com/vacp2p/nim-libp2p/pull/2262) fix(autotls): letsencrypt challenge type change
- [vacp2p/nim-libp2p#2266](https://github.com/vacp2p/nim-libp2p/pull/2266) fix(bump): waku vendor init failing
- [logos-messaging/logos-delivery#3812](https://github.com/logos-messaging/logos-delivery/pull/3812) chore: bump nim-jwt version
- [vacp2p/nim-libp2p#2295](https://github.com/vacp2p/nim-libp2p/pull/2295) feat: extend libp2p_network_bytes and agents traffic metrics to all transports
- [vacp2p/nim-libp2p#2293](https://github.com/vacp2p/nim-libp2p/pull/2293) chore: bump nph to v0.7.0
- [vacp2p/nim-libp2p#2297](https://github.com/vacp2p/nim-libp2p/pull/2297) chore: update copilot instructions to reflect latest repository state
- [vacp2p/nim-libp2p#2370](https://github.com/vacp2p/nim-libp2p/pull/2370) fix(pubsub): track pending sends without adding backpressure
- [vacp2p/nim-libp2p#2368](https://github.com/vacp2p/nim-libp2p/pull/2368) feat(pubsub): reduce publish-time message copies with sink
- [status-im/nimbus-eth2#7775](https://github.com/status-im/nimbus-eth2/pull/7775) feat: quic transport support
- [vacp2p/nim-libp2p#2283](https://github.com/vacp2p/nim-libp2p/pull/2283) feat: reset stream
- [vacp2p/nim-libp2p#2390](https://github.com/vacp2p/nim-libp2p/pull/2390) refactor: unify default DNS servers under dnsresolver
- [vacp2p/nim-libp2p#2376](https://github.com/vacp2p/nim-libp2p/pull/2376) fix: prevent GossipSub from relaying messages back to original source
- [vacp2p/nim-libp2p#2374](https://github.com/vacp2p/nim-libp2p/pull/2374) fix: truncated `identify: decoded message` log due to unbounded address list
- [vacp2p/nim-libp2p#2377](https://github.com/vacp2p/nim-libp2p/pull/2377) chore: move interop ignore items to their own gitignore
- [vacp2p/nim-libp2p#2379](https://github.com/vacp2p/nim-libp2p/pull/2379) fix: replace generic `payload` log key with descriptive names in pubsub
- [vacp2p/nim-libp2p#2375](https://github.com/vacp2p/nim-libp2p/pull/2375) chore: add clang-format linter for cbind/ C code
- [vacp2p/nim-libp2p#2389](https://github.com/vacp2p/nim-libp2p/pull/2389) fix: propagate shortAgent through wrapped connection chain to restore peer metrics
- [vacp2p/nim-libp2p#2365](https://github.com/vacp2p/nim-libp2p/pull/2365) chore: removing `.public.` pragma
- [vacp2p/nim-libp2p#2366](https://github.com/vacp2p/nim-libp2p/pull/2366) chore: removing deprecated things
- [vacp2p/nim-libp2p#2386](https://github.com/vacp2p/nim-libp2p/pull/2386) chore(readme): license cosmetics
- [vacp2p/nim-libp2p#2382](https://github.com/vacp2p/nim-libp2p/pull/2382) docs: add new items to navigation and reminder
- [vacp2p/nim-libp2p#2381](https://github.com/vacp2p/nim-libp2p/pull/2381) ci(docs): use stable nim version
- [vacp2p/nim-libp2p#2347](https://github.com/vacp2p/nim-libp2p/pull/2347) ci: add timeout for `coverage` workflow
- [vacp2p/nim-libp2p#2355](https://github.com/vacp2p/nim-libp2p/pull/2355) chore: remove runAfter
- [vacp2p/nim-libp2p#2399](https://github.com/vacp2p/nim-libp2p/pull/2399) fix(ci): codecov test clashing T type
- [vacp2p/nim-libp2p#2360](https://github.com/vacp2p/nim-libp2p/pull/2360) fix(muxer): accept loop stuck
- [vacp2p/nim-libp2p#2380](https://github.com/vacp2p/nim-libp2p/pull/2380) fix(ci): failing on nim < 2.2.6
- [vacp2p/nim-libp2p#2428](https://github.com/vacp2p/nim-libp2p/pull/2428) chore(MultiAddress): memory optimization
- [vacp2p/nim-libp2p#2418](https://github.com/vacp2p/nim-libp2p/pull/2418) chore(identify): cosmetics improvement
- [vacp2p/nim-libp2p#2414](https://github.com/vacp2p/nim-libp2p/pull/2414) test: stabilize flaky `Heartbeat::catch up on slow heartbeat` timing assertion
- [vacp2p/nim-libp2p#2423](https://github.com/vacp2p/nim-libp2p/pull/2423) test(websocket): stabilize WebSocket EOF write assertion in stream transport tests
- [vacp2p/nim-libp2p#2447](https://github.com/vacp2p/nim-libp2p/pull/2447) test: drop `untilTimeout` and standardize on `checkUntilTimeout`
- [vacp2p/nim-libp2p#2445](https://github.com/vacp2p/nim-libp2p/pull/2445) test: fix flaky service-discovery test for two advertisers on one service
- [vacp2p/nim-libp2p#2442](https://github.com/vacp2p/nim-libp2p/pull/2442) chore: drop `newStandardSwitch` and `newStandardSwitchBuilder` from public API
- [vacp2p/nim-libp2p#2407](https://github.com/vacp2p/nim-libp2p/pull/2407) fix(daily): cover traffic leaking channels
- [vacp2p/nim-libp2p#2410](https://github.com/vacp2p/nim-libp2p/pull/2410) fix(autotls): withAutotls independent ordering
- [vacp2p/nim-libp2p#2396](https://github.com/vacp2p/nim-libp2p/pull/2396) chore: remove old nim hacks
- [vacp2p/nim-libp2p#2459](https://github.com/vacp2p/nim-libp2p/pull/2459) fix(peerstore): reset identify stream on cancellation
- [vacp2p/nim-libp2p#2465](https://github.com/vacp2p/nim-libp2p/pull/2465) chore(deps): bump nim-websock to >= 0.4.0
- [status-im/nim-websock#195](https://github.com/status-im/nim-websock/pull/195) 0.4.0
- [vacp2p/boringssl#2](https://github.com/vacp2p/boringssl/pull/2) chore: sync BoringSSL upstream
- [vacp2p/nim-libp2p#2462](https://github.com/vacp2p/nim-libp2p/pull/2462) refactor(Switch): Service lifecycle
- [vacp2p/nim-libp2p#2466](https://github.com/vacp2p/nim-libp2p/pull/2466) chore(SwitchBuilder): `build()` proc cleanup
- [vacp2p/nim-libp2p#2473](https://github.com/vacp2p/nim-libp2p/pull/2473) chore(PeerInfo): cosmetics
- [vacp2p/nim-libp2p#2472](https://github.com/vacp2p/nim-libp2p/pull/2472) test(Noise): cosmetics
- [vacp2p/nim-libp2p#2451](https://github.com/vacp2p/nim-libp2p/pull/2451) chore: utilize `cancelAndWait` template
- [vacp2p/nim-libp2p#2456](https://github.com/vacp2p/nim-libp2p/pull/2456) test: stabilize `Switch::e2e max outgoing connection limits` by forcing TCP transport
- [vacp2p/nim-libp2p#2453](https://github.com/vacp2p/nim-libp2p/pull/2453) test: simplify `makeStandardSwitch` and `makeStandardSwitchBuilder`
- [vacp2p/nim-libp2p#2454](https://github.com/vacp2p/nim-libp2p/pull/2454) chore: makefile instead of nimble
- [vacp2p/nim-libp2p#2433](https://github.com/vacp2p/nim-libp2p/pull/2433) fix(ci): add skip to autotls integration tests
- [vacp2p/nim-libp2p#2495](https://github.com/vacp2p/nim-libp2p/pull/2495) fix(cancellation): preserve `CancelledError` in handlers
- [vacp2p/nim-lsquic#85](https://github.com/vacp2p/nim-lsquic/pull/85) chore: bump lsquic
- [vacp2p/nim-libp2p#2482](https://github.com/vacp2p/nim-libp2p/pull/2482) chore: better names for streams and connections
- [vacp2p/nim-boringssl#5](https://github.com/vacp2p/nim-boringssl/pull/5) chore: update BoringSSL submodule and bindings
- [vacp2p/boringssl#3](https://github.com/vacp2p/boringssl/pull/3) chore: sync BoringSSL upstream
- [vacp2p/nim-libp2p#2506](https://github.com/vacp2p/nim-libp2p/pull/2506) chore: remove implicit `result` variable usage across libp2p source
- [vacp2p/nim-libp2p#2518](https://github.com/vacp2p/nim-libp2p/pull/2518) chore: remove remaining `result` keyword usage
- [vacp2p/nim-libp2p#2497](https://github.com/vacp2p/nim-libp2p/pull/2497) fix(autotls): parsing failed due to missing enum value
- [vacp2p/nim-libp2p#2519](https://github.com/vacp2p/nim-libp2p/pull/2519) fix(autotls): avoid `dns-persist-01` challenge and raise api errors
- [vacp2p/nim-libp2p#2507](https://github.com/vacp2p/nim-libp2p/pull/2507) chore(readme): add Mix Protocol to project list
- [vacp2p/nim-libp2p#2498](https://github.com/vacp2p/nim-libp2p/pull/2498) chore(ai): add instruction for perserving error message
- [vacp2p/nim-libp2p#2486](https://github.com/vacp2p/nim-libp2p/pull/2486) chore(SwitchBuilder): gracePeriod disabled by default
- [vacp2p/nim-libp2p#2475](https://github.com/vacp2p/nim-libp2p/pull/2475) chore(SwitchBuilder): drop `withServices`
- [vacp2p/nim-libp2p#2476](https://github.com/vacp2p/nim-libp2p/pull/2476) chore(SwitchBuilder): avoid braking building chain
- [vacp2p/nim-libp2p#2481](https://github.com/vacp2p/nim-libp2p/pull/2481) chore(ci): unify dependency cache keys across workflows
- [vacp2p/nim-libp2p#2471](https://github.com/vacp2p/nim-libp2p/pull/2471) fix(websocket): avoid asyncSpawn
- [vacp2p/nim-libp2p#2548](https://github.com/vacp2p/nim-libp2p/pull/2548) chore: harden ZeroQueue edge cases
- [vacp2p/nim-libp2p#2567](https://github.com/vacp2p/nim-libp2p/pull/2567) fix(quic): harden certificate parsing and peer verification
- [vacp2p/nim-lsquic#86](https://github.com/vacp2p/nim-lsquic/pull/86) fix: handle closed accepts and client redials
- [vacp2p/nim-libp2p#2562](https://github.com/vacp2p/nim-libp2p/pull/2562) fix(hpservice): stop autorelay with hole punching service
- [vacp2p/nim-libp2p#2553](https://github.com/vacp2p/nim-libp2p/pull/2553) fix(ping): keep inbound ping streams reusable
- [vacp2p/nim-libp2p#2549](https://github.com/vacp2p/nim-libp2p/pull/2549) fix: avoid nim range-backed integer types
- [vacp2p/nim-libp2p#2546](https://github.com/vacp2p/nim-libp2p/pull/2546) fix(multiaddress): onion size and DNS/IP consistency
- [vacp2p/nim-libp2p#2545](https://github.com/vacp2p/nim-libp2p/pull/2545) fix(peerinfo): wrap peer ID initialization errors
- [vacp2p/nim-libp2p#2547](https://github.com/vacp2p/nim-libp2p/pull/2547) fix(SwitchBuilder): initialization of services dependent of Rng
- [vacp2p/nim-libp2p#2550](https://github.com/vacp2p/nim-libp2p/pull/2550) refactor(dial): keep low-level dial APIs off Dial interface
- [vacp2p/nim-libp2p#2552](https://github.com/vacp2p/nim-libp2p/pull/2552) chore: remove standard_switch.nim
- [vacp2p/nim-libp2p#2527](https://github.com/vacp2p/nim-libp2p/pull/2527) feat: v2.0.0
- [vacp2p/nim-libp2p#2569](https://github.com/vacp2p/nim-libp2p/pull/2569) fix(PartialMessage): handle messages if requested partial for topic
- [vacp2p/nim-libp2p#2543](https://github.com/vacp2p/nim-libp2p/pull/2543) chore(future): add completeOnce template
- [vacp2p/nim-libp2p#2531](https://github.com/vacp2p/nim-libp2p/pull/2531) chore: more standard builders
- [vacp2p/nim-libp2p#2530](https://github.com/vacp2p/nim-libp2p/pull/2530) test(tools): adding multiaddress tools
- [vacp2p/nim-libp2p#2525](https://github.com/vacp2p/nim-libp2p/pull/2525) chore(MultistreamSelect): handle cosmetics
- [status-im/nim-style-guide#33](https://github.com/status-im/nim-style-guide/pull/33) add compiler page
- [vacp2p/nim-libp2p#2556](https://github.com/vacp2p/nim-libp2p/pull/2556) chore(autotls): remove libp2p_autotls_support flag
- [vacp2p/nim-libp2p#2536](https://github.com/vacp2p/nim-libp2p/pull/2536) chore: replace unmaintained dnsclient with internal DNS codec
- [vacp2p/nim-libp2p#2534](https://github.com/vacp2p/nim-libp2p/pull/2534) chore(autotls): encapsulate broker interaction behind AutotlsBroker
- [vacp2p/nim-libp2p#2539](https://github.com/vacp2p/nim-libp2p/pull/2539) chore: replace nim-jwt with internal JWS signer
- [vacp2p/nim-libp2p#2538](https://github.com/vacp2p/nim-libp2p/pull/2538) chore: unify and dedup utilities
- [vacp2p/nim-libp2p#2535](https://github.com/vacp2p/nim-libp2p/pull/2535) chore(builders): avoid ref objects for SwitchBuilder configs
- [vacp2p/nim-libp2p#2537](https://github.com/vacp2p/nim-libp2p/pull/2537) chore: remove Nim <2 leftovers (unsafeAddr, newSeqUninit shim)
- [nim-libp2p v2.0.0](https://github.com/vacp2p/nim-libp2p/releases/tag/v2.0.0) Release with connection manager, service discovery, expanded C bindings, GossipSub, Kademlia, NAT, Identify, and transport upgrades
- [vacp2p/nim-libp2p#2587](https://github.com/vacp2p/nim-libp2p/pull/2587) Support QUIC hole punching
- [vacp2p/nim-libp2p#2598](https://github.com/vacp2p/nim-libp2p/pull/2598) Support CIDv1 peer IDs
- [vacp2p/nim-lsquic#89](https://github.com/vacp2p/nim-lsquic/pull/89) Route shared-socket QUIC packets by destination CID
- [vacp2p/nim-lsquic#87](https://github.com/vacp2p/nim-lsquic/pull/87) Add shared socket endpoint
- [vacp2p/nim-lsquic#88](https://github.com/vacp2p/nim-lsquic/pull/88) Map enums manually
- [vacp2p/nim-boringssl#7](https://github.com/vacp2p/nim-boringssl/pull/7) Avoid automatic mapping for `ptr_diff` and enums
- [vacp2p/nim-libp2p#2593](https://github.com/vacp2p/nim-libp2p/pull/2593) Remove unnecessary transport argument
- [vacp2p/nim-libp2p#2589](https://github.com/vacp2p/nim-libp2p/pull/2589) Remove codecs from `addHandler`
- [vacp2p/nim-libp2p#2602](https://github.com/vacp2p/nim-libp2p/pull/2602) Bump metrics to v0.2.2
- [vacp2p/nim-libp2p#2599](https://github.com/vacp2p/nim-libp2p/pull/2599) Clean up Identify
- [vacp2p/nim-libp2p#2594](https://github.com/vacp2p/nim-libp2p/pull/2594) Fix flaky peer-limit test
- [vacp2p/nim-libp2p#2558](https://github.com/vacp2p/nim-libp2p/pull/2558) Remove go-libp2p patch from AutoNAT v2 tests
- [libp2p/go-libp2p#3513](https://github.com/libp2p/go-libp2p/pull/3513) Expose `AllowPrivateAddrs` through an option
- [vacp2p/nim-libp2p#2618](https://github.com/vacp2p/nim-libp2p/pull/2618) fix: enable hole punching
- [logos-storage/logos-storage-nim#1443](https://github.com/logos-storage/logos-storage-nim/pull/1443) chore: update libp2p to 2.0.0
- [vacp2p/roadmap#473](https://github.com/vacp2p/roadmap/pull/473) chore: update p2p commitments
- [vacp2p/nim-libp2p#2606](https://github.com/vacp2p/nim-libp2p/pull/2606) refactor(Identify): remove peerId argument form IdentifyPushHandler
- [logos-co/logos-libp2p-module#50](https://github.com/logos-co/logos-libp2p-module/pull/50) fix: small improvements
- [logos-co/logos-libp2p-module#48](https://github.com/logos-co/logos-libp2p-module/pull/48) feat(ci): ASan and TSan jobs for unit tests


### KAD-DHT optimizations

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:kad-dht-optimizations`
* owner: gabe
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Implement KAD-DHT optimizations and follow-up hardening work for nim-libp2p.

#### Deliverables
- [vacp2p/nim-libp2p#2345](https://github.com/vacp2p/nim-libp2p/pull/2345) fix(kad): race in randomFind
- [vacp2p/nim-libp2p#2164](https://github.com/vacp2p/nim-libp2p/pull/2164) chore(kad): handle dial failed exception
- [vacp2p/nim-libp2p#2560](https://github.com/vacp2p/nim-libp2p/pull/2560) chore(kad): limits
- [vacp2p/nim-libp2p#2559](https://github.com/vacp2p/nim-libp2p/pull/2559) refactor(kad): rewrite randomRecords around new lookOnce primitive

### Peerstore Address TTL

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:peerstore-address-ttl`
* owner: gabe
* status: done
* start-date: 2026/05/01
* end-date: 2026/05/19

#### Description
Add TTL support for addresses stored in the peerstore. Addresses should no
longer be stored indefinitely by default. Instead, use different TTLs
depending on how trustworthy the address is: 
- use shorter TTLs for unverified addresses, like those coming from
  discovery mechanism or from identify (unless it's the address used in 
  the active connection), 
- longer TTLs for addresses that have been confirmed as valid or 
   successfully connected to, 
- infinite TTL when explicitly requested.

#### Deliverables
- Peerstore support for address TTLs
- Different TTL policies for unverified, validated, connected, and permanent addresses
- Expiration logic to remove stale addresses automatically
- [vacp2p/nim-libp2p#2425](https://github.com/vacp2p/nim-libp2p/pull/2425) feat(peerstore): address TTL

### IdentifyPush

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:identify-push`
* owner: vlado
* status: done
* start-date: 2026/04/01
* end-date: 2026/05/12

#### Description
Enable the IdentifyPush protocol so connected peers receive protocol and
address updates when local capabilities change. Maintain a set of connected
peers that advertise the IdentifyPush protocol. After running Identify on a
peer, if its protocol list includes the IdentifyPush codec, store its peer ID
in that set. If the peer disconnects or later re-identifies without that
protocol, remove it. Whenever our multiaddresses change or new protocols are
mounted, send IdentifyPush updates to every peer in the set.

#### Deliverables
- IdentifyPush protocol is mounted and used
- [vacp2p/nim-libp2p#2440](https://github.com/vacp2p/nim-libp2p/pull/2440) refactor(IdentifyPusher): as Service
- [vacp2p/nim-libp2p#2439](https://github.com/vacp2p/nim-libp2p/pull/2439) feat(PeerInfo): add observer
- [vacp2p/nim-libp2p#2412](https://github.com/vacp2p/nim-libp2p/pull/2412) feat: identify pusher


### Quic Multiaddress Support

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:quic-maddrs`
* owner: vlado
* status: done
* start-date: 2026/04/01
* end-date: 2026/04/02

#### Description
Add support for multiple QUIC v1 multiaddresses in the QUIC transport.

#### Deliverables
- [vacp2p/nim-libp2p#2193](https://github.com/vacp2p/nim-libp2p/pull/2193) feat(quic): add support for listening on many addresses


### Kademlia Interop tests

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:kademlia-interop-tests`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Integrate libp2p test plans' Kad-DHT interop tests as part of the CI tests executed on each PR.
If these tests are available during Q2, integrate them into CI. Otherwise,
prepare the CI integration work and defer execution until the tests are
available. This task was originally planned for 2026q1, but the Kademlia
interop tests were not available.

#### Deliverables
- New github workflow: `Interoperability Tests / Run Kad-dht interoperability tests`

### ORC in CI

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:orc-ci`
* owner: gabe / miran
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Nimbus is evaluating ORC. Some previous work has already been done in this regard in
- https://github.com/vacp2p/nim-libp2p/issues/2077
- https://github.com/vacp2p/nim-libp2p/pull/2148
Nim 2.2.8 cannot be used with ORC at the moment, but the fix has already been
applied to the Nim branch that will become 2.2.10. Once Nim 2.2.10 is
available, test this version and memory model to ensure nim-libp2p works with
ORC. If Nim 2.2.10 is not released during Q2, prepare the CI changes and defer
execution to the next quarter.

#### Deliverables
- nim-libp2p CI jobs work with both `--mm:refc` and `--mm:orc`
- [vacp2p/nim-libp2p#2595](https://github.com/vacp2p/nim-libp2p/pull/2595) fix(tests): `test_all` to fix i386 and ORC out-of-memory failures
- [vacp2p/nim-libp2p#2148](https://github.com/vacp2p/nim-libp2p/pull/2148) chore: test ORC memory management
- [vacp2p/nim-libp2p#2339](https://github.com/vacp2p/nim-libp2p/pull/2339) chore(ci): test Nim 2.2.4 and 2.2.10

### Exception trace cleanup

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:exception-review`
* owner: not assigned yet
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Review runtime exception traces emitted by `nim-libp2p` and related libraries in connection, transport, and protocol paths
when those surface through `nim-libp2p` logs. Focus on the highest-noise
or least-actionable exceptions, decide whether each one of them should stay as
is, be downgraded, be deduplicated, or be handled without logging them, and
implement the agreed changes. 

#### Deliverables
- Reviewed list of targeted exception, affected code paths, and the
  chosen action for each
- PRs or filed issues for the changes in `nim-libp2p` and any library that needs an update
- Reduced noisy or redundant exception logs in the targeted high-frequency paths


### WSS handler socket leak

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:wss-socket-leak`
* owner: richard
* status: done
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Review how to complete [logos-delivery#3634](https://github.com/logos-messaging/logos-delivery/issues/3634),
validate the proposed solutions already documented in the related PRs and discussions,
and decide whether nim-libp2p should take ownership of part of the fix. This
should also assess whether Chronos accept concurrency work is required as part
of the solution.
Some related work available is:
- https://github.com/status-im/nim-websock/pull/181
- https://github.com/vacp2p/nim-libp2p/pull/1937

#### Deliverables
- Agreed technical direction for `logos-delivery#3634`
- Ownership decision between nim-libp2p and the relevant dependent components
- Follow-up issue or PR breakdown, including Chronos work if needed
- [status-im/nim-websock](https://github.com/status-im/nim-websock/pull/193) chore: expose HTTP accept primitives
- [vacp2p/nim-libp2p#2359](https://github.com/vacp2p/nim-libp2p/pull/2359) fix(ws): process pending handshakes concurrently

### Large RSA key limit

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:large-rsa-key-limit`
* owner: richard
* status: done
* start-date: 2026/05/01
* end-date: 2026/05/26

#### Description
Fix [vacp2p/nim-libp2p#1327](https://github.com/vacp2p/nim-libp2p/issues/1327)
by rejecting RSA keys that are too large to parse or verify safely. This should
protect nodes from resource exhaustion attacks where a malicious peer sends an
oversized RSA key and forces expensive signature verification. Use the
go-libp2p fix in
[libp2p/go-libp2p#2454](https://github.com/libp2p/go-libp2p/pull/2454) as
guidance, including the `<= 8192` bit maximum.

#### Deliverables
- Maximum RSA key size enforced during key parsing and generation
- Tests for accepted RSA keys and rejected oversized RSA keys
- Documentation or changelog note describing the compatibility/security behavior
- [vacp2p/nim-libp2p#2494](https://github.com/vacp2p/nim-libp2p/pull/2494) fix(rsa): cap max key size
- [vacp2p/nim-libp2p#2491](https://github.com/vacp2p/nim-libp2p/pull/2491) fix(rsa): reject imported keys below 2048 bits


### Sink performance exploration

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:sink-performance-exploration`
* owner: richard
* status: done
* start-date: 2026/05/01
* end-date: 2026/05/26

#### Description
Explore using Nim `sink` parameters in internal code paths where ownership
transfer can reduce unnecessary copies and improve memory performance. This is
tracked in
[vacp2p/nim-libp2p#1641](https://github.com/vacp2p/nim-libp2p/issues/1641).
Maintain backward compatibility for public APIs.

#### Deliverables
- Benchmarked list of candidate internal hot paths
- PRs applying `sink` where the ownership semantics are clear and beneficial
- Tests or benchmarks showing no behavioral regression
- No public API break.
- [vacp2p/nim-libp2p#2504](https://github.com/vacp2p/nim-libp2p/pull/2504) feat(protobuf): Use `sink` in protobuf decode paths
- [vacp2p/nim-libp2p#2503](https://github.com/vacp2p/nim-libp2p/pull/2503) feat(pubsub): use `sink` for RPC buffers
- [vacp2p/nim-libp2p#2501](https://github.com/vacp2p/nim-libp2p/pull/2501) feat(streams): use `sink` for write buffers
- [vacp2p/nim-libp2p#2517](https://github.com/vacp2p/nim-libp2p/pull/2517) feat: more `sink` changes

### nim-protobuf-serialization

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-maintenance:nim-protobuf-serialization`
* owner: vlado
* status: in progress (60%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description
Replace minprotobuf usage within nim-libp2p with nim-protobuf-serialization. See [nim-libp2p#841](https://github.com/vacp2p/nim-libp2p/issues/841)

#### Deliverables
- [vacp2p/nim-libp2p#2508](https://github.com/vacp2p/nim-libp2p/pull/2508) chore: use `protobuf_serialization` 0.4.0
- [vacp2p/nim-libp2p#2601](https://github.com/vacp2p/nim-libp2p/pull/2601) Use `protobuf_serialization` in Identify
- [vacp2p/nim-libp2p#2612](https://github.com/vacp2p/nim-libp2p/pull/2612) chore(autonatv2): utilize protobuf_serialization
- [vacp2p/nim-libp2p#2619](https://github.com/vacp2p/nim-libp2p/pull/2619) chore(protobuf): add chronos/time extensions
- [vacp2p/nim-libp2p#2616](https://github.com/vacp2p/nim-libp2p/pull/2616) chore(relay): utilize protobuf_serialization
- [vacp2p/nim-libp2p#2614](https://github.com/vacp2p/nim-libp2p/pull/2614) chore(routing-record): utilize protobuf_serialization
- [vacp2p/nim-libp2p#2610](https://github.com/vacp2p/nim-libp2p/pull/2610) chore(Noise): utilize protobuf_serialization
- [vacp2p/nim-libp2p#2609](https://github.com/vacp2p/nim-libp2p/pull/2609) chore(protobuf): decode procs to return result
