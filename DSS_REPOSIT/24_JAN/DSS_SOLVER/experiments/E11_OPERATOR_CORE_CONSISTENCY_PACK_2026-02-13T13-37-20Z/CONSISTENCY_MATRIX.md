# CONSISTENCY_MATRIX

| Spec clause | Policy decision | Routing rule | Status | Notes |
|---|---|---|---|---|
| S08.5 inserted between S08 and S09 (`OPERATOR_CORE_SPEC_v1.0`, §2) | Q4 new schema version for Operator Core enablement | GateCR table exists | OK | Alignment complete |
| GateCR mandatory before S09 (`OPERATOR_CORE_SPEC_v1.0`, §2) | Q5 GateCR mixed (structural+assisted) | GateCR tri-state table | OK | Compatible |
| GateCR outcomes PASS/SOFT_FAIL/HARD_FAIL (`OPERATOR_CORE_SPEC_v1.0`, §8) | Q6 tri-state only | Tri-state table | OK | Compatible |
| SOFT_FAIL => `COMPROMISE_MODE=TRUE` (`OPERATOR_CORE_SPEC_v1.0`, §2/§8) | Q3 mandatory in S12 | Routing row SOFT_FAIL sets mandatory flag | OK | Compatible |
| SOFT_FAIL run-level mapping | Q1 overall PARTIAL | Routing §3 defines PARTIAL | OK | Compatible |
| Deterministic priority B>A>C>D (`OPERATOR_CORE_SPEC_v1.0`, §3) | Q7 all detected types + dominant rationale | Not contradicted | OK | Requires schema fields in implementation |
| Separation Illusion Test included (`OPERATOR_CORE_SPEC_v1.0`, §7) | Q8 any single YES => HARD_FAIL | Not contradicted | OK | Deterministic policy clear |
| Canonical HARD_FAIL message (`OPERATOR_CORE_SPEC_v1.0`, §2/§8 text shown) | Q10 fixed canonical string only | Routing §5 fixed canonical | OK | Compatible |
| Historical runs exempt | Q9 exempt by schema/version flag | Routing §4 explicit exempt | OK | Compatible |
| HARD_FAIL propagation scope (`OPERATOR_CORE_SPEC_v1.0`, §2/§8 says S09–S12) | Q2 says block S09–S14 | Routing §2 says S09–S14 | CONFLICT | Spec vs Policy/Routing mismatch on propagation boundary |
| “No harness code changes” (`OPERATOR_CORE_SPEC_v1.0`, §10) | E11 objective is pre-integration planning | Routing introduces runtime behavior target | AMBIGUOUS | Clause appears phase-specific; needs explicit “applies only to v1.0 fixation phase” |
| Canonical string exact value | Q10 fixed canonical string | Routing §5 fixed canonical, but no literal value | AMBIGUOUS | Missing exact canonical literal for implementation lock |

## CONFLICT DETAILS
1) Propagation boundary conflict:
- Spec source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_SPEC_v1.0.md` §2, §8 (S09–S12)
- Policy source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OWNER_POLICY_DECISIONS_v1.0.md` Q2 (S09–S14)
- Routing source: `/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/OPERATOR_CORE_ROUTING_RULES_v1.0.md` §2 (S09–S14)
- Incompatibility: different NOT_RUN propagation scope.
