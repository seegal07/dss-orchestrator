# E22_E23_MASTER_REPORT_v0.1

- selected_case: `EP_CASE_10` (mapped to `E19_LIVE_VALIDATION_2026-02-19T11-02-33Z`)

## V1/V2/V3 text-diff summary and invariants
- V1: baseline text as-is from selected EP case.
- V2: wording-only rephrase of X/Y; no new variables and no scope change.
- V3: wording-only rephrase of X/Y; no new variables and no scope change.
- Invariants confirmed: same SYSTEM_SCOPE, same constraints, X/Y meaning preserved.

## E22 results table (V1/V2/V3)
| Run | fingerprint | PFL verdict | PFL reason | attempt_index | scope | boundary | search_loop | manual_override_used | GateCR |
|---|---|---|---|---:|---|---|---|---|---|
| E22_V1 | `a07b142a56a1625609289ae3b0bf910fb9f2cfa1337ca8b92b0e7624a4d82166` | `PASS` | `NONE` | `1` | `правило запуска новых филиалов в Европе` | `Внутри: процедура запуска, ресурсы и подготовка; снаружи: локальные условия рынка Европы.` | `True` | `False` | `soft_fail` |
| E22_V2 | `56dc8bb0626130f38ae25a5d856332cb1143fa2607df7729542afb5e3acaeb3a` | `FAIL` | `SOLUTION_AS_XY` | `1` | `правило запуска новых филиалов в Европе` | `Внутри: процедура запуска, ресурсы и подготовка; снаружи: локальные условия рынка Европы.` | `True` | `False` | `NOT_REACHED/NA` |
| E22_V3 | `788fb9b6ec68a1d1664bc275941096849d1db3189f4a29cace20df5801eeb3a2` | `PASS` | `NONE` | `1` | `правило запуска новых филиалов в Европе` | `Внутри: процедура запуска, ресурсы и подготовка; снаружи: локальные условия рынка Европы.` | `True` | `False` | `soft_fail` |

## admission_volatility_index
- PFL_variance: `50.0`%
- scope_variance: `0.0`%
- search_loop_variance: `0.0`
- override_variance: `0.0`%
- key_driver: `PFL_variance`

## E23a repeatability verdict
- status: `PASS`
- evidence: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E23A_R1_export.json`, `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E23A_R2_export.json`

## E23b engine_repeatability_gate
- status: `STABLE`
- evidence: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E23B_R1_export.json`, `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E23B_R2_export.json`, `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_E23_VARIABILITY_PACK_2026-02-20T11-39-12Z/RUN_EXPORT_SNIPPETS/E23B_R3_export.json`

Stage A validation only; solution quality not assessed
