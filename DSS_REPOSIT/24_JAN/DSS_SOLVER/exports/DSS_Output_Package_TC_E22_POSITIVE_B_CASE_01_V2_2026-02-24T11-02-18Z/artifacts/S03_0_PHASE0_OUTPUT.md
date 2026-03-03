# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "2731d164ec510c17faf5ff70f37e7c02bc90dae3726f1d5ed84039f32f1159da",
  "canonical_hash_v0": "2731d164ec510c17faf5ff70f37e7c02bc90dae3726f1d5ed84039f32f1159da",
  "canonical_hash_text": "57e02640435c0da72d514c19ae1710516a563aa755b1cecc02baa359ad6fbde2",
  "canonical_slots_v0": {
    "scope": "Запуск филиалов в Европе",
    "X_direction": "other",
    "X_metric": "точность",
    "X_object": "прогноза",
    "Y_direction": "other",
    "Y_metric": "время",
    "Y_object": "филиалов",
    "constraints": [
      "Без роста бюджета и без увеличения длительности исследования/подготовки"
    ],
    "trace_markers": []
  },
  "raw_hash": "0aaebcd307e46d289df53d2a1fea1ae1d1015794fe776575b93a23222ad77a7c",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "Запуск филиалов в Европе",
  "canonical_X": "точность прогноза",
  "canonical_Y": "время запуска филиалов в Европе",
  "canonical_constraints": [
    "Без роста бюджета и без увеличения длительности исследования/подготовки"
  ],
  "phase0_trace": [
    {
      "raw_fragment": "точность прогноза",
      "interpreted_parameter": "точность прогноза",
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