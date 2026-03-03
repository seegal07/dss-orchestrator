# PROBLEM_FRAMING_LAYER_SPEC_v0.2
# (PFL — Architectural Admission Layer Before S04)

Owner: Alex
Status: ARCH_DRAFT (normative)
Scope: Architecture-only (no implementation)

---------------------------------------------------------------------
0. ROLE OF THIS LAYER

PFL — обязательный детерминированный admission-layer перед S04.
Цель: допускать в DSS только структурно валидные X/Y в одном scope,
чтобы мусорный вход не разрушал downstream (Operator Layer, GateCR, decision).

PFL НЕ:
- генерирует идеи/механизмы/ходы,
- не предлагает варианты,
- не “улучшает” формулировку смыслом,
- не добавляет новые сущности системы.

PFL МОЖЕТ:
- требовать структурного ужесточения X/Y,
- давать только ФОРМАТ конвертации симптома в измеряемое свойство (без содержания),
- задавать 1–2 фиксированных уточнения для направления зависимости (без новых переменных).

---------------------------------------------------------------------
1. POSITION IN PIPELINE

S00 → S01 → S02 → S03 → PFL → (PASS) → S04
                        ↘ (FAIL) → STOP

PFL не заменяет S04. PFL только admission.

---------------------------------------------------------------------
2. OUTPUT CONTRACT (STRICT)

PFL output MUST include exactly these fields:

X = {statement}
Y = {statement}
conflict_type_candidate = {causal | temporal | interaction | scale}
structural_tension = {TRUE|FALSE}
pfl_verdict = {PASS|FAIL}
pfl_reason = {NONE|INVALID_DUAL_TENSION|NO_MUTUAL_DEGRADATION|OUT_OF_SCOPE|SYMPTOM_FRAMING|TRIVIAL_CONFLICT|SOLUTION_AS_XY}
attempt_index = {1..MAX_REFRAME_ATTEMPTS}

MAX_REFRAME_ATTEMPTS = 3

If pfl_verdict = FAIL after MAX_REFRAME_ATTEMPTS:
→ STOP
→ canonical message: "structural contradiction not formulated"
→ S04+ = NOT_RUN

---------------------------------------------------------------------
3. ADMISSIBILITY CRITERIA (DETERMINISTIC)

A’) DUAL-TENSION CONDITION

- X и Y — два требования к ОДНОЙ системе в одном scope.
Допускаются:
- goal vs constraint
- constraint vs constraint
- goal vs goal (если есть trade-off)
Запрещено:
- solution-as-X/Y (когда X или Y уже механизм/ход/действие)

Если X/Y не образуют tension в одной системе → FAIL: INVALID_DUAL_TENSION
Если X или Y является механизмом → FAIL: SOLUTION_AS_XY

---------------------------------------------------------------------

B) MUTUAL DEGRADATION CONDITION

Требование:
- При усилении X в рамках текущего scope ухудшается Y (или наоборот).

Если направление не задано, разрешено задать максимум 2 фиксированных вопроса:

Q1:
"Когда усиливаем X в рамках текущего scope — каким эффектом ухудшается Y? (1 строка)"

Q2:
"И наоборот: когда усиливаем Y — каким эффектом ухудшается X? (1 строка)"

Если после этих уточнений направление не задано →
FAIL: NO_MUTUAL_DEGRADATION

---------------------------------------------------------------------

C) SAME SYSTEM BOUNDARY CONDITION

- X и Y должны находиться в одном system scope, заданном upstream (S00–S03).
Если scope отсутствует или X/Y относятся к разным системам →
FAIL: OUT_OF_SCOPE

---------------------------------------------------------------------

D) NON-TRIVIALITY TEST

Если простое удаление одного элемента полностью снимает tension без потерь →
FAIL: TRIVIAL_CONFLICT

---------------------------------------------------------------------
4. SYMPTOM FRAMING FILTER

Если X или Y — симптом/жалоба/состояние →
FAIL: SYMPTOM_FRAMING

PFL может вернуть только формат инструкции:

