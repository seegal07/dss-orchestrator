# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "02023e4fc493d7c24f6aefac4b9cf6a66b0d88f3d827b0a4d6a00d91f8c58eda",
  "canonical_hash_v0": "02023e4fc493d7c24f6aefac4b9cf6a66b0d88f3d827b0a4d6a00d91f8c58eda",
  "canonical_hash_text": "d5d04afda9f04fcbe5f2d716b936b2b8f7918a2210fdd1e35704eced188b91d9",
  "canonical_slots_v0": {
    "scope": "смена страны проживания с Польши на Испанию при удаленной работе",
    "X_direction": "other",
    "X_delta_direction": "unknown",
    "X_metric_polarity": "UNKNOWN",
    "X_metric": "качество",
    "X_object": null,
    "Y_direction": "other",
    "Y_delta_direction": "unknown",
    "Y_metric_polarity": "HIGHER_IS_BETTER",
    "Y_metric": "точность",
    "Y_object": "UNKNOWN",
    "constraints": [
      "желательно старшую школу заканчивать в Европе с обучением на английском",
      "ребенок заканчивает 9 класс",
      "с сентября ребенку нужно идти в школу или в Польше или в Испании",
      "Хочу принять решение до июля текущего года"
    ],
    "trace_markers": [
      "MISSING_SLOT:X_object",
      "MISSING_SLOT:Y_object",
      "MISSING_SLOT:X_delta_direction",
      "MISSING_SLOT:Y_delta_direction",
      "UNKNOWN_POLARITY:X"
    ]
  },
  "raw_hash": "7a55723263de142c1e39a85c2422b7be4f53729ffdc1b80fafac25ba63f4fba1",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "смена страны проживания с Польши на Испанию при удаленной работе",
  "canonical_X": "качество жизни и обучения ребенка в Испании",
  "canonical_Y": "финансовая достаточность после налогов и расходов",
  "canonical_constraints": [
    "желательно старшую школу заканчивать в Европе с обучением на английском",
    "ребенок заканчивает 9 класс",
    "с сентября ребенку нужно идти в школу или в Польше или в Испании",
    "Хочу принять решение до июля текущего года"
  ],
  "canonical_conflict_type_candidate_trace": null,
  "phase0_trace": [
    {
      "raw_fragment": "качество жизни и обучения ребенка в Испании",
      "interpreted_parameter": "качество жизни и обучения ребенка в Испании",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "финансовая достаточность после налогов и расходов",
      "interpreted_parameter": "финансовая достаточность после налогов и расходов",
      "reasoning_trace": "Y:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "смена страны проживания с Польши на Испанию при удаленной работе",
      "interpreted_parameter": "смена страны проживания с Польши на Испанию при удаленной работе",
      "reasoning_trace": "scope:scope_projection",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "['Хочу принять решение до июля текущего года', 'с сентября ребенку нужно идти в школу или в Польше или в Испании', 'ребенок заканчивает 9 класс', 'желательно старшую школу заканчивать в Европе с обучением на английском']",
      "interpreted_parameter": [
        "желательно старшую школу заканчивать в Европе с обучением на английском",
        "ребенок заканчивает 9 класс",
        "с сентября ребенку нужно идти в школу или в Польше или в Испании",
        "Хочу принять решение до июля текущего года"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}