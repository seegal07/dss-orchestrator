# TEST_VECTOR_SCHEMA_v0.5
Status: Instrumentation extension only (ZERO_LOGIC_CHANGE).
Backward compatibility: vectors with `schema_version < 0.5` remain valid; behavior of PFL/GateCR/routing unchanged.

## Purpose
Add machine-readable Stage A instrumentation fields for deterministic auditability.

## Added Instrumentation Fields
- `input_fingerprint`: string (sha256), deterministic hash of canonical_X + canonical_Y + scope + constraints.
- `manual_override_used`: boolean (`TRUE|FALSE`).
- `override_type`: enum string or `NULL`.
- `normalized_reason_codes`: list of normalized machine-readable reason codes.
- `gatecr_status_mirror`: enum (`PASS|SOFT_FAIL|HARD_FAIL|NOT_APPLICABLE`) mirrored into S08.5 export payload.

## Scope
- Instrumentation/export only.
- No changes to PFL logic.
- No changes to GateCR logic.
- No changes to routing/state-machine.

## Notes
- `override_type` MUST be `NULL` when `manual_override_used=FALSE`.
- `gatecr_status_mirror` duplicates GateCR tri-state for cross-artifact consistency checks.
