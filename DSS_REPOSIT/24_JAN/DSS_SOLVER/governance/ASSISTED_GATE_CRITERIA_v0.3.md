# ASSISTED_GATE_CRITERIA_v0.3

Ссылка на базовый контур: DSS_SOLVER/governance/DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md

---

## Gate4 — CONTRADICTION_STATEMENT
PASS:
- improve_x / worsen_y заданы измеримо.
- statement_1l в форме «если X, ухудшается Y».
- measurement_hint содержит baseline или PROXY + validation_date.

FAIL:
- нет измеримости / нет measurement_hint.

BLOCKED:
- отсутствуют ключевые поля Step4.

---

## Gate8 — TRIZ_CORE_ENFORCEMENT
PASS:
- TRIZ_CORE.CONTRADICTION_1L задан.
- TRIZ_CORE.IKR_1L задан.
- TRIZ_CORE.separation_strategy содержит ≥1 стратегию (time/space/condition/part‑whole).
- PRINCIPLES_TO_ACTION.PRINCIPLES содержит ≥2 принципа.
- PRINCIPLES_TO_ACTION.ACTIONS содержит ≥2 действий, связанных с принципами.

FAIL:
- отсутствует хотя бы один из обязательных элементов.

BLOCKED:
- отсутствуют блоки TRIZ_CORE или PRINCIPLES_TO_ACTION.

---

## Gate9 — CONCEPT_TRACEABILITY
PASS:
- Каждый концепт в Step9 содержит поле traceability и ссылку на принцип или стратегию разделения.

FAIL:
- хотя бы у одного концепта нет traceability.

BLOCKED:
- отсутствуют концепты.

---

## Gate12 — DECISION_RECORD
PASS:
- chosen_concept_index существует в Step9.
- reasons ссылаются на ≥1 separation_strategy и ≥1 principle→action.
- success_criteria содержат thresholds (switch + kill/stop) + baseline/proxy.

FAIL:
- причины не содержат ссылок на separation или principle‑action.
- thresholds отсутствуют.

BLOCKED:
- выбранный концепт / причины отсутствуют.
