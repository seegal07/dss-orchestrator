# SCHEMA_FIELD_SPEC_APPENDIX_v0.1

- `input_fingerprint` (string): sha256(canonical_X + canonical_Y + scope + constraints).
- `manual_override_used` (boolean): manual override usage flag from input vector.
- `override_type` (string|null): override category when manual_override_used=true, otherwise null.
- `normalized_reason_codes` (list[string]): normalized gate reason codes for machine checks.
- `gatecr_status_mirror` (enum): GateCR tri-state mirrored in S08.5 export and case instrumentation.
