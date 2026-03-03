# DSS_TRIZ_FULL_AUDIT_DOSSIER_v0.1

## A) EXECUTIVE FACTS

### Что система делает сейчас по факту
Текущий исполняемый контур в ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py` запускает структурные гейты `Gate0..Gate14`, накладывает assisted-оценки только для `Gate4/5/6/11/12`, затем обязательный `GateTRIZ` через ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py`, после чего пишет evidence (`RUN/BUGLIST`) и экспорт (`gate_log.json`, `gate_summary.json`, `artifacts/*`) через `_export_package()` (`harness.py:287`, `harness.py:455`).

### Что система НЕ делает
Система не генерирует концепты/механизмы самостоятельно в коде: `S09.concepts` и `S10.concept_specs` приходят из входного TC/диалога; harness только валидирует наличие/минимальную структуру (`gates_structural.py:187`, `gates_structural.py:203`). В коде нет отдельной логической проверки «противоречие X/Y снято каждым концептом» и нет машинной проверки human-confirmation на Gate9/11/12.

### Где сейчас есть/нет “точка прыжка”
TRIZ-ядро как валидатор есть в `GateTRIZ` (физическое противоречие, separation, system operator, transformation model, non-obviousness): `validators.py:47-152`. Но “jump” как operator-driven генерация решений отсутствует в исполняемом pipeline: Step9/10 создаются клиентом/оператором, не движком.

### ACTIVE контуры
- Canon: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/`
- Governance: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/`
- Harness: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/`
- TRIZ validator: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/`
- Experiments/evidence: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/`, ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/exports/`

---

## B) TIMELINE & PIVOTS (fact-based)

| Период | Evidence | Что изменилось | Objective / acceptance | Outcome |
|---|---|---|---|---|
| 2026-02-07 ранние solver-runs | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E1_REAL_CASE_001_2026-02-07T09-11-11Z/notes/SUMMARY_E1.md` | Full-vector запуск с evidence/export | Проверка базового solver-контура | Case зависал при missing в decision-зоне |
| 2026-02-08 TRIZ validator integration period | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/TRIZ_CORE_INTEGRATION_CONTRACT_v0.2.md` + `harness.py:431-444` | GateTRIZ обязателен в run_tc | INVALID TRIZ должен блокировать прогон | Реализовано: GateTRIZ пишется в log/summary |
| 2026-02-08 Pilot V1.2 | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_2_BRANCH_AUTONOMY_2026-02-08T16-00-52Z/PILOT_RUN_REPORT_v0.1.md` | Проверка guide-loop и TRIZ-block | Минимум 1 TRIZ-block, затем проход | Iteration1 FAIL (G4), Iteration2 PASS |
| 2026-02-08 Pilot V1.3 early-block | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/PILOT_V1_3_EARLY_BLOCK_2026-02-08T16-13-32Z/PILOT_RUN_REPORT_v1.3.md` | Тест раннего блока до G4 | Ранний блок желателен | `NEEDS_MANDATORY_SEPARATION_BLOCK` |
| 2026-02-09 Enforcement (Gate9/11/12) | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E1_ENFORCEMENT_2026-02-09T12-46-29Z/E1_ENFORCEMENT_REPORT_v0.1.md` + `gates_structural.py:198,220-229,301-308` | Жёстко включены: Gate9>=3, Gate11 refs, Gate12 unreachable on fail | Case A/B должны падать по правилам | Подтверждено |
| 2026-02-09 Stability / Alignment / R0-R1 | `E2_STABILITY.../E2_STABILITY_REPORT_v0.1.md`, `E3_ALIGNMENT.../E3_ALIGNMENT_REPORT_v0.1.md`, `R0_R1_COMPARATIVE.../R0_R1_COMPARATIVE_REPORT_v0.1.md` | Проверка стабильности и выравнивания данных | VALID/EDGE должны стабильно проходить после alignment | E2=UNSTABLE, E3=Aligned&Passable, R1 not justified |
| 2026-02-10 Freeze + client-path start | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/DRYRUN_CLIENT_INTERACTION_2026-02-10T20-05-42Z/CASE_FREEZE.md`, `.../CLIENT_PATH_PILOT_V1.../CLIENT_PATH_PILOT_REPORT_v0.1.md` | Зафиксирован кейс и live path | Дойти до S09 passability | Останов на S09 (>2 clarifications) |
| 2026-02-11/12 Continuation E5.1→E8 | `E5_1_REPORT_v0.1.md`, `E6_REPORT_v0.1.md`, `E7_REPORT_v0.1.md`, `E8_REPORT_v0.1.md` | Пошаговое закрытие S09/S10/S11/S12 | decision-closure без реинтейка | S09 passable, S10 3/3, S11 criteria=3, S12 commit=YES |
| 2026-02-12 E9 UX fixation | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E9_POSTRUN_UX_FIXATION_2026-02-12T13-56-38Z/UX_BREAKS_E6_E8_v0.1.md` | Consolidated friction evidence | Зафиксировать UX breakpoints | HIGH=2, MED=6, LOW=16 |
| DSS_TRIZ-3 draft (SDP/DCF) | ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/SDP_SPEC_v1.0.md`, `DCF_*.md`, `.../SDP_INSTRUMENTATION.../SDP_INSTRUMENTATION_REPORT_v0.1.md`, `.../OFFLINE_SIM_DCF_REPLAY.../OFFLINE_SIM_DCF_REPORT_v0.1.md` | Добавлен stagnation/fallback draft слой | Проверить trigger/round mechanics | Инструментация READY; offline DCF работает в replay |

---

## C) ARCHITECTURE MAP (as-is)

### 1) Components
- Harness gates + orchestration:
  - ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/gates_structural.py`
  - ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/harness.py`
- TRIZ validator:
  - ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/TRIZ_CORE_ENGINE/validators.py`
- Governance SoT (ключевые):
  - `DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md`
  - `DSS_TRIZ_2_DECISION_ROLE_SPEC_v1.0.md`
  - `DSS_TRIZ_2_GATE9_12_SPEC_v1.0.md`
  - `TRIZ_CORE_INTEGRATION_CONTRACT_v0.2.md`
  - `DSS_EXECUTION_MODE_SPEC_v1.1.md`
  - `SDP_SPEC_v1.0.md`, `DCF_DATA_MODEL_v1.0.md`, `DCF_GENERATOR_SPEC_v1.0.md`

### 2) Data flow (факт)
1. TC YAML (`full_vector.step_0..step_14`) + semantic answers YAML.
2. `run_structural_gates()` → structural statuses.
3. `_apply_semantic()` на Gate4/5/6/11/12 (`harness.py:26`, `harness.py:121`).
4. `triz_validate()` → `GateTRIZ` (`harness.py:431-444`).
5. Evidence: `RUN_*.yaml`, `BUGLIST_*.yaml`.
6. Export package: `case.json`, `manifest.json`, `gate_log.json`, `gate_summary.json`, `artifacts/S00..S14`.

Human-in-loop/assisted:
- В коде human-in-loop не enforce-ится как обязательное поле гейтов 9/11/12.
- Assisted ввод применяется только через answers-файл на ограниченном наборе gate.

---

## D) PIPELINE TRUTH TABLE (S01–S14)
См. отдельную таблицу: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/governance/DSS_TRIZ_FULL_AUDIT_TABLES_v0.1.md`

---

## E) TRIZ-JUMP GAP ANALYSIS (evidence)

### Где должна быть проверка conflict resolved
В текущем коде отдельной проверки “X/Y снят каждым концептом” нет. Ближайшие прокси:
- S04 формулирует X/Y (`gates_structural.py:106-120`)
- S11 проверяет наличие refs `contradiction/ikr/barrier` (`gates_structural.py:220-229`)
Но логической валидации разрешения противоречия per concept нет.

### Кто генерирует механизмы
- По evidence-логам (E5.1/E6/E7/E8), концепты и mechanism-specs формируются в диалоге клиентом/оператором.
- Harness только валидирует наличие/формат полей в S09/S10.

### Где возникает “ABC feeling”
По фактам из live-логов:
- S09 asks фактически как “дай 3 хода”: `E5_1.../DIALOGUE_LOG.md`.
- S10/S11 частые clarification на формулировках, а не на operator-трансформации: `E9 UX_BREAKS_E6_E8_v0.1.md`.
- S11 содержит reject reasons/criteria, что по опыту клиента воспринимается как выбор вариантов, не как invention-jump.

### Почему архитектурно это decision protocol
- Gate9: минимум 3 концепта (count), без operator-semantics (`gates_structural.py:187-200`).
- Gate10: наличие concept_specs (list), без проверки механизмов A–G в коде.
- Gate11: проверка refs и флага secondary contradiction, но не логики снятия X/Y каждым ходом.
- Gate12: commit check по полям выбранного решения.

---

## F) OPERATOR LAYER INVENTORY

### 1) 9 FORMS
- Описание: ` /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/canon/CANON_9FORMS_v1.1.docx` (формы №1..№9, PRIMARY mapping, output-schema Step8).
- Фактическая интеграция в коде:
  - только структурное требование наличия Step8 полей (`PRIMARY_FORM`, `BOUNDARY_CHECK`, `PRINCIPLES_TO_ACTION` и т.д.): `gates_structural.py:166-184`.
  - Нет машинной проверки соответствия выбранной формы её PRIMARY mapping и D-marker правилам из канона.
- Статус использования: частично (как декларация/поле), не как operator engine.

### 2) 40 PRINCIPLES / PRINCIPLES_TO_ACTION
- Policy: `DSS_TRIZ_2_40_PRINCIPLES_ROLE_DECISION_v1.0.md` (R0 default, R1 эксперимент).
- Enforced в коде:
  - `Step8.PRINCIPLES_TO_ACTION.PRINCIPLES` и `ACTIONS` должны быть не пустыми (`gates_structural.py:172-177`).
- Не enforced:
  - принадлежность принципов к PRIMARY формы;
  - semantically correct mapping principle→action;
  - использование как обязательного генератора S09.

### 3) Другие TRIZ-инструменты (что реально enforced)
- separation: да (`validators.py:61-72`).
- system operator: да (`validators.py:74-91`).
- physical contradiction: да (`validators.py:47-59`).
- transformation model: да (`validators.py:132-138`).
- non-obviousness: да (`validators.py:93-129`).
- resource analysis: частично структурно (`gates_structural.py:143-163`).
- vepol/Su-Field: в active enforcement не обнаружено.

---

## G) CLIENT PATH AUDIT (операционная применимость)

Источник: `DRYRUN_REPORT_v0.2`, `CLIENT_PATH_PILOT_REPORT_v0.1`, E5.1→E8 logs, `UX_BREAKS_E6_E8_v0.1.md`.

- Сильный friction узел: S09/S10/S11.
- Clarification evidence:
  - Dry-run v0.2: 7 clarifications, stop at S09.
  - E6/E7/E8: многократные clarification turns при формулировке mechanism/risk/criteria rationale.
- Правило “1 вопрос за раз” в целевом E5.1→E8 соблюдалось по dialogue logs; до этого были остановки из-за protocol/mode mismatch (см. E6 retry цепочку в experiments).
- Остановка/блок в client-path v1: S09, из-за недоформулированных альтернатив и повторных clarification.

---

## H) CONSISTENCY CHECK: “narrative vs repo truth”

1. **Норматив Gate9 требует traceability/не-тривиальность**, но код Gate9 проверяет только `concepts` list и count>=3.  
   Evidence: `DSS_TRIZ_2_GATE9_12_SPEC_v1.0.md` vs `gates_structural.py:187-200`.

2. **Gate10 нормативно требует механизм A–G per concept**, но код проверяет только наличие списка `concept_specs`.  
   Evidence: `CANON_PIPELINE_v1.2` (Gate10 section) vs `gates_structural.py:203-212`.

3. **Gate11 нормативно требует comparison/selection validity**, код проверяет refs+flag, не сравнение концептов.  
   Evidence: `DSS_TRIZ_2_GATE9_12_SPEC_v1.0.md` vs `gates_structural.py:215-231`.

4. **Gate12 нормативно включает commit-структуру и ответственность**, код проверяет только 3 поля (`chosen_concept_index/name/reasons`).  
   Evidence: `DSS_TRIZ_2_GATE9_12_SPEC_v1.0.md` vs `gates_structural.py:234-241`.

5. **Decision Role Spec требует human confirmation на 9/11/12**, но в исполняемом gate-коде нет обязательных human confirmation полей.  
   Evidence: `DSS_TRIZ_2_DECISION_ROLE_SPEC_v1.0.md` vs `gates_structural.py` + `harness.py`.

6. **Policy по 40 principles: не обязательны (R0 default)**, но Step8 структурно требует non-empty `PRINCIPLES_TO_ACTION` всегда.  
   Evidence: `DSS_TRIZ_2_40_PRINCIPLES_ROLE_DECISION_v1.0.md` vs `gates_structural.py:172-177`.

7. **SDP rule “one DCF round per trigger”** vs DCF model/spec `max rounds = 3` на run.  
   Evidence: `SDP_SPEC_v1.0.md` vs `DCF_DATA_MODEL_v1.0.md`, `DCF_GENERATOR_SPEC_v1.0.md`.

8. **Execution mode spec говорит MODE-missing => do nothing**, но это governance-правило не проверяется runtime-кодом harness.  
   Evidence: `DSS_EXECUTION_MODE_SPEC_v1.1.md` vs `harness.py` (нет MODE parsing/check).

---

## I) MINIMAL NEXT MOVES (ограниченно, по фактам)

### A) Decision protocol first
- Изменения в артефактах/спеках (без кода):
  - синхронизировать DSS_TRIZ_2 Gate9-12 spec с тем, что реально проверяет код (as-implemented baseline).
- Acceptance test:
  - для 2 кейсов report “spec-to-code parity = 100% по Gate9-12 required fields”.
- Риск:
  - сохраняется ABC-ощущение, т.к. invention слой не добавляется.

### B) Operator-assisted invention
- Изменения в артефактах/спеках (без кода):
  - формально задать operator-required поля для S09/S10 (в spec), привязанные к contradiction/IKR/resource.
- Acceptance test:
  - на 2 кейсах в `S09/S10` каждый ход имеет operator trace + mechanism link к X/Y, и это зафиксировано в артефактах.
- Риск:
  - может вырасти когнитивная нагрузка в client path (см. E9 friction).

### C) Hybrid
- Изменения в артефактах/спеках (без кода):
  - оставить текущий protocol слой и добавить отдельный contradiction-resolved evidence block для Step10/11.
- Acceptance test:
  - в decision record для выбранного хода есть явный блок “X/Y resolved evidence” + check method.
- Риск:
  - без runtime enforcement останется частично декларативным.

