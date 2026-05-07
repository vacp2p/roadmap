---
title: LIP Index Maintenance
tags:
  - 2026q2
  - rfc
  - ift
draft: false
description: Continuous maintenance of lip-index and related publication workflows.
---

`ift-ts:rfc:ift:2026q2-lip-index-maintenance`

## Description

This commitment covers recurring maintenance for the LIP ecosystem:
reviewing updates, keeping references consistent, and handling routine quality improvements.

## Task List

### Maintenance

* fully qualified name: `ift-ts:rfc:ift:2026q2-lip-index-maintenance:maintenance`
* owner: filip/florin
* status: in progress (30%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Maintain lip.logos.co quality through routine review and cleanup tasks
(such as new gitbook addons)
including fixes to
content consistency, metadata, and publication hygiene.
This includes (and is not limited to) fixing any errors found,
adding new rules and features to the website,
as well as any potential improvements discussed by the team(s).

#### Deliverables
- https://github.com/logos-co/logos-lips/pull/319
- https://github.com/logos-co/logos-lips/pull/314
- https://github.com/logos-co/logos-lips/pull/313
- https://github.com/logos-co/logos-lips/pull/312
- https://github.com/logos-co/logos-lips/pull/320


### Review Pipeline

- fully qualified name: `ift-ts:rfc:ift:2026q2-lip-index-maintenance:review-pipeline`
- owner: cofson
- status: in progress (30%)
- start-date: 2026/04/01
- end-date: 2026/06/30

#### Description
This task revolves around
the effort of reviews and support
of all the teams that use the specifications,
this includes (and not limited to)
Blockchain, Storage, Anoncomms, ACZ.

#### Deliverables
- https://github.com/logos-co/logos-lips/pull/303
- https://github.com/logos-co/logos-lips/pull/305
- https://github.com/logos-co/logos-lips/pull/310


### Adversarial Spec - IFT

* fully qualified name: `ift-ts:rfc:ift:2026q2-lip-index-maintenance:adversarial-spec-ift`
* owner: filip
* status: in progress (60%)
* start-date: 2026/04/01
* end-date: 2026/06/30

#### Description

Develop, educate the teams and support the creation
of new specs based on https://github.com/vacp2p/adversarial-spec-ift
while polishing the skill and engaging in relevant workshops in regards to it.

#### Deliverables
- https://github.com/vacp2p/adversarial-spec-ift/pull/1

### COSS Update

* fully qualified name: `ift-ts:rfc:ift:2026q2-lip-index-maintenance:coss-update`
* owner: filip
* status: done
* start-date: 2026/04/01
* end-date: 2026/05/01

#### Description

Based on discussions from Lisbon, do updates of 1/COSS:

- Make Track optional instead of mandatory (informational, core, etc.).
- Introduce a new status: Approved
meaning it has been verified by the internal dev team
and is ready to be moved to the Index.
- Introduce a new document type (in addition to RFC) -
CFR (Change For Request): used to aggregate multiple LIPs
and process their changes together. 
- Miscellaneous fields that are currently mandatory should become optional,
at least temporarily. TBD
- Introduce a new status: Verified
when something has been implemented by a non-IFT entity.

#### Deliverables
- https://github.com/logos-co/logos-lips/pull/308
