# S09_CONCEPT_SET_LIVE

## Baseline from lineage
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/CLIENT_PATH_PILOT_V1_2026-02-10T20-39-02Z/S09_DRAFT_CONCEPTS.md
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E4_S09_UX_REDESIGN_2026-02-10T20-30-30Z/S09_DRAFT_CONCEPTS.md

## Current concepts (live)
- Концепт 1: двухэтапный договор аренды: до 30 июня с правом выхода, затем продление только при росте студентов.
- Концепт 2: переносить старт переезда: сначала ремонт и запуск на 30%, полный переезд после достижения порога посещаемости.
- Концепт 3: разделить потоки: оставить часть групп в старой локации, новые запускать в новой.

## Gate9 instrumentation
- M1 concept_count: 3
- Distinguishability checks:
  - C2 != C1: C1 меняет контрактный механизм, C2 меняет последовательность ввода локации.
  - C3 != C1: C1 про условия аренды, C3 про операционное разделение потоков обучения.
  - C3 != C2: C2 про фазовый переезд одной локации, C3 про параллельное сосуществование двух локаций.
- Traceability placeholders:
  - concept1: contradiction_ref=S06, ikr_ref=S07, resource_ref=S08
  - concept2: contradiction_ref=S06, ikr_ref=S07, resource_ref=S08
  - concept3: contradiction_ref=S06, ikr_ref=S07, resource_ref=S08

## Gate9 status (offline operator check)
- Gate9: PASS (M1>=3, distinguishable mechanisms present, placeholders set)
