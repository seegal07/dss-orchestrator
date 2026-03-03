# TEMPLATE_RESOLUTION_RULES

## How templates are selected
- Current harness does not resolve template files by path/version at runtime.
- Runtime exports artifacts directly from `full_vector` content (JSON-to-markdown dump style).
- Template files under `templates/operator_core/` are currently reference assets for authoring/process, not executable render templates.

## Path and naming behavior
- Artifact export filenames are hardcoded in `harness/harness.py`:
  - `S08_5_OPERATOR_PROMPT.md`
  - `S08_5_OPERATOR_OUTPUT.md`
  - `GATECR_RECORD.md`
  - plus existing S00..S14 exports.

## Versioning behavior
- No dynamic template version resolution in harness.
- Effective versioning is implicit through:
  - schema flag (`TEST_VECTOR_SCHEMA_v0.2`), and
  - template filename conventions.

## Missing-template fallback behavior
- Missing files in `templates/operator_core/` do not affect harness run (not loaded).
- Missing required step data in input vector triggers gate FAIL/SOFT_FAIL/HARD_FAIL according to gate logic.
