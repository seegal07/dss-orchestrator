# TRIZ_V0_3_REVIEW_BUNDLE

## Table of Contents

- Governance docs (v0.3)

- Case C evidence

- Reality Check (verbatim excerpts)

- Non-obviousness check


## Governance docs (v0.3)

### ASSISTED_GATE_CRITERIA_v0.3.md
```markdown
# ASSISTED_GATE_CRITERIA_v0.3

Ссылка на базовый контур: DSS_SOLVER/governance/DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md

---

## Gate4 — CONTRADICTION_STATEMENT
PASS:
- improve_x / worsen_y заданы измеримо.
- statement_1l в форме «если X, ухудшается Y».
- measurement_hint содержит baseline или PROXY + validation_date.

FAIL:
- нет измеримости / нет measurement_hint.

BLOCKED:
- отсутствуют ключевые поля Step4.

---

## Gate8 — TRIZ_CORE_ENFORCEMENT
PASS:
- TRIZ_CORE.CONTRADICTION_1L задан.
- TRIZ_CORE.IKR_1L задан.
- TRIZ_CORE.separation_strategy содержит ≥1 стратегию (time/space/condition/part‑whole).
- PRINCIPLES_TO_ACTION.PRINCIPLES содержит ≥2 принципа.
- PRINCIPLES_TO_ACTION.ACTIONS содержит ≥2 действий, связанных с принципами.

FAIL:
- отсутствует хотя бы один из обязательных элементов.

BLOCKED:
- отсутствуют блоки TRIZ_CORE или PRINCIPLES_TO_ACTION.

---

## Gate9 — CONCEPT_TRACEABILITY
PASS:
- Каждый концепт в Step9 содержит поле traceability и ссылку на принцип или стратегию разделения.

FAIL:
- хотя бы у одного концепта нет traceability.

BLOCKED:
- отсутствуют концепты.

---

## Gate12 — DECISION_RECORD
PASS:
- chosen_concept_index существует в Step9.
- reasons ссылаются на ≥1 separation_strategy и ≥1 principle→action.
- success_criteria содержат thresholds (switch + kill/stop) + baseline/proxy.

FAIL:
- причины не содержат ссылок на separation или principle‑action.
- thresholds отсутствуют.

BLOCKED:
- выбранный концепт / причины отсутствуют.
```

### DSS_INTAKE_SPEC_v0.3.md
```markdown
# DSS_INTAKE_SPEC_v0.3

Ссылка на базовый контур: DSS_SOLVER/governance/DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md

Цель v0.3: обеспечить извлечение TRIZ‑механизмов для решения (separation + principles→actions) и трассируемость до концептов.

## Обязательные блоки (v0.3)

### 1) BASELINE
Требуется baseline ключевой метрики или PROXY‑диапазон + validation_date.

### 2) THRESHOLDS
Требуются минимум 2 порога (switch + kill/stop). Диапазоны допустимы, но должны быть явными.

### 3) SEPARATION STRATEGY
Требуется минимум 1 стратегия разделения (time / space / condition / part‑whole), привязанная к противоречию (S04) и ограничениям (S01).

### 4) PRINCIPLES → ACTIONS
Требуются минимум 2 принципа (business‑адаптация) и для каждого — конкретное действие.

### 5) TRACEABILITY
Каждый концепт в S09 должен ссылаться на принцип или стратегию разделения, из которых он получен.

## Маппинг на S‑steps
- BASELINE → S04/S12/S14
- THRESHOLDS → S12/S14
- SEPARATION → S08 (TRIZ_CORE.separation_strategy)
- PRINCIPLES→ACTIONS → S08 (PRINCIPLES_TO_ACTION)
- TRACEABILITY → S09 (concept.traceability)

## Правило блокировки
Если нет separation / principles→actions / traceability, решение блокируется (Gate8/9/12).
```

