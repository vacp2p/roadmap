---

title: Logos Delivery Consulting
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Support Logos Delivery integration with the Logos libp2p module

---

`ift-ts:p2p:ift:2026q3-logos-delivery-consulting`

Support the Logos Delivery team's integration with the Logos libp2p module,
with particular focus on service discovery and Kademlia usage

## Description

P2P provides consulting and implementation support to Logos Delivery as they
integrate libp2p functionality through the Logos libp2p module. The integration
should remain opt-in so Logos Delivery can choose between their own C bindings
and the Logos libp2p module depending on the deployment and feature needs.

This commitment is high priority for Q3 because it keeps the downstream Logos
Delivery integration aligned with nim-libp2p and Logos Core capabilities while
avoiding hard coupling to one integration path.

## Task List

### Integration Review

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-delivery-consulting:integration-review`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Review the current Logos Delivery integration plan and identify where the Logos
libp2p module should be used directly, where existing Logos Delivery C bindings
should remain supported, and where additional nim-libp2p or module APIs are
required.

#### Deliverables
- Documented integration options for Logos Delivery
- List of missing or blocking APIs in nim-libp2p, Logos Core, or the Logos libp2p module
- Recommendations for keeping service discovery and Kademlia usage opt-in


### Service Discovery And Kademlia Support

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-delivery-consulting:service-discovery-kad`
* owner: Gabe
* status: in progress (59%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support Logos Delivery engineers as they use service discovery and Kademlia
through the Logos libp2p module or their own bindings. Clarify configuration,
bootstrap, provider record, discovery, and routing-table behavior as integration
questions arise.

#### Deliverables
- [vacp2p/nim-libp2p#2967](https://github.com/vacp2p/nim-libp2p/pull/2967) fix(kad): keep peer addresses when the admission probe cap is full
- [vacp2p/nim-libp2p#2943](https://github.com/vacp2p/nim-libp2p/pull/2943) fix(kad): findNode no longer double-hashes a service table's target
- [vacp2p/nim-libp2p#2939](https://github.com/vacp2p/nim-libp2p/pull/2939) chore(kad): stop re-probing a peer whose admission probe just failed
- [vacp2p/nim-libp2p#2937](https://github.com/vacp2p/nim-libp2p/pull/2937) feat(kad): re-seed a routing table that fell below a minimum size
- [vacp2p/nim-libp2p#2938](https://github.com/vacp2p/nim-libp2p/pull/2938) chore(kad): per-bucket IP diversity caps
- [vacp2p/nim-libp2p#2936](https://github.com/vacp2p/nim-libp2p/pull/2936) fix(kad): an admission probe no longer waits out the dialer timeout
- [vacp2p/nim-libp2p#2922](https://github.com/vacp2p/nim-libp2p/pull/2922) fix(service-disco): validate advert length and re-check client mode
- [vacp2p/nim-libp2p#2901](https://github.com/vacp2p/nim-libp2p/pull/2901) chore(kad): reuse per-peer streams instead of dialing a fresh stream per RPC
- [vacp2p/nim-libp2p#2920](https://github.com/vacp2p/nim-libp2p/pull/2920) fix(service-disco): initialise the network size estimator
- [vacp2p/nim-libp2p#2910](https://github.com/vacp2p/nim-libp2p/pull/2910) feat(kad): dynamic client/server mode via reachability
- [vacp2p/nim-libp2p#2903](https://github.com/vacp2p/nim-libp2p/pull/2903) chore(kad): converge lookups on beta and confirm the k closest in a follow-up phase
- [vacp2p/nim-libp2p#2911](https://github.com/vacp2p/nim-libp2p/pull/2911) feat(kad): send optimistic ADD_PROVIDER during lookup
- [vacp2p/nim-libp2p#2902](https://github.com/vacp2p/nim-libp2p/pull/2902) chore(kad): batch reprovide by keyspace region
- [vacp2p/nim-libp2p#2864](https://github.com/vacp2p/nim-libp2p/pull/2864) chore(kad): replace round-synchronized lookup with a continuous alpha-concurrency pipeline
- [vacp2p/nim-libp2p#2863](https://github.com/vacp2p/nim-libp2p/pull/2863) chore(kad): probe peers before inserting them into the routing table
- [vacp2p/nim-libp2p#2879](https://github.com/vacp2p/nim-libp2p/pull/2879) fix(kad): flaky Get providers returns at most k closest peers
- [libp2p/py-libp2p#1387](https://github.com/libp2p/py-libp2p/pull/1387) fix(kad-dht): don't dial ourselves on FIND_NODE, and return the target per the spec exception
- [libp2p/py-libp2p#1398](https://github.com/libp2p/py-libp2p/pull/1398) fix(pubsub): replay recent messages once a peer's outbound stream is registered
- [vacp2p/nim-libp2p#2862](https://github.com/vacp2p/nim-libp2p/pull/2862) chore(kad): liveness-gated bucket eviction
- [vacp2p/nim-libp2p#2850](https://github.com/vacp2p/nim-libp2p/pull/2850) fix(kad): exclude the requester from closerPeers
- [vacp2p/nim-libp2p#2842](https://github.com/vacp2p/nim-libp2p/pull/2842) fix(kad): target the requested bucket when refreshing
- [vacp2p/nim-libp2p#2841](https://github.com/vacp2p/nim-libp2p/pull/2841) fix(service-disco): don't rescale bucket index by maxBuckets
- Guidance for service discovery and Kademlia configuration
- Implementation support for integration blockers found during Q3


### Opt-In Integration Path

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-delivery-consulting:opt-in-path`
* owner: Gabe
* status: in progress (50%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Ensure Logos Delivery can enable libp2p functionality explicitly without forcing
the Logos libp2p module into deployments that still need to use the existing
bindings or a custom embedding strategy.

#### Deliverables
- Opt-in module configuration reviewed with Logos Delivery
- Follow-up issues or PRs for any integration gaps
