---
title: Keycard Testing 
tags:
  - "2025q3"
  - "qa"
  - "keycard"  
draft: true  
description: Ensure quality of Keycard applications.
---

`vac:qa:keycard:2025q3-keycard-testing`

## Description

**Alignment with VAC Narratives:**

* The VAC QA team supports internal collaboration and efficiency
  by maintaining the quality and reliability of Keycard applications.

## Task List

### Keycard Shell Tests

* fully qualified name: `vac:qa:keycard:2025q3-keycard-testing:shell-tests`
* owner: romanzac
* status: done
* start-date: 2025/07/01
* end-date: 2025/09/01

#### Description
Create a suite of tests that verify that the Keycard Shell works as expected.

#### Deliverables
- Created [test plan](https://www.notion.so/Keycard-Shell-Test-Plan-2298f96fb65c8051b7f6edd281ad3372?source=copy_link)
- Test [results](https://www.notion.so/Keycard-Shell-Test-Results-22b8f96fb65c80faa06fcc195373624b?source=copy_link)
- [issue: shell interoperability tests with wallets](https://github.com/keycard-tech/keycard-shell/issues/81)
- [issue: Malformed data or unsupported format - send transaction](https://github.com/keycard-tech/keycard-shell/issues/145)

### Keycard Shell Tests with Multichain Wallets

* fully qualified name: `vac:qa:keycard:2025q3-keycard-testing:shell-multichain-wallets`
* owner: romanzac
* status: done
* start-date: 2025/07/28
* end-date: 2025/09/01

#### Description
Create a suite of tests that verify that the Keycard Shell works as expected with multichain wallets.

#### Deliverables
- [multi chain wallets results](https://www.notion.so/Keycard-Shell-Test-Results-22b8f96fb65c80faa06fcc195373624b?source=copy_link)
- [remaining OKX wallet test finished with results](https://www.notion.so/Keycard-Shell-Test-Results-22b8f96fb65c80faa06fcc195373624b?source=copy_link)

### Keycard-go Unit Tests

* fully qualified name: `vac:qa:keycard:2025q3-keycard-testing:keycard-go-unit-tests`
* owner: romanzac
* status: not started
* start-date: 
* end-date: 

#### Description
Review existing tests and add more tests to improve coverage. Add debugging tools and test coverage reporting.

#### Deliverables
- PRs and CI runs

### Status-keycard-java Unit Tests

* fully qualified name: `vac:qa:keycard:2025q3-keycard-testing:status-keycard-java-unit-tests`
* owner: romanzac
* status: not started
* start-date: 
* end-date: 

#### Description
Review existing tests and add more tests to improve coverage. Add debugging tools and test coverage reporting.

#### Deliverables
- PRs and CI runs

### Keycard Shell v0.10 Integration Tests

* fully qualified name: `vac:qa:keycard:2025q3-keycard-testing:shell-os-v0.10`
* owner: romanzac
* status: in progress (10%)
* start-date: 2025/08/18
* end-date: 2025/08/29

#### Description
Retest 3rd party wallet integration with Shell OS version 0.10.

#### Deliverables
- PRs and CI runs
