**Juan**:
Last week:

- `ift:2025q1-nimble`
    - Research an propone a fix for https://github.com/status-im/nim-metrics/pull/98
    - Research and propone a fix for https://github.com/status-im/nim-json-serialization/pull/136
    - Research multiple nwaku issues
    - Interview Chris
    - Interview Constantine
  - fixes #1483 Infinite Reading official package list (https://github.com/nim-lang/nimble/pull/1494)
  - Fixes #1432: Missing package name in warning (https://github.com/nim-lang/nimble/pull/1492)
  - Fix tempDir causing git checkout failures in tag processing loop (https://github.com/nim-lang/nimble/pull/1490)
  - Fixes global nim install to update symlink to the correct version (https://github.com/nim-lang/nimble/pull/1488)

This week:
 - Research why https://github.com/status-im/nim-metrics/pull/98 works for Nim 2.x if it supposed to dont have any config.nims file
 - Improve the way the include.paths is generated/updated
 - Continue researching/assisting nwaku as lib
 - Continue work towards 1.0 if there is time left
Blockers:

**Esteban**:
Last week:

- `vac:nim:ift:2025q3-nim-core-libs:nim-cbor-serialization`
  - Add regression tests to `nim-serialization` "Test generic suite" (used by cbor) https://github.com/status-im/nim-serialization/pull/110
  - Support nested tests at comptime in `nim-unittest2` (used by cbor) https://github.com/status-im/nim-unittest2/pull/59
  - Improve checkpoint output at comptime in `nim-unittest2` (used by cbor) https://github.com/status-im/nim-unittest2/pull/60
- `vac:nim:ift:2025q3-nim-core-libs:nim-confutils`
    - Remove `-d:nimOldCaseObjects` requirement https://github.com/status-im/nim-confutils/pull/117
- Release `nim-json-serialization` v0.4.4 https://github.com/status-im/nim-json-serialization/pull/138

This week:
- Avoid using `{.cast(uncheckedAssign).}` in nim-confutils
- Document nim-serialization extension points

Blockers: