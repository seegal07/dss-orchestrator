# DSS_DECISION_RECORD_SPEC_v0.2

Назначение: фиксировать решение solver-контурa как формальный артефакт, основанный на pipeline (S00–S14) и gate_log criteria_results.

## Поля DSS Decision Record
- **decision_id**
- **chosen_mechanism** (один; ссылка на S10/Step10)
- **rejected_alternatives** (2–5; ссылки на S09/Step9)
- **ikR_link** (ссылка на S05)
- **contradiction_link** (ссылка на S04)
- **key_constraints** (из S01)
- **acceptability_criteria** (из S12.success_criteria + criteria_results)
- **decision_criteria_status** (список criterion_id + status)
- **invalid_conditions** (условия недействительности решения; из S14.rule_statement_if_then + S06)

## Источники полей (pipeline mapping)
- decision_id → RUN run_id + test_case_id (evidence)
- chosen_mechanism → S10.concept_specs + S12.chosen_concept_index
- rejected_alternatives → S12.rejected_alternatives + S09.concepts
- ikR_link → S05.ikr_1l
- contradiction_link → S04.statement_1l
- key_constraints → S01.constraints
- acceptability_criteria → S12.success_criteria + Gate4/5/6/11/12 (gate_log criteria_results)
- decision_criteria_status → gate_log criteria_results (ASSISTED gates)
- invalid_conditions → S14.rule_statement_if_then + S06.barrier_1l

## Decision‑critical criteria (обязательные)
Решение недопустимо, если любой из критериев ниже имеет статус FAIL/BLOCKED:
- Gate4: G4-P1, G4-P2, G4-P3
- Gate5: G5-P1, G5-P2
- Gate6: G6-P1, G6-P2
- Gate11: G11-P1
- Gate12: G12-P1, G12-P2, G12-P3

## Decision invalidation triggers
- Любой decision‑critical criterion = FAIL/BLOCKED.
- Отсутствуют criteria_results для ASSISTED gates.
- chosen_concept_index отсутствует или не соответствует Step9.

## Примечание
Decision Record формируется только из существующих артефактов и gate_log без новых допущений.
