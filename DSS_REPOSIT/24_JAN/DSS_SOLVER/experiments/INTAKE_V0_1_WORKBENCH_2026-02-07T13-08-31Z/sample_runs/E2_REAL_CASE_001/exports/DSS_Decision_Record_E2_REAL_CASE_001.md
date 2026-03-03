# DSS Decision Record — E2_REAL_CASE_001

**decision_id:** TC_E2_REAL_CASE_001__2026-02-07T13-11-05Z  
**decision_status:** DECISION_VALID

## chosen_mechanism
Правила гибридного доступа (Step10.concept_specs[concept_index=1]).

## rejected_alternatives
- Офлайн‑ядро
- Контроль посещаемости

## ikR_link
"Группа сохраняет ≥12 студентов через 2 месяца и ≥8 до конца курса при фиксированной цене и часах"

## contradiction_link
"Если увеличиваем гибкость (онлайн‑доступ), ухудшается стабильность офлайн‑группы"

## key_constraints
- Цена 900 PLN/мес фиксирована
- 16 часов/мес фиксированы
- Набор группы — 2 месяца
- Маркетинг ≤10% потенциальной выручки студента
- Срок стабилизации — 2 месяца после старта

## acceptability_criteria
- ≥12 студентов через 2 месяца
- ≥8 до конца курса

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
Если через 2 месяца численность <12, то правила гибридного доступа пересматриваются.

## evidence_links
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/INTAKE_V0_1_WORKBENCH_2026-02-07T13-08-31Z/sample_runs/E2_REAL_CASE_001/exports/DSS_Output_Package_TC_E2_REAL_CASE_001_2026-02-07T13-11-05Z/gate_log.json
- case: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/INTAKE_V0_1_WORKBENCH_2026-02-07T13-08-31Z/sample_runs/E2_REAL_CASE_001/exports/DSS_Output_Package_TC_E2_REAL_CASE_001_2026-02-07T13-11-05Z/case.json
