# REQUIRED_CHANGES_LIST

## Document-level changes required before integration (do not apply in E11)

1) **Patch target**: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_SPEC_v1.0.md`
- **Section**: §2 Pipeline insertion, §8 Outcomes logic
- **Required change**: align HARD_FAIL propagation from `S09–S12` to `S09–S14` per Owner lock (Q2).

2) **Patch target**: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_SPEC_v1.0.md`
- **Section**: §10 What we do NOT change
- **Required change**: add phase-bound qualifier clarifying no-code rule applies to fixation phase only, not to approved E12 integration patch.

3) **Patch target**: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_ROUTING_RULES_v1.0.md`
- **Section**: §5 Canonical HARD_FAIL message
- **Required change**: define exact canonical literal value.

4) **Patch target**: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OWNER_POLICY_DECISIONS_v1.0.md`
- **Section**: Q10
- **Required change**: add exact canonical HARD_FAIL message string to remove ambiguity.

5) **Patch target**: (new schema doc in E12)
- **Section**: schema version routing block
- **Required change**: formalize Operator Core enable flag and backward-compat rule from Q9.
