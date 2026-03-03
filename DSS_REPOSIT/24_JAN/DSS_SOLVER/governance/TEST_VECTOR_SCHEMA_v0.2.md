# TEST_VECTOR_SCHEMA_v0.2

Status: Operator Core enabled schema extension for S08.5 + GateCR routing.
Backward compatibility: v0.1 vectors remain valid historical runs and are GateCR-exempt.

## Enablement Flag
- `canon_versions.schema` MUST include `TEST_VECTOR_SCHEMA_v0.2` to enable GateCR.

## New fields (full_vector)

### step_8_5
- `operator_selected`: enum `SEPARATION | MEDIATOR | LEVEL_SHIFT | DEPENDENCY_INVERSION`
- `detected_conflict_types`: list of conflict types (values from `A|B|C|D`)
- `dominant_conflict_type`: single value from `A|B|C|D`
- `transformed_conflict_frame`: string
- `what_changed_structurally`: string
- `structural_resolution_confirmed`: boolean
- `separation_illusion_test`: boolean
- `assisted_matrix`: list (expected 5 checks with `question_id` + `answer=YES|NO`)
- `gatecr_status`: enum `PASS|SOFT_FAIL|HARD_FAIL` (optional prefilled; runtime source of truth is harness result)
- `hard_fail_message`: string (required when `gatecr_status=HARD_FAIL`, exact canonical literal)
- `operator_prompt`: object/string (optional, for artifact trace)

### step_12
- `compromise_mode`: boolean
  - mandatory `true` when `GateCR=SOFT_FAIL`

## GateCR routing outputs
- `gatecr_status`: tri-state only (`PASS|SOFT_FAIL|HARD_FAIL`)
- `hard_fail_message`: exact `structural resolution not found` on `HARD_FAIL`
- `compromise_mode=true` enforced in S12 for `SOFT_FAIL`

## Hard fail canonical literal
- `structural resolution not found`
