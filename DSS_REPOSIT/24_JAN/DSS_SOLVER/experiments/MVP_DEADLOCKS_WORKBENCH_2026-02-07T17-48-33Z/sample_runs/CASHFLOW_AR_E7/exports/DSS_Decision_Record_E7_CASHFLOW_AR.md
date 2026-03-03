# DSS Decision Record — E7_CASHFLOW_AR

**decision_id:** TC_E7_CASHFLOW_AR__2026-02-07T17-53-24Z  
**decision_status:** DECISION_VALID

## chosen_mechanism
Сегментация и сценарии (Step10.concept_specs[concept_index=1]).

## rejected_alternatives
- Ранние уведомления
- Эскалации

## ikR_link
"DSO ≤45 дней без потери клиентов и без изменения контрактов"

## contradiction_link
"Если ускоряем инкассацию, ухудшается лояльность"

## key_constraints
- Нельзя менять контракты и цены
- Нельзя привлекать долг
- Срок эффекта — 2 месяца

## acceptability_criteria
- DSO ≤45
- Просрочка >30 дней ≤10%

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
Если DSO >45 дней через 2 месяца, то сценарии пересматриваются.

## evidence_links
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/MVP_DEADLOCKS_WORKBENCH_2026-02-07T17-48-33Z/sample_runs/CASHFLOW_AR_E7/exports/DSS_Output_Package_TC_E7_CASHFLOW_AR_2026-02-07T17-53-24Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/MVP_DEADLOCKS_WORKBENCH_2026-02-07T17-48-33Z/sample_runs/CASHFLOW_AR_E7/exports/DSS_Output_Package_TC_E7_CASHFLOW_AR_2026-02-07T17-53-24Z/case.json
