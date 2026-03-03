# ASSISTED_GATE_CRITERIA_v0.2

Источник канона: DSS_SOLVER/canon/CANON_PIPELINE_v1.2.docx, CANON_9FORMS_v1.1.docx (без изменений).
Назначение: формальные критерии для ASSISTED gates (semantic checks) с учётом proxy‑метрик.

---

## Gate4 — CONTRADICTION_STATEMENT
**Purpose:** проверить корректность формулировки противоречия и его измеримость.

**PASS conditions:**
1. `improve_x` и `worsen_y` заданы как наблюдаемые величины.
2. `statement_1l` соответствует форме «Если улучшаем X, ухудшается Y».
3. `measurement_hint` описывает измерение X/Y **или** указан proxy‑диапазон (PROXY) + `validation_date`.
4. Противоречие относится к границам системы (Step2).
5. Нет явной логической тавтологии (X=Y).

**FAIL conditions:**
- X/Y не измеримы или описаны как намерения.
- `statement_1l` не содержит ухудшаемого параметра.
- `measurement_hint` отсутствует и proxy‑диапазоны не заданы.

**BLOCKED conditions:**
- Отсутствуют поля Step4 (improve_x / worsen_y / statement_1l).

**Mapping (pipeline steps):** S04.

---

## Gate5 — IKR_CARD
**Purpose:** проверить, что IKR формулируется как результат без механизма.

**PASS conditions:**
1. `ikr_1l` описывает конечный эффект, а не действие.
2. В `ikr_1l` отсутствуют механизмы («через/путём/используя»).
3. `no_new_harm_clause` (если задан) не противоречит IKR.

**FAIL conditions:**
- IKR содержит механизм или средство.
- IKR противоречит заявленным ограничениям.

**BLOCKED conditions:**
- `ikr_1l` отсутствует.

**Mapping:** S05.

---

## Gate6 — HARD_BARRIER
**Purpose:** проверить жёсткий барьер как эквивалент противоречия.

**PASS conditions:**
1. `barrier_1l` описывает взаимоисключающую пару условий.
2. `equivalent_to_step4` = true.
3. Барьер соответствует X/Y из Step4.

**FAIL conditions:**
- Барьер описывает частный риск, а не взаимоисключение.
- `equivalent_to_step4` = false.

**BLOCKED conditions:**
- `barrier_1l` отсутствует.

**Mapping:** S06.

---

## Gate11 — SECONDARY_CONTRADICTION_CHECK
**Purpose:** проверить корректность вывода о наличии/отсутствии нового противоречия.

**PASS conditions:**
1. `new_contradiction_exists` задано (true/false).
2. Если false — нет описанных новых конфликтов в Steps 9–10.
3. Если true — новый конфликт описан в связанной записи (manual note).

**FAIL conditions:**
- `new_contradiction_exists=false`, но в решениях выявлены новые противоречия.
- `new_contradiction_exists=true` без описания.

**BLOCKED conditions:**
- Поле `new_contradiction_exists` отсутствует.

**Mapping:** S11.

---

## Gate12 — DECISION_RECORD
**Purpose:** проверить обоснованность выбранного решения и связку с критериями успеха.

**PASS conditions:**
1. `chosen_concept_index` соответствует одному из решений Step9.
2. `reasons` указывает на соответствие ограничениям и целевым метрикам.
3. `success_criteria` согласованы с Step5/Step4.
4. `success_criteria` содержат **thresholds** (минимум 2: switch + kill/stop).
5. Если thresholds заданы диапазоном, это **PROXY** и указан `validation_date`.

**FAIL conditions:**
- Выбранный концепт не существует в Step9.
- `reasons` не связаны с метриками/ограничениями.
- `success_criteria` отсутствуют или противоречат IKR.
- thresholds отсутствуют.

**BLOCKED conditions:**
- `chosen_concept_index`/`reasons` отсутствуют.

**Mapping:** S12.
