# E21_REPORT_v0.1

## Case Selection (LIVE_SET_PATCHED)
- case_loop_yes: EP_CASE_10 (source: E19, LOOP_RISK=YES / search_loop=TRUE)
- case_loop_no: EP_CASE_05 (source: E14 run01, LOOP_RISK=NO in selected baseline)

## What fields added and where
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
  - export `case.json.instrumentation`: input_fingerprint, manual_override_used, override_type, normalized_reason_codes, gatecr_status_mirror
  - export `gate_log.json[*].normalized_reason_codes`
  - export `gate_summary.json.normalized_reason_codes`
  - export `artifacts/S08_5_OPERATOR_OUTPUT.md`: gatecr_status_mirror
  - export `artifacts/GATECR_RECORD.md`: normalized_reason_codes
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.5.md`
- `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_2_DECISION_LAYER_LINKS_v1.1.md`

## Schema version bump details
- Activated instrumentation schema v0.5 (no behavioral gate/routing changes).

## Example payload snippets
- A1: fingerprint=`a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`
- A2: fingerprint=`a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`
- B1: fingerprint=`20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`
- B2: fingerprint=`20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`

## Determinism results table
| Check | Result |
|---|---|
| fingerprint(A1)==fingerprint(A2) | PASS |
| fingerprint(B1)==fingerprint(B2) | PASS |
| PFL(A1)==PFL(A2) | PASS |
| GateCR(A1)==GateCR(A2) | PASS |
| PFL(B1)==PFL(B2) | PASS |
| GateCR(B1)==GateCR(B2) | PASS |

| Run | input_fingerprint | PFL | GateCR |
|---|---|---|---|
| A1 | `a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166` | `None` | `None` |
| A2 | `a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166` | `None` | `None` |
| B1 | `20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2` | `None` | `None` |
| B2 | `20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2` | `None` | `None` |
