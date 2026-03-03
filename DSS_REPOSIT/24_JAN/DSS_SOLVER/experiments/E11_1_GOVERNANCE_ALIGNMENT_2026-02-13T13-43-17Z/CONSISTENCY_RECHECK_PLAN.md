# CONSISTENCY_RECHECK_PLAN

1) Rebuild consistency matrix against v1.1 documents:
- OPERATOR_CORE_SPEC_v1.1
- OWNER_POLICY_DECISIONS_v1.1
- OPERATOR_CORE_ROUTING_RULES_v1.1

2) Validate mandatory checkpoints:
- HARD_FAIL propagation = S09–S14 across all three SoT docs.
- Canonical HARD_FAIL literal exactly equal in routing + owner policy.
- Phase-bound qualifier present in spec/policy set.

3) Recompute summary counters:
- OK / CONFLICT / AMBIGUOUS
- READY_FOR_E12 = YES only if CONFLICT=0 and AMBIGUOUS on blockers=0.
