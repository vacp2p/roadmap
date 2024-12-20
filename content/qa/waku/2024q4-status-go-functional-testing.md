---
title: Status Go Functional Testing
tags:
  - "2024q4"
  - "qa"
  - "waku"  
draft: false  
description: Collaborate with Status QA in creating a test framework that uses status-backend
  to do functional testing for status go, by integrating existing Status CLI tests into it.
---

`vac:qa:waku:2024q4-status-go-functional-testing`

## Description
Collaborate with Status QA in creating a test framework that uses status-backend
to do functional testing for status go,
by integrating existing Status CLI tests into it.

The Status Go devs have created a [new tool](https://github.com/status-im/status-go/pull/5847)
for functional testing of Status Go features.
Status QA and VAC QA will collaborate to build a testing framework around this tool
and add new test coverage through this framework.
In the beginning, Status QA will move the statusd tests,
while VAC QA will integrate the status-cli tests to set up the framework.
After that, VAC QA will be responsible for the message tests,
though this is still to be determined.
The tests should validate Status features under normal and abnormal conditions and usage.
We will track test coverage to measure progress.

**Alignment with VAC Narratives:**
- By helping create a robust functional testing framework for Status Go,
  VAC QA contributes directly to the narrative of internal collaboration and efficiency.
- Additionally, it aligns with the goal of fostering a strong RFC culture
  by ensuring the tests provide valuable feedback for maintaining high standards in the specifications.

## Task List

### Migrate to Status Backend

* fully qualified name: `vac:qa:waku:2024q4-status-go-functional-testing:migrate-to-status-backend`
* owner: fbarbu15
* status: done
* start-date: 2024/10/07
* end-date: 2024/11/11

#### Description
Update the existing tests to use status-backend and ensure alignment
with the Status Go testing framework.
The existing Status Go tests created by VAC QA and Status QA
have been using the status-cli or statusd tools, which are primarily CLI-based.
Now, developers want to replace them with status-backend,
a more advanced tool with a JSON-RPC based approach.
Move all the tests we developed into the status-go repo
since Status QA has started a similar effort using Python.

#### Deliverables
PRs:
* https://github.com/status-im/status-go/pull/6119
* https://github.com/status-im/status-go/pull/6225
* https://github.com/status-im/status-go/pull/6167
* https://github.com/status-im/status-go/pull/6212

CI:
* https://ci.status.im/blue/organizations/jenkins/status-go%2Fprs%2Ftests-rpc/detail/PR-6225/9/pipeline

### Message tests

* fully qualified name: `vac:qa:waku:2024q4-status-go-functional-testing:message-tests`
* owner: fbarbu15
* status: not started
* start-date: 2024/11/11
* end-date: 2024/11/25

#### Description
It seems that the intention is for message-related tests to be handled
by the Waku/VAC team, but this is still to be confirmed, so this task may change.

#### Deliverables
* PR with the new tests

