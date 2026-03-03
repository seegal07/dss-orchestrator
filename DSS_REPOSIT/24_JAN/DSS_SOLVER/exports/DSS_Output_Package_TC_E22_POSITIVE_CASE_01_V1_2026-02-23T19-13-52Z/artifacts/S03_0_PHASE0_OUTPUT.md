# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "354f1db9bc52edae6d519e2a5cb932f5cde50ddcd2f43afb40a77295aef9dba8",
  "canonical_hash_v0": "354f1db9bc52edae6d519e2a5cb932f5cde50ddcd2f43afb40a77295aef9dba8",
  "canonical_hash_text": "ebec08d469c7204646241f6ea730ba2c68c7e1e909c0196b55ca431af1a74feb",
  "canonical_slots_v0": {
    "scope": "Запуск филиалов в Европе",
    "X_direction": "accelerate",
    "X_metric": "точность",
    "X_object": "филиалов и точность",
    "Y_direction": "increase",
    "Y_metric": "срок",
    "Y_object": null,
    "constraints": [
      "Не увеличивать бюджет и не увеличивать срок исследования/подготовки"
    ],
    "trace_markers": [
      "MISSING_SLOT:Y_object"
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