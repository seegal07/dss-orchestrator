# OWNER_POLICY_DECISIONS_v0.1

Статус: filled for Owner review
Назначение: зафиксировать решения Owner/CEO по policy-блокерам перед E11.
Контекст: `E10_OPERATOR_CORE_INTEGRATION_PLAN_2026-02-12T20-46-45Z`

---

## Q1
**Question:** GateCR status policy: should SOFT_FAIL count as overall run `PASS` or `PARTIAL`?

**Options:**
- O1: SOFT_FAIL => overall `PASS`
- O2: SOFT_FAIL => overall `PARTIAL`

**RECOMMENDATION:** O2 (`PARTIAL`)

**Risk if chosen differently:**
- If O1: скрывается компромисс и теряется сигнал качества operator-layer.

**Impact (harness/backward compatibility):**
- Harness: needs mapping `GateCR=SOFT_FAIL` to run-level `PARTIAL`.
- Backward: old runs unaffected (no GateCR).

---

## Q2
**Question:** For HARD_FAIL, do we block exactly S09–S12 only, or also S13–S14 in same run?

**Options:**
- O1: block only S09–S12
- O2: block S09–S14

**RECOMMENDATION:** O2 (block S09–S14)

**Risk if chosen differently:**
- If O1: возможны артефакты post-decision без решения (логическая неконсистентность).

**Impact (harness/backward compatibility):**
- Harness: simpler NOT_RUN propagation to all downstream gates.
- Backward: none for historical runs.

---

## Q3
**Question:** Is `COMPROMISE_MODE=TRUE` mandatory in S12_DECISION_RECORD when GateCR=SOFT_FAIL?

**Options:**
- O1: mandatory in S12
- O2: optional in S12 (only in GateCR evidence)

**RECOMMENDATION:** O1 (mandatory)

**Risk if chosen differently:**
- If O2: компромисс не виден в финальном decision artifact.

**Impact (harness/backward compatibility):**
- Harness/export: add field propagation to S12 artifact.
- Backward: old S12 artifacts remain valid as legacy (no GateCR).

---

## Q4
**Question:** What is authoritative SoT for schema extension: `TEST_VECTOR_SCHEMA_v0.1` or a new schema version file?

**Options:**
- O1: edit existing `TEST_VECTOR_SCHEMA_v0.1`
- O2: create new versioned schema (e.g., v0.2)

**RECOMMENDATION:** O2 (new version)

**Risk if chosen differently:**
- If O1: ломается воспроизводимость старых тестов и сравнение исторических evidence.

**Impact (harness/backward compatibility):**
- Harness: dual support for v0.1 + v0.2 input.
- Backward: preserved by version routing.

---

## Q5
**Question:** Should GateCR be assisted-only at first release, or mixed (structural+assisted)?

**Options:**
- O1: assisted-only
- O2: mixed (structural + assisted)

**RECOMMENDATION:** O2 (mixed)

**Risk if chosen differently:**
- If O1: слишком много невалидных input-форматов дойдут до semantic stage.

**Impact (harness/backward compatibility):**
- Harness: add structural presence gate + assisted matrix.
- Backward: no effect on pre-GateCR runs.

---

## Q6
**Question:** Can GateCR produce FAIL (besides HARD_FAIL), or only PASS/SOFT_FAIL/HARD_FAIL as final states?

**Options:**
- O1: keep tri-state only (PASS/SOFT_FAIL/HARD_FAIL)
- O2: allow additional FAIL

**RECOMMENDATION:** O1 (tri-state only)

**Risk if chosen differently:**
- If O2: дублирование смыслов FAIL vs HARD_FAIL и рост ambiguity в routing.

**Impact (harness/backward compatibility):**
- Harness: simpler transition table.
- Backward: none.

---

## Q7
**Question:** For operator selection (B>A>C>D), do we require explicit evidence of all detected types or only dominant type?

**Options:**
- O1: evidence only for dominant type
- O2: evidence for all detected types + dominant selection rationale

**RECOMMENDATION:** O2 (all detected + dominant rationale)

**Risk if chosen differently:**
- If O1: сложно аудировать корректность priority-rule применения.

**Impact (harness/backward compatibility):**
- Harness/artifact parser: store `detected_conflict_types[]` and `dominant_conflict_type`.
- Backward: none.

---

## Q8
**Question:** Separation Illusion Test: is any single YES enough for HARD_FAIL, or weighted decision?

**Options:**
- O1: any single YES => HARD_FAIL
- O2: weighted decision across items

**RECOMMENDATION:** O1 (single YES => HARD_FAIL)

**Risk if chosen differently:**
- If O2: субъективность scoring и нестабильность решений между кейсами.

**Impact (harness/backward compatibility):**
- Harness: deterministic boolean rule.
- Backward: none.

---

## Q9
**Question:** Should existing historical runs be exempt from GateCR requirements (backward compatibility rule: yes/no)?

**Options:**
- O1: yes, exempt historical runs
- O2: no, retroactive invalidation

**RECOMMENDATION:** O1 (exempt)

**Risk if chosen differently:**
- If O2: исторические evidence теряют валидность и ломают audit continuity.

**Impact (harness/backward compatibility):**
- Harness: apply GateCR only when schema/version indicates Operator Core enabled.
- Backward: preserved.

---

## Q10
**Question:** Message text on HARD_FAIL: fixed canonical string only, or localized variants allowed?

**Options:**
- O1: fixed canonical string only
- O2: localized variants allowed

**RECOMMENDATION:** O1 (fixed canonical string)

**Risk if chosen differently:**
- If O2: сложнее машинный аудит/поиск по incident patterns.

**Impact (harness/backward compatibility):**
- Harness/export: stable constant for downstream tooling.
- Backward: none.

---

Готовность к E11:
- [x] Все 10 policy-решений заполнены (как рекомендация по умолчанию).
