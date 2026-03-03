# TEST_VECTOR_SCHEMA_v0.6
Status: Phase0 minimal integration (backward-compatible)
Backward compatibility: historical vectors default to `phase0_enabled=false` and remain valid.

## Purpose
Introduce Phase0 canonical formalization fields before PFL admission without changing GateCR logic, tri-state logic, or engine behavior.

## Activation
- `phase0_enabled`: boolean
- Default for historical vectors: `false`

## Added top-level fields
- `phase0_enabled` (bool)
- `phase0_verdict` (`PASS|FAIL`)
- `phase0_reason_code` (`AMBIGUOUS_INTENT|INSUFFICIENT_SCOPE|MECHANISM_ONLY_INPUT|OTHER|NONE`)
- `canonical_hash` (string)
- `raw_hash` (string)
- `phase0_trace` (list)
- `canonical_scope` (string)
- `canonical_X` (string)
- `canonical_Y` (string)
- `canonical_constraints` (list)
- `canonical_conflict_type_candidate` (`causal|temporal|interaction|scale`)

## Admission input contract
When `phase0_enabled=true`, PFL must consume canonical fields only:
- `canonical_X`
- `canonical_Y`
- `canonical_constraints`
- `canonical_scope`

## Policy notes
- `SOLUTION_AS_XY` applies to canonical fields only.
- No mutation of historical vectors required.
- No tri-state/GateCR logic changes in this schema revision.
