---
title: Status Go Functional Testing
tags:
  - "2025q2"
  - "qa"
  - "status"  
draft: false  
description: Enhance functional testing for status-go features by implementing tests focused on Waku functionality.
---

`vac:qa:status:2025q2-status-go-functional-testing`

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

* fully qualified name: `vac:qa:status:2025q2-status-go-functional-testing:chat-actions-tests`
* owner: radek
* status: done
* start-date: 2025/04/01
* end-date: 2025/04/07

#### Description
Cover the core functionality of Status related to [wakuext messages](https://github.com/status-im/status-go/issues/6072)

#### Deliverables
- [test_: Tests for chat actions 1](https://github.com/status-im/status-go/pull/6453)
- [test_: Tests for chat actions 2](https://github.com/status-im/status-go/pull/6492)
- [test_: run wakuext tests on light client as well](https://github.com/status-im/status-go/pull/6518) 
- [test_: reliability tests on staging fleet](https://github.com/status-im/status-go/pull/6543)


### Contact requests tests

* fully qualified name: `vac:qa:status:2025q2-status-go-functional-testing:contact-requests-tests`
* owner: fbarbu15
* status: done
* start-date: 2025/04/01
* end-date: 2025/04/07

#### Description
Cover the [wakuext contact requests](https://github.com/status-im/status-go/issues/6085)

#### Deliverables
* [test_: contact requests 1](https://github.com/status-im/status-go/pull/6425)
* [test_: contact requests 2](https://github.com/status-im/status-go/pull/6437)


### Group chats tests

* fully qualified name: `vac:qa:status:2025q2-status-go-functional-testing:group-chats-tests`
* owner: fbarbu15
* status: not started
* start-date: 
* end-date: 

#### Description
Moved to Q3! Could not be completed in Q2 because we were responsible for integrating status QA CCs into our team.
Cover the [wakuext group chats](https://github.com/status-im/status-go/issues/6071)

#### Deliverables
* PRs with the new tests

### Tests on light mode

* fully qualified name: `vac:qa:status:2025q2-status-go-functional-testing:light-mode`
* owner: fbarbu15
* status: done
* start-date: 2025/04/07
* end-date: 2025/04/24

#### Description
Enable running all waku tests also on light client mode

#### Deliverables
- Enabled light client mode for [waku functional tests](https://github.com/status-im/status-go/pull/6518/files)
- Created dedicated Readme for the status-backend reliability [test suite](https://github.com/status-im/status-go/pull/6700)
