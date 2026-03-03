# OPEN_QUESTIONS_FOR_OWNER_v0.1

1) GateCR status policy: should SOFT_FAIL count as overall run `PASS` or `PARTIAL`?
2) For HARD_FAIL, do we block exactly S09–S12 only, or also S13–S14 in same run?
3) Is `COMPROMISE_MODE=TRUE` mandatory in S12_DECISION_RECORD when GateCR=SOFT_FAIL?
4) What is authoritative SoT for schema extension: `TEST_VECTOR_SCHEMA_v0.1` or a new schema version file?
5) Should GateCR be assisted-only at first release, or mixed (structural+assisted)?
6) Can GateCR produce FAIL (besides HARD_FAIL), or only PASS/SOFT_FAIL/HARD_FAIL as final states?
7) For operator selection (B>A>C>D), do we require explicit evidence of all detected types or only dominant type?
8) Separation Illusion Test: is any single YES enough for HARD_FAIL, or weighted decision?
9) Should existing historical runs be exempt from GateCR requirements (backward compatibility rule: yes/no)?
10) Message text on HARD_FAIL: fixed canonical string only, or localized variants allowed?
