# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "3b83600f606e14b8f43a86836e48081d3cdabe6430ebbf64d348fb14c4e7f57c",
  "canonical_hash_v0": "3b83600f606e14b8f43a86836e48081d3cdabe6430ebbf64d348fb14c4e7f57c",
  "s2a_hash": "bb0109a1fea5264d07c5cf9983a4d3cd8f62efe5a7101e3dc209cad98f43e6b6",
  "canonical_hash_text": "57e02640435c0da72d514c19ae1710516a563aa755b1cecc02baa359ad6fbde2",
  "canonical_slots_v0": {
    "scope": "Запуск филиалов в Европе",
    "X_direction": "other",
    "X_delta_direction": "increase",
    "X_metric_polarity": "HIGHER_IS_BETTER",
    "X_metric": "точность",
    "X_object": "прогноза",
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
  "raw_hash": "0aaebcd307e46d289df53d2a1fea1ae1d1015794fe776575b93a23222ad77a7c",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "Запуск филиалов в Европе",
  "canonical_X": "точность прогноза",
  "canonical_Y": "время запуска филиалов в Европе",
  "canonical_constraints": [
    "Без роста бюджета и без увеличения длительности исследования/подготовки"
  ],
  "canonical_conflict_type_candidate_trace": null,
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