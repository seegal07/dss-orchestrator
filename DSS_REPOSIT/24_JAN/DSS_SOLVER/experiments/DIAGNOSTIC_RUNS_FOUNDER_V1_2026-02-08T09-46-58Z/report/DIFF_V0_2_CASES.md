# DIFF v0.2 — CASE A & CASE B

## Что изменилось
- Добавлены proxy‑диапазоны + validation_date (2026-03-01) в baseline/thresholds.
- В S12 добавлен chosen_concept_name, чтобы закрыть структурный fail Gate12.
- Критерии Gate4/Gate12 учитывают proxy‑диапазоны (ASSISTED_GATE_CRITERIA_v0.2).

## Case A (Customization vs Standardization)
**До v0.2:** Gate4=fail, Gate11=blocked, Gate12=fail.
**После v0.2:** Gate4=pass, Gate11=pass, Gate12=pass.
**Почему:** proxy‑пороги X/Y + baseline релизов с validation_date закрыли измеримость и критерии выбора.

Ссылки:
- До: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION_2026-02-08T09-49-12Z/gate_summary.json
- После: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION_v2_2026-02-08T10-23-24Z/gate_summary.json

## Case B (Growth vs Profitability)
**До v0.2:** Gate5=blocked, Gate6=blocked, Gate11=blocked, Gate12=fail.
**После v0.2:** Gate4=pass, Gate5=pass, Gate6=pass, Gate11=pass, Gate12=pass.
**Почему:** proxy‑диапазоны по runway/burn/margin и пороги переключения позволили сформировать IKR, барьер и критерии решения.

Ссылки:
- До: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS_2026-02-08T09-49-17Z/gate_summary.json
- После: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS_v2_2026-02-08T10-23-31Z/gate_summary.json
