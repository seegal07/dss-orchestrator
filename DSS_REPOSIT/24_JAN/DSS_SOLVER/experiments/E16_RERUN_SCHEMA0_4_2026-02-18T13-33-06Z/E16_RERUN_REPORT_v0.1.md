# E16_RERUN_REPORT_v0.1

## Objective
Controlled rerun of the same E16 business case with only schema upgrade to v0.4 and deterministic `search_loop=TRUE` flag.

## Evidence checks
- schema_version=0.4: CONFIRMED (`TEST_VECTOR_v0.4.json`, `TC_E16_RERUN_SCHEMA0_4.yaml`)
- search_loop=TRUE: CONFIRMED (`TC_E16_RERUN_SCHEMA0_4.yaml:step_8_5.search_loop`, `GATECR_RECORD.md`)
- mechanism wording unchanged: CONFIRMED
  - `Если Sintegrum >=8 и оба интервью PASS, делаем оффер; иначе стоп и новый поиск.`

## GateCR outcome
- GateCR status: `SOFT_FAIL`
- risk_shift_detected: `TRUE`
- PASS blocked as expected under E17 policy

## S09–S12 run-state
From `gate_summary.json`:
- Gate9: pass
- Gate10: pass
- Gate11: pass
- Gate12: pass

## Deterministic verdict
Patch behavior is valid for this controlled rerun: loop-flag forced GateCR away from PASS.
