# DSS_DECISION_RECORD_SPEC_v0.1

Назначение: фиксировать решение solver-контурa как формальный артефакт, основанный на pipeline (S00–S14) и gate_log.

## Поля DSS Decision Record
- **decision_id**
- **chosen_mechanism** (один; ссылка на S10/Step10)
- **rejected_alternatives** (2–5; ссылки на S09/Step9)
- **ikR_link** (ссылка на S05)
- **contradiction_link** (ссылка на S04)
- **key_constraints** (из S01)
- **acceptability_criteria** (из S12.success_criteria + gate_log)
- **invalid_conditions** (условия недействительности решения; из S14.rule_statement_if_then + S06)

## Источники полей (pipeline mapping)
- decision_id → RUN run_id + test_case_id (evidence)
- chosen_mechanism → S10.concept_specs + S12.chosen_concept_index
- rejected_alternatives → S12.rejected_alternatives + S09.concepts
- ikR_link → S05.ikr_1l
- contradiction_link → S04.statement_1l
- key_constraints → S01.constraints
- acceptability_criteria → S12.success_criteria + Gate4/5/6/11/12 (gate_log criteria_results)
- invalid_conditions → S14.rule_statement_if_then + S06.barrier_1l

## Примечание
Decision Record формируется только из существующих артефактов и gate_log без новых допущений.
