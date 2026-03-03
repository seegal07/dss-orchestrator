# SCHEMA_DELTA_PFL_FIELDS_v0.1

## Minimal pfl_* fields to add (names only)
- `pfl_verdict`
- `pfl_reason`
- `pfl_attempt_index`
- `pfl_x`
- `pfl_y`
- `pfl_conflict_type_candidate`
- `pfl_structural_tension`

## Compatibility risk with existing vectors
- Current vectors contain none of the above fields (search evidence: no matches across `DSS_SOLVER/*.json|*.yaml`).
- Backward-compatibility impact:
  - If fields are mandatory without version flag/exemption -> historical vectors will fail.
  - If introduced as versioned optional fields (PFL-enabled runs only) -> historical vectors remain valid.
- Additional note:
  - Existing schema v0.2 currently models Operator Core only (`step_8_5` + `step_12.compromise_mode`); no PFL contract section exists yet.
