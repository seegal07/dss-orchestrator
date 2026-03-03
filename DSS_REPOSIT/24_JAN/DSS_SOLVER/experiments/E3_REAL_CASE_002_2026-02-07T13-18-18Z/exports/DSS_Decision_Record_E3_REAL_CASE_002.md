# DSS Decision Record — E3_REAL_CASE_002

**decision_id:** TC_E3_REAL_CASE_002__2026-02-07T13-19-40Z  
**decision_status:** DECISION_VALID

## chosen_mechanism
Разделение потоков заказов (Step10.concept_specs[concept_index=1]).

## rejected_alternatives
- Оптимизация маршрутов
- Контрольные точки

## ikR_link
"Заказы отгружаются в SLA без роста ошибок и без увеличения штата"

## contradiction_link
"Если ускоряем сборку, растёт число ошибок; если усиливаем контроль, падает скорость"

## key_constraints
- Штат не увеличиваем
- Новый WMS не внедряем
- Бюджет ≤ 30 000 EUR
- Срок эффекта — 3 месяца

## acceptability_criteria
- SLA ≥ 95%
- Ошибки ≤ 1%

## decision_criteria_status (decision‑critical)
- G4-P1: PASS
- G4-P2: PASS
- G4-P3: PASS
- G5-P1: PASS
- G5-P2: PASS
- G6-P1: PASS
- G6-P2: PASS
- G11-P1: PASS
- G12-P1: PASS
- G12-P2: PASS
- G12-P3: PASS

## invalid_conditions
Если SLA <95% через 3 месяца, то правила очередей пересматриваются.

## evidence_links
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E3_REAL_CASE_002_2026-02-07T13-18-18Z/exports/DSS_Output_Package_TC_E3_REAL_CASE_002_2026-02-07T13-19-40Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E3_REAL_CASE_002_2026-02-07T13-18-18Z/exports/DSS_Output_Package_TC_E3_REAL_CASE_002_2026-02-07T13-19-40Z/case.json
