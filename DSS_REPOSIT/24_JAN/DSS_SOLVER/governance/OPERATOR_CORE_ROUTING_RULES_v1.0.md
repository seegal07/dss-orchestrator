# OPERATOR_CORE_ROUTING_RULES_v1.0

Status: SoT for Operator Core routing (E11)

## 1) GateCR tri-state transition table

| GateCR status | S09 | S10 | S11 | S12 | S13 | S14 | Required flags | Run-level status |
|---|---|---|---|---|---|---|---|---|
| PASS | RUN | RUN | RUN | RUN | RUN | RUN | `COMPROMISE_MODE=FALSE` | no GateCR downgrade |
| SOFT_FAIL | RUN | RUN | RUN | RUN | RUN | RUN | `COMPROMISE_MODE=TRUE` (mandatory in S12_DECISION_RECORD) | `PARTIAL` |
| HARD_FAIL | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | canonical hard-fail message only | `FAIL`/blocked by policy |

## 2) NOT_RUN propagation on HARD_FAIL
- Mandatory propagation target: S09–S14.
- No downstream step execution after GateCR=HARD_FAIL.

## 3) Run-level mapping
- GateCR=SOFT_FAIL => overall run status must be `PARTIAL`.
- GateCR=PASS => run-level status is determined by remaining gates.
- GateCR=HARD_FAIL => downstream steps NOT_RUN; run reported as failed/blocked per harness policy.

## 4) Backward compatibility rule
- Historical runs are exempt from GateCR.
- GateCR applies only when Operator Core is enabled by schema/version flag.
- Existing artifacts without S08.5/GateCR remain valid historical evidence.

## 5) Canonical HARD_FAIL message
- Fixed canonical string only.
- Localized variants are not allowed for machine-audit consistency.
