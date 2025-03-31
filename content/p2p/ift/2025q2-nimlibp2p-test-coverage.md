---

title: nim-libp2p Test Coverage
tags:
  - "2025q2"
  - "p2p"
  - "ift"
draft: false
description: nim-libp2p Test Coverage

---

`vac:p2p:ift:2025q2-nimlibp2p-test-coverage`


nim-libp2p Improved Test Coverage

## Description
Work closely with the QA and DST teams to identify key areas for improvement in the release and testing of nim-libp2p,
ensuring better test coverage and reliability. 


## Task List

### Improve DST test node

* fully qualified name: `vac:p2p:ift:2025q2-test-coverage:dst-test-node`
* owner:
* status: not started
* start-date:
* end-date: 

#### Description
DST uses this [node](https://github.com/vacp2p/dst-gossipsub-test-node/blob/dockerized/main.nim) to do regression testing 
on each libp2p release. DST team has suggested that we collaborate in the refactoring of the node to allow custom test 
scenarios via specifying arguments/flags:
- Choose the multiplexer to use without having to recompile
- Number of nodes to connect to
- Message Ratio
- Message Weight
- Connection parameters (currently all nodes try to connect to other N nodes)
- External script for message injection instead of cron job

#### Deliverables



### QA Consulting over test coverage

* fully qualified name: `vac:p2p:ift:2025q2-test-coverage:qa-consulting`
* owner:
* status: not started
* start-date:
* end-date: 

P2P provides consulting and support to QA by addressing queries, reviewing, formulating and designing strategies to test 
nim-libp2p more effectively, as well as offering guidance on resolving coding challenges that may arise during the 
development of the test units.

#### Deliverables



### Improve CI performance

* fully qualified name: `vac:p2p:ift:2025q2-test-coverage:ci-performance`
* owner:
* status: not started
* start-date:
* end-date: 

Currently the test units take ~50m to complete, which is somewhat excessive, specially compared to other implementations.
With this commitment we will look into techniques and resources available that could improve the efficiency of the CI tests 
to reduce the time it takes for Pull Requests to complete all checks. Investigate whether it's possible to run tests in parallel,
use the ooutput of `vac:p2p:ift:2025q2-nimlibp2p-transport:memory-transport` to remove network components from the tests that 
do not need it, review the timeout lengths, as well as using runners with better perfomance.  

#### Deliverables

