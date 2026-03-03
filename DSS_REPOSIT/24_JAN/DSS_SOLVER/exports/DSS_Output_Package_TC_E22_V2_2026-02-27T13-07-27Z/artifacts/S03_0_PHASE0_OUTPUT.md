# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "ddc966dff3a02b1d49ca8e105fe6a61b15cd3e4c509c81bf860a2904577593f6",
  "canonical_hash_v0": "ddc966dff3a02b1d49ca8e105fe6a61b15cd3e4c509c81bf860a2904577593f6",
  "s2a_hash": "0a651ad3caa267ecfc9d0ced21690ccfa9cbe4d44dcb0861e9c8ec6fb04d4996",
  "canonical_hash_text": "b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302",
  "canonical_slots_v0": {
    "scope": "правило запуска новых филиалов в Европе",
    "X_direction": "accelerate",
    "X_delta_direction": "accelerate",
    "X_metric_polarity": "UNKNOWN",
    "X_metric": "прогноз",
    "X_object": "филиалов",
    "Y_direction": "other",
    "Y_delta_direction": "unknown",
    "Y_metric_polarity": "LOWER_IS_BETTER",
    "Y_metric": "стоимость",
    "Y_object": "запуска",
    "constraints": [
      "не раздувать исследовательский бюджет/срок"
    ],
    "trace_markers": [
      "MISSING_SLOT:Y_delta_direction",
      "UNKNOWN_POLARITY:X"
    ]
  },
  "raw_hash": "d4028706e3cf04fd0c6b89b5385fdeb940ab41856606329a97260e6930666c2e",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "правило запуска новых филиалов в Европе",
  "canonical_X": "Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
  "canonical_Y": "Не повышать чрезмерно длительность и стоимость подготовки запуска.",
  "canonical_constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "canonical_conflict_type_candidate_trace": null,
  "phase0_trace": [
    {
      "raw_fragment": "Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
      "interpreted_parameter": "Ускорить выход филиалов в Европе и сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "Не повышать чрезмерно длительность и стоимость подготовки запуска.",
      "interpreted_parameter": "Не повышать чрезмерно длительность и стоимость подготовки запуска.",
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