# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "1920a1e97a05906ef2d233a11be308654e11c3714ca7c680b8bbfa36ac23562d",
  "canonical_hash_v0": "1920a1e97a05906ef2d233a11be308654e11c3714ca7c680b8bbfa36ac23562d",
  "canonical_hash_text": "15ac1363a8cf1ac8973431b910de9865c43d7df5039ee2de9955671fb6c0b676",
  "canonical_slots_v0": {
    "scope": "Запуск филиалов в Европе",
    "X_direction": "other",
    "X_delta_direction": "increase",
    "X_metric_polarity": "HIGHER_IS_BETTER",
    "X_metric": "точность",
    "X_object": "филиалов",
    "Y_direction": "other",
    "Y_delta_direction": "increase",
    "Y_metric_polarity": "LOWER_IS_BETTER",
    "Y_metric": "время",
    "Y_object": "филиалов",
    "constraints": [
      "Без роста бюджета и без увеличения длительности исследования/подготовки"
    ],
    "trace_markers": [
      "DELTA_FROM_RAW:X",
      "DELTA_FROM_RAW:Y"
    ]
  },
  "raw_hash": "b14d72a327e0d74b4f9ef96833f1ef845e411907c3a737033f41aa9db48e0838",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "Запуск филиалов в Европе",
  "canonical_X": "точность прогноза для запуска филиалов в Европе",
  "canonical_Y": "время запуска филиалов в Европе",
  "canonical_constraints": [
    "Без роста бюджета и без увеличения длительности исследования/подготовки"
  ],
  "canonical_conflict_type_candidate_trace": null,
  "phase0_trace": [
    {
      "raw_fragment": "точность прогноза для запуска филиалов в Европе",
      "interpreted_parameter": "точность прогноза для запуска филиалов в Европе",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "время запуска филиалов в Европе",
      "interpreted_parameter": "время запуска филиалов в Европе",
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
      "raw_fragment": "['Без роста бюджета и без увеличения длительности исследования/подготовки']",
      "interpreted_parameter": [
        "Без роста бюджета и без увеличения длительности исследования/подготовки"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}