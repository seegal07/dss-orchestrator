# MECHANISM_SPEC C01

{
  "concept_index": 1,
  "A_name_tagline": "Два SLA потока",
  "B_axis_and_resource": "Категория запроса",
  "C_mechanism_steps": [
    "Классифицировать запросы",
    "Применять SLA"
  ],
  "D_assumptions_constraints": [
    "Категории определены"
  ],
  "E_risks_failures": [
    "Ошибочная классификация"
  ],
  "F_metrics": {
    "leading": [
      "Доля критичных"
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