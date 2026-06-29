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
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Support Logos Delivery engineers as they use service discovery and Kademlia
through the Logos libp2p module or their own bindings. Clarify configuration,
bootstrap, provider record, discovery, and routing-table behavior as integration
questions arise.

#### Deliverables
- Guidance for service discovery and Kademlia configuration
- Implementation support for integration blockers found during Q3


### Opt-In Integration Path

* fully qualified name: `ift-ts:p2p:ift:2026q3-logos-delivery-consulting:opt-in-path`
* owner: not assigned yet
* status: not started
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Ensure Logos Delivery can enable libp2p functionality explicitly without forcing
the Logos libp2p module into deployments that still need to use the existing
bindings or a custom embedding strategy.

#### Deliverables
- Opt-in module configuration reviewed with Logos Delivery
- Follow-up issues or PRs for any integration gaps
