---

title: Nim Libp2p Testing
tags:
  - "2025q2"
  - "qa"
  - "vac"  
draft: false  
description: Extend nim-libp2p testing coverage, documentation and tooling. 

---

`vac:qa:vac:2025q2-nim-libp2p-testing`

## Description
Extend nim-libp2p testing coverage, documentation, and tooling.

Create test plans, implement tests, and increase coverage for all the
[modules](https://github.com/vacp2p/nim-libp2p?tab=readme-ov-file#modules)
implemented in nim libp2p.
Improve tooling around nim libp2p testing.

**Alignment with VAC Narratives:**
* Nim-libp2p is a key component of the VAC ecosystem,
  and improving its testing coverage and tooling strengthens our internal expertise
  and the overall reliability of the network.
* By enhancing these tests, and creating test plans,
  we support the RFC culture by providing feedback to the specifications,
  ensuring they align with real-world implementation.
* These efforts also contribute to scaling the project’s capacity,
  as better testing tools empower the open-source community to participate effectively.

## Task List

### Gossipsub Extended

* fully qualified name: `vac:qa:vac:2025q2-nim-libp2p-testing:gossipsub-extended`
* owner: radek
* status: done
* start-date: 2025/04/01
* end-date: 2025/05/15

#### Description
In 2025 Q2, expand Gossipsub test coverage to include more advanced
and edge-case scenarios that go beyond core functionality.
This will cover additional use cases and less common interactions within the protocol,
ensuring the robustness of Gossipsub in a wider range of environments.
The extended tests will address any remaining gaps not covered in Q4 
and aim to improve overall test completeness.

Focus: clean up `nim-libp2p` PRs and issues related to `GossipSub` tests which were open for a long time and got out dated.  

#### Deliverables
- revived stale PR: [test(gossipsub): message propagation](https://github.com/vacp2p/nim-libp2p/pull/1184), updated it and made sure it builds in CI
- [test: parallel execution POC](https://github.com/vacp2p/nim-libp2p/pull/1326)
- [chore(ci): decouple examples from unit tests](https://github.com/vacp2p/nim-libp2p/pull/1334)
- [test: combine tests](https://github.com/vacp2p/nim-libp2p/pull/1335)
- [test: include missing tests in testall](https://github.com/vacp2p/nim-libp2p/pull/1338)
- [test(gossipsub): optimise heartbeat interval and sleepAsync](https://github.com/vacp2p/nim-libp2p/pull/1342)
- [test(gossipsub): reorganize tests by feature category](https://github.com/vacp2p/nim-libp2p/pull/1350)
- [test(gossipsub): control message](https://github.com/vacp2p/nim-libp2p/pull/1191)
- [test(gossipsub): Topic Membership Tests](https://github.com/vacp2p/nim-libp2p/pull/1201) - closed, but extracted some of tests into [test(gossipsub): Topic Membership Tests - updated](https://github.com/vacp2p/nim-libp2p/pull/1363)
- [test(gossipsub): refactor testgossipinternal](https://github.com/vacp2p/nim-libp2p/pull/1366) - which closed an issue [Improve testgossipinternal file](https://github.com/vacp2p/nim-libp2p/issues/1207)
- [test(gossipsub): block5 protobuf test cases](https://github.com/vacp2p/nim-libp2p/pull/1204) - and closed an issue [Protobuf encoding & decoding not compatible with different references](https://github.com/vacp2p/nim-libp2p/issues/1208)

### Gossipsub Extended - part2

* fully qualified name: `vac:qa:vac:2025q2-nim-libp2p-testing:gossipsub-extended-part2`
* owner: radek
* status: in progress (0%)
* start-date: 2025/05/19
* end-date: 2025/06/09

#### Description
Focus: implementation of tests according to the test plan, sections:
- Heartbeat Mechanism Tests
- Topic Membership Tests
- Message Cache Tests
- Parameter Configuration Tests

#### Deliverables
* PRs with links to added tests

### Gossipsub Extended - part3

* fully qualified name: `vac:qa:vac:2025q2-nim-libp2p-testing:gossipsub-extended-part3`
* owner: radek
* status: not started (0%)
* start-date: 2025/06/09
* end-date: 2025/06/30

#### Description
Focus: implementation of tests according to the test plan, sections:
- Stress and Performance Tests
- Security and Privacy Testing
- Denial of Service (DoS) and Robustness Testing
- Compatibility of Older/Newer Versions of the Protocol 

#### Deliverables
* PRs with links to added tests

### Pubsub

* fully qualified name: `vac:qa:vac:2025q2-nim-libp2p-testing:pubsub`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Expand the pubsub test coverage by following the test plan,
checking what’s not covered, and implementing new tests for those scenarios.

#### Deliverables
* PRs with links to added tests

### Floodsub

* fully qualified name: `vac:qa:vac:2025q2-nim-libp2p-testing:floodsub`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Expand the floodsub test coverage by following the test plan,
checking what’s not covered, and implementing new tests for those scenarios.

#### Deliverables
* PRs with links to added tests

### Test Plans

* fully qualified name: `vac:qa:vac:2025q2-nim-libp2p-testing:test-plans`
* owner: fbarbu15
* status: in progress (20%)
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
Update and add new test plans for identify / push identify, ping, mplex multiplexer,
and others to be determined later.

#### Deliverables
* Link with the Notion pages