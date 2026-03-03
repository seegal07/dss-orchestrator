# DIAGNOSTIC_RUNS_SUMMARY — Founder v1

## Case A — CASE_A_CUSTOMIZATION_VS_STANDARDIZATION
- Статус решения: **DECISION_INVALID** (см. Decision Record).
- Причина: отсутствуют пороги X/Y и baseline скорости релизов.
- Gate summary: Gate4=fail, Gate11=blocked, Gate12=fail. (см. gate_summary.json)
- Где DSS добавила ценность: явная фиксация данных, без которых выбор решения недопустим.
- Где DSS не смогла завершить: отсутствие порогов, необходимых для выбора.

Ключевые файлы:
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_DECISION_RECORD_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION.md
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION_2026-02-08T09-49-12Z/gate_summary.json

## Case B — CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS
- Статус решения: **DECISION_INVALID**.
- Причина: отсутствуют базовые метрики LTV/CAC/маржа/runway и пороги переключения режима.
- Gate summary: Gate5=blocked, Gate6=blocked, Gate11=blocked, Gate12=fail. (см. gate_summary.json)
- Где DSS добавила ценность: зафиксировала минимальный список данных, без которых решение невозможно.
- Где DSS не смогла завершить: отсутствуют данные для IKR и порогов.

Ключевые файлы:
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_DECISION_RECORD_CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS.md
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS_2026-02-08T09-49-17Z/gate_summary.json

## Сравнение
- Оба кейса блокируются из‑за отсутствия decision‑critical входных данных.
- Case A имеет определённое противоречие и IKR, но не имеет порогов выбора.
- Case B не имеет минимального набора финансовых метрик, поэтому блокируется раньше (Gate5/6/11/12).
