# S00_S03_SCOPE_FIELD_AUDIT_v0.1

## Scope/boundary collection points (evidence)
- Harness structural requirements: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
  - `gate1_case_owner`: requires `step_1.owner_scope` (mandatory for Gate1 PASS).
  - `gate2_system_boundary`: requires `step_2.actor`, `step_2.system`, `step_2.environment`, `step_2.boundary_note_1l` (all mandatory for Gate2 PASS).
  - `gate3_interaction`: requires `step_3.elements`, `step_3.flows[*].from/to/type/note`, `step_3.symptom_location` (mandatory for Gate3 PASS).
- Export artifact mapping: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
  - `S01_PROBLEM_OWNER_CARD.md` <= `step_1`
  - `S02_SYSTEM_BOUNDARY_MAP.md` <= `step_2`
  - `S03_INTERACTION_MAP.md` <= `step_3`
- Live prompt evidence (scope question exists but not templated in `/templates`):
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E13_LIVE_NEW_CLIENT_FULL_RUN_2026-02-15T09-37-22Z/DIALOGUE_LOG.md`
    - S02 format: `система=<что внутри>; внешнее=<что снаружи>`
    - S03 format: `блокировка=<кто задерживает какое решение>`

## Mandatory vs optional (current system)
- In harness run path, S01/S02/S03 fields above are mandatory for Gate1/2/3.
- S00 is not structurally gated as `step_0` in current gates (no dedicated GateS00 validation).
- In live/manual flows, capture discipline depends on operator questioning; no centralized S00–S03 template file in `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates` except operator-core templates.

## Existing test-vector field names (current evidence)
- `step_1`: `owner_role`, `owner_scope`, optional contextual fields like `problem_1l`.
- `step_2`: `system`, `actor` (list), `environment` (list), `boundary_note_1l`.
- `step_3`: `elements` (list), `flows[]` (`from`,`to`,`type`,`note`), `symptom_location`.
- Confirmed in:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/tests/TC_DSS01.yaml`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/tests/TC_DSS02_NEGATIVE.yaml`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E13_LIVE_NEW_CLIENT_FULL_RUN_2026-02-15T09-37-22Z/TEST_VECTOR_v0.2.json`

## Evidence for SOLUTION_AS_XY exposure upstream
- Current structural Gate4 checks only field presence (`improve_x`, `worsen_y`, `statement_1l`, `measurement_hint`) and does not reject mechanism-in-X/Y.
- Evidence path: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py` (`gate4_contradiction`).
- Therefore upstream S00–S03 currently do not enforce SOLUTION_AS_XY prevention; this is a gap addressed only by new PFL spec, not implemented yet.
