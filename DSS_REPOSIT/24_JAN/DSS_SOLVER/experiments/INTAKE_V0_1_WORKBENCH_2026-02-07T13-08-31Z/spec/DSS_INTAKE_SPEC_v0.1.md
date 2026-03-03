# DSS_INTAKE_SPEC_v0.1

Цель: staged intake для DSS_SOLVER, закрывающий данные для S00–S14 и минимизирующий BLOCKED по Gate4/5/6/11/12. Клиент не знает TRIZ.

## Этапы (staged)

### Этап 1 — Контекст и границы (S00–S03)
**Q1. Проблема (1–2 предложения).**
- Заполняет: S00.symptom_1l

**Q2. Владелец решения, зона контроля, ограничения, срок.**
- Заполняет: S01.owner_role, S01.owner_scope, S01.constraints

**Q3. Границы системы (внутри/снаружи).**
- Заполняет: S02.actor, S02.system, S02.environment, S02.boundary_note_1l

**Q4. Элементы и потоки (как проходит процесс сейчас).**
- Заполняет: S03.elements, S03.flows, S03.symptom_location

**Критерии перехода:** если S00–S03 заполнены, идём дальше. Если нет — Guided Correction по S00–S03.

### Этап 2 — Decision‑critical ядро (S04–S06)
**Q5. Противоречие X/Y и измеримость.**
- Заполняет: S04.improve_x, S04.worsen_y, S04.statement_1l, S04.measurement_hint
- Закрывает Gate4 (G4‑P1..P3)

**Q6. IKR (идеальный результат без механизма).**
- Заполняет: S05.ikr_1l, S05.no_new_harm_clause
- Закрывает Gate5 (G5‑P1..P2)

**Q7. Жёсткий барьер (взаимоисключение), эквивалент Step4.**
- Заполняет: S06.barrier_1l, S06.equivalent_to_step4
- Закрывает Gate6 (G6‑P1..P2)

**Критерии перехода:** если S04/05/06 заполнены — продолжаем. Если нет — Guided Correction по Gate4/5/6.

### Этап 3 — Ресурсы и решения (S07–S10)
**Q8. Ресурсы и рычаги внутри системы.**
- Заполняет: S07.resources

**Q9. Основная форма / логика выбора (без TRIZ‑жаргона).**
- Заполняет: S08

**Q10. 3–5 возможных решений (кратко).**
- Заполняет: S09.concepts

**Q11. Механизм выбранных решений (минимум): шаги, риски, метрики.**
- Заполняет: S10.concept_specs

### Этап 4 — Проверка и выбор (S11–S12)
**Q12. Есть ли новое противоречие после решений?**
- Заполняет: S11.new_contradiction_exists (+ описание при true)
- Закрывает Gate11 (G11‑P1)

**Q13. Выбор решения: индекс + причины + критерии успеха.**
- Заполняет: S12.chosen_concept_index, S12.chosen_concept_name, S12.reasons, S12.success_criteria, S12.rejected_alternatives, S12.assumptions
- Закрывает Gate12 (G12‑P1..P3)

**Критерии перехода:** если S11/S12 заполнены — продолжаем. Если нет — Guided Correction по Gate11/12.

### Этап 5 — Фиксация (S13–S14)
**Q14. План внедрения (2–4 потока).**
- Заполняет: S13.workstreams

**Q15. Правило/обновление (если‑то‑то).**
- Заполняет: S14.*

## Guided Correction (включение)
- **Gate4 BLOCKED/FAIL:** запросить X/Y, измеримость, формулу.
- **Gate5 BLOCKED/FAIL:** запросить IKR без механизма и ограничение на новый вред.
- **Gate6 BLOCKED/FAIL:** запросить жёсткий барьер и эквивалент Step4.
- **Gate11 BLOCKED/FAIL:** запросить наличие/отсутствие нового противоречия.
- **Gate12 BLOCKED/FAIL:** запросить выбор решения, причины, критерии успеха, отклонённые альтернативы.

## Mapping: вопросы → S‑поля
- Q1 → S00.symptom_1l
- Q2 → S01.owner_role, S01.owner_scope, S01.constraints
- Q3 → S02.actor, S02.system, S02.environment, S02.boundary_note_1l
- Q4 → S03.elements, S03.flows, S03.symptom_location
- Q5 → S04.improve_x, S04.worsen_y, S04.statement_1l, S04.measurement_hint
- Q6 → S05.ikr_1l, S05.no_new_harm_clause
- Q7 → S06.barrier_1l, S06.equivalent_to_step4
- Q8 → S07.resources
- Q9 → S08
- Q10 → S09.concepts
- Q11 → S10.concept_specs
- Q12 → S11.new_contradiction_exists
- Q13 → S12.*
- Q14 → S13.workstreams
- Q15 → S14.*
