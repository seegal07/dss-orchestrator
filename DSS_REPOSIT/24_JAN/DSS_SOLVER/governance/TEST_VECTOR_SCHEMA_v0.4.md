# TEST_VECTOR_SCHEMA_v0.4

Status: GateCR PASS integrity extension for loop risk-shift detection.
Backward compatibility: vectors with `schema_version < 0.4` are exempt from `search_loop` enforcement.

## Required field for schema_version >= 0.4
- `step_8_5.search_loop`: boolean `TRUE|FALSE`

## Enforcement rule
- If `schema_version >= 0.4` and `step_8_5.search_loop == TRUE`:
  - `risk_shift_detected = TRUE`
  - GateCR verdict cannot be `PASS`
  - If GateCR would be `PASS`, it must be downgraded to `SOFT_FAIL`

## Historical exemption
- If `schema_version < 0.4` OR `step_8_5.search_loop` is absent in historical vectors:
  - this rule is not enforced retroactively
