---
title: Waku Interop Testing
tags:
  - "2025q1"
  - "qa"
  - "waku"  
draft: false  
description: Maintain and ensure the reliability of Waku interop tests.
---

`vac:qa:waku:2025q1-interop-testing`

## Description
Maintain and ensure the continued reliability of the Waku interop testing framework. 
This includes addressing regressions, adapting to changes in `nwaku` and `gowaku`, 
and performing minor improvements to keep the framework functional and effective.

**Alignment with VAC Narratives:**

* The VAC QA team supports internal collaboration and efficiency by maintaining the quality and reliability of the Waku interop framework.

## Task List

### Maintenance

* fully qualified name: `vac:qa:waku:2025q1-interop-testing:maintenance`
* owner: fbarbu15
* status: done
* start-date: 2025/01/01
* end-date: 2025/03/31

#### Description
Ongoing maintenance of Waku interop tests. 
This includes updating tests for changes in `nwaku` or `gowaku`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
* [bug: SQL logic error table Message has no column named storedAt](https://github.com/waku-org/nwaku/issues/3243)
* [bug: wakuorg/nwaku:latest node fails to start for RLN tests](https://github.com/waku-org/nwaku/issues/3247)
* [bug: nwaku<->gowaku interop tests started failing at filter subscription](https://github.com/waku-org/nwaku/issues/3263)
* [chore: store fixes](https://github.com/waku-org/waku-interop-tests/pull/101)
* [chore: add reconciliation metrics](https://github.com/waku-org/waku-interop-tests/pull/100)
* [bug: nwaku<->gowaku interop tests fail with only one received message push when multiple messages are sent](https://github.com/waku-org/nwaku/issues/3271)
* [chore: js-waku test report improvements](https://github.com/waku-org/js-waku/pull/2247)
* [chore: store hash fixes](https://github.com/waku-org/waku-interop-tests/pull/104)
* [chore: Skip all RLN tests due to problems with registration](https://github.com/waku-org/waku-interop-tests/pull/107)
* [bug: Waku requests rejected by Infura RPC provider - not EIP-155 compliant](https://github.com/waku-org/nwaku/issues/3313)
* [chore: fix Overall job result](https://github.com/waku-org/waku-interop-tests/pull/108)
* [chore: RLN Metric rename](https://github.com/waku-org/waku-interop-tests/pull/109)
