# E25_REPORT_v0.1

## Determinism check results
- canonical_object_identical: `True`
- canonical_hash_identical: `True`
- reconstruction_trace_identical: `True`
- PFL_verdict_identical: `True`
- GateCR_verdict_identical: `True`

## canonical_hash comparison table
| Run | canonical_hash | raw_hash | PFL | GateCR |
|---|---|---|---|---|
| R1 | `738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c` | `cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c` | `pass` | `soft_fail` |
| R2 | `738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c` | `cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c` | `pass` | `soft_fail` |
| R3 | `738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c` | `cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c` | `pass` | `soft_fail` |

## trace diff check
- trace_diff_detected: `False`
- evidence files:
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E25_PHASE0_REPEATABILITY_2026-02-20T18-15-29Z/RUN_EXPORT_SNIPPETS/R1_export.json`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E25_PHASE0_REPEATABILITY_2026-02-20T18-15-29Z/RUN_EXPORT_SNIPPETS/R2_export.json`
  - `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E25_PHASE0_REPEATABILITY_2026-02-20T18-15-29Z/RUN_EXPORT_SNIPPETS/R3_export.json`

## PASS/FAIL conclusion
- PHASE0_REPEATABILITY: `PASS`
