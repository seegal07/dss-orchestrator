# LIVE_INPUT_DIAGNOSTIC

Pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z

## A) Phase0 outputs (truth artifacts)
- canonical_slots_v0: {"scope": "выбор страны проживания семьи (Польша vs Испания) при удаленной работе", "X_direction": "other", "X_delta_direction": "increase", "X_metric_polarity": "UNKNOWN", "X_metric": null, "X_object": null, "Y_direction": "other", "Y_delta_direction": "increase", "Y_metric_polarity": "UNKNOWN", "Y_metric": null, "Y_object": "UNKNOWN", "constraints": ["бюджет семьи не должен уходить в дефицит", "до июля 2026", "обучение на английском языке", "школа для ребенка должна быть определена к сентябрю 2026"], "trace_markers": ["MISSING_SLOT:X_metric", "MISSING_SLOT:Y_metric", "MISSING_SLOT:X_object", "MISSING_SLOT:Y_object", "DELTA_FROM_RAW:X", "DELTA_FROM_RAW:Y", "UNKNOWN_POLARITY:X", "UNKNOWN_POLARITY:Y"]}
- canonical_hash_v0: 7b529a5df816d766ab760942e72c27ccc6675573b3d08136c7c80b56a6a2c67d
- scope: выбор страны проживания семьи (Польша vs Испания) при удаленной работе
- constraints: ['бюджет семьи не должен уходить в дефицит', 'до июля 2026', 'обучение на английском языке', 'школа для ребенка должна быть определена к сентябрю 2026']
- timeframe: NOT_PRESENT_IN_ARTIFACT
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:10 :: canonical_slots_v0
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:8 :: canonical_hash_v0
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:11 :: scope
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:22 :: constraints

## B) StageA verdict truth-source
- GatePFL primary (gate_log): result=fail, reason=NO_MUTUAL_DEGRADATION
- GatePFL secondary (gate_summary): result=None, reason=None
- secondary_matches_primary: NOT_AVAILABLE
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/gate_log.json:90 :: gate_id=GatePFL
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/gate_log.json:92 :: result
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/gate_log.json:96 :: reason
- PFL from S03_5: status=PFL_READY, verdict=FAIL, reason=NO_MUTUAL_DEGRADATION, attempt_index=1, structural_tension=False
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:5 :: pfl_status
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:7 :: pfl_verdict
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_2026-02-25T19-41-55Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:8 :: pfl_reason

## C) DoD evaluation (explicit)
- Phase0 PASS; canonical_hash_v0 non-null: PASS
- scope non-empty; X_metric+X_object non-null; Y_metric+Y_object non-null: FAIL
- NO MISSING_SLOT:X_object / NO MISSING_SLOT:Y_object: FAIL
- GatePFL truth-source obeyed; if summary used, matches extractor path: PASS
- GatePFL may be FAIL/NO_MUTUAL_DEGRADATION (not a failure): ACK

## D) Classification vs REGRESSION_MIN_SET_v0.1
- closest_class: POSITIVE_C
- regressions_run: NO