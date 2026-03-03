# SPEC_GAP_REPORT_v0.2

Scope: read-only gap check for Operator Core v1.2 questions against current implementation.

1. Is `iteration_index` already supported in `TEST_VECTOR_SCHEMA_v0.2`?
- No.
- `governance/TEST_VECTOR_SCHEMA_v0.2.md` does not define `iteration_index` (or any GateCR retry counter fields).

2. Can GateCR differentiate first and subsequent `SOFT_FAIL`?
- No.
- `harness/gates_structural.py::gatecr_operator_core()` returns tri-state only and has no stateful retry context.
- No persistence key is read (e.g., `iteration_index`, `retry_count`, `prior_gatecr_status`).

3. Where to insert `OPERATOR_ITERATION_LOG` emission?
- Primary insertion point: `harness/harness.py::_export_package()` alongside current `GATECR_RECORD.md` export.
- Optional secondary insertion: after GateCR evaluation in `harness/gates_structural.py::run_structural_gates()` if runtime-only log is needed before export.

4. Does routing allow `RETRY_ONCE` before S09?
- No.
- Current routing in `run_structural_gates()` is:
  - `HARD_FAIL` => immediate `NOT_RUN` for `Gate9..Gate14`.
  - `SOFT_FAIL` => continue directly to `Gate9`.
- No branch/state for `RETRY_ONCE` exists in routing tables or code.

5. Any conflict with harness reachability rules?
- Yes, if `RETRY_ONCE` is added without control-flow patch.
- Existing reachability is deterministic and single-pass. A retry path would require explicit new branch before `Gate9` and clear termination guards.

6. Any schema migration needed?
- Yes, if v1.2 requires explicit retry/iteration semantics.
- Minimal additions would need a new schema version (do not mutate v0.2 in place if backward integrity is required).

7. Backward compatibility with historical runs?
- Yes, currently preserved.
- GateCR enablement is schema-flag based (`_is_operator_core_enabled` checks `TEST_VECTOR_SCHEMA_v0.2`).
- Historical vectors without v0.2 remain GateCR-exempt.
