# TRIZ_GUIDED_ELICITATION_SPEC_v0.1

## 1) PURPOSE
TRIZ_GUIDED_ELICITATION — слой Guided Elicitation / Form‑Filler для обязательных полей TRIZ_CORE_ENGINE. Назначение: запрашивать минимальные данные и давать допустимые шаблоны заполнения полей. Это НЕ коучинг, НЕ брейнсторминг, НЕ TRIZ‑обучение, НЕ генерация решений.

## 2) INPUTS / OUTPUTS
**Inputs:**
- Список fail_reason из результата TRIZ_CORE_ENGINE (fail_reason.code).
- Текущий tc dict (read‑only).

**Outputs:**
- Question pack: по одному минимальному вопросу + допустимые шаблоны на каждый fail_code.
- Acceptance criteria: что должно быть заполнено, чтобы валидатор мог пройти повторно.

## 3) NON-NEGOTIABLE BOUNDARIES
- Слой не изобретает противоречия, separation, transformation model или non‑obviousness.
- Слой может только: (a) задать один минимальный вопрос на fail_code; (b) дать допустимые шаблоны заполнения.
- Автор всех TRIZ‑полей — пользователь.

## 4) FAIL_CODE → QUESTION PACK MAP

### TRIZ_G1_MISSING
**Вопрос:** Укажите физическое противоречие: какой объект должен быть в двух взаимно исключающих состояниях?
**Шаблоны:**
1) object=__ ; parameter=__ ; state_a=__ ; state_not_a=__
2) «Объект __ должен быть __ и не‑__ по параметру __»
**Минимальные критерии приёма:**
- Поля object, parameter, state_a, state_not_a заполнены.
**Недопустимые паттерны:**
- state_a = state_not_a
- «объект просто должен быть лучше» (без параметра)

### TRIZ_G1_INCOMPLETE
**Вопрос:** Какие конкретные поля физического противоречия отсутствуют (object/parameter/state_a/state_not_a)?
**Шаблоны:**
1) object=__ ; parameter=__ ; state_a=__ ; state_not_a=__
2) object=__ ; parameter=__ ; state_a=__ ; state_not_a=__ (все 4 обязательны)
**Минимальные критерии приёма:**
- Все 4 поля заполнены и различимы.
**Недопустимые паттерны:**
- пропуск любого поля
- state_a = state_not_a

### TRIZ_G1_TAUTOLOGY
**Вопрос:** Чем именно отличается state_a от state_not_a?
**Шаблоны:**
1) state_a=__ ; state_not_a=__ (должны быть различны)
2) «Состояние А: __; состояние не‑А: __»
**Минимальные критерии приёма:**
- state_a и state_not_a не совпадают.
**Недопустимые паттерны:**
- одинаковые значения
- «больше/лучше» без параметра

### TRIZ_G2_MISSING
**Вопрос:** Какой тип разделения выбран (time/space/condition/part‑whole) и что именно меняется?
**Шаблоны:**
1) separation_type=__ ; what_changes=__ ; expected_resolution=__
2) «Разделение по __: меняется __, ожидаемый эффект __»
**Минимальные критерии приёма:**
- separation_type задан и входит в список допустимых.
- what_changes и expected_resolution заполнены.
**Недопустимые паттерны:**
- separation_type вне списка
- «просто разделить» без указания что меняется

### TRIZ_G2_INVALID_TYPE
**Вопрос:** Выберите один тип разделения: time / space / condition / part‑whole.
**Шаблоны:**
1) separation_type=time; what_changes=__; expected_resolution=__
2) separation_type=space; what_changes=__; expected_resolution=__
3) separation_type=condition; what_changes=__; expected_resolution=__
4) separation_type=part‑whole; what_changes=__; expected_resolution=__
**Минимальные критерии приёма:**
- separation_type из списка + заполнены what_changes/expected_resolution.
**Недопустимые паттерны:**
- произвольный тип
- пустые поля what_changes/expected_resolution

### TRIZ_G2_INCOMPLETE
**Вопрос:** Уточните what_changes и expected_resolution для выбранного separation_type.
**Шаблоны:**
1) what_changes=__ ; expected_resolution=__
2) «Меняем __, чтобы получить __»
**Минимальные критерии приёма:**
- what_changes и expected_resolution заполнены.
**Недопустимые паттерны:**
- «станет лучше» без указания изменений

### TRIZ_G3_MISSING
**Вопрос:** Заполните 9‑экранов: system_present обязательно, плюс ещё минимум два поля.
**Шаблоны:**
1) system_present=__ ; system_past=__ ; supersystem_present=__
2) system_present=__ ; subsystem_present=__ ; system_future=__
**Минимальные критерии приёма:**
- system_present заполнено + ещё минимум 2 ячейки.
**Недопустимые паттерны:**
- заполнено только system_present

### TRIZ_G3_NO_PRESENT
**Вопрос:** Что является «системой в настоящем» (system_present)?
**Шаблоны:**
1) system_present=__
2) «Система сейчас: __»
**Минимальные критерии приёма:**
- system_present заполнено.
**Недопустимые паттерны:**
- пустое поле

### TRIZ_G3_MIN_CELLS
**Вопрос:** Добавьте минимум два дополнительных поля в 9‑экранах.
**Шаблоны:**
1) subsystem_present=__ ; supersystem_present=__
2) system_past=__ ; system_future=__
**Минимальные критерии приёма:**
- заполнено минимум 3 ячейки суммарно.
**Недопустимые паттерны:**
- менее 3 ячеек

### TRIZ_G4_MISSING
**Вопрос:** Укажите, какая исходная предпосылка нарушается или почему решение неочевидно.
**Шаблоны:**
1) assumption_broken=__
2) why_not_obvious=__
**Минимальные критерии приёма:**
- заполнено хотя бы одно поле.
**Недопустимые паттерны:**
- «это очевидно»

### TRIZ_G4_INCOMPLETE
**Вопрос:** Заполните assumption_broken или why_not_obvious.
**Шаблоны:**
1) assumption_broken=__
2) why_not_obvious=__
**Минимальные критерии приёма:**
- заполнено хотя бы одно поле.
**Недопустимые паттерны:**
- пустые поля

### TRIZ_GX_MISSING
**Вопрос:** Заполните transformation_model: что меняется, во что превращается и почему это снимает противоречие.
**Шаблоны:**
1) changed_object=__ ; new_state=__ ; resolution_link=__
2) «Меняем __ → __, это снимает противоречие потому что __»
**Минимальные критерии приёма:**
- заполнены changed_object, new_state, resolution_link.
**Недопустимые паттерны:**
- описания без связи с противоречием

### TRIZ_GX_INCOMPLETE
**Вопрос:** Укажите недостающие поля transformation_model.
**Шаблоны:**
1) changed_object=__
2) new_state=__
3) resolution_link=__
**Минимальные критерии приёма:**
- все 3 поля заполнены.
**Недопустимые паттерны:**
- отсутствие любого поля

## 5) GOVERNANCE & TRACEABILITY
- Каждый question pack обязан ссылаться на конкретный fail_code.
- Свободные вопросы вне маппинга запрещены.
- Версионирование: спецификация меняется только при появлении новых fail_code или изменении шаблонов.

## 6) DEFINITION OF DONE (for this spec)
- Все текущие fail_codes TRIZ_CORE_ENGINE покрыты.
- Для каждого fail_code есть: 1 вопрос, 2–4 шаблона, критерии приёма, примеры недопустимых ответов.
- Нет генерации решений.
