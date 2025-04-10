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
* status: in progress (10%)
* start-date: 2025/04/01
* end-date: 2025/05/15

#### Description
In 2025 Q2, expand Gossipsub test coverage to include more advanced
and edge-case scenarios that go beyond core functionality.
This will cover additional use cases and less common interactions within the protocol,
ensuring the robustness of Gossipsub in a wider range of environments.
The extended tests will address any remaining gaps not covered in Q4 
and aim to improve overall test completeness.


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