"Переформулируй симптом как измеряемое свойство системы:
метрика + порог/частота/время/стоимость/ошибка. 1 строка."

Запрещено:
- предлагать метрики
- предлагать механизм
- вводить новые сущности

---------------------------------------------------------------------
5. CONFLICT TYPE CANDIDATE

causal — явная причинность X↑ → Y↓  
temporal — конкуренция в одном времени  
interaction — конфликт прямого взаимодействия сторон  
scale — конфликт уровня/масштаба  

Если маркеры отсутствуют →
FAIL: NO_MUTUAL_DEGRADATION

---------------------------------------------------------------------
6. CONTROL FLOW

PASS:
→ S04

FAIL:
→ tightening request
→ after MAX_REFRAME_ATTEMPTS → STOP

---------------------------------------------------------------------
7. TRACEABILITY FIELDS

Fields to be stored in test vector:

- pfl_verdict
- pfl_reason
- attempt_index
- X
- Y
- conflict_type_candidate
- structural_tension

---------------------------------------------------------------------
8. IMPLEMENTATION BINDING v0.1 (normative for harness)

### Inputs (Phase0-enabled)
PFL MUST consume canonical fields only:
- canonical_X, canonical_Y, canonical_scope, canonical_constraints, canonical_conflict_type_candidate
and must NOT read raw text.

### Truth-source mirror note (normative)
- This PFL spec defines compute contract and input binding only.
- Truth-source for admission verdict/metrics is GatePFL evidence (`gate_log.json` primary, `gate_summary.json` secondary) as defined in StageA metrics SoT.
- Snapshot artifacts (including `summary.json` and `S03_5_PFL_OUTPUT.md`) are not verdict truth-source for metrics.

### Minimal compute (v0.1)
- Must output all strict fields (per §2), non-null.
- Must be deterministic (same canonical inputs -> same outputs).
- Rules implemented in v0.1: A (dual-tension), B (mutual degradation), C (same boundary), SOLUTION_AS_XY filter, symptom framing filter.
- Rules deferred (explicitly): non-triviality test, conflict_type_candidate inference beyond canonical value.

### Attempt index
- attempt_index increments only if PFL produces tightening request (FAIL) and caller retries.
- For harness v0.1, single-pass execution sets attempt_index=1.

### v0.1 Two-phase compute (normative)
Phase A — Structural checks (FAIL-only):
- OUT_OF_SCOPE if canonical_scope empty
- INVALID_DUAL_TENSION if canonical_X/canonical_Y missing or equal
- INSUFFICIENT_DATA if required canonical fields missing for any decision

Phase B — Marker filters (FAIL-only, closed lists, MUST NOT produce PASS):
- SOLUTION_AS_XY if canonical_X or canonical_Y contains any ACTION_MARKERS (closed list below)
- SYMPTOM_FRAMING if canonical_X or canonical_Y contains any SYMPTOM_MARKERS (closed list below)

### Closed lists (versioned, normative)
ACTION_MARKERS = ["внедр", "запуст", "сдела", "улучш", "оптимиз", "автоматиз", "наня", "увелич", "сниз", "повыс", "ускор"]
SYMPTOM_MARKERS = ["проблем", "плохо", "не работа", "хаос", "бардак", "пожар", "падает", "кризис"]

### PASS rule (normative)
- PASS is allowed only when a strict mutual-degradation criterion is defined and satisfied.
- For v0.1, mutual degradation proof is DEFERRED → therefore default outcome after passing Phase A and B is:
  - FAIL with reason NO_MUTUAL_DEGRADATION (only if canon explicitly provides a strict criterion), else FAIL with INSUFFICIENT_DATA.
(Leave the exact default as: FAIL/INSUFFICIENT_DATA for v0.1, unless spec already defines strict mutual degradation.)

### v0.1 semantic interpretation (normative)
- In v0.1, `NO_MUTUAL_DEGRADATION` MUST be interpreted as `NOT_PROVEN` (trade-off proof deferred), not as "proven absent".

---------------------------------------------------------------------
9. MUTUAL DEGRADATION CRITERION v0.2 (normative)

