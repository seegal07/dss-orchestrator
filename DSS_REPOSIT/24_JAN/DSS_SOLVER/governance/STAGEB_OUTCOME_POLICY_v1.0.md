# STAGEB_OUTCOME_POLICY_v1.0
Status: ACTIVE
Scope: Stage B outcome classification only

## Outcome Domain
Allowed values:
- JUMP
- COMPROMISE
- INCONCLUSIVE

## Deterministic Rule
Every Stage B run must produce exactly one outcome from the allowed domain.

## Validation
- Value must be uppercase exact match.
- Any value outside the domain is invalid.

## Notes
This policy defines outcome labels only and does not alter engine, harness, PFL, or Phase0 logic.
