# HARNESS_IMPACT_NOTES_v0.1

## 1) New runtime recognition points
- New step id: `S08.5` (operator frame artifact).
- New gate id: `GateCR`.
- New statuses: PASS|SOFT_FAIL|HARD_FAIL for GateCR (mapped into run status policy).

## 2) Required orchestration behavior
- Evaluate GateCR after S08/Gate8(+GateTRIZ), before S09.
- If GateCR=HARD_FAIL -> set Gate9..Gate12 to NOT_RUN.
- If GateCR=SOFT_FAIL -> allow S09..S12 with `COMPROMISE_MODE=TRUE` attached to outputs.

## 3) Logging/export impact
- `gate_log.json` / `gate_summary.json` must include GateCR entry.
- Export artifacts must include:
  - S08_5_OPERATOR_FRAME
  - GATECR_EVIDENCE
  - S09_MECHANISM_TRACE

## 4) Unchanged semantics confirmation
- Gate9 semantics unchanged.
- Gate10 semantics unchanged.
- Gate11 semantics unchanged.
- Gate12 semantics unchanged.
- Only reachability is additionally gated by GateCR outcome.

## 5) Assisted/live mode note
- Assisted/live flows may produce S08.5/GateCR artifacts manually.
- Machine-run mode must normalize them into gate statuses identically.
