# TEST_VECTOR_SCHEMA_v0.3

Status: PFL-enabled schema extension before S04.
Backward compatibility: vectors with schema_version < 0.3 and without `pfl_enabled=true` are PFL-exempt.

## PFL activation rule
PFL is executed only if at least one condition is true:
- `schema_version >= 0.3`
- `pfl_enabled = true`
- `canon_versions.schema` contains `TEST_VECTOR_SCHEMA_v0.3`

## Top-level PFL fields (no nested step object)
- `pfl_enabled`: boolean (optional, default false)
- `pfl_verdict`: enum `PASS|FAIL`
- `pfl_reason`: enum `NONE|INVALID_DUAL_TENSION|NO_MUTUAL_DEGRADATION|OUT_OF_SCOPE|SYMPTOM_FRAMING|TRIVIAL_CONFLICT|SOLUTION_AS_XY`
- `pfl_attempt_index`: integer `1..3`
- `pfl_structural_tension`: boolean
- `pfl_conflict_type_candidate`: enum `causal|temporal|interaction|scale`
- `pfl_X`: string
- `pfl_Y`: string

## Terminal fail behavior
If `pfl_verdict=FAIL` on `pfl_attempt_index=3`, terminal fail message must be exactly:
- `structural contradiction not formulated`

On terminal PFL fail:
- Gate4..Gate14 = NOT_RUN
- pipeline stops before Operator Layer / GateCR

## Coexistence with v0.2 fields
- All v0.2 Operator Core fields remain valid and unchanged.
- This document extends v0.2 with top-level PFL admission fields only.
