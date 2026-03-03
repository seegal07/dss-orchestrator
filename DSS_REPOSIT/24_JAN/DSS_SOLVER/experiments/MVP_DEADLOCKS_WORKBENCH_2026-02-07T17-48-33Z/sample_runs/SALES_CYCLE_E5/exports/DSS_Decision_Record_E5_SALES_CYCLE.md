# DSS Decision Record — E5_SALES_CYCLE

**decision_id:** TC_E5_SALES_CYCLE__2026-02-07T17-50-42Z  
**decision_status:** DECISION_VALID

## chosen_mechanism
Сегментация лидов (Step10.concept_specs[concept_index=1]).

## rejected_alternatives
- Жёсткая квалификация
- Автоскоринг

## ikR_link
"Цикл сделки ≤45 дней при сохранении качества лидов и без роста штата"

## contradiction_link
"Если ускоряем квалификацию, падает точность"

## key_constraints
- Штат не увеличиваем
- Маркетинг не растим
- Срок эффекта — 3 месяца

## acceptability_criteria
- Цикл ≤45 дней
- Конверсия ≥ текущей

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
Если цикл >45 дней через 3 месяца, то сегментация пересматривается.

## evidence_links
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/MVP_DEADLOCKS_WORKBENCH_2026-02-07T17-48-33Z/sample_runs/SALES_CYCLE_E5/exports/DSS_Output_Package_TC_E5_SALES_CYCLE_2026-02-07T17-50-42Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/MVP_DEADLOCKS_WORKBENCH_2026-02-07T17-48-33Z/sample_runs/SALES_CYCLE_E5/exports/DSS_Output_Package_TC_E5_SALES_CYCLE_2026-02-07T17-50-42Z/case.json
