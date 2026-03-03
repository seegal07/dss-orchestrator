# PATCHLOG

## Governance materialization
1. Added `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/GATECR_PASS_INTEGRITY_POLICY_v0.1.md` (verbatim policy SoT).
2. Added `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.4.md` with `step_8_5.search_loop` rule.
3. Updated `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_2_DECISION_LAYER_LINKS_v1.1.md`:
   - Active: `TEST_VECTOR_SCHEMA_v0.4.md`, `GATECR_PASS_INTEGRITY_POLICY_v0.1.md`
   - Superseded: `TEST_VECTOR_SCHEMA_v0.3.md`

## Minimal deterministic code patch
1. Updated `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`:
   - GateCR now enforces for `schema_version >= 0.4`:
     - `step_8_5.search_loop` is required boolean.
     - `search_loop == TRUE` => `risk_shift_detected=true` and PASS forbidden (returns SOFT_FAIL).
   - Tri-state structure unchanged.
2. Updated `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`:
   - GateCR export adds `schema_version`, `search_loop`, `risk_shift_detected`.
   - Added safe schema_version numeric parsing in export path.
   - Operator core enabled marker in exported record now recognizes schema v0.2/v0.3/v0.4 and explicit `operator_core_enabled`.
3. Updated template `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S08_5_OPERATOR_OUTPUT.md`:
   - Added mandatory field `search_loop` and owner instruction.

## Acceptance runs
- Workspace: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E17_GATECR_LOOP_PATCH_2026-02-18T13-19-32Z/HARNESS_RUN_EVIDENCE`
- RunA (`search_loop=TRUE`, schema 0.4): GateCR=SOFT_FAIL.
- RunB (`search_loop=FALSE`, schema 0.4): GateCR=PASS.
- RunC (schema 0.3, no `search_loop`): GateCR=PASS (historical exempt).
- RunD (control rerun, schema 0.4 + `search_loop=TRUE`): GateCR=SOFT_FAIL.