- Default state: `NOT_PROVEN` unless strict proof signals are present.
- Telemetry: `conflict_type_candidate_trace` is TRACE-ONLY and MUST NOT be used as proof while domain is trivial (`{causal}`).
- `conflict_type_candidate` (and `*_trace`) is `DEFAULT_ONLY` in current writer-path and has `PROOF_WEIGHT=0`.
- It MUST NOT be used as a PROVEN signal until a real source exists: `pfl_conflict_type_candidate` from UI/manual/classifier.
- PROVEN signals (future, list only):
  1) stable direction slots for both X and Y (direction/metric/object) + explicit opposite effect
  2) stable constraints boundary + trade-off pattern
  3) non-trivial conflict_type_candidate domain with defined semantics (to be added when evidence exists)
- Until PROVEN: PFL verdict remains FAIL with reason `NO_MUTUAL_DEGRADATION` interpreted as `NOT_PROVEN`.

### v0.2 PROVEN SIGNAL #1 (Structure-ready)

- PROVEN_SIGNAL_1 requires non-null stable slots:
  - `X_metric`, `X_object`, `Y_metric`, `Y_object`, `scope` (boundary_scope)
- Distinctness rule:
  - `X_metric` and `Y_metric` MUST be different.
  - `X_object` and `Y_object` MAY be the same object if both metrics differ; this is allowed in v0.2-S1.
- Direction rule:
  - `direction` is explicitly deferred and is NOT required in v0.2-S1.

### v0.2 PROVEN_SIGNAL_1 interpretation

- If PROVEN_SIGNAL_1 is satisfied, state MUST be labeled:
  - `STRUCTURE_READY_FOR_PROOF`
- This label does NOT grant admission PASS and does NOT change the default:
  - state remains `NOT_PROVEN` until strict trade-off proof is implemented.

### v0.2 PROVEN_SIGNAL_1 reporting

- Reports MUST output whether PROVEN_SIGNAL_1 is satisfied.
- Reports MUST include evidence anchors to slot fields used in the check.

### v0.2 PROVEN SIGNAL #2a (Declared direction opposition; normative)

Purpose:
- Establish "trade-off declared in model" (not real-world causality proof).

Required fields (must be non-null, stable):
- `X_delta_direction` ∈ {`increase`, `decrease`, `accelerate`, `decelerate`}
- `Y_delta_direction` ∈ {`increase`, `decrease`, `accelerate`, `decelerate`}
- `X_metric_polarity` ∈ {`HIGHER_IS_BETTER`, `LOWER_IS_BETTER`}
- `Y_metric_polarity` ∈ {`HIGHER_IS_BETTER`, `LOWER_IS_BETTER`}
- `X_metric`, `Y_metric`, `scope` (must already satisfy PROVEN_SIGNAL_1)

Rule (S2a):
- PASS if (`X_improve` AND `Y_worsen`) OR (`X_worsen` AND `Y_improve`), where:
  - `improve` = (`polarity == HIGHER_IS_BETTER` AND `delta_direction ∈ {increase, accelerate}`)
            OR (`polarity == LOWER_IS_BETTER` AND `delta_direction ∈ {decrease, decelerate}`)
  - `worsen` = negation of `improve` within the same family
- If polarity is unknown for any side => `NOT_PROVEN` (no guessing).

### v0.2 Closed polarity mapping (minimal, evidence-driven)

- `accuracy` / `точность` -> `HIGHER_IS_BETTER`
- `time` / `время` / `срок` -> `LOWER_IS_BETTER`
- `cost` / `стоимость` -> `LOWER_IS_BETTER`
- `risk` / `риск` -> `LOWER_IS_BETTER`
- any other metric -> `UNKNOWN` -> `NOT_PROVEN`

Interpretation:
- If S1 PASS and S2a PASS => STATE = `DECLARED_TRADEOFF`
- This still does NOT assert causality or constraint-backed proof (S2b deferred).

Reporting:
- Reports must output `X_delta_direction`/`Y_delta_direction`, metric polarity values, and S2a verdict with anchors.

---------------------------------------------------------------------
END OF SPEC
