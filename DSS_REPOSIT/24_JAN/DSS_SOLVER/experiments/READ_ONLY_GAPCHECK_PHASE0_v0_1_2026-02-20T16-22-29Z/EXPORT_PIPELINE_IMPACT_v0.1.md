# EXPORT_PIPELINE_IMPACT_v0.1

Current export writer (reference):
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
  - `_export_package(...)`
  - `_write_gate_logs(...)`

Where machine-readable fields should appear (if implemented later):
1. `case.json.instrumentation`
- Existing pattern already used for machine fields (fingerprint/override/reason codes).

2. Stage artifact file
- Existing PFL artifact slot: `artifacts/S03_5_PFL_OUTPUT.md` (JSON payload block).
- Phase0 can be exported as dedicated artifact (e.g. `S03_0_PHASE0_OUTPUT.md`) or structured extension in existing admission artifact set.

3. `gate_log.json` and `gate_summary.json`
- Existing normalized reason code path already present.
- Phase0 verdict/reason can be mirrored in summary for deterministic audits.

How to ensure machine-readable fields appear:
- Write fields through a single export surface (`_export_package`) and include in manifest-tracked files.
- Keep fields as JSON scalars/arrays (no prose-only fields).

No runtime execution performed in this audit.
