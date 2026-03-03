# DIALOGUE_CHANGELOG_CLIENT_SELF_RUN

## Итерация 1 (baseline)
- Стартовый факт‑тупик от клиента (гибридная группа Python распадается).
- TRIZ‑поля отсутствуют: physical_contradiction, separation, system_operator, transformation_model, non_obviousness.
- GateTRIZ: FAIL (TRIZ_G1_MISSING, TRIZ_G2_MISSING, TRIZ_G3_MISSING, TRIZ_G4_MISSING, TRIZ_GX_MISSING).

## Итерация 2 (guided elicitation, первая попытка заполнения)
- Клиент дал:
  - physical_contradiction (object/parameter/state_a/state_not_a).
  - separation_type=condition; what_changes/expected_resolution.
  - system_present/subsystem_present/system_future.
  - non_obviousness (общая формулировка без явной ссылки на separation).
  - transformation_model.
- GateTRIZ: FAIL (TRIZ_G4_INVALID — non‑obviousness без явной ссылки на separation).

## Итерация 3 (guided elicitation, уточнение non‑obviousness)
- Клиент подтвердил формулировку, явно содержащую фразу из separation:
  - why_not_obvious=«офлайн остаётся основным режимом, онлайн — исключение без распада группы».
- GateTRIZ: PASS.
- Но Gate11/Gate12: BLOCKED (нет концептов, выбора и критериев).

## Языковые/формулировочные моменты
- Требовалась явная текстовая привязка non‑obviousness к separation (условие) — без этого G4 валидатор блокировал.
- Переформулировки шли с пользовательского языка на структурированный формат TRIZ_CORE.
- Отдельных переходов русского → английского не было; использовались только структурные поля.

## Итог
- TRIZ‑блок пройден, но решение не сформировано из‑за отсутствия Step9/Step12.
- Статус кейса: BLOCKED.
