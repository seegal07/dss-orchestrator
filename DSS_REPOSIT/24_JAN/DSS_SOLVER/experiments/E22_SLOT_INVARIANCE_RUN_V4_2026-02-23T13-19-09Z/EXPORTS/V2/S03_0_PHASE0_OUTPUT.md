# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "fdabe9c337b187131f7db90d3c90e3a861886c769bb823dcdd27c981f854e64c",
  "canonical_hash_v0": "fdabe9c337b187131f7db90d3c90e3a861886c769bb823dcdd27c981f854e64c",
  "canonical_hash_text": "b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302",
  "canonical_slots_v0": {
    "scope": "правило запуска новых филиалов в Европе",
    "X_direction": "accelerate",
    "X_metric": "Ускорить выход филиалов в Европе и",
    "X_object": "сделать прогноз CAPEX/OPEX+PMF точнее до старта.",
    "Y_direction": "other",
    "Y_metric": "Не повышать чрезмерно длительность и стоимость",
    "Y_object": "подготовки запуска.",
    "constraints": [
      "не раздувать исследовательский бюджет/срок"
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