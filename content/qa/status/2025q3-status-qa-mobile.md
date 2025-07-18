---

title: Status QA Mobile
tags:
  - "2025q3"
  - "qa"
  - "status"
draft: false
description: Status QA Mobile

---

`vac:qa:status:2025q3-status-qa-mobile`

## Description
Collaborate with Status team to ensure that the new Status mobile/tablet app behaves as expected.
Extend and adjust the existing e2e test Framework to support testing on mobile/tablet.


**Alignment with VAC Narratives:**
* By helping create a robust mobile testing framework for the new Status App, 
  VAC QA contributes directly to the narrative of internal collaboration and efficiency..
* Helps maintain a high standard for both internal and external contributions 
  by detecting discrepancies early and closing testing gaps.

## Task List

### Framework Adjustments

* fully qualified name: `vac:qa:status:2025q3-status-qa-mobile:framework-adjustments`
* owner: magnus
* status: in progress (15%)
* start-date: 2025/07/01
* end-date: 2025/07/30

#### Description
- Adjust the existing squish Framework to run on mobile/tablet.
- POC: Port at least 1 test to run on mobile/tablet.

#### Deliverables
- Attached Squish to tablet build locally but encountered several [issues regarding locators and driving emulators](https://www.notion.so/Test-automation-for-tablet-builds-Squish-Appium-etc-2288f96fb65c80a5bc44e77bc4349d81?source=copy_link)
- Investigated appium as alternative for tablet build
  - Successully launched a test on a tablet build using LamdaTest virtual devices. 
- Investigated Maestro as an alternative for some use cases 
  -  Successfully attached to app and used AI for navigation
- Started new Appium-based framework (Android-only for now), modeled on existing status-mobile and desktop frameworks.

### Port desktop tests

* fully qualified name: `vac:qa:status:2025q3-status-qa-mobile:port-tests`
* owner: magnus/nastya
* status: in progress (5%)
* start-date: 2025/07/01
* end-date: 2025/09/01

#### Description
- Port all relevant tests to run on mobile/tablet.

#### Deliverables
- built android app on mac locally
- built iOS app on mac locally and on real device as well


### Multiple devices

* fully qualified name: `vac:qa:status:2025q3-status-qa-mobile:multiple-devices`
* owner: magnus
* status: 
* start-date:
* end-date: 

#### Description
- Make necessary changes so that tests can run on different Android and iOS mobile/table devices.

#### Deliverables
- PRs and CI runs
