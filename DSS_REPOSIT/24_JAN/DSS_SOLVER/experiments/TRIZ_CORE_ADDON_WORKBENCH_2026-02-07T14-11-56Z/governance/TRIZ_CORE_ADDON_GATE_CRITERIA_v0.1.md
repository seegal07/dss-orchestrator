# TRIZ_CORE_ADDON_GATE_CRITERIA_v0.1

## Gate15 — TRIZ_9_SCREENS
PASS:
- Все 9 ячеек заполнены.
- Логика времени (past/present/future) различима.
BLOCKED:
- Любая из 9 ячеек отсутствует.
FAIL:
- Явные дубли, отсутствие различий между всеми экранами.

## Gate16 — TRIZ_PHYSICAL_CONTRADICTION
PASS:
- parameter задан.
- state_A и state_B заданы и взаимоисключают друг друга.
- separation_principle указан.
BLOCKED:
- отсутствует parameter или states.
FAIL:
- state_A == state_B.

## Gate17 — CONTRADICTION_SHARPENING
PASS:
- initial_contradiction задан (ссылка на S04).
- sharpened_contradiction задан.
- justification задан.
BLOCKED:
- отсутствует sharpened_contradiction.
FAIL:
- sharpened_contradiction не отличается от initial.

## Gate18 — SUFIELD/VEPol
PASS:
- S1, S2, Field заданы.
- problematic_link задан.
- proposed_transformations ≥2.
BLOCKED:
- отсутствуют S1/S2/Field.
FAIL:
- proposed_transformations пусты.
