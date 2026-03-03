# PATCHLOG

## Modified existing files
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
  - Added Operator Core enablement detection by schema flag (`TEST_VECTOR_SCHEMA_v0.2`).
  - Added `GateCR` tri-state evaluator with deterministic HARD_FAIL on Separation Illusion Test.
  - Added canonical hard-fail literal handling (`structural resolution not found`).
  - Wired GateCR before S09 and enforced HARD_FAIL NOT_RUN propagation to S09–S14.
  - Added S12 rule: `compromise_mode=true` mandatory when `GateCR=SOFT_FAIL`.

- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
  - Added support for `step_8_5` parsing (`step_8_5` -> internal step key `85`).
  - Added `HARD_FAIL`/`SOFT_FAIL` handling to overall run status logic.
  - Added GateCR pipeline step mapping and OPERATOR_CORE log typing.
  - Added artifact export for `S08_5_OPERATOR_PROMPT.md`, `S08_5_OPERATOR_OUTPUT.md`, `GATECR_RECORD.md`.
  - Added GateCR evidence fields in exported `GATECR_RECORD` (`detected_conflict_types`, `dominant_conflict_type`, etc.).

## Created new files
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.2.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S08_5_OPERATOR_PROMPT.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S08_5_OPERATOR_OUTPUT.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/GATECR_RECORD.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/templates/operator_core/S12_DECISION_RECORD_TEMPLATE_v1.1.md`

## Verification runs executed
- RunA: GateCR PASS path.
- RunB: GateCR HARD_FAIL path (S09–S14 NOT_RUN).
- RunC: GateCR SOFT_FAIL path (`overall_status=PARTIAL`, `compromise_mode=true`).
- RunD: Historical v0.1 schema case (GateCR exempt).