### DSS_INTAKE_FORM_v0.3.md
```markdown
# DSS_INTAKE_FORM_v0.3 (без TRIZ‑терминов)

Ссылка на базовый контур: DSS_SOLVER/governance/DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md

## Блок A — Контекст решения
1) В чём тупик (1–2 предложения)?
2) Кто принимает решение и чем реально управляет?
3) Жёсткие ограничения (время/люди/качество/репутация).

## Блок B — BASELINE (обязателен)
4) Базовый уровень ключевой метрики сейчас.
   - Если неизвестно: `UNKNOWN` + PROXY‑диапазон + validation_date.

## Блок C — THRESHOLDS (обязателен)
5) Порог переключения (switch‑threshold).
6) Порог остановки/отказа (kill/stop‑threshold).

## Блок D — Разделение решения (обязателен)
7) Где и как разделить проблему так, чтобы снять конфликт?
   - Варианты: по времени / по пространству / по условиям / по частям.

## Блок E — Принципы → действия (обязателен)
8) Назовите минимум 2 принципа/механики (в бизнес‑форме) и для каждого — конкретное действие.

## Блок F — Варианты решения
9) Минимум 2 концепта, каждый должен ссылаться на принцип или стратегию разделения.

## Блок G — Уже пробовали
10) Что уже пробовали (2–3 варианта)?
```

### DSS_INTAKE_GUIDED_CORRECTION_MAP_v0.3.md
```markdown
# DSS_INTAKE_GUIDED_CORRECTION_MAP_v0.3

Ссылка на базовый контур: DSS_SOLVER/governance/DSS_TRIZ_STRATEGIC_BASELINE_v1.0.md

## Gate8 — TRIZ_CORE
Запросить:
- separation_strategy (time/space/condition/part‑whole) + привязка к противоречию.
- principles list (минимум 2) + action для каждого.

## Gate9 — CONCEPTS TRACEABILITY
Запросить:
- для каждого концепта: ссылка на принцип или стратегию разделения.

## Gate12 — DECISION
Запросить:
- причины выбора, где явно указан минимум 1 separation + 1 principle‑action.
- success_criteria с thresholds (switch + kill/stop) и baseline/proxy.
```


## Case C evidence

### gate_summary.json
```json
{
  "case_id": "DSS_Output_Package_TC_CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION_2026-02-08T12-13-52Z",
  "run_id": "2026-02-08T12-13-52Z",
  "latest": {
    "Gate0": "pass",
    "Gate1": "pass",
    "Gate2": "pass",
    "Gate3": "pass",
    "Gate4": "pass",
    "Gate5": "pass",
    "Gate6": "pass",
    "Gate7": "pass",
    "Gate8": "pass",
    "Gate9": "pass",
    "Gate10": "fail",
    "Gate11": "pass",
    "Gate12": "pass",
    "Gate13": "fail",
    "Gate14": "fail"
  }
}
```

### gate_log.json (Gate8/9/12 excerpts)
```json
[
  {
    "gate_log_entry_id": "2026-02-08T12-13-52Z-Gate8",
    "case_id": "DSS_Output_Package_TC_CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION_2026-02-08T12-13-52Z",
    "gate_id": "Gate8",
    "pipeline_step": 8,
    "result": "pass",
    "check_type": "AUTOMATED",
    "criteria_scope": "CANON",
    "criteria_results": [],
    "reason": "",
    "canon_ref": "CANON_PIPELINE_v1.2",
    "run_id": "2026-02-08T12-13-52Z",
    "timestamp": "2026-02-08T12-13-52Z",
    "actor_type": "system",
    "actor_user_id": null
  },
  {
    "gate_log_entry_id": "2026-02-08T12-13-52Z-Gate9",
    "case_id": "DSS_Output_Package_TC_CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION_2026-02-08T12-13-52Z",
    "gate_id": "Gate9",
    "pipeline_step": 9,
    "result": "pass",
    "check_type": "AUTOMATED",
    "criteria_scope": "CANON",
    "criteria_results": [],
    "reason": "",
    "canon_ref": "CANON_PIPELINE_v1.2",
    "run_id": "2026-02-08T12-13-52Z",
    "timestamp": "2026-02-08T12-13-52Z",
    "actor_type": "system",
    "actor_user_id": null
  },
  {
    "gate_log_entry_id": "2026-02-08T12-13-52Z-Gate12",
    "case_id": "DSS_Output_Package_TC_CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION_2026-02-08T12-13-52Z",
    "gate_id": "Gate12",
    "pipeline_step": 12,
    "result": "pass",
    "check_type": "ASSISTED",
    "criteria_scope": "CANON",
    "criteria_results": [
      {
        "criterion_id": "G12-P1",
        "status": "pass",
        "evidence": "chosen_concept_index=1"
      },
      {
        "criterion_id": "G12-P2",
        "status": "pass",
        "evidence": "reasons содержат separation + principle‑action"
      },
      {
        "criterion_id": "G12-P3",
        "status": "pass",
        "evidence": "success_criteria содержат thresholds + validation_date"
      }
    ],
    "reason": "G12-P1: chosen_concept_index=1, G12-P2: reasons содержат separation + principle‑action, G12-P3: success_criteria содержат thresholds + validation_date",
    "canon_ref": "CANON_PIPELINE_v1.2",
    "run_id": "2026-02-08T12-13-52Z",
    "timestamp": "2026-02-08T12-13-52Z",
    "actor_type": "system",
    "actor_user_id": null
  }
]
```

### DSS_DECISION_RECORD_CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION.md
```markdown
# DSS Decision Record — CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION

## Context
Кастомизация ядра для крупного клиента при риске деградации продукта и роста поддержки.

## Options
1) Модуль расширений.
2) Контур кастомизации для сегмента.

## Decision
DECISION_VALID — выбран концепт 1 (Модуль расширений).

## Trade-offs
Сделка vs сохранение ядра и скорости релизов.

## Thresholds
- Кастомизация ≤ 20% (PROXY)
- Рост поддержки ≤ +25% (PROXY)
- validation_date=2026-03-01

## Review
Ревью после validation_date.

## References
- gate_log: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/TRIZ_V0_3_WORKBENCH_2026-02-08T12-11-27Z/sample_runs/CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION/exports/DSS_Output_Package_TC_CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION_2026-02-08T12-12-55Z/gate_log.json
```

### USER_VIEW_WALKTHROUGH_CASE_C.md
```markdown
# USER_VIEW_WALKTHROUGH — CASE_C_CUSTOMIZATION_TRIZ_RESOLUTION

## Противоречие
Нужно принять кастомизацию ради сделки, но нельзя разрушать роадмап и поддержку.

## IKR
Сделка закрыта без перегрузки поддержки и без срыва роадмапа.

## Стратегия разделения
- По условиям: кастомизация только для ограниченного сегмента.
- По частям: вынести кастомизацию в отдельный слой.

## Принципы → действия
- «Разделение по условиям» → контур кастомизации с отдельным SLA.
- «Дробление» → модульный слой расширений вне ядра.

## Альтернативные концепты
1) Модуль расширений (trace: принцип «Дробление», separation part‑whole).
2) Контур кастомизации для сегмента (trace: принцип «Разделение по условиям», separation condition).

## Выбранный концепт и почему
Выбран «Модуль расширений», потому что сохраняет ядро и укладывается в thresholds (≤20% ёмкости, ≤+25% поддержки) при validation_date=2026-03-01.
```

### DIFF_V0_2_vs_V0_3.md
```markdown
# DIFF v0.2 → v0.3

## Что стало обязательным
- Gate8: separation_strategy + principles→actions (минимум 2) в TRIZ_CORE.
- Gate9: traceability для каждого концепта.
- Gate12: причины решения должны ссылаться на separation и principle‑action.

## Как это изменило выход
- Решения больше не фиксируются только через thresholds; требуется механизм разрешения противоречия.
- Концепты привязаны к источнику (принцип/стратегия), что исключает «произвольные варианты».

## Где зафиксировано
- ASSISTED_GATE_CRITERIA_v0.3.md
- DSS_INTAKE_SPEC_v0.3.md
- DSS_INTAKE_FORM_v0.3.md
- DSS_INTAKE_GUIDED_CORRECTION_MAP_v0.3.md
```


## Reality Check (verbatim excerpts)

### Противоречие (Step4)
```yaml
    improve_x: "Вероятность закрытия сделки"
    worsen_y: "Стабильность продукта и нагрузка поддержки"
    statement_1l: "Если принимаем кастомизацию, растёт нагрузка поддержки и замедляется роадмап; если отказываемся, риск потери сделки"
    measurement_hint: "PROXY: релизы 2–3/мес; thresholds 20% ёмкости, +25% поддержка; validation_date=2026-03-01"
```

### IKR (Step5)
```yaml
    ikr_1l: "Сделка закрыта без деградации ядра и без роста поддержки"
    no_new_harm_clause: "Не ухудшать сервис текущим клиентам"
```

### Separation strategies + Principles→Actions (Step8)
```yaml
    PRIMARY_FORM: "Форма противоречия"
    BOUNDARY_CHECK:
      NEAREST_FORMS: ["Форма политики", "Форма контракта"]
      WHY_NOT_X: ["Нельзя расширять команду"]
      WHY_NOT_Y: ["Нельзя портить сервис действующим клиентам"]
    TRIZ_CORE:
      CONTRADICTION_1L: "Нужно принять кастомизацию ради сделки, но нельзя разрушать роадмап и поддержку"
      IKR_1L: "Сделка закрыта без перегрузки поддержки и без срыва роадмапа"
      separation_strategy:
        - type: "condition"
          description: "Разделить по условиям: кастомизация только для ограниченного сегмента"
        - type: "part-whole"
          description: "Разделить по частям: вынести кастомизацию в отдельный слой"
    PRINCIPLES_TO_ACTION:
      PRINCIPLES: ["Разделение по условиям", "Дробление"]
      ACTIONS: ["Контур кастомизации с SLA", "Модульный слой расширений вне ядра"]
    IKR_TEST:
      Q1: "YES"
      Q2: "YES"
    CONFIDENCE:
      score: 2
      justification: "Separation + principles заданы"
```

### Concepts with traceability (Step9)
```yaml
    count_rule: "3–5"
    concepts:
      - concept_index: 1
        name: "Модуль расширений"
        idea_1l: "Вынести кастомизацию в модульный слой"
        linked_form: "Форма разделения"
        linked_principles: ["Дробление"]
        linked_resources: ["Архитектура продукта"]
        ikr_alignment_1l: "Сохраняет ядро"
        traceability: "principle:Дробление; separation:part-whole"
      - concept_index: 2
        name: "Контур кастомизации для сегмента"
        idea_1l: "Разрешать кастомизацию только для сегмента с отдельным SLA"
        linked_form: "Форма условий"
        linked_principles: ["Разделение по условиям"]
        linked_resources: ["Политика кастомизации"]
        ikr_alignment_1l: "Ограничивает нагрузку"
        traceability: "principle:Разделение по условиям; separation:condition"
```

### Chosen concept + reasons (Step12)
```yaml
    chosen_concept_index: 1
    chosen_concept_name: "Модуль расширений"
    reasons:
      - "Ссылается на separation part‑whole и принцип дробления"
      - "Сохраняет ядро при thresholds 20%/+25%"
    success_criteria:
      - "Кастомизация ≤ 20% (PROXY)"
      - "Рост поддержки ≤ +25% (PROXY)"
      - "validation_date=2026-03-01"
```


## Non-obviousness check

- Решение использует разделение по частям и по условиям, а не только пороги X%.
- Выбранный механизм — модульный слой расширений, что меняет архитектуру, а не только правила доступа.
- Варианты концептов связаны с принципами/стратегиями, то есть генерируются из TRIZ‑механики, а не из общего списка опций.
- Причины выбора ссылаются на separation и principle‑action (Gate12), а не на абстрактные KPI.
- Два альтернативных концепта имеют трассируемость к разным TRIZ‑источникам, что исключает один‑единственный «пороговый» ответ.

VERDICT: PASS (решение не сводится к единственному «set thresholds»).
