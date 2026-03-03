# PATCHLOG

## 1) PFL gate insertion and routing
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
- Added constants for PFL canonical terminal message and enums.
- Added activation logic: PFL executes only when `schema_version >= 0.3` OR `pfl_enabled=true` OR `canon_versions.schema` contains `TEST_VECTOR_SCHEMA_v0.3`.
- Added `gatepfl_problem_framing(...)` with deterministic checks over top-level `pfl_*` fields.
- Inserted GatePFL immediately after Gate3 and before Gate4.
- Added propagation: on GatePFL FAIL => `Gate4..Gate14 = NOT_RUN` and stop before Operator Layer.

## 2) Harness logging/export integration
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- Added GatePFL mapping to gate log (`pipeline_step=35`, `check_type=PFL`, `criteria_scope=PFL`).
- Added PFL export artifact payload as `S03_5_PFL_OUTPUT.md` in package artifacts.

## 3) Governance schema and index
- Created `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.3.md` with top-level `pfl_*` contract.
- Updated `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_2_DECISION_LAYER_LINKS_v1.1.md`:
  - ACTIVE: `TEST_VECTOR_SCHEMA_v0.3.md`
  - SUPERSEDED: `TEST_VECTOR_SCHEMA_v0.2.md`

## 4) PFL templates
- Created `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/problem_framing/S03_5_PFL_PROMPT.md`
- Created `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/problem_framing/S03_5_PFL_OUTPUT.md`
