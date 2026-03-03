# R0_R1_COMPARATIVE_REPORT_v0.1

## Case list
- CASE_01_SIMPLE: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/
- CASE_02_MEDIUM: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/

---

## CASE_01_SIMPLE
**Inputs origin:**
- R0 TC: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/tests/TC_CASE_01_SIMPLE_R0.yaml
- R1 TC: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/tests/TC_CASE_01_SIMPLE_R1.yaml
- HITL confirmation: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/notes/HITL_CONFIRMATION.md

### RUN_R0 metrics
- M1 concepts: 3 (target 3–5) — PASS
- M2 traceability completeness: 100% (concept → resource → contradiction element) — PASS
- M3 Step10 completeness: 100% (mechanism/price/bounds/risks present) — PASS
- M4 Step11 completeness: criteria derived from Core — NOT EXPLICIT (only reasons/alternatives present) — PARTIAL
- M5 taste-based choice: 0% (no arbitrary principle choice stated) — PASS
Gate9–Gate12: PASS/PASS/PASS/PASS

### RUN_R1 metrics
- M1 concepts: 3 — PASS
- M2 traceability completeness: 100% (principle→action + resource + contradiction) — PASS
- M3 Step10 completeness: 100% — PASS
- M4 Step11 completeness: criteria derived from Core — NOT EXPLICIT — PARTIAL
- M5 taste-based choice: 0% — PASS
Gate9–Gate12: PASS/PASS/PASS/PASS

### Delta (R0 vs R1)
- R1 добавляет явные principle→action связи, но качество Step10 не улучшилось.
- Нет измеримого улучшения M1–M3; M4 остаётся частичным.

**Verdict:** R1 justified? **NO** — улучшения метрик не зафиксированы.

**Evidence index:**
- R0 gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/exports/DSS_Output_Package_TC_CASE_01_SIMPLE_R0_2026-02-09T11-46-07Z/gate_log.json
- R0 gate_summary: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/exports/DSS_Output_Package_TC_CASE_01_SIMPLE_R0_2026-02-09T11-46-07Z/gate_summary.json
- R0 RUN: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/evidence/RUN_TC_CASE_01_SIMPLE_R0_2026-02-09T11-46-07Z.yaml
- R0 BUGLIST: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/evidence/BUGLIST_TC_CASE_01_SIMPLE_R0_2026-02-09T11-46-07Z.yaml
- R1 gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/exports/DSS_Output_Package_TC_CASE_01_SIMPLE_R1_2026-02-09T11-46-23Z/gate_log.json
- R1 gate_summary: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/exports/DSS_Output_Package_TC_CASE_01_SIMPLE_R1_2026-02-09T11-46-23Z/gate_summary.json
- R1 RUN: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/evidence/RUN_TC_CASE_01_SIMPLE_R1_2026-02-09T11-46-23Z.yaml
- R1 BUGLIST: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_01_SIMPLE/evidence/BUGLIST_TC_CASE_01_SIMPLE_R1_2026-02-09T11-46-23Z.yaml

---

## CASE_02_MEDIUM
**Inputs origin:**
- R0 TC: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/tests/TC_CASE_02_MEDIUM_R0.yaml
- R1 TC: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/tests/TC_CASE_02_MEDIUM_R1.yaml
- HITL confirmation: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/notes/HITL_CONFIRMATION.md

### RUN_R0 metrics
- M1 concepts: 2 — FAIL (target 3–5)
- M2 traceability completeness: 100% — PASS
- M3 Step10 completeness: 100% — PASS
- M4 Step11 completeness: criteria derived from Core — NOT EXPLICIT — PARTIAL
- M5 taste-based choice: 0% — PASS
Gate9–Gate12: PASS/PASS/PASS/PASS

### RUN_R1 metrics
- M1 concepts: 2 — FAIL
- M2 traceability completeness: 100% — PASS
- M3 Step10 completeness: 100% — PASS
- M4 Step11 completeness: criteria derived from Core — NOT EXPLICIT — PARTIAL
- M5 taste-based choice: 0% — PASS
Gate9–Gate12: PASS/PASS/PASS/PASS

### Delta (R0 vs R1)
- R1 добавляет принципные ссылки, но M1/M4 не улучшаются.
- Концептов по‑прежнему 2 (ниже цели 3–5).

**Verdict:** R1 justified? **NO** — улучшения метрик не зафиксированы.

**Evidence index:**
- R0 gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/exports/DSS_Output_Package_TC_CASE_02_MEDIUM_R0_2026-02-09T11-46-36Z/gate_log.json
- R0 gate_summary: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/exports/DSS_Output_Package_TC_CASE_02_MEDIUM_R0_2026-02-09T11-46-36Z/gate_summary.json
- R0 RUN: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/evidence/RUN_TC_CASE_02_MEDIUM_R0_2026-02-09T11-46-36Z.yaml
- R0 BUGLIST: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/evidence/BUGLIST_TC_CASE_02_MEDIUM_R0_2026-02-09T11-46-36Z.yaml
- R1 gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/exports/DSS_Output_Package_TC_CASE_02_MEDIUM_R1_2026-02-09T11-47-04Z/gate_log.json
- R1 gate_summary: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/exports/DSS_Output_Package_TC_CASE_02_MEDIUM_R1_2026-02-09T11-47-04Z/gate_summary.json
- R1 RUN: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/evidence/RUN_TC_CASE_02_MEDIUM_R1_2026-02-09T11-47-04Z.yaml
- R1 BUGLIST: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/R0_R1_COMPARATIVE_2026-02-09T11-43-19Z/CASE_02_MEDIUM/evidence/BUGLIST_TC_CASE_02_MEDIUM_R1_2026-02-09T11-47-04Z.yaml

