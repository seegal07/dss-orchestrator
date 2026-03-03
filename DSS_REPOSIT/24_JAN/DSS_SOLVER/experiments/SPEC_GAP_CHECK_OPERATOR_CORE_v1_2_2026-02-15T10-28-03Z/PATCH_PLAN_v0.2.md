# PATCH_PLAN_v0.2

Read-only plan (no patch applied).

## If v1.2 requires retry-aware Operator Core
1. Introduce schema `TEST_VECTOR_SCHEMA_v0.3` (or equivalent new version).
2. Add optional fields (v0.3):
- `step_8_5.iteration_index` (int)
- `step_8_5.retry_allowed` (bool)
- `step_8_5.retry_consumed` (bool)
- `step_8_5.prior_gatecr_status` (enum)
3. Extend GateCR routing logic in `harness/gates_structural.py`:
- On first `SOFT_FAIL` and `retry_allowed=true` and `retry_consumed=false` => route to retry branch (before `Gate9`).
- On subsequent `SOFT_FAIL` => continue to `Gate9` with `PARTIAL` (or policy-defined behavior).
- Preserve existing `HARD_FAIL` immediate `NOT_RUN`.
4. Emit `OPERATOR_ITERATION_LOG` in `harness/harness.py::_export_package()`.
5. Keep historical exemption unchanged via schema gating.

## Acceptance criteria (future)
- First `SOFT_FAIL` with retry flag triggers exactly one retry.
- Second `SOFT_FAIL` does not retry again.
- `HARD_FAIL` remains terminal.
- Historical non-v0.3 runs unchanged.
