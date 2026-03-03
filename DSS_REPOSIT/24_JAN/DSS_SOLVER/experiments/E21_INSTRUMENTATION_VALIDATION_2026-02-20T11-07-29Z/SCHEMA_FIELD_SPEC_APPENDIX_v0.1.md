# SCHEMA_FIELD_SPEC_APPENDIX_v0.1

- `input_fingerprint` (string): sha256 of canonical_X + canonical_Y + scope + constraints.
- `manual_override_used` (bool): whether manual override was used in input vector.
- `override_type` (enum|null): override category if manual override is used; otherwise null.
- `normalized_reason_codes` (list[enum]): machine-readable normalized gate reason codes.
- `gatecr_status_mirror` (enum): explicit GateCR tri-state mirror for S08.5/export consistency.
