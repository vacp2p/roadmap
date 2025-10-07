---
title: Status Go Functional Testing
tags:
  - "2025q4"
  - "qa"
  - "status"  
draft: false  
description: Enhance functional and e2e testing for status-go features by implementing tests using status-backend.
---

`vac:qa:status:2025q4-status-go-functional-testing`

## Description
Expand functional and e2e testing for status-go by implementing tests using status-backend,
with focus on wallet, settings and waku methods.

**Alignment with VAC Narratives:**
* By helping create a robust functional testing framework for Status Go,
  VAC QA contributes directly to the narrative of internal collaboration and efficiency.
* By finding issues in the project code and specs during testing,
  VAC QA strengthens the RFC culture, contributing to continuous improvement and community engagement.

## Task List

### Wallet features

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:wallet`
* owner: fbarbu15
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/01

#### Description
Add functional test coverage to wallet features,
in order to catch regressions introduced by wallet backend refactoring.
Focus on e2e scenarios that can be automated at this level.
TODO! This taks will need to be broken down into smaller task once we have more info

#### Deliverables
* PRs with the new tests

### Settings features

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:settings`
* owner: aya
* status: in progress (20%)
* start-date: 2025/10/01
* end-date: 2025/10/20

#### Description
Add functional test coverage to settings features.

#### Deliverables
* PRs with the new tests

### Waku features

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:waku`
* owner: fbarbu15
* status: in progress (20%)
* start-date: 2025/10/01
* end-date: 2025/12/01

#### Description
Add functional test coverage to waku features
as outlined in this [epic](https://github.com/status-im/status-go/issues/6064). 

#### Deliverables
- [bug: MyPendingRequestsToJoin still return request after the request has been declined](https://github.com/status-im/status-go/issues/6975)
- [bug: checkAndDeletePendingRequestToJoinCommunity doesn't clear pending requests](https://github.com/status-im/status-go/issues/6976)
- [test: community membership requests](https://github.com/status-im/status-go/pull/6977)

### Emoji reactions

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:emoji-reactions`
* owner: aya
* status: not started
* start-date: 2025/10/20
* end-date: 2025/10/30

#### Description
Add functional tests for the new emoji reactions API 
as outlined [here](https://github.com/status-im/status-desktop/issues/18822)

### Reliability in Status Communities

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:reliability-communities`
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

### Maintenance

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:maintenance`
* owner: fbarbu15
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Ongoing maintenance of Status Functional tests. 
This includes updating tests for changes in `status-go`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.
