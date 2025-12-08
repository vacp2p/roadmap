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

## Task List

### Wallet features

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:wallet`
* owner: roman
* status: in progress (20%)
* start-date: 2025/10/01
* end-date: 2025/12/01

#### Description
Add functional test coverage to wallet features,
in order to catch regressions introduced by wallet backend refactoring.
Focus on e2e scenarios that can be automated at this level.
This taks will need to be broken down into smaller task once we have more info

#### Deliverables
- [Signal and backend state inconsistency before accept_request_to_join_community call](https://github.com/status-im/status-go/issues/7161)
- [Automatic member kick-off not working with fake token addresses](https://github.com/status-im/status-go/issues/7114)
- [Unable to get user into Admin role](https://github.com/status-im/status-go/issues/7135)
- [No stopMessenger equivalent implemented for the public API](https://github.com/status-im/status-go/issues/7139)

### Settings features

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:settings`
* owner: aya
* status: done
* start-date: 2025/10/01
* end-date: 2025/11/19

#### Description
Add functional test coverage to settings features.

#### Deliverables
* [test: First draft for settings wrappers and test file added](https://github.com/status-im/status-go/pull/6984)
* PRs with the new tests

### Waku features

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:waku`
* owner: fbarbu15
* status: in progress (35%)
* start-date: 2025/10/01
* end-date: 2025/12/01

#### Description
Add functional test coverage to waku features
as outlined in this [epic](https://github.com/status-im/status-go/issues/6064). 

#### Deliverables
- [bug: MyPendingRequestsToJoin still return request after the request has been declined](https://github.com/status-im/status-go/issues/6975)
- [bug: checkAndDeletePendingRequestToJoinCommunity doesn't clear pending requests](https://github.com/status-im/status-go/issues/6976)
- [test: community membership requests](https://github.com/status-im/status-go/pull/6977)
- [bug: displayName is ignored for wakuext_createCommunityChat](https://github.com/status-im/status-go/issues/6985)
- [test: community chats](https://github.com/status-im/status-go/pull/6987)
- [bug: Inconsistent replied_at timestamp format in GetVerificationRequestSentTo response](https://github.com/status-im/status-go/issues/6995)
- [test: contact verification](https://github.com/status-im/status-go/pull/6997)

### Emoji reactions

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:emoji-reactions`
* owner: aya
* status: not started
* start-date: 2025/10/20
* end-date: 2025/10/30

#### Description
Add functional tests for the new emoji reactions API 
as outlined [here](https://github.com/status-im/status-desktop/issues/18822)

#### Deliverables
* PRs with the new tests

### Reliability in Status Communities

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:reliability-communities`
* owner: fbarbu15
* status: not started
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
- R1. When sending a message in a group, the publisher can ascertain the message was received by at least one recipient.
- R2. When receiving messages in a group, the receiver can ascertain most missed messages by receiving one recent message from the group.
- See [Waku FURPS](https://github.com/waku-org/pm/blob/2025H2/draft-roadmap/introduce_e2e_reliability_in_status.md?plain=1#L40)

Schedule note: Dates reflect quarter bounds; update when actual timing is known.

#### Deliverables
* PRs with the new tests

### Maintenance

* fully qualified name: `vac:qa:status:2025q4-status-go-functional-testing:maintenance`
* owner: roman
* status: in progress (30%)
* start-date: 2025/10/01
* end-date: 2025/12/31

#### Description
Ongoing maintenance of Status Functional tests. 
This includes updating tests for changes in `status-go`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- [Flaky test `test_update_keycard_uid_success`](https://github.com/status-im/status-go/issues/7032)
- [Temporary guard for `test_update_keycard_uid_success`](https://github.com/status-im/status-go/commit/92cd47e98b4553a9e6b153ef39a55e7205cad6c6)
- PRs with the new tests
