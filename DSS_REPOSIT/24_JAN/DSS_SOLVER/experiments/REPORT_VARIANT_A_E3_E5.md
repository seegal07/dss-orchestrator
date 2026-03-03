# REPORT_VARIANT_A_E3_E5

Эксперименты:

1) E3_REAL_CASE_002_2026-02-07T13-18-18Z — DECISION_VALID
- Где ломалось: не ломалось (decision‑critical PASS)
- Слабые места: нет

2) E4_REAL_CASE_003_2026-02-07T13-18-18Z — DECISION_INVALID
- Где ломалось: S05 (IKR), S06 (барьер), S11 (новое противоречие), S12 (выбор решения)
- Decision‑critical: Gate5/6/11/12 = BLOCKED

3) E5_REAL_CASE_004_2026-02-07T13-18-18Z — DECISION_VALID
- Где ломалось: не ломалось (decision‑critical PASS)

Частые точки поломки intake:
- Формулирование IKR (S05)
- Формулирование барьера (S06)
- Выбор решения и критерии успеха (S12)
