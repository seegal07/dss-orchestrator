# LIVE_INPUT_DIAGNOSTIC

Pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z

## A) Phase0 outputs (truth artifacts)
- canonical_slots_v0: {"scope": "выбор страны проживания семьи (Польша vs Испания) при удаленной работе", "X_direction": "other", "X_delta_direction": "increase", "X_metric_polarity": "HIGHER_IS_BETTER", "X_metric": "комфорт", "X_object": null, "Y_direction": "other", "Y_delta_direction": "increase", "Y_metric_polarity": "LOWER_IS_BETTER", "Y_metric": "налоги", "Y_object": "мой доход", "constraints": ["бюджет семьи не должен уходить в дефицит", "до июля 2026", "обучение на английском языке", "школа для ребенка должна быть определена к сентябрю 2026"], "trace_markers": ["MISSING_SLOT:X_object", "OBJ_FROM_NA_PATTERN:Y", "DELTA_FROM_RAW:X", "DELTA_FROM_RAW:Y"]}
- canonical_hash_v0: b26aabc331b3a80d7af755aefb6ebfebfb321f32d475630921b428cf1e36a188
- scope: выбор страны проживания семьи (Польша vs Испания) при удаленной работе
- constraints: ['бюджет семьи не должен уходить в дефицит', 'до июля 2026', 'обучение на английском языке', 'школа для ребенка должна быть определена к сентябрю 2026']
- timeframe: NOT_PRESENT_IN_ARTIFACT
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:10 :: canonical_slots_v0
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:8 :: canonical_hash_v0
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:11 :: scope
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:22 :: constraints

## B) StageA verdict truth-source
- GatePFL primary (gate_log): result=fail, reason=NO_MUTUAL_DEGRADATION
- GatePFL secondary (gate_summary): result=None, reason=None
- secondary_matches_primary: NOT_AVAILABLE
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/gate_log.json:90 :: gate_id=GatePFL
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/gate_log.json:92 :: result
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/gate_log.json:96 :: reason
- PFL from S03_5: status=PFL_READY, verdict=FAIL, reason=NO_MUTUAL_DEGRADATION, attempt_index=1, structural_tension=False
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:5 :: pfl_status
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:7 :: pfl_verdict
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:8 :: pfl_reason

## C) DoD evaluation (explicit PASS/FAIL)
- 1) Phase0 PASS; canonical_hash_v0 non-null: PASS
- 2) scope non-empty: PASS
- 3) X_metric non-null AND X_object non-null: FAIL
- 4) Y_metric non-null AND Y_object non-null (Y_object must not be UNKNOWN): PASS
- 5) NO MISSING_SLOT:X_metric/Y_metric/X_object/Y_object: FAIL
- 6) Polarity values non-UNKNOWN if determinable: PASS (X=HIGHER_IS_BETTER, Y=LOWER_IS_BETTER)
- 7) OBJ_FROM_NA_PATTERN:Y present: PASS (anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH_2026-02-26T09-09-26Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:30)
- 8) Truth-source GatePFL from gate_log; if summary used, matches via extractor: PASS

## D) Classification vs REGRESSION_MIN_SET_v0.1
- closest_class: POSITIVE_C
- regressions_run: NO