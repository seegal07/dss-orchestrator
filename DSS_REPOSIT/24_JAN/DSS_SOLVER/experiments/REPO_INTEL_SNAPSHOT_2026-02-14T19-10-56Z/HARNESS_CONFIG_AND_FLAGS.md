# HARNESS_CONFIG_AND_FLAGS

## Flags/knobs affecting Operator Core routing
- Schema enablement for GateCR:
  - location: `tc.canon_versions.schema`
  - condition: contains `TEST_VECTOR_SCHEMA_v0.2`
  - implementation: `harness/gates_structural.py::_is_operator_core_enabled`

- Historical-run exemption:
  - behavior: if schema != v0.2 and no `operator_core_enabled=true`, GateCR is skipped
  - effect: legacy vectors run old path (no retroactive GateCR)

- GateCR tri-state status:
  - produced by: `gatecr_operator_core()`
  - values: `PASS | SOFT_FAIL | HARD_FAIL`

- NOT_RUN propagation:
  - trigger: GateCR `HARD_FAIL`
  - scope: `Gate9..Gate14` -> `NOT_RUN`
  - reason literal: `structural resolution not found`

- compromise_mode enforcement:
  - trigger: GateCR `SOFT_FAIL`
  - rule: `step_12.compromise_mode` must be `true`
  - implementation: `gate12_decision_record(... gatecr_status='SOFT_FAIL' ...)`

- Overall run status mapping:
  - `HARD_FAIL` present => `FAIL`
  - `SOFT_FAIL` present => `PARTIAL`
  - implementation: `harness/harness.py::_overall_status`

- Addon strictness (independent of GateCR):
  - CLI flag: `--addon-strict`
  - when enabled, addon gate results are decision-critical.
