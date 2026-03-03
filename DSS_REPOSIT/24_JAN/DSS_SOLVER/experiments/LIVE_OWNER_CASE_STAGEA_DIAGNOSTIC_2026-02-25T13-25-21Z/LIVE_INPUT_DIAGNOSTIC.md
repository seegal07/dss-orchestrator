# LIVE_INPUT_DIAGNOSTIC

Pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z

## A) Phase0 outputs (truth artifacts)
- canonical_slots_v0: {"scope": "смена страны проживания с Польши на Испанию при удаленной работе", "X_direction": "other", "X_delta_direction": "unknown", "X_metric_polarity": "UNKNOWN", "X_metric": "качество", "X_object": null, "Y_direction": "other", "Y_delta_direction": "unknown", "Y_metric_polarity": "HIGHER_IS_BETTER", "Y_metric": "точность", "Y_object": "UNKNOWN", "constraints": ["желательно старшую школу заканчивать в Европе с обучением на английском", "ребенок заканчивает 9 класс", "с сентября ребенку нужно идти в школу или в Польше или в Испании", "Хочу принять решение до июля текущего года"], "trace_markers": ["MISSING_SLOT:X_object", "MISSING_SLOT:Y_object", "MISSING_SLOT:X_delta_direction", "MISSING_SLOT:Y_delta_direction", "UNKNOWN_POLARITY:X"]}
- canonical_hash_v0: 02023e4fc493d7c24f6aefac4b9cf6a66b0d88f3d827b0a4d6a00d91f8c58eda
- scope: смена страны проживания с Польши на Испанию при удаленной работе
- constraints: ['желательно старшую школу заканчивать в Европе с обучением на английском', 'ребенок заканчивает 9 класс', 'с сентября ребенку нужно идти в школу или в Польше или в Испании', 'Хочу принять решение до июля текущего года']
- timeframe: NOT_PRESENT_IN_ARTIFACT
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_0_PHASE0_OUTPUT.md:10 :: "canonical_slots_v0": {
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_0_PHASE0_OUTPUT.md:8 :: "canonical_hash_v0": "02023e4fc493d7c24f6aefac4b9cf6a66b0d88f3d827b0a4d6a00d91f8c58eda",
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_0_PHASE0_OUTPUT.md:39 :: "canonical_scope": "смена страны проживания с Польши на Испанию при удаленной работе",
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_0_PHASE0_OUTPUT.md:42 :: "canonical_constraints": [

## B) Stage A verdict (truth-source)
- GatePFL (truth-source gate_log): result=fail, reason=NO_MUTUAL_DEGRADATION
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/gate_log.json:90 :: gate_id
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/gate_log.json:92 :: result
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/gate_log.json:96 :: reason
- PFL from S03_5: status=PFL_READY, verdict=FAIL, reason=NO_MUTUAL_DEGRADATION, attempt_index=1, structural_tension=False
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:5 :: "pfl_status": "PFL_READY",
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:7 :: "pfl_verdict": "FAIL",
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:8 :: "pfl_reason": "NO_MUTUAL_DEGRADATION",
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:9 :: "pfl_attempt_index": 1,
- anchor /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_DIAGNOSTIC_2026-02-25T13-25-21Z/EXPORTS/V1/artifacts/S03_5_PFL_OUTPUT.md:10 :: "pfl_structural_tension": false,

## C) Input classification (artifact-derived)
- labels: insufficient-data
- triggers: GatePFL reason=NO_MUTUAL_DEGRADATION; PFL reason=NO_MUTUAL_DEGRADATION; trace_markers=['MISSING_SLOT:X_object', 'MISSING_SLOT:Y_object', 'MISSING_SLOT:X_delta_direction', 'MISSING_SLOT:Y_delta_direction', 'UNKNOWN_POLARITY:X']

## D) Delta vs REGRESSION_MIN_SET_v0.1
- closest_class: POSITIVE_C
- basis: GatePFL reason matches POSITIVE_C signature
- regressions_run: NO