# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "76ef3f231419c0429ba80c521932f613dd121628a4a2a6ad4a1dcc0726c55974",
  "canonical_hash_v0": "76ef3f231419c0429ba80c521932f613dd121628a4a2a6ad4a1dcc0726c55974",
  "s2a_hash": "92f96700b807199c402805c83c21ddc699373a6c1ce7fb10329f075e09c3d742",
  "canonical_hash_text": "26160f1f447d4ca0067978ba76d14c8d5d27bbe63b069e2e50d2184aeaa73f9e",
  "canonical_slots_v0": {
    "scope": "правило запуска новых филиалов в Европе",
    "X_direction": "accelerate",
    "X_delta_direction": "unknown",
    "X_metric_polarity": "UNKNOWN",
    "X_metric": "темп",
    "X_object": "филиалов",
    "Y_direction": "increase",
    "Y_delta_direction": "unknown",
    "Y_metric_polarity": "LOWER_IS_BETTER",
    "Y_metric": "срок",
    "Y_object": "запуска",
    "constraints": [
      "не раздувать исследовательский бюджет/срок"
    ],
    "trace_markers": [
      "MISSING_SLOT:X_delta_direction",
      "MISSING_SLOT:Y_delta_direction",
      "UNKNOWN_POLARITY:X"
    ]
  },
  "raw_hash": "19a8bcdc887b225c0bf6b007e8e1477a0a12bc1e4b0e439cb7641cc3cc2f45f8",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "правило запуска новых филиалов в Европе",
  "canonical_X": "Повысить темп запуска европейских филиалов при более точной предоценке CAPEX/OPEX и PMF до открытия.",
  "canonical_Y": "Не увеличивать избыточно сроки и расходы на подготовку запуска.",
  "canonical_constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "canonical_conflict_type_candidate_trace": null,
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