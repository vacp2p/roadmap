---

title: nim-libp2p Stream Budgets
tags:
  - "2026q2"
  - "p2p"
  - "ift"
draft: false
description: Per-protocol stream budgets in nim-libp2p

---

`ift-ts:p2p:ift:2026q2-nimlibp2p-stream-budgets`

Add opt-in per-protocol stream budgets to nim-libp2p so stream-count abuse can be rejected before a protocol handler is overloaded.

## Description

nim-libp2p currently exposes `LPProtocol.maxIncomingStreams` as an inbound
per-peer limit for a protocol, but it does not provide a complete budget model
for total inbound streams, outbound streams, or protocol-wide stream pressure.
This leaves protocol handlers vulnerable to overload when one peer or many
peers consume too much stream capacity.

This commitment extends the existing `LPProtocol.maxIncomingStreams` model into
a small per-protocol stream budget matrix. The work should keep the V1 scope
narrow: it limits stream counts only, does not attempt memory accounting, idle
time tracking, or peer reputation, and keeps new limits opt-in unless a separate
compatibility decision changes existing defaults.

## Task List

### Budget API And Accounting

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-stream-budgets:budget-api`
* owner: vlado
* status: done
* start-date: 2026/05/01
* end-date: 2026/05/26

#### Description
Extend `LPProtocol` with stream budget settings for inbound total streams,
outbound per-peer streams, and outbound total streams, while preserving
`maxIncomingStreams` as the existing inbound per-peer cap. Track open stream
counters per mounted protocol handler, direction, and peer where per-peer caps
need it. If one protocol handler exposes multiple compatible codec strings, all
compatible codec strings should share the same budget.

#### Deliverables
- `maxTotalIncomingStreams`, `maxOutgoingStreams`, and `maxTotalOutgoingStreams`
  added to `LPProtocol`
- Existing `maxIncomingStreams` behavior preserved as the inbound per-peer cap
- Open stream accounting scoped by mounted protocol handler and direction
- Shared budget behavior for compatible codec strings mounted by the same protocol handler
- [vacp2p/nim-libp2p#2522](https://github.com/vacp2p/nim-libp2p/pull/2522) feat(LPProtocol): stream limits


### Inbound Stream Enforcement

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-stream-budgets:inbound-enforcement`
* owner: vlado
* status: done
* start-date: 2026/05/01
* end-date: 2026/05/26

#### Description
Enforce inbound per-peer and total protocol caps in the multistream accept path
after protocol negotiation, next to the existing `maxIncomingStreams` check. On
breach, reject or close the new stream while keeping the peer connection open.
Counters must be decremented on clean close, error close, connection drop,
handler crash, and muxer close paths.

#### Deliverables
- Inbound per-peer stream limit enforced through the existing `maxIncomingStreams` path
- Inbound total stream limit enforced per mounted protocol handler
- Rejection behavior that closes only the new stream and keeps the connection up
- Tests covering clean close, error close, connection drop, handler crash, and muxer close
- [vacp2p/nim-libp2p#2522](https://github.com/vacp2p/nim-libp2p/pull/2522) feat(LPProtocol): stream limits


### Outbound Stream Enforcement

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-stream-budgets:outbound-enforcement`
* owner: vlado
* status: done
* start-date: 2026/05/01
* end-date: 2026/06/30

#### Description
Enforce outbound per-peer and total protocol caps after outbound protocol
negotiation, because the muxer and connection manager stream-open path does not
know which protocol will be selected before negotiation completes. Failed
negotiation, cancellation, stream close or reset, and muxer close must roll back
any counter reservation.

#### Deliverables
- Outbound per-peer stream limit enforced after protocol negotiation
- Outbound total stream limit enforced per mounted protocol handler
- Counter rollback for negotiation failure, cancellation, stream close/reset, and muxer close
- Tests covering outbound negotiation failure and outbound cancellation
- [vacp2p/nim-libp2p#2522](https://github.com/vacp2p/nim-libp2p/pull/2522) feat(LPProtocol): stream limits


### Metrics And Validation

* fully qualified name: `ift-ts:p2p:ift:2026q2-nimlibp2p-stream-budgets:metrics-validation`
* owner: vlado
* status: done
* start-date: 2026/05/01
* end-date: 2026/06/09

#### Description
Expose protocol stream budget metrics and validate the feature against overload
and lifecycle scenarios. Metrics should include protocol, direction, and scope
labels where useful, but should not add a per-peer label.

#### Deliverables
- [vacp2p/nim-libp2p#2577](https://github.com/vacp2p/nim-libp2p/pull/2577) feat(LPProtocol): add metrics
- [vacp2p/nim-libp2p#2603](https://github.com/vacp2p/nim-libp2p/pull/2603) Add LPProtocol metrics-value tests
- [vacp2p/nim-libp2p#2584](https://github.com/vacp2p/nim-libp2p/pull/2584) Add LPProtocol fast path when there are no limits
- `libp2p_protocol_stream_cap_rejections_total{protocol, direction, scope}` metric
- `libp2p_protocol_streams_open{protocol, direction}` metric
- Integration tests for inbound and outbound cap breaches
- Documentation describing the opt-in V1 behavior and compatibility expectations
