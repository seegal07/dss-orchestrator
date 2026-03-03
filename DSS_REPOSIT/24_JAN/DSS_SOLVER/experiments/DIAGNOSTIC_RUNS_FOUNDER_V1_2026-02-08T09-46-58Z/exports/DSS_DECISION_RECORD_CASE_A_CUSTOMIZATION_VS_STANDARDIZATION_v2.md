# DSS Decision Record — CASE_A_CUSTOMIZATION_VS_STANDARDIZATION (v2)

## Context
Кастомизация ядра ради крупной сделки против риска деградации продукта, поддержки и скорости релизов. Решение нужно в течение 2 недель.

## Options
1) Ограниченная кастомизация (ёмкость в пределах порога).
2) Полный отказ от кастомизации.
3) Кастомизация как отдельная опция/контур.

## Decision
**DECISION_VALID** — выбран вариант 1 (ограниченная кастомизация).

## Baseline
- Скорость релизов: **2–3 релиза/месяц (PROXY)**

## Thresholds
- Кастомизация ≤ **15–25% (PROXY)**
- Рост нагрузки поддержки ≤ **+15–30% (PROXY)**
- Validation date: **2026-03-01**

## Proxy flags
Все thresholds и baseline заданы как PROXY‑диапазоны.

## Trade-offs
Сделка vs устойчивость продукта и поддержки.

## Review
Ревью через 60 дней, с обязательной валидацией proxy‑метрик до 2026-03-01.

## References
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION_v2_2026-02-08T10-23-24Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/tests/TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION_v2.yaml
