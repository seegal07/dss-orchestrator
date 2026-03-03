# MECHANISM_SPEC C03

{
  "concept_index": 3,
  "A_name_tagline": "Категорийная очередь",
  "B_axis_and_resource": "Категория сложности",
  "C_mechanism_steps": [
    "Классифицировать сложности",
    "Разнести очереди"
  ],
  "D_assumptions_constraints": [
    "Категории известны"
  ],
  "E_risks_failures": [
    "Смещение нагрузки"
  ],
  "F_metrics": {
    "leading": [
      "Доля простых запросов"
    ],
    "lagging": [
      "Время ответа"
    ]
  },
  "G_experiment": {
    "timebox": "30 дней",
    "budget": "0",
    "pass_criteria": "Скорость ответа не ухудшается"
  }
}