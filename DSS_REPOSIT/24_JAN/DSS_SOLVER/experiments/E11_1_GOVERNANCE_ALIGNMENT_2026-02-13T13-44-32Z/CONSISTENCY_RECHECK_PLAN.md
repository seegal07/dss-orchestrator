# CONSISTENCY_RECHECK_PLAN

1. Re-run E11 consistency matrix using v1.1 sources:
   - OPERATOR_CORE_SPEC_v1.1.md
   - OPERATOR_CORE_ROUTING_RULES_v1.1.md
   - OWNER_POLICY_DECISIONS_v1.1.md

2. Verify three required alignments:
   - HARD_FAIL propagation scope is `S09–S14` across all three documents.
   - Canonical HARD_FAIL literal is identical in routing §5 and owner Q10.
   - Phase-bound qualifier is present and explicitly scoped to fixation-only no-code, with E12 authorized integration allowance.

3. Confirm unchanged semantics:
   - Tri-state remains PASS / SOFT_FAIL / HARD_FAIL.
   - Gate9–Gate12 semantics unchanged.

4. Expected E11 recheck output:
   - conflict count for governance alignment = 0
   - READY_FOR_E12 = YES
