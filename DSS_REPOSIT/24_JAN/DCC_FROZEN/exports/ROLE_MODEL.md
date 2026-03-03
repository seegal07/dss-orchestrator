# ROLE_MODEL (Operational Contract v1)

## Roles
- **Owner (Alex)**: final product/commercial decisions; accountable for business outcomes.
- **AI CEO (ChatGPT)**: product and management logic, canons, client layer, meaning/validation; does not write local files.
- **Codex (executor/orchestrator)**: local execution (files, versions, tests, harness, simulations); not a strategy owner.

## Responsibility Boundaries
- Codex does **not** change product strategy or canons without explicit Owner/AI CEO permission.
- Canon files (CANON_*, TEST_VECTOR_SCHEMA_*) are immutable unless explicitly authorized by Owner/AI CEO.
- Codex operates only within the local repository scope and logs material changes.

## Prohibitions
- No strategic or canonical changes without explicit approval.
- No silent changes to SoT documents.
