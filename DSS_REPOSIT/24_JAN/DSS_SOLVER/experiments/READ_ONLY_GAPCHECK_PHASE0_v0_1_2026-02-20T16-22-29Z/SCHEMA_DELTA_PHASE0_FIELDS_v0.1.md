# SCHEMA_DELTA_PHASE0_FIELDS_v0.1

Minimal top-level fields to add (names only):
- `phase0_enabled`
- `phase0_verdict`
- `phase0_reason_code`
- `system_scope`
- `X_param`
- `Y_param`
- `tension_direction`
- `constraints`
- `conflict_type_candidate`
- `canonical_hash`
- `raw_hash`
- `trace`
- `trace_count`
- `confidence_summary`
- `input_fingerprint`

Compatibility plan (historical vectors):
- Gate by `schema_version` and/or `phase0_enabled=true`.
- For historical vectors: Phase0 not executed, behavior unchanged.
- Existing compatibility precedent:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`_is_pfl_enabled`, schema/version checks)
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.5.md` (versioned additive approach).
