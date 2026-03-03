# PILOT_RUN_REPORT_v1.3

## 1) MODE
EXECUTION via harness (DSS_SOLVER/harness/harness.py run --tc-path).

## 2) INPUTS (verbatim)
Context:
- Same company: 8 branches, avg €120–150k/month, total €1.0–1.2M/month.
- CEO operational cap: 25 h/week (hard).
- Incident baseline: 8/month.
- Cost per incident: €10–30k.
- HQ hiring budget: €0 for next 90 days.

Target:
- +30% revenue in 90 days.
- Incidents must remain ≤ 8/month (hard cap).
- CEO involvement must not increase.

Deadlock (intentionally “normal”):
- Growth requires faster local decisions.
- Faster decisions require delegating approval thresholds.
- Delegation increases local mistakes and risk exposure.
- CEO cannot review more decisions.

## 3) BLOCK ANALYSIS TABLE
| Stage | Gate status | fail_reason.code | Short explanation |
|---|---|---|---|
| Contradiction | PASS (Gate4) | — | Измеримые X/Y и формула противоречия заданы |
| IKR | PASS (Gate5) | — | IKR без механизма задан |
| Separation | PASS (GateTRIZ) | — | Separation по условию задана |
| G4 (non‑obviousness) | PASS (GateTRIZ) | — | Non‑obviousness ссылается на separation |

## 4) FINAL OUTCOME
- EARLY_BLOCK_CONFIRMED: NO
- Stage where block occurred: —
- Outcome: NEEDS_MANDATORY_SEPARATION_BLOCK
- Note: NORMAL MANAGEMENT PASS (решение = пороговая автономия)

## 5) DECISION RECORD PATH (only if PASS)
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/exports/DSS_Output_Package_TC_PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-16-53Z/artifacts/S12_DECISION_RECORD.md

## 6) EVIDENCE INDEX (paths only)
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/tests/TC_PILOT_V1_3_EARLY_BLOCK.yaml
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/tests/TC_PILOT_V1_3_EARLY_BLOCK_semantic_answers.yaml
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/evidence/RUN_TC_PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-16-53Z.yaml
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/exports/DSS_Output_Package_TC_PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-16-53Z/gate_log.json
- /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/exports/DSS_Output_Package_TC_PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-16-53Z/gate_summary.json
