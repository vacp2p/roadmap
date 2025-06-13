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


### Wallet features

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:wallet`
* owner: fbarbu15
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

### Messaging features

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:messaging`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Add functional test coverage to messaging features that are not already covered by tests,
in order to catch regressions introduced by messaging backend refactoring.
Focus on e2e scenarios that can be automated at this level.

#### Deliverables
* Test plans
* PRs with the new tests

### Performance tests

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:performance`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Measure and export performance metrics during running and usage of status-backend.
Check for leaks and performance degradations between runs.
Create separate workflow that runs nightly.

#### Deliverables
* PRs with the new tests

### Framework usage improvements

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:framework-improvements`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Improve and simplify user/dev experience when running tests locally.
Update readme and debugging.

#### Deliverables
* PRs with the new tests

### Status-backend based on nwaku

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:status-based-on-nwaku`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Run all status-backend tests on a 
[nwaku-based build](https://github.com/waku-org/pm/blob/2025H2/draft-roadmap/integrate_nwaku_in_status_desktop_relay_mode_only.md?plain=1#L7)
as described in the Waku FURPS

#### Deliverables
* Test Reports

### Reliability in Status Communities

* fully qualified name: `vac:qa:status:2025q3-status-go-functional-testing:reliability-communities`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
- R1. When sending a message in a group, the publisher can ascertain the message was received by at least one recipient.
- R2. When receiving messages in a group, the receiver can ascertain most missed messages by receiving one recent message from the group.
- See [Waku FURPS](https://github.com/waku-org/pm/blob/2025H2/draft-roadmap/introduce_e2e_reliability_in_status.md?plain=1#L40)

#### Deliverables
* PRs with the new tests

