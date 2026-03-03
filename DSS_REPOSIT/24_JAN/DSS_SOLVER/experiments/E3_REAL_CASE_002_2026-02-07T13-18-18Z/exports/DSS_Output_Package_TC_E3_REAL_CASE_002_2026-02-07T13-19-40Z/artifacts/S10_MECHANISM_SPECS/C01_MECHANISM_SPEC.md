# MECHANISM_SPEC C01

{
  "concept_index": 1,
  "A_name_tagline": "Разделение потоков",
  "B_axis_and_resource": "Очереди + приоритеты",
  "C_mechanism_steps": [
    "Сегментировать заказы",
    "Назначить правила очередей"
  ],
  "D_assumptions_constraints": [
    "Без нового WMS"
  ],
  "E_risks_failures": [
    "Ошибки сегментации"
  ],
  "F_metrics": {
    "leading": [
      "Время цикла"
    ],
    "lagging": [
      "SLA",
      "% ошибок"
    ]
  },
  "G_experiment": {
    "timebox": "3 месяца",
    "budget": "≤30 000 EUR",
    "pass_criteria": "SLA ≥95%, ошибки ≤1%"
  }
}