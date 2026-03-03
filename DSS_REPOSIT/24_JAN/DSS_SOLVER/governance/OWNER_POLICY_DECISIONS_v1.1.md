# OWNER_POLICY_DECISIONS_v1.1

Status: Owner-locked SoT
Applies to: Operator Core integration starting E11.1
Decision timestamp (UTC): 2026-02-13T14-58-00Z

---

## Q1
OWNER_LOCKED=TRUE
Decision: SOFT_FAIL => overall PARTIAL

## Q2
OWNER_LOCKED=TRUE
Decision: HARD_FAIL blocks S09–S14

## Q3
OWNER_LOCKED=TRUE
Decision: If GateCR=SOFT_FAIL then COMPROMISE_MODE=TRUE mandatory in S12_DECISION_RECORD

## Q4
OWNER_LOCKED=TRUE
Decision: Create new schema version file; do NOT edit v0.1; target TEST_VECTOR_SCHEMA_v0.2 (or equivalent naming)

## Q5
OWNER_LOCKED=TRUE
Decision: GateCR = mixed (structural presence + assisted matrix)

## Q6
OWNER_LOCKED=TRUE
Decision: GateCR outputs tri-state only: PASS / SOFT_FAIL / HARD_FAIL

## Q7
OWNER_LOCKED=TRUE
Decision: Require evidence for all detected conflict types + dominant rationale (store detected_conflict_types[] + dominant_conflict_type)

## Q8
OWNER_LOCKED=TRUE
Decision: Separation Illusion Test: any single YES => HARD_FAIL (deterministic boolean)

## Q9
OWNER_LOCKED=TRUE
Decision: Historical runs exempt from GateCR (GateCR applies only when Operator Core enabled by schema/version flag)

## Q10
OWNER_LOCKED=TRUE
Decision: HARD_FAIL message = fixed canonical string only
Canonical literal: `structural resolution not found`

---

## Phase-bound qualifier
- No-code restriction is applied to fixation phase only.
- Integration patch is allowed in E12 when authorized.
