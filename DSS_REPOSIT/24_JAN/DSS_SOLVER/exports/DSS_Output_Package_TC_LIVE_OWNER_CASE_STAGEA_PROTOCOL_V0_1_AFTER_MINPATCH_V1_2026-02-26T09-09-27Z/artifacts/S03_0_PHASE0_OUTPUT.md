# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "b26aabc331b3a80d7af755aefb6ebfebfb321f32d475630921b428cf1e36a188",
  "canonical_hash_v0": "b26aabc331b3a80d7af755aefb6ebfebfb321f32d475630921b428cf1e36a188",
  "canonical_hash_text": "c6746c9a0ee1c7592aea63bb40a1e5d2cc2b917d06119c74eb7f3e4dcbf3d593",
  "canonical_slots_v0": {
    "scope": "выбор страны проживания семьи (Польша vs Испания) при удаленной работе",
    "X_direction": "other",
    "X_delta_direction": "increase",
    "X_metric_polarity": "HIGHER_IS_BETTER",
    "X_metric": "комфорт",
    "X_object": null,
    "Y_direction": "other",
    "Y_delta_direction": "increase",
    "Y_metric_polarity": "LOWER_IS_BETTER",
    "Y_metric": "налоги",
    "Y_object": "мой доход",
    "constraints": [
      "бюджет семьи не должен уходить в дефицит",
      "до июля 2026",
      "обучение на английском языке",
      "школа для ребенка должна быть определена к сентябрю 2026"
    ],
    "trace_markers": [
      "MISSING_SLOT:X_object",
      "OBJ_FROM_NA_PATTERN:Y",
      "DELTA_FROM_RAW:X",
      "DELTA_FROM_RAW:Y"
    ]
  },
  "raw_hash": "219f78ef3089c057a51225ef171b0fccb3246f79beeb7cef3f677195685cb990",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "выбор страны проживания семьи (Польша vs Испания) при удаленной работе",
  "canonical_X": "комфорт проживания семьи",
  "canonical_Y": "налоговая нагрузка на мой доход",
  "canonical_constraints": [
    "бюджет семьи не должен уходить в дефицит",
    "до июля 2026",
    "обучение на английском языке",
    "школа для ребенка должна быть определена к сентябрю 2026"
  ],
  "canonical_conflict_type_candidate_trace": null,
  "phase0_trace": [
    {
      "raw_fragment": "комфорт проживания семьи",
      "interpreted_parameter": "комфорт проживания семьи",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "налоговая нагрузка на мой доход",
      "interpreted_parameter": "налоговая нагрузка на мой доход",
      "reasoning_trace": "Y:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "выбор страны проживания семьи (Польша vs Испания) при удаленной работе",
      "interpreted_parameter": "выбор страны проживания семьи (Польша vs Испания) при удаленной работе",
      "reasoning_trace": "scope:scope_projection",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "['школа для ребенка должна быть определена к сентябрю 2026', 'бюджет семьи не должен уходить в дефицит', 'обучение на английском языке', 'до июля 2026']",
      "interpreted_parameter": [
        "бюджет семьи не должен уходить в дефицит",
        "до июля 2026",
        "обучение на английском языке",
        "школа для ребенка должна быть определена к сентябрю 2026"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}