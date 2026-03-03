# E22 SLOT INVARIANCE RUN v1

## Active SoT
- ACTIVE index: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_2_DECISION_LAYER_LINKS_v1.1.md
- Active Phase0 spec: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/PHASE0_CONFLICT_FORMALIZATION_SPEC_v0.2.md
- Active StageA metrics spec: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/STAGEA_METRICS_SPEC_v0.1.1_v1.2.md

## Source vectors
- V1: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z/TC_PATCHED/E22_V1.yaml
- V2: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z/TC_PATCHED/E22_V2.yaml
- V3: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z/TC_PATCHED/E22_V3.yaml

## Step1: slot-invariance via canonical_hash
- Result: FAIL
- V1: hash=738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c
  anchor: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_SLOT_INVARIANCE_RUN_2026-02-23T10-14-08Z/EXPORTS/V1/S03_0_PHASE0_OUTPUT.md:7:"canonical_hash": "738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c",
- V2: hash=b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302
  anchor: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_SLOT_INVARIANCE_RUN_2026-02-23T10-14-08Z/EXPORTS/V2/S03_0_PHASE0_OUTPUT.md:7:"canonical_hash": "b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302",
- V3: hash=26160f1f447d4ca0067978ba76d14c8d5d27bbe63b069e2e50d2184aeaa73f9e
  anchor: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_SLOT_INVARIANCE_RUN_2026-02-23T10-14-08Z/EXPORTS/V3/S03_0_PHASE0_OUTPUT.md:7:"canonical_hash": "26160f1f447d4ca0067978ba76d14c8d5d27bbe63b069e2e50d2184aeaa73f9e",
- SLOT_DIVERGENCE:
  - canonical_X: {'V1': '"Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска."', 'V2': '"Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта."', 'V3': '"Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия."'}
  - canonical_Y: {'V1': '"Не увеличивать чрезмерно время и стоимость подготовки запуска."', 'V2': '"Не повышать чрезмерно длительность и стоимость подготовки запуска."', 'V3': '"Не увеличивать избыточно сроки и расходы на подготовку запуска."'}
  - raw_hash: {'V1': '"cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c"', 'V2': '"d4028706e3cf04fd0c6b89b5385fdeb940ab41856606329a97260e6930666c2e"', 'V3': '"19a8bcdc887b225c0bf6b007e8e1477a0a12bc1e4b0e439cb7641cc3cc2f45f8"'}

## Step2: verdict-invariance via GatePFL
- Result: NOT_APPLICABLE

- Summary JSON: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_SLOT_INVARIANCE_RUN_2026-02-23T10-14-08Z/SUMMARY.json