# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "99f905759bcbc66f7d21937912469b72585e7f24cc245cffd942b51a0e28b937",
  "canonical_hash_v0": null,
  "canonical_hash_text": null,
  "canonical_slots_v0": null,
  "raw_hash": "19a8bcdc887b225c0bf6b007e8e1477a0a12bc1e4b0e439cb7641cc3cc2f45f8",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "правило запуска новых филиалов в Европе",
  "canonical_X": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",
  "canonical_Y": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",
  "canonical_constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "phase0_trace": [
    {
      "raw_fragment": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",
      "interpreted_parameter": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",
      "interpreted_parameter": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",
      "reasoning_trace": "Y:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "правило запуска новых филиалов в Европе",
      "interpreted_parameter": "правило запуска новых филиалов в Европе",
      "reasoning_trace": "scope:scope_projection",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "['не раздувать исследовательский бюджет/срок']",
      "interpreted_parameter": [
        "не раздувать исследовательский бюджет/срок"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}