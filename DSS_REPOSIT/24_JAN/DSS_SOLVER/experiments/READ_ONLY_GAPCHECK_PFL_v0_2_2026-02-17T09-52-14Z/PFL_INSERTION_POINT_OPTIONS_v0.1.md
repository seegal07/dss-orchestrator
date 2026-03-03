# PFL_INSERTION_POINT_OPTIONS_v0.1

## Option A (direct structural gate insertion before Gate4)
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
- Location: `run_structural_gates()` sequence, immediately after `gate3_interaction(step_map)` and before `gate4_contradiction(step_map)`.
- Effect:
  - `GatePFL=PASS` -> continue to Gate4.
  - `GatePFL=FAIL` -> stop progression and set `Gate4..Gate14 = NOT_RUN` (or minimally S04+ NOT_RUN per PFL spec).

## Option B (operator-core-style branch with dedicated fail propagation)
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
- Pattern reuse: same branching approach currently used for GateCR HARD_FAIL (sets `Gate9..Gate14 = NOT_RUN`).
- Effect for PFL:
  - Add pre-S04 branch: when PFL fails after max attempts, emit canonical fail reason and mark S04+ NOT_RUN.

## Option C (log/export registration point)
- File: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- Locations impacted once PFL exists:
  - `_write_gate_logs()` to map GatePFL to a pipeline step id.
  - `_export_package()` if dedicated PFL artifact file must be exported.
- Current behavior has no GatePFL mapping.

## Expected downstream effect (required by PFL spec)
- On terminal PFL fail:
  - canonical message: `structural contradiction not formulated`
  - S04+ must be `NOT_RUN`
- This behavior is not present in current code; current pre-S04 stop exists only for Gate0 block.
