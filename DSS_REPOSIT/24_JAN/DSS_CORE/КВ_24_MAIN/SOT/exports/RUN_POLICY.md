# RUN_POLICY (Operational Contract v1)

## OK_RUN
- A RUN is executed **only** after explicit OK_RUN from Alex.

## Evidence Versioning
- Each RUN creates a **new** evidence version (RUN + BUG_LIST), without overwriting prior evidence.

## No-Promote Default
- Evidence does **not** become ACTIVE unless separately decided and KB_INDEX is patched.

## Integrity
- Evidence is never deleted or overwritten without explicit permission.

## Traceability
- Each change should include a brief "what/why" note in AUDIT_LOG or KB_INDEX.
