---
title: Waku Scaling
tags:
  - "2025q4"
  - "dst"
  - "waku"
draft: false
description: "Use experiments determine and
improve Waku's scaling properties.
Find the limits of Waku's capabilities
and measure them in different scenarios.
Deliver hard numbers and actionable insights.
Confirm or reject our ideas or presented ones."
---

`vac:dst:waku:2025q4-waku-scaling`

## Description

We will use realistic Waku node experiments to evaluate
and improve Waku's scalability by conducting
performance measurements across its key components and tasks.
These efforts contains supporting on-chain RLN memberships,
strengthening the foundations for private chats, optimize 
browser bootstrapping for improved responsiveness, 
integrate nwaku in Status Desktop for seamless relay functionality,
and implement the SDS protocol for group messaging reliability and recovery.


### Background

### Narratives

These efforts will support the Conduit of Expertise narrative by
accelerating Waku Improvements,
providing measurable insights
to enhance developer experience
within and beyond the IFT ecosystem.
Enhancing RFC Development by enabling faster,
more informed RFC development
through performance insights during the drafting process.

## Task list


### Hardening and Scaling Foundations for Private Chats
> *Note*: This needs more input from project

[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/hardening_and_scaling_foundation_for_private_chat.md#hardening-and-scaling-foundations-for-private-chats)

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description

To have: Vac-DST: status-backend benchmarks

#### Deliverables
- Code: 
- Report:


### Optimise Browser Bootstrapping

[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/improve_devex_api_twn_metrics_docs.md#optimise-browser-bootstrapping)

* fully qualified name: `vac:dst:waku:2025q4-waku-scaling:optimise-browser-bootstrapping`
* owner: Pearson
* status: 10%
* start-date: 2025-10-15
* end-date: 2025-10-31

#### Description

Using js-waku, prove that:
- From an operating state, a node can 
resume transmitting messages within 1 second 
after disconnection; in a network with 1 bootstrap node,
100 service nodes and 500 browser nodes.

- From a cold start, a node can start transmitting 
messages within 5 seconds; in a network with 1 bootstrap
node, 100 service nodes and 500 browser nodes.

#### Deliverables
- Code: 
- Report:



### Integrate nwaku in Status Desktop, relay mode only
> *Note*: This needs more input from project

[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/integrate_nwaku_in_status_desktop_relay_mode_only.md#integrate-nwaku-in-status-desktop-relay-mode-only)

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description

Waku estimated date of completion: 30 June

Vac-DST to complete go-waku-based benchmark works and proceed with
nwaku-based vs go-waku-based status-backend comparisons.

#### Deliverables
- Code: 
- Report:


### SDS protocol in Status - basic integration

> *Note*: This needs more input from project

[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/introduce_e2e_reliability_in_status.md#sds-protocol-in-status---basic-integration)

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description
Waku estimated date of completion: 31 Aug

Prove that:
- When sending a message in a group, the publisher
can ensure the message was received by at least one 
recipient within `S` seconds

- When receiving messages in a group, the receiver
can detect 90% of missed messages within `3*S` seconds


#### Deliverables
- Code:
- Report:



### SDS protocol in Status - basic recovery

> *Note*: This needs more input from project

[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/introduce_e2e_reliability_in_status.md#sds-protocol-in-status---basic-recovery)

* fully qualified name: `-`
* owner: -
* status: -
* start-date: -
* end-date: -

#### Description
Waku estimated date of completion: 31 Aug 2025

Prove that:
- When receiving messages in group, the receiver can 
- reach eventual consistency within `6*S` seconds

#### Deliverables
- Code:
- Report:


### TWN supports RLN onchain tree and deposits, existing memberships only
> *Note*: Moved from previous quarter

[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/deploy_rln_onchain_tree_on_l2_testnet.md#twn-supports-rln-onchain-tree-and-deposits-existing-memberships-only)
[Link to Waku FURPS](https://github.com/waku-org/pm/blob/master/draft-roadmap/rln_mainnet.md#twn-supports-rln-onchain-tree-and-deposits-existing-memberships-only)

* fully qualified name: `vac:dst:waku:2025q4-waku-scaling:TWN-supports-RLN-tree`
* owner: Alberto
* status: 70%
* start-date: 2025/10/06
* end-date: 2025/10/24

#### Description
Prove that a new node setup with an RLN membership can be ready
to verify RLN proof within 5s, no matter the size of the tree.

#### Deliverables
- Code: 
- Report:
