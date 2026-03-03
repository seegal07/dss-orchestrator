# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "676fb154a9b228d9ee7b856cec18650d023bc5c0b06fbf765dde4e19cc6e0e5b",
  "canonical_hash_v0": "676fb154a9b228d9ee7b856cec18650d023bc5c0b06fbf765dde4e19cc6e0e5b",
  "s2a_hash": "647e3d2ebaa9f7e4ffc8c640344bcb5c5c660fb5b9472396604d51c34fb7d35b",
  "canonical_hash_text": "ebec08d469c7204646241f6ea730ba2c68c7e1e909c0196b55ca431af1a74feb",
  "canonical_slots_v0": {
    "scope": "Запуск филиалов в Европе",
    "X_direction": "accelerate",
    "X_delta_direction": "accelerate",
    "X_metric_polarity": "HIGHER_IS_BETTER",
    "X_metric": "точность",
    "X_object": "филиалов и точность",
    "Y_direction": "increase",
    "Y_delta_direction": "accelerate",
    "Y_metric_polarity": "LOWER_IS_BETTER",
    "Y_metric": "срок",
    "Y_object": "UNKNOWN",
    "constraints": [
      "Не увеличивать бюджет и не увеличивать срок исследования/подготовки"
    ],
    "trace_markers": [
      "MISSING_SLOT:Y_object",
      "DELTA_FROM_RAW:Y"
    ]
  },
  "raw_hash": "1e91653c5551b5fbb01f83e1a6901bfec9427f6630c39b1d67924dcae235c87f",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "Запуск филиалов в Европе",
  "canonical_X": "ускорение запуска филиалов и точность прогноза",
  "canonical_Y": "рост бюджета и срока исследования/подготовки",
  "canonical_constraints": [
    "Не увеличивать бюджет и не увеличивать срок исследования/подготовки"
  ],
  "canonical_conflict_type_candidate_trace": null,
  "phase0_trace": [
    {
      "raw_fragment": "ускорение запуска филиалов и точность прогноза",
      "interpreted_parameter": "ускорение запуска филиалов и точность прогноза",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "рост бюджета и срока исследования/подготовки",
      "interpreted_parameter": "рост бюджета и срока исследования/подготовки",
      "reasoning_trace": "Y:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "Запуск филиалов в Европе",
      "interpreted_parameter": "Запуск филиалов в Европе",
      "reasoning_trace": "scope:scope_projection",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "['Не увеличивать бюджет и не увеличивать срок исследования/подготовки']",
      "interpreted_parameter": [
        "Не увеличивать бюджет и не увеличивать срок исследования/подготовки"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}