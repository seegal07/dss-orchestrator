# ACTIVE_SET_INDEX

## Active schema(s)
- Historical/default test vectors still mostly point to: `canon/TEST_VECTOR_SCHEMA_v0.1.md.docx` (via `canon_versions.schema` inside test YAML files).
- Operator Core enable schema (new): `governance/TEST_VECTOR_SCHEMA_v0.2.md`.
- Runtime switch location: `harness/gates_structural.py` in `_is_operator_core_enabled()`.
- Rule: GateCR active only when `canon_versions.schema` contains `TEST_VECTOR_SCHEMA_v0.2` (or explicit `operator_core_enabled=true`).

## Governance specs actually used by harness
- Direct machine-loaded governance file(s): none.
- Harness behavior is code-defined in:
  - `harness/harness.py`
  - `harness/gates_structural.py`
- Governance files are reference SoT for humans/architecture alignment, not parsed at runtime.

## Active operator-core templates
- `templates/operator_core/S08_5_OPERATOR_PROMPT.md`
- `templates/operator_core/S08_5_OPERATOR_OUTPUT.md`
- `templates/operator_core/GATECR_RECORD.md`
- `templates/operator_core/S12_DECISION_RECORD_TEMPLATE_v1.1.md`

## Active gate set and registration
- Structural: `Gate0..Gate14` in `harness/gates_structural.py`.
- TRIZ: `GateTRIZ` appended in `harness/harness.py` after structural/assisted processing.
- Operator Core: `GateCR` inserted before Gate9 in `run_structural_gates()` when schema flag enables it.
- Addon: `Gate15..Gate18` computed in `harness/harness.py` when addon answers provided.
