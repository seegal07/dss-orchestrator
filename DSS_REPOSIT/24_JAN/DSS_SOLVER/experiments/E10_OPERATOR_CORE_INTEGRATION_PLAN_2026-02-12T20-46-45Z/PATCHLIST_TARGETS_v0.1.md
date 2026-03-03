# PATCHLIST_TARGETS_v0.1

## Existing files/modules requiring future edits (not now)

1) `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
- Add structural check function for S08.5 artifact presence.
- Add GateCR structural shell (field presence + status normalization).
- Add NOT_RUN propagation from GateCR HARD_FAIL to Gate9–Gate12.

2) `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- Insert GateCR execution point between Step8 checks and Step9 path.
- Add GateCR to gate log/summary export.
- Carry `COMPROMISE_MODE` flag into export artifacts.

3) `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py`
- Add operator-core validator entry point (or parallel validator module) for GateCR matrix.
- Keep existing GateTRIZ validation unchanged.

4) `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/ASSISTED_GATE_CRITERIA_*.md`
- Introduce GateCR assisted criteria definition (new version file, do not overwrite old).

5) `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/TEST_VECTOR_SCHEMA_v0.1.md.docx` (or active schema SoT)
- Add S08.5 fields + GateCR result fields + trace flags.

6) `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/_export_package` area in `harness.py`
- Emit new artifacts:
  - S08_5_OPERATOR_FRAME
  - GATECR_EVIDENCE
  - S09_MECHANISM_TRACE

## Scope control
- No edits to DCF/SDP specs.
- No edits to Gate9–Gate12 semantics.
- No activation of 40 principles/9 forms as generation layer.
