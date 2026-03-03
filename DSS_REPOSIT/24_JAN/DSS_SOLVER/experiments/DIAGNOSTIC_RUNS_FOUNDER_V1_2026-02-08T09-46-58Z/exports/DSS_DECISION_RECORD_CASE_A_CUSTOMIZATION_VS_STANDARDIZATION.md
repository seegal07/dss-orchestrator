# DSS Decision Record — CASE_A_CUSTOMIZATION_VS_STANDARDIZATION

## Context
Крупный клиент требует кастомизацию ядра. Без неё высок риск потери сделки; с ней — риск деградации продукта, роста поддержки и замедления roadmap. Решение нужно в течение 2 недель.

## Options (из зафиксированных вариантов)
1) Ограниченная кастомизация с жёсткой ёмкостью.
2) Полный отказ от кастомизации.
3) Кастомизация как отдельная опция/контур.

## Decision
**DECISION_INVALID** — недостаточно данных для выбора и фиксации решения.

**Блокирующие причины:**
- Нет порога ёмкости кастомизации X%.
- Нет предельного роста поддержки Y.
- Нет baseline скорости релизов для сравнения.

## Trade-offs
- Сделка vs стабильность продукта.
- Краткосрочная выручка vs долгосрочная поддерживаемость.

## Thresholds
- Допустимая ёмкость кастомизации (X%): **MISSING**
- Допустимый рост поддержки (Y): **MISSING**
- Baseline скорости релизов: **MISSING**

## Review
Проверка через 60 дней после принятия решения (при наличии порогов X/Y и baseline).

## References
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION_2026-02-08T09-49-12Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/tests/TC_CASE_A_CUSTOMIZATION_VS_STANDARDIZATION.yaml
