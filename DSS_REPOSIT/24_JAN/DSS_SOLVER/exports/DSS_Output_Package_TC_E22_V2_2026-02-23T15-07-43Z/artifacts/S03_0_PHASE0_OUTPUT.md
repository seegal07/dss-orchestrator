# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "13b5000df2cfc3ff4275fd2c8ca1ff54f0cb468aecaa0e10953207428457b1a6",
  "canonical_hash_v0": "13b5000df2cfc3ff4275fd2c8ca1ff54f0cb468aecaa0e10953207428457b1a6",
  "canonical_hash_text": "b25073ac64450aae4012a2c378611a1685618aaad7873e52c3bc576ef9896302",
  "canonical_slots_v0": {
    "scope": "правило запуска новых филиалов в Европе",
    "X_direction": "accelerate",
    "X_metric": null,
    "X_object": "филиалов в европе",
    "Y_direction": "other",
    "Y_metric": "стоимость",
    "Y_object": "запуска",
    "constraints": [
      "не раздувать исследовательский бюджет/срок"
    ],
    "trace_markers": [
      "MISSING_SLOT:X_metric"
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