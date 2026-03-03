# SOURCE_OF_TRUTH (Operational Contract v1)

## Status Authority
- **KB_INDEX** is the single source of truth for ACTIVE / EVIDENCE / ARCHIVE status.
- If there is a conflict between directory structure and KB_INDEX, **KB_INDEX has priority**.

## Status Rules
- ACTIVE / EVIDENCE / ARCHIVE are defined only by KB_INDEX.
- Files in folders do not define status by themselves.

## Read-Before-Write Rule
- Any change to SoT requires reading the current version first.

## Canon Integrity
- CANON_* and TEST_VECTOR_SCHEMA_* may not be modified without explicit Owner/AI CEO approval.
