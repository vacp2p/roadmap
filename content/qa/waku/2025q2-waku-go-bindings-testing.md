---
title: waku-go-bindings Testing 
tags:
  - "2025q2"
  - "qa"
  - "waku"  
draft: false  
description: Expand protocol coverage for waku-go-bindings 
---

`vac:qa:waku:2025q2-waku-go-bindings-testing`

## Description
Expand protocol coverage for `waku-go-bindings` with filter and lightpush tests.

The framework should cover those protocols as they are covered in `waku-interop-tests`

**Alignment with VAC Narratives:**

* The VAC QA team plays a key role in supporting internal collaboration
  and efficiency across projects by ensuring the quality of Nwaku Go Bindings
  and the sunsetting of go-waku.
* By finding issues in specs during testing,
  VAC strengthens the RFC culture,
  contributing to continuous improvement and community engagement.

## Task List

### Filter Protocol Testing

* fully qualified name: `vac:qa:waku:2025q2-waku-go-bindings-testing:filter`
* owner: aya
* status: not started
* start-date: 
* end-date: 

#### Description
Add test coverage by implementing tests for the filter protocol.
These tests should mirror the approach used in `waku-interop-tests`
and ensure reliable message propagation across multiple nodes.

#### Deliverables
PRs and issues

### Lightpush Protocol Testing

* fully qualified name: `vac:qa:waku:2025q2-waku-go-bindings-testing:lightpush`
* owner: aya
* status: not started
* start-date: 
* end-date: 

#### Description
Add test coverage by implementing tests for the lightpush protocol.
These tests should mirror the approach used in `waku-interop-tests`
and ensure reliable message propagation across multiple nodes.

#### Deliverables
PRs and issues

### Maintenance

* fully qualified name: `vac:qa:waku:2025q2-waku-go-bindings-testing:maintenance`
* owner: aya
* status: in progress (30%)
* start-date: 2025/04/01
* end-date: 2025/06/30

#### Description
Ongoing maintenance of Waku go bindings tests. 
This includes updating tests for changes in the bindings or in `nwaku`, addressing regressions, 
investigating and resolving issues, and implementing minor improvements to the testing framework as needed.

#### Deliverables
- [bug: High-Throughput Test Hangs or Fails Beyond 1024 Iterations](https://github.com/waku-org/waku-go-bindings/issues/65)
- [bug: Node Doesn’t Fully Shut Down After Test Completion (Rendezvous & AutoNAT Tasks Keep Running)](https://github.com/waku-org/waku-go-bindings/issues/64) 
- Increase endurance tests iterations after the fix in [PR](https://github.com/waku-org/waku-go-bindings/pull/62)

### 12H Longevity

* fully qualified name: `vac:qa:waku:2025q2-waku-go-bindings-testing:12hlongevity`
* owner: aya
* status: not started
* start-date: 2025/04/03
* end-date: 2025/04/15

#### Description
Create a github actions workflow that runs on self hosted infra 
and can run a 12 hour longevity test.

#### Deliverables
- PR and CI run
