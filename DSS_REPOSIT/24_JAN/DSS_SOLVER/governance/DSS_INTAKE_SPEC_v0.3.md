# DSS_INTAKE_SPEC_v0.3

Ссылка на базовый контур: DSS_SOLVER/governance/DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md

Цель v0.3: обеспечить извлечение TRIZ‑механизмов для решения (separation + principles→actions) и трассируемость до концептов.

## Обязательные блоки (v0.3)

### 1) BASELINE
Требуется baseline ключевой метрики или PROXY‑диапазон + validation_date.

### 2) THRESHOLDS
Требуются минимум 2 порога (switch + kill/stop). Диапазоны допустимы, но должны быть явными.

### 3) SEPARATION STRATEGY
Требуется минимум 1 стратегия разделения (time / space / condition / part‑whole), привязанная к противоречию (S04) и ограничениям (S01).

### 4) PRINCIPLES → ACTIONS
Требуются минимум 2 принципа (business‑адаптация) и для каждого — конкретное действие.

### 5) TRACEABILITY
Каждый концепт в S09 должен ссылаться на принцип или стратегию разделения, из которых он получен.

## Маппинг на S‑steps
- BASELINE → S04/S12/S14
- THRESHOLDS → S12/S14
- SEPARATION → S08 (TRIZ_CORE.separation_strategy)
- PRINCIPLES→ACTIONS → S08 (PRINCIPLES_TO_ACTION)
- TRACEABILITY → S09 (concept.traceability)

## Правило блокировки
Если нет separation / principles→actions / traceability, решение блокируется (Gate8/9/12).
