# DSS_INTAKE_GUIDED_CORRECTION_MAP_v0.2

## Gate4 (S04) — Противоречие и измеримость
Запросить:
- baseline метрик X/Y или proxy‑диапазон с validation_date.

## Gate5 (S05) — IKR
Запросить:
- формулировку желаемого результата без механизма + базовые метрики (точные или proxy).

## Gate6 (S06) — Барьер
Запросить:
- формулировку взаимоисключения, привязанную к X/Y и ограничениям.

## Gate11 (S11) — Вторичное противоречие
Запросить:
- флаг new_contradiction_exists (true/false).

## Gate12 (S12) — Решение и критерии
Запросить:
- выбранный концепт (index)
- причины выбора
- **thresholds** (switch + kill/stop), диапазоны допустимы
- если thresholds в proxy‑диапазонах → указать PROXY + validation_date
