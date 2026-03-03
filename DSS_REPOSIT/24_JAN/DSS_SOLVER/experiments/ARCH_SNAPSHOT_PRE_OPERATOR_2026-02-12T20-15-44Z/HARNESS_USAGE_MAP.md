# HARNESS_USAGE_MAP

## Governance files used in machine-run mode (directly or as SoT references)

### Directly used by code
- Runtime logic:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/api.py`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py`

### Referenced as canonical/governance SoT in artifacts/docs
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_PIPELINE_v1.2.docx`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_9FORMS_v1.1.docx`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/ASSISTED_GATE_CRITERIA_v0.1.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/ASSISTED_GATE_CRITERIA_v0.2.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/ASSISTED_GATE_CRITERIA_v0.3.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TRIZ_CORE_INTEGRATION_CONTRACT_v0.2.md`

## Inputs expected in machine-run
- `--tc` or `--tc-path` test case YAML with `full_vector.step_0..step_14`.
- `--answers` semantic answers YAML for assisted gates.
- optional `--addon-answers` for Gate15–Gate18.

## Outputs produced in machine-run
- Evidence:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/evidence/RUN_<tc>_<timestamp>.yaml`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/evidence/BUGLIST_<tc>_<timestamp>.yaml`
- Export package:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports/DSS_Output_Package_<tc>_<timestamp>/`
  - includes `gate_log.json`, `gate_summary.json`, `manifest.json`, `case.json`, `artifacts/S00..S14`

## Steps bypassed/softened in assisted/live mode (based on experiment evidence)
- Assisted/live flows can run without harness and without RUN/BUGLIST export.
- In those flows, validation is conversational and artifact-level (workspace `DIALOGUE_LOG`, `S10_MECHANISM_SPECS`, `S11_SELECTION_CRITERIA`, `S12_DECISION_RECORD`) instead of machine gate execution.
- Evidence examples:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E5_1_LIVE_S09_RERUN_2026-02-11T19-09-58Z/`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E6_LIVE_S10_UX_RETRY_V1_1_2026-02-12T08-59-13Z/`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E7_LIVE_S11_UX_2026-02-12T11-48-47Z/`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E8_LIVE_S12_COMMIT_2026-02-12T13-31-20Z/`
