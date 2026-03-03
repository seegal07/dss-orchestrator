# E21_REPORT_v0.1

## Added instrumentation fields and file paths
- Harness export instrumentation: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- Schema bump: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TEST_VECTOR_SCHEMA_v0.5.md`
- Governance active index update: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_2_DECISION_LAYER_LINKS_v1.1.md`

## Schema version bump details
- Active schema moved from v0.4 to v0.5 for instrumentation fields only.
- No Gate/PFL/GateCR/routing decision behavior changes introduced.

## Example payload snippets
- A1: input_fingerprint=`a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`
- A2: input_fingerprint=`a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`
- B1: input_fingerprint=`20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`
- B2: input_fingerprint=`20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2`, manual_override_used=`False`, override_type=`None`, gatecr_status_mirror=`NOT_APPLICABLE`

## Determinism results (A1/A2/B1/B2)
| Check | Result |
|---|---|
| fingerprint_A_equal | PASS |
| fingerprint_B_equal | PASS |
| pfl_A_equal | PASS |
| gatecr_A_equal | PASS |
| pfl_B_equal | PASS |
| gatecr_B_equal | PASS |

| Run | fingerprint | PFL | GateCR |
|---|---|---|---|
| A1 | `a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166` | `None` | `None` |
| A2 | `a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166` | `None` | `None` |
| B1 | `20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2` | `None` | `None` |
| B2 | `20fdffdab5b5af455a75eab34a8db337621672f245ceba19fb0bfc6e18f3a2b2` | `None` | `None` |
