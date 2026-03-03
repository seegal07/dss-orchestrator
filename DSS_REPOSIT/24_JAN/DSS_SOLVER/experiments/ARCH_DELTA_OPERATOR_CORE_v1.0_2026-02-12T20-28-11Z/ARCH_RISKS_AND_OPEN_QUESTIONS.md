# ARCH_RISKS_AND_OPEN_QUESTIONS

1. Final canonical location for S08.5 schema (pipeline canon vs governance-only) is not fixed.
2. Exact evidence format for GateCR Q1..Q5 (text-only vs structured keys) requires Owner choice.
3. SOFT_FAIL threshold boundary is not numerically bounded; requires explicit acceptance threshold.
4. Interaction between GateTRIZ FAIL and GateCR status precedence needs ordering rule.
5. Whether COMPROMISE_MODE propagates into S12 decision record as mandatory field is unresolved.
6. Required minimum traceability depth (`operator_used` + X/Y + structural change) needs Owner lock for audit strictness.
7. Source-of-truth for dominant conflict type classification (manual vs deterministic parser) is unspecified.
8. Separation Illusion Test evidence granularity (single line vs checklist proof) is unspecified.
9. Whether HARD_FAIL message text must be canonicalized globally is unresolved.
10. Backward compatibility policy for historical runs without S08.5/GateCR is not defined.
