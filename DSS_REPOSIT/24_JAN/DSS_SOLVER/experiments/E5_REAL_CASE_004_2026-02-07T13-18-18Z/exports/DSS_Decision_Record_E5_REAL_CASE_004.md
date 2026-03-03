# DSS Decision Record — E5_REAL_CASE_004

**decision_id:** TC_E5_REAL_CASE_004__2026-02-07T13-23-23Z  
**decision_status:** DECISION_VALID

## chosen_mechanism
Сегментация и сценарии (Step10.concept_specs[concept_index=1]).

## rejected_alternatives
- Ранние уведомления
- Эскалации

## ikR_link
"DSO снижен до 45 дней без потери клиентов и без изменения условий контрактов"

## contradiction_link
"Если ускоряем инкассацию, ухудшается лояльность; если сохраняем лояльность, растёт просрочка"

## key_constraints
- Нельзя менять условия контрактов и цены
- Нельзя привлекать новый долг
- Срок эффекта — 2 месяца

## acceptability_criteria
- DSO ≤45 дней
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
Если DSO >45 дней через 2 месяца, то сценарии напоминаний пересматриваются.

## evidence_links
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E5_REAL_CASE_004_2026-02-07T13-18-18Z/exports/DSS_Output_Package_TC_E5_REAL_CASE_004_2026-02-07T13-23-23Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E5_REAL_CASE_004_2026-02-07T13-18-18Z/exports/DSS_Output_Package_TC_E5_REAL_CASE_004_2026-02-07T13-23-23Z/case.json
