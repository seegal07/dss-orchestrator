# OPERATOR_LAYER_EXECUTION_RULES_v1.1

Status: ACTIVE SoT (architecture lock)

## 1) Execution boundary
Operator Layer executes at S08.5 and GateCR only.

## 2) Deterministic operator routing
- Conflict type priority order is mandatory: `B > A > C > D`.
- Selected operator must follow this order when multiple types are present.

## 3) Mechanism production rule
- System enforces transformed frame and structural checks.
- Decision Owner provides mechanism within that frame.

## 4) GateCR enforcement
- GateCR must execute before S09.
- GateCR outcome controls S09–S14 reachability.

## 5) Reachability table
- GateCR `PASS` -> S09, S10, S11, S12, S13, S14 = RUN.
- GateCR `SOFT_FAIL` -> S09, S10, S11, S12, S13, S14 = RUN.
- GateCR `HARD_FAIL` -> S09, S10, S11, S12, S13, S14 = NOT_RUN.

## 6) Mandatory flags and statuses
- If GateCR = `SOFT_FAIL`, then `COMPROMISE_MODE=TRUE` is mandatory in S12_DECISION_RECORD.
- GateCR = `SOFT_FAIL` must map run-level status to `PARTIAL`.

## 7) Canonical fail message
- For GateCR `HARD_FAIL`, message must be exactly:
  - `structural resolution not found`

## 8) Compatibility rule
- Operator Layer is active only when schema/version flag enables Operator Core.
- Historical non-Operator runs remain valid and are exempt.

## 9) Governance phase qualifier
- No-code restriction applied to fixation phase only.
- Integration patch allowed when separately authorized.
