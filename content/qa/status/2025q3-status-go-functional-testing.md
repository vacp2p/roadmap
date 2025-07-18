---
title: Status Go Functional Testing
tags:
  - "2025q3"
  - "qa"
  - "status"  
draft: false  
description: Enhance functional and e2e testing for status-go features by implementing tests using status-backend.
---

`vac:qa:status:2025q3-status-go-functional-testing`

## Description
Expand functional and e2e testing for status-go by implementing tests using status-backend,
as outlined in this [epic](https://github.com/status-im/status-go/issues/6064). 

**Alignment with VAC Narratives:**
* By helping create a robust functional testing framework for Status Go,
  VAC QA contributes directly to the narrative of internal collaboration and efficiency.
* By finding issues in the project code and specs during testing,
  VAC QA strengthens the RFC culture, contributing to continuous improvement and community engagement.

## Task List

### Critical user flows

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:critical-flows`
* owner: chu
* status: in progress (20%)
* start-date: 2025/07/01
* end-date: 2025/08/15

#### Description
Add functional test coverage to critical user flows like onboarding, 
asset management or messaging as described in this [epic](https://github.com/status-im/status-go/issues/6064). 

#### Deliverables
* test_: [critical flow RecoverAndLogin with 12,15,24 words mnemonic](https://github.com/status-im/status-go/pull/6688)


### Wallet features

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:wallet`
* owner: chu
* status: not started
* start-date: 
* end-date: 

#### Description
Add functional test coverage to wallet features,
in order to catch regressions introduced by wallet backend refactoring.
Focus on e2e scenarios that can be automated at this level.
TODO! This taks will need to be broken down into smaller task once we have more info

#### Deliverables
* Test plans
* PRs with the new tests


### Framework usage improvements

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:framework-improvements`
* owner: chu/florin
* status: in progress (50%)
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description
Improve and simplify user/dev experience when running tests locally.
Update readme and debugging.

#### Deliverables
- Fixed the [reliability failures](https://github.com/status-im/status-go/pull/6736)
- [Refactoring on how test fixtures are used](https://github.com/status-im/status-go/pull/6725)

### Status-backend based on nwaku

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:status-based-on-nwaku`
* owner: florin
* status: in progress (20%)
* start-date: 2025/07/01
* end-date: 2025/09/30

#### Description
Run all status-backend tests on a 
[nwaku-based build](https://github.com/waku-org/pm/blob/2025H2/draft-roadmap/integrate_nwaku_in_status_desktop_relay_mode_only.md?plain=1#L7)
as described in the Waku FURPS

#### Deliverables
- Created this short [guide](https://www.notion.so/status-staging-testing-guide-2248f96fb65c80efb5eafe029d964343) on how to validate staging deploys
- Executed status related tests for nwaku v0.36 and created a [test report](https://www.notion.so/Nwaku-v0-36-in-status-staging-2248f96fb65c8023b38cd4901646a105)
- Executed waku interop tests for nwaku v0.36 and created a [test report](https://www.notion.so/Waku-regression-testing-v0-36-2268f96fb65c8073bd6bce16733d09cb)


### Reliability in Status Communities

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:reliability-communities`
* owner: chu
* status: not started
* start-date: 
* end-date: 

#### Description
- R1. When sending a message in a group, the publisher can ascertain the message was received by at least one recipient.
- R2. When receiving messages in a group, the receiver can ascertain most missed messages by receiving one recent message from the group.
- See [Waku FURPS](https://github.com/waku-org/pm/blob/2025H2/draft-roadmap/introduce_e2e_reliability_in_status.md?plain=1#L40)

#### Deliverables
* PRs with the new tests


### Group chats tests

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:group-chats-tests`
* owner: fbarbu15
* status: in progress (30%)
* start-date: 11/07/2025
* end-date: 24/07/2025

#### Description
Cover the [wakuext group chats](https://github.com/status-im/status-go/issues/6071)

#### Deliverables
* PRs with the new tests
