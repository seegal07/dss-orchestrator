# RISKS_AND_OPEN_QUESTIONS_PHASE0_v0.1

## Top risks
- P0: Determinism drift if trace ordering/normalization rules are not fully canonicalized.
- P0: Boundary between "implicit parameter reveal" and "new intent injection" may be inconsistently interpreted.
- P1: Field duplication conflict (`constraints`, `system_scope`) between Phase0 top-level and existing step artifacts.
- P1: Stop-propagation semantics ambiguity (where FAIL is recorded and how NOT_RUN is represented across logs).
- P1: Hash-policy confusion if `raw_hash`, `canonical_hash`, and `input_fingerprint` are computed from mixed payload scopes.

## Blocking open questions
- Should Phase0 canonical fields be top-level only, or mirrored into `full_vector.step_3*` for downstream compatibility?
- On `phase0_verdict=FAIL`, should `GatePFL` be `NOT_RUN` or explicitly logged as skipped-by-Phase0 with separate reason code?
- Is `input_fingerprint` authoritative from Phase0 onward (overriding current pre-Phase0 derivation), or dual-reported during transition?
- Must `trace` be fully exported for all runs, or can it be summarized with `trace_count/confidence_summary` plus optional full trace artifact?
- Which exact schema-version threshold activates Phase0 by default?
