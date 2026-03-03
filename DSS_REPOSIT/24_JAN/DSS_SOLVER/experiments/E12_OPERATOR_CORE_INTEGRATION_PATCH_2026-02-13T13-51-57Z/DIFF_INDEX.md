# DIFF_INDEX

## Code impact map

### 1) Gate insertion and routing
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
- Key additions:
  - `CANONICAL_HARD_FAIL_MESSAGE`
  - `_is_operator_core_enabled()`
  - `gatecr_operator_core()`
  - GateCR wiring in `run_structural_gates()` before Gate9.
  - S09–S14 NOT_RUN propagation block for `GateCR=HARD_FAIL`.

### 2) Run-level status and export layer
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- Key additions:
  - `_build_step_map()` support for `step_8_5`.
  - `_overall_status()` mapping for `HARD_FAIL` and `SOFT_FAIL`.
  - Gate log typing and pipeline-step mapping for GateCR.
  - S08.5/GateCR artifact exports.

### 3) Schema/template assets
- New schema: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.2.md`
- New templates:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S08_5_OPERATOR_PROMPT.md`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S08_5_OPERATOR_OUTPUT.md`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/GATECR_RECORD.md`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S12_DECISION_RECORD_TEMPLATE_v1.1.md`

## Useful re-check commands
- `python3 /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py run --tc-path <tc.yaml> --answers <answers.yaml>`
- `jq '.latest' <export_path>/gate_summary.json`
- `jq '.[] | select(.gate_id=="GateCR")' <export_path>/gate_log.json`
