# DSS Decision Record — CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS (v2)

## Context
Дилемма: рост vs прибыль/ранвей при отсутствии точных метрик. Горизонт решения — 90 дней.

## Options
1) Режим роста.
2) Режим прибыльности.

## Decision
**DECISION_VALID** — выбран вариант 1 (режим роста) с порогами переключения.

## Baseline
- Runway: **5–7 месяцев (PROXY)**
- Burn: **90–130k $/месяц (PROXY)**
- Gross margin: **55–65% (PROXY)**

## Thresholds
- Если runway < 5 мес → переключиться на режим прибыльности.
- Если burn > 130k $/мес → переключиться на режим прибыльности.
- Validation date: **2026-03-01**

## Proxy flags
Все thresholds и baseline заданы как PROXY‑диапазоны.

## Trade-offs
Рост выручки vs устойчивость cash‑flow.

## Review
Ревью на дату валидации 2026-03-01 и далее каждые 30 дней.

## References
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/exports/DSS_Output_Package_TC_CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS_v2_2026-02-08T10-23-31Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DIAGNOSTIC_RUNS_FOUNDER_V1_2026-02-08T09-46-58Z/tests/TC_CASE_B_GROWTH_VS_PROFITABILITY_DATA_GAPS_v2.yaml
