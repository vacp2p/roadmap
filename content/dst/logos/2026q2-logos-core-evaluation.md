---
title: Logos-core Evaluation
tags:
  - "2026q2"
  - "dst"
  - "logos"
draft: false
description: "Perform integration scenarios in logos core
with different components and evaluate their behaviour."
---

`ift-ts:dst:logos:2026q2-logos-core-evaluation`


## Description

Realize integration scenarios in logos core with
different components and evaluate their behavior.
Scenarios should work independently with each component,
while also work in a full stack manner.
These componentes are logos-messaging, logos-storage and logos-blockchain.

## Task list

### logos-core evaluation
* fully qualified name: `ift-ts:dst:logos:2026q2-logos-core-evaluation:evaluation`
* owner: Pearson
* status: in progress (99%)
* start-date: 2026/05/05
* end-date: 2026/06/30

#### Description
Integrate logos-core in the DST lab, evaluating its behaviour.
Take as an example [logos-integration-test-framework](https://github.com/logos-messaging/logos-integration-test-framework)
and check if this could be reused or we need to add this functionality in 10ksim.
This is supposed to be working with [logos-logoscore-py](https://github.com/logos-co/logos-logoscore-py).
In order to better have an idea of how it will work, add logos-delivery(waku) to logos core.
No need to evaluate logos-delivery. Just start the integration and report issues or missing functionalitys that we might 
need to do our experiments.

#### Deliverables
- Code:
  - Added Dockerfile scripts so StatefulSets automatically create their secrets.
  - Integrated logos-core with pod-api-requester for Kubernetes secret token retrieval and arbitrary function calls.
  - [vacp2p/10ksim#301](https://github.com/vacp2p/10ksim/pull/301) logos core builder changes
- Reports:
  - https://app.notion.com/p/Work-in-Progress-logos-core-10ksim-integration-36b8f96fb65c801bab58d1124fefa2b4


### logos-messaging
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q2-logos-core-evaluation:logos-messaging`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Add logos-messaging component into the evaluation.
Realize the same scenarios and reports as in `evaluation` task.

#### Deliverables
- Reports:
- Related PRs if apply:


### logos-storage
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q2-logos-core-evaluation:logos-storage`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Add logos-storage component into the evaluation.
Realize the same scenarios and reports as in `evaluation` task.


#### Deliverables
- Code:
- Reports:


### logos-blockchain
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q2-logos-core-evaluation:logos-blockchain`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Add logos-blockchain component into the evaluation.
Realize the same scenarios and reports as in `evaluation` task.

#### Deliverables
- Code:
- Reports:


### full stack
> *Note*: This needs more input from project
* fully qualified name: `ift-ts:dst:logos:2026q2-logos-core-evaluation:full-stack`
* owner: TBD
* status: not started
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Add all components into the evaluation.
Realize the same scenarios and reports as in `evaluation` task.


#### Deliverables
- Code:
- Reports:
