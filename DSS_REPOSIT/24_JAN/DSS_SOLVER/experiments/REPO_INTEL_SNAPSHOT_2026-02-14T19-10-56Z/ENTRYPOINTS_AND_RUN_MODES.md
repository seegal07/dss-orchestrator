# ENTRYPOINTS_AND_RUN_MODES

## Canonical harness entrypoints
- CLI entry: `harness/harness.py`
- Main function: `main()`
- Run executor: `run_tc(tc_id, answers_path, tc_path, addon_answers_path, addon_strict)`
- Structural gate call: `run_structural_gates(tc, step_map)` from `harness/gates_structural.py`

## Supported run modes in executable runtime
- Runtime supports one CLI command mode: `run`.
- Inputs/flags:
  - `--tc` or `--tc-path`
  - `--answers`
  - optional `--addon-answers`
  - optional `--addon-strict`

## Governance-defined interaction modes
Defined in `governance/DSS_EXECUTION_MODE_SPEC_v1.1.md`:
- `ARCHITECTURE_ONLY`
- `OFFLINE_SIMULATION`
- `LIVE_CLIENT`
- `REPLAY_FREEZE`
- `GOVERNANCE_UPDATE`

## Mode validation implementation status
- In harness code: no explicit MODE header parsing/validation.
- In governance docs: mode rules and MODE_MISMATCH protocol are defined normatively.
- Effective state: mode enforcement is process-level/documentary, not runtime-enforced in `harness/*.py`.
