---

title: Status QA Mobile
tags:
- "2025q4"
- "qa"
- "status"
draft: false
description: Status QA Mobile

---

`vac:qa:status:2025q4-status-qa-mobile`

## Description

Collaborate with Status team to ensure that the new Status mobile/tablet app behaves as expected.

Extend and adjust the existing E2E test framework to support testing on mobile/tablet.

**Alignment with VAC Narratives:**

- Builds a reliable mobile testing framework for the new Status App, improving internal collaboration and efficiency.

- Maintains quality for internal and external contributions by detecting discrepancies early and closing testing gaps.


## Task List

### Port desktop tests

- fully qualified name: `vac:qa:status:2025q4-status-qa-mobile:port-tests`
- owner: magnus
- status: in progress (30%)
- start-date: 2025/10/01
- end-date: 2025/12/31

#### Description

Port relevant desktop E2E to mobile/tablet Appium tests including:
- messaging (1x1, group)
- communities (category/permissions)
- onboarding sync
- account add/delete
- community pin/unpin

#### Deliverables
- [test: e2e appium/test settings password change password](https://github.com/status-im/status-desktop/pull/18977)

### Test hooks

- fully qualified name: `vac:qa:status:2025q4-status-qa-mobile:introspection`
- owner: magnus
- status: not started
- start-date: 2025/10/01
- end-date: 2025/10/15

#### Description

Investigate how to extend test hooks to reveal more qt properties to help with test capabilities and reliability

#### Deliverables

- PRs / Issues
  

### Android CI workflow & test

- fully qualified name: `vac:qa:status:2025q4-status-qa-mobile:test-ci`
- owner: magnus
- status: in progress (70%)
- start-date: 2025/11/01
- end-date: 2025/11/15

#### Description

Add mobile tests to CI mobile build workflow when the pipeline becomes available

#### Deliverables
- [[Mobile] fix(ci): Android GitHub workflow android-build.yml](https://github.com/status-im/status-desktop/pull/18975)
- [build: add Android x86_64 support to Makefile](https://github.com/status-im/status-go/pull/6990)
- [mobile: add support for browserstack](https://github.com/status-im/status-desktop/issues/19088)

### LambdaTest performance tuning

- fully qualified name: `vac:qa:status:2025q4-status-qa-mobile:lambdatest-performance`
- owner: magnus
- status: not started
- start-date: 2025/11/16
- end-date: 2025/11/30

#### Description

Reduce runtime gap vs local and eliminate avoidable waits/retries.

#### Deliverables

- PRs / Issues


### Multi-device support & parallel sessions

- fully qualified name: `vac:qa:status:2025q4-status-qa-mobile:multi-device-support`
- owner: magnus
- status: not started
- start-date: 2025/12/01
- end-date: 2025/12/20

#### Description

Enable tests that require multiple devices and basic concurrent execution.

#### Deliverables

- PRs / Issues


### Release testing

- fully qualified name: `vac:qa:status:2025q4-status-qa-mobile:release-testing`
- owner: magnus
- status: in progress (10%)
- start-date: 2025/12/01
- end-date: 2025/12/20

#### Description

- Supporting release testing efforts via manual and exploratory testing

#### Deliverables
- Supported test day
- Bug triage calls
