---

title: Nim Libp2p Testing
tags:
  - "2025q3"
  - "qa"
  - "vac"  
draft: false  
description: Continue expanding nim-libp2p testing coverage with focus on pubsub, yamux, rendezvous and floodsub protocols. 

---

`vac:qa:vac:2025q3-nim-libp2p-testing`

## Description
Continue expanding nim-libp2p testing coverage, documentation, and tooling with focus on protocols beyond Gossipsub.

Complete any remaining Gossipsub testing tasks, expand pubsub testing coverage for scenarios not covered by Gossipsub tests, implement comprehensive testing for Yamux multiplexer and Rendezvous protocol, and add Floodsub testing if time permits.
Improve tooling around nim libp2p testing and ensure all implemented modules have adequate test coverage.

**Alignment with VAC Narratives:**
* Nim-libp2p is a key component of the VAC ecosystem,
  and improving its testing coverage and tooling strengthens our internal expertise
  and the overall reliability of the network.
* By enhancing these tests, and creating test plans,
  we support the RFC culture by providing feedback to the specifications,
  ensuring they align with real-world implementation.
* These efforts also contribute to scaling the project's capacity,
  as better testing tools empower the open-source community to participate effectively.

## Task List

### Gossipsub Extended - Completion

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:gossipsub-completion`
* owner: radek
* status: done
* start-date: 2025/07/01
* end-date: 2025/07/22

#### Description
Complete any remaining Gossipsub testing tasks from Q2 if not fully finished.
Ensure all edge cases and advanced scenarios are properly covered.

#### Deliverables
- [test(gossipsub): refactor compatibility related tests](https://github.com/vacp2p/nim-libp2p/pull/1495)
- [test(gossipsub): Signature flags tests](https://github.com/vacp2p/nim-libp2p/pull/1496)
- [test(gossipsub): behavior unit tests 1](https://github.com/vacp2p/nim-libp2p/pull/1501)
- [test(gossipsub): behavior unit tests 2](https://github.com/vacp2p/nim-libp2p/pull/1503)
- [test(gossipsub): gossipsub unit tests 1](https://github.com/vacp2p/nim-libp2p/pull/1508)
- [test(gossipsub): gossipsub unit tests 2](https://github.com/vacp2p/nim-libp2p/pull/1511)

### Pubsub Testing

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:pubsub`
* owner: radek
* status: not started
* start-date: 2025/07/15
* end-date: 2025/07/31

#### Description
Investigate and implement pubsub tests that can be done in isolation and make sense
beyond what is already covered by Gossipsub testing. Focus on core pubsub functionality,
base protocol behaviors, subscription management, message validation, and pubsub router
interactions that are protocol-agnostic.

#### Deliverables
* PRs with links to added tests

### Yamux Multiplexer Testing

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:yamux`
* owner: radek
* status: in progress (10%)
* start-date: 2025/08/01
* end-date: 2025/08/31

#### Description
Implement testing for the Yamux multiplexer protocol in nim-libp2p.
Yamux is a stream multiplexing protocol that allows multiple logical streams
over a single connection. Testing should cover stream creation and management,
flow control, backpressure handling, concurrent stream operations, error handling,
and edge cases.

#### Deliverables
* [test(yamux): Add header unit tests](https://github.com/vacp2p/nim-libp2p/pull/1625)

### Rendezvous Protocol Testing

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:rendezvous`
* owner: radek
* status: not started
* start-date: 2025/09/01
* end-date: 2025/09/30

#### Description
Implement testing for the Rendezvous protocol, which provides a way for peers
to discover each other through a rendezvous point. The protocol allows peers
to register themselves at a rendezvous point and discover other peers with
similar interests or capabilities.

#### Deliverables
* PRs with links to added tests

### Floodsub Testing (If Time Permits)

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:floodsub`
* owner: radek
* status: not started
* start-date: 2025/09/15
* end-date: 2025/09/30

#### Description
If previous tasks are completed ahead of schedule, implement comprehensive
testing for the Floodsub protocol. Floodsub is a basic pubsub implementation
that floods messages to all peers in the network, serving as a simpler
alternative to Gossipsub.

#### Deliverables
* PRs with links to added tests

### Test Plans and Documentation

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:test-plans`
* owner: fbarbu15
* status: not started
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
Update and add new test plans for identify / push identify, ping, mplex multiplexer,
and others to be determined later.

#### Deliverables
* Link with the Notion pages

### GossipSub Performance Testing

* fully qualified name: `vac:qa:vac:2025q3-nim-libp2p-testing:gossipsub-performance`
* owner: radek
* status: done
* start-date: 2025/07/15
* end-date: 2025/07/31

#### Description: 
Implement small scale performance tests for GossipSub that can run between a few nodes in the nim-libp2p repository. Set up GitHub Actions workflow to run these tests automatically and post results to PRs. Focus on performance scenarios that make sense at the integration test level, complementary to DST's multi-node testing. Include baseline measurements and automated result reporting.

#### Deliverables:
* [test(gossipsub): performance tests PoC](https://github.com/vacp2p/nim-libp2p/pull/1544)
* [test(gossipsub): Performance tests - base scenario and runner](https://github.com/vacp2p/nim-libp2p/pull/1573)
* [test(gossipsub): Performance tests - aggregation script and workflow](https://github.com/vacp2p/nim-libp2p/pull/1577)
* [test(gossipsub): Performance tests - more scenarios](https://github.com/vacp2p/nim-libp2p/pull/1585)
* [test(gossipsub): Performance tests - docker stats](https://github.com/vacp2p/nim-libp2p/pull/1593)
* [test(gossipsub): Performance tests - plot docker stats](https://github.com/vacp2p/nim-libp2p/pull/1597)
* [test(gossipsub): Performance tests - plot latency history](https://github.com/vacp2p/nim-libp2p/pull/1608)
* [test(performance): fetch before push and improve latency history](https://github.com/vacp2p/nim-libp2p/pull/1617)
