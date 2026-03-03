# DSS_INTAKE_SPEC_v0.2

Цель: обеспечить извлечение baseline, thresholds и proxy‑metrics без догадок, чтобы решение могло быть валидным либо корректно блокировалось.

## Обязательные блоки (v0.2)

### 1) BASELINE
Требуется явный baseline по ключевой метрике решения.
- Если baseline неизвестен: фиксировать `UNKNOWN` и требовать proxy‑диапазон + дату валидации.

### 2) THRESHOLDS
Требуется минимум 2 порога:
- switch‑threshold (когда меняем режим)
- kill/stop‑threshold (когда прекращаем решение)
Пороги могут быть диапазонами, но должны быть явно заданы.

### 3) PROXY‑METRICS
Если точные метрики отсутствуют, допускаются только proxy‑диапазоны с пометкой `PROXY` и `validation_date`.
Разрешённые proxy:
- gross margin band (диапазон)
- cash runway band (недели/месяцы)
- CAC payback band
- burn band

## Правило блокировки
Если нет baseline + thresholds (или хотя бы proxy‑диапазонов с датой валидации), решение блокируется.

## Маппинг на S‑steps
- BASELINE → S04/S12/S14
- THRESHOLDS → S12/S14
- PROXY‑METRICS → S04/S05/S12
