---

title: Nim-libp2p maintenance
tags:
  - "2026q3"
  - "p2p"
  - "ift"
draft: false
description: Maintain nim-libp2p through improvements, bug fixes, and user support

---

`ift-ts:p2p:ift:2026q3-nimlibp2p-maintenance`

Maintain nim-libp2p through improvements, bug fixes, and user support

## Description

Continue supporting and maintaining the nim-libp2p repository through ongoing improvements, refactoring, and bug fixes.
This includes a range of ad-hoc tasks critical to sustaining code quality, overall stability, correct functionality,
and performance of the project.
Additionally, it provides a platform for addressing small developer requests,
ensuring that nim-libp2p remains functional and usable for its primary users, Nimbus and Waku, as their needs evolve.

## Task List

### Maintenance

* fully qualified name: `ift-ts:p2p:ift:2026q3-nimlibp2p-maintenance:maintenance`
* owner: rramos/vlado/gabe
* status: in progress (5%)
* start-date: 2026/07/01
* end-date: 2026/09/30

#### Description
Maintain the [nim-libp2p](https://github.com/vacp2p/nim-libp2p) repository via improvements, refactors, and bug fixes.

#### Deliverables
- [status-im/nimbus-eth2#8699](https://github.com/status-im/nimbus-eth2/pull/8699) chore: bump libp2p to 2.1.3
- [vacp2p/nim-libp2p#2745](https://github.com/vacp2p/nim-libp2p/pull/2745) test(pubsub): cover stale peer cleanup after dropped connection
- [vacp2p/nim-boringssl#11](https://github.com/vacp2p/nim-boringssl/pull/11) chore(ci): test PR against nim-libp2p and nim-lsquic
- [vacp2p/nim-libp2p#2737](https://github.com/vacp2p/nim-libp2p/pull/2737) fix(connmanager): avoid late Joined after peer drop
- [vacp2p/nim-libp2p#2734](https://github.com/vacp2p/nim-libp2p/pull/2734) fix(peerstore): keep connected peer addresses from expiring
- [vacp2p/nim-libp2p#2729](https://github.com/vacp2p/nim-libp2p/pull/2729) fix(pubsub): avoid sink params for small RPC fields
- [vacp2p/nim-libp2p#2716](https://github.com/vacp2p/nim-libp2p/pull/2716) feat(ci): allow selecting nim-libp2p ref for dependency bumps and disabling scheduled run
- [vacp2p/nim-libp2p#2719](https://github.com/vacp2p/nim-libp2p/pull/2719) fix(autotls): decouple ACME RSA keys from libp2p identity schemes
- [status-im/nimbus-eth2#8536](https://github.com/status-im/nimbus-eth2/pull/8536) chore: bump libp2p to 2.1.2
- [vacp2p/nim-libp2p#2699](https://github.com/vacp2p/nim-libp2p/pull/2699) fix(autotls): release certificate keys after CSR generation
- [vacp2p/boringssl#6](https://github.com/vacp2p/boringssl/pull/6) chore: sync BoringSSL upstream
- [vacp2p/nim-lsquic#96](https://github.com/vacp2p/nim-lsquic/pull/96) fix: leaks
- [vacp2p/nim-libp2p#2687](https://github.com/vacp2p/nim-libp2p/pull/2687) fix(tests): remove chronicles import hacks
- [vacp2p/nim-libp2p#2693](https://github.com/vacp2p/nim-libp2p/pull/2693) chore(ci): add mm to the job names
- [vacp2p/nim-libp2p#2647](https://github.com/vacp2p/nim-libp2p/pull/2647) chore(pubsub): adjust incoming message validation order
- [vacp2p/nim-libp2p#2670](https://github.com/vacp2p/nim-libp2p/pull/2670) fix(connmanager): emit Joined before trimming new peers
- [vacp2p/nim-libp2p#2742](https://github.com/vacp2p/nim-libp2p/pull/2742) test: utilize new switch builder with multiple addresses
- [vacp2p/nim-libp2p#2740](https://github.com/vacp2p/nim-libp2p/pull/2740) fix(test): use captured variable for closure
- [vacp2p/nim-libp2p#2724](https://github.com/vacp2p/nim-libp2p/pull/2724) fix(gossipsub): sending duplicate IHAVE
- [vacp2p/nim-libp2p#2739](https://github.com/vacp2p/nim-libp2p/pull/2739) ci(daily): remove concurrent test job
- [vacp2p/nim-libp2p#2728](https://github.com/vacp2p/nim-libp2p/pull/2728) ci: avoiding cache for trivial jobs
- [vacp2p/nim-libp2p#2730](https://github.com/vacp2p/nim-libp2p/pull/2730) ci: only save build cache on master
- [vacp2p/nim-libp2p#2721](https://github.com/vacp2p/nim-libp2p/pull/2721) ci: force save build cache
- [vacp2p/nim-libp2p#2707](https://github.com/vacp2p/nim-libp2p/pull/2707) ci: add line trace
- [vacp2p/nim-libp2p#2715](https://github.com/vacp2p/nim-libp2p/pull/2715) ci: add build cache to workflows
- [vacp2p/nim-libp2p#2709](https://github.com/vacp2p/nim-libp2p/pull/2709) ci: rework test workflow
- [vacp2p/nim-libp2p#2747](https://github.com/vacp2p/nim-libp2p/pull/2747) chore(readme): update badge link of test workflow
- [vacp2p/nim-libp2p#2743](https://github.com/vacp2p/nim-libp2p/pull/2743) ci: add build prerequisites to daily with no flags
- [vacp2p/nim-libp2p#2738](https://github.com/vacp2p/nim-libp2p/pull/2738) ci: force save cache
- [vacp2p/nim-libp2p#2701](https://github.com/vacp2p/nim-libp2p/pull/2701) ci: i386 temp workflow
