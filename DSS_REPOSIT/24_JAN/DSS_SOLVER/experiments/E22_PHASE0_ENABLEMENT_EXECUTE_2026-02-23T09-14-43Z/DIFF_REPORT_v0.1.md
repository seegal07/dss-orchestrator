# V2 Failure Analysis — DIFF_REPORT v0.1
PACK: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z

## 0) Inputs (raw text snippets)

### V1
MISSING: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z/INPUTS/V1_input.txt

### V2
MISSING: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z/INPUTS/V2_input.txt

### V3
MISSING: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_PHASE0_ENABLEMENT_EXECUTE_2026-02-23T09-14-43Z/INPUTS/V3_input.txt

## 1) GatePFL verdicts/reasons (truth-source)

### V1 gate_log GatePFL extract
7:    "result": "pass",
11:    "reason": "",
24:    "result": "pass",
28:    "reason": "",
41:    "result": "pass",
45:    "reason": "",
58:    "result": "fail",
62:    "reason": "Step3.flows[0] not a dict",
77:    "result": "pass",
81:    "reason": "",
90:    "gate_log_entry_id": "2026-02-23T09-14-43Z-GatePFL",
92:    "gate_id": "GatePFL",
94:    "result": "pass",
98:    "reason": "",
111:    "result": "pass",
131:    "reason": "G4-P1: Step4: improve_x/worsen_y заданы как измеримые параметры, G4-P2: statement_1l в форме 'Если улучшаем X, ухудшается Y', G4-P3: measurement_hint описывает метрики X/Y",
148:    "result": "pass",
163:    "reason": "G5-P1: IKR описывает результат без механизма, G5-P2: нет конструкций 'через/путём/используя'",
179:    "result": "pass",
194:    "reason": "G6-P1: barrier_1l выражает взаимоисключение, G6-P2: equivalent_to_step4=true",
210:    "result": "fail",
214:    "reason": "Step7.resources is not a list",
229:    "result": "pass",
233:    "reason": "",
246:    "result": "soft_fail",
250:    "reason": "Step8_5.assisted_matrix missing, risk_shift_detected=true (search_loop=true)",
266:    "result": "fail",
270:    "reason": "Step9.concepts is not a list",
285:    "result": "fail",
289:    "reason": "Step10.concept_specs is not a list",
304:    "result": "pass",
314:    "reason": "G11-P1: new_contradiction_exists=false и в решениях нет новых конфликтов",
329:    "result": "not_run",
349:    "reason": "Gate12 blocked due to Gate9/Gate11 FAIL",
364:    "result": "fail",
368:    "reason": "Step13.workstreams missing",
383:    "result": "fail",
387:    "reason": "Step14.rule_id missing, Step14.rule_statement_if_then missing, Step14.criterion missing, Step14.boundaries missing, Step14.evidence_from_case missing, Step14.test_case_action missing, Step14.version_note missing, Step14.rationale_1l missing",
409:    "result": "fail",
413:    "reason": "TRIZ_G4_INVALID: non-obviousness has no reference to separation (step_8.TRIZ_CORE.non_obviousness_check)",

### V2 gate_log GatePFL extract
7:    "result": "pass",
11:    "reason": "",
24:    "result": "pass",
28:    "reason": "",
41:    "result": "pass",
45:    "reason": "",
58:    "result": "fail",
62:    "reason": "Step3.flows[0] not a dict",
77:    "result": "pass",
81:    "reason": "",
90:    "gate_log_entry_id": "2026-02-23T09-14-44Z-GatePFL",
92:    "gate_id": "GatePFL",
94:    "result": "fail",
98:    "reason": "SOLUTION_AS_XY",
100:      "SOLUTION_AS_XY"
113:    "result": "not_run",
133:    "reason": "SOLUTION_AS_XY",
135:      "SOLUTION_AS_XY"
148:    "result": "not_run",
163:    "reason": "SOLUTION_AS_XY",
165:      "SOLUTION_AS_XY"
178:    "result": "not_run",
193:    "reason": "SOLUTION_AS_XY",
195:      "SOLUTION_AS_XY"
208:    "result": "not_run",
212:    "reason": "SOLUTION_AS_XY",
214:      "SOLUTION_AS_XY"
227:    "result": "not_run",
231:    "reason": "SOLUTION_AS_XY",
233:      "SOLUTION_AS_XY"
246:    "result": "not_run",
250:    "reason": "SOLUTION_AS_XY",
252:      "SOLUTION_AS_XY"
265:    "result": "not_run",
269:    "reason": "SOLUTION_AS_XY",
271:      "SOLUTION_AS_XY"
284:    "result": "not_run",
294:    "reason": "SOLUTION_AS_XY",
296:      "SOLUTION_AS_XY"
309:    "result": "not_run",
329:    "reason": "SOLUTION_AS_XY",
331:      "SOLUTION_AS_XY"
344:    "result": "not_run",
348:    "reason": "SOLUTION_AS_XY",
350:      "SOLUTION_AS_XY"
363:    "result": "not_run",
367:    "reason": "SOLUTION_AS_XY",
369:      "SOLUTION_AS_XY"
382:    "result": "fail",
386:    "reason": "TRIZ_G4_INVALID: non-obviousness has no reference to separation (step_8.TRIZ_CORE.non_obviousness_check)",

### V3 gate_log GatePFL extract
7:    "result": "pass",
11:    "reason": "",
24:    "result": "pass",
28:    "reason": "",
41:    "result": "pass",
45:    "reason": "",
58:    "result": "fail",
62:    "reason": "Step3.flows[0] not a dict",
77:    "result": "pass",
81:    "reason": "",
90:    "gate_log_entry_id": "2026-02-23T09-14-44Z-GatePFL",
92:    "gate_id": "GatePFL",
94:    "result": "pass",
98:    "reason": "",
111:    "result": "pass",
131:    "reason": "G4-P1: Step4: improve_x/worsen_y заданы как измеримые параметры, G4-P2: statement_1l в форме 'Если улучшаем X, ухудшается Y', G4-P3: measurement_hint описывает метрики X/Y",
148:    "result": "pass",
163:    "reason": "G5-P1: IKR описывает результат без механизма, G5-P2: нет конструкций 'через/путём/используя'",
179:    "result": "pass",
194:    "reason": "G6-P1: barrier_1l выражает взаимоисключение, G6-P2: equivalent_to_step4=true",
210:    "result": "fail",
214:    "reason": "Step7.resources is not a list",
229:    "result": "pass",
233:    "reason": "",
246:    "result": "soft_fail",
250:    "reason": "Step8_5.assisted_matrix missing, risk_shift_detected=true (search_loop=true)",
266:    "result": "fail",
270:    "reason": "Step9.concepts is not a list",
285:    "result": "fail",
289:    "reason": "Step10.concept_specs is not a list",
304:    "result": "pass",
314:    "reason": "G11-P1: new_contradiction_exists=false и в решениях нет новых конфликтов",
329:    "result": "not_run",
349:    "reason": "Gate12 blocked due to Gate9/Gate11 FAIL",
364:    "result": "fail",
368:    "reason": "Step13.workstreams missing",
383:    "result": "fail",
387:    "reason": "Step14.rule_id missing, Step14.rule_statement_if_then missing, Step14.criterion missing, Step14.boundaries missing, Step14.evidence_from_case missing, Step14.test_case_action missing, Step14.version_note missing, Step14.rationale_1l missing",
409:    "result": "fail",
413:    "reason": "TRIZ_G4_INVALID: non-obviousness has no reference to separation (step_8.TRIZ_CORE.non_obviousness_check)",

## 2) Phase0 outputs (canonical_* + hashes + trace)

### V1 S03_0_PHASE0_OUTPUT.md (canonical + trace)
4:  "phase0_enabled": true,
5:  "phase0_verdict": "PASS",
6:  "phase0_reason_code": "NONE",
7:  "canonical_hash": "738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c",
8:  "raw_hash": "cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c",
9:  "trace_count": 4,
10:  "confidence_summary": "HIGH",
11:  "canonical_scope": "правило запуска новых филиалов в Европе",
12:  "canonical_X": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
13:  "canonical_Y": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
14:  "canonical_constraints": [

### V2 S03_0_PHASE0_OUTPUT.md (canonical + trace)
4:  "phase0_enabled": true,
5:  "phase0_verdict": "PASS",
6:  "phase0_reason_code": "NONE",
7:  "canonical_hash": "b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302",
8:  "raw_hash": "d4028706e3cf04fd0c6b89b5385fdeb940ab41856606329a97260e6930666c2e",
9:  "trace_count": 4,
10:  "confidence_summary": "HIGH",
11:  "canonical_scope": "правило запуска новых филиалов в Европе",
12:  "canonical_X": "Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
13:  "canonical_Y": "Не повышать чрезмерно длительность и стоимость подготовки запуска.",
14:  "canonical_constraints": [

### V3 S03_0_PHASE0_OUTPUT.md (canonical + trace)
4:  "phase0_enabled": true,
5:  "phase0_verdict": "PASS",
6:  "phase0_reason_code": "NONE",
7:  "canonical_hash": "26160f1f447d4ca0067978ba76d14c8d5d27bbe63b069e2e50d2184aeaa73f9e",
8:  "raw_hash": "19a8bcdc887b225c0bf6b007e8e1477a0a12bc1e4b0e439cb7641cc3cc2f45f8",
9:  "trace_count": 4,
10:  "confidence_summary": "HIGH",
11:  "canonical_scope": "правило запуска новых филиалов в Европе",
12:  "canonical_X": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",
13:  "canonical_Y": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",
14:  "canonical_constraints": [

## 3) Canonical object used by Admission (case.json)

### V1 case.json canonical_object extract
SOURCE: instrumentation.canonical_object
{
  "system_scope": "правило запуска новых филиалов в Европе",
  "X_param": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
  "Y_param": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
  "constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "conflict_type_candidate": "causal"
}

### V2 case.json canonical_object extract
SOURCE: instrumentation.canonical_object
{
  "system_scope": "правило запуска новых филиалов в Европе",
  "X_param": "Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
  "Y_param": "Не повышать чрезмерно длительность и стоимость подготовки запуска.",
  "constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "conflict_type_candidate": "causal"
}

### V3 case.json canonical_object extract
SOURCE: instrumentation.canonical_object
{
  "system_scope": "правило запуска новых филиалов в Европе",
  "X_param": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",
  "Y_param": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",
  "constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "conflict_type_candidate": "causal"
}

## 4) Diff summary (V2 vs V1/V3) — canonical fields
### Phase0 canonical_* line diff (grep-based)

#### canonical_hash
V1: 7:  "canonical_hash": "738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c",
V2: 7:  "canonical_hash": "b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302",
V3: 7:  "canonical_hash": "26160f1f447d4ca0067978ba76d14c8d5d27bbe63b069e2e50d2184aeaa73f9e",

#### canonical_scope
V1: 11:  "canonical_scope": "правило запуска новых филиалов в Европе",
V2: 11:  "canonical_scope": "правило запуска новых филиалов в Европе",
V3: 11:  "canonical_scope": "правило запуска новых филиалов в Европе",

#### canonical_X
V1: 12:  "canonical_X": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
V2: 12:  "canonical_X": "Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
V3: 12:  "canonical_X": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",

#### canonical_Y
V1: 13:  "canonical_Y": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
V2: 13:  "canonical_Y": "Не повышать чрезмерно длительность и стоимость подготовки запуска.",
V3: 13:  "canonical_Y": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",

#### canonical_constraints
V1: 14:  "canonical_constraints": [
V2: 14:  "canonical_constraints": [
V3: 14:  "canonical_constraints": [

#### raw_hash
V1: 8:  "raw_hash": "cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c",
V2: 8:  "raw_hash": "d4028706e3cf04fd0c6b89b5385fdeb940ab41856606329a97260e6930666c2e",
V3: 8:  "raw_hash": "19a8bcdc887b225c0bf6b007e8e1477a0a12bc1e4b0e439cb7641cc3cc2f45f8",

#### trace_count
V1: 9:  "trace_count": 4,
V2: 9:  "trace_count": 4,
V3: 9:  "trace_count": 4,

## 5) Preliminary localization (facts only, no hypotheses)
- If V2 canonical_X/Y/scope/constraints differ from V1/V3 while invariants expected, Phase0 normalization is changing the object.
- If V2 canonical_* identical but GatePFL differs, SOLUTION_AS_XY detector reacts to something else (e.g., action markers in canonical text) not captured by these keys.
- This report does not change logic; it only surfaces evidence.
