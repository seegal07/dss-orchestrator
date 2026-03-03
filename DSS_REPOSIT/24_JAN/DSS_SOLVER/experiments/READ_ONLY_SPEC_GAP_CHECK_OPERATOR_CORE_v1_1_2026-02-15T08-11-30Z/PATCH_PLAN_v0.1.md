# PATCH_PLAN_v0.1

Read-only planning output (no patch applied).

## Minimal plan if strict alignment is requested

1. **Governance clarification patch (docs-only)**
- Target: execution-mode docs/index.
- Add explicit line: harness currently enforces schema/gates; MODE protocol is process-level unless implemented in code.

2. **Schema/runtime authority clarification (docs-only)**
- Target: `TEST_VECTOR_SCHEMA_v0.2.md`.
- Clarify that `step_8_5.gatecr_status` and `hard_fail_message` may be input placeholders, but runtime-calculated GateCR is authoritative.

3. **Optional runtime hardening (code, not executed in this task)**
- Add explicit warning in export when prefilled input GateCR fields differ from computed GateCR.

4. **Acceptance checks (future, not executed)**
- Case A: GateCR HARD_FAIL -> S09–S14 NOT_RUN + canonical literal exact match.
- Case B: GateCR SOFT_FAIL -> overall PARTIAL + S12 `compromise_mode=true` required.
- Case C: historical v0.1 schema -> GateCR exempt.
