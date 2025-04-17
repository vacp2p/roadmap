---
title: Status Go Functional Testing
tags:
  - "2025q2"
  - "qa"
  - "waku"  
draft: false  
description: Enhance functional testing for status-go features by implementing tests focused on Waku functionality.
---

`vac:qa:waku:2025q2-status-go-functional-testing`

## Description
Expand functional testing for status-go by implementing targeted Waku feature tests, 
including chat actions, contact requests, and group chats, 
as outlined in this [epic](https://github.com/status-im/status-go/issues/6064). 

**Alignment with VAC Narratives:**
* By helping create a robust functional testing framework for Status Go,
  VAC QA contributes directly to the narrative of internal collaboration and efficiency.
* By finding issues in the project code and specs during testing,
  VAC QA strengthens the RFC culture, contributing to continuous improvement and community engagement.

## Task List


### Chat actions tests

* fully qualified name: `vac:qa:waku:2025q2-status-go-functional-testing:chat-actions-tests`
* owner: radek
* status: done
* start-date: 2025/04/01
* end-date: 2025/04/07

#### Description
Cover the core functionality of Status related to [wakuext messages](https://github.com/status-im/status-go/issues/6072)

#### Deliverables
- [test_: Tests for chat actions 1](https://github.com/status-im/status-go/pull/6453)
- [test_: Tests for chat actions 2](https://github.com/status-im/status-go/pull/6492)


### Contact requests tests

* fully qualified name: `vac:qa:waku:2025q2-status-go-functional-testing:contact-requests-tests`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Cover the [wakuext contact requests](https://github.com/status-im/status-go/issues/6085)

#### Deliverables
* PRs with the new tests


### Group chats tests

* fully qualified name: `vac:qa:waku:2025q2-status-go-functional-testing:group-chats-tests`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Cover the [wakuext group chats](https://github.com/status-im/status-go/issues/6071)

#### Deliverables
* PRs with the new tests

### Tests on light mode

* fully qualified name: `vac:qa:waku:2025q2-status-go-functional-testing:light-mode`
* owner: fbarbu15
* status: in progress (50%)
* start-date: 2025/04/07
* end-date: 2025/04/24

#### Description
Enable running all waku tests also on light client mode

#### Deliverables
- Enabled light client mode for [waku functional tests](https://github.com/status-im/status-go/pull/6518/files)
