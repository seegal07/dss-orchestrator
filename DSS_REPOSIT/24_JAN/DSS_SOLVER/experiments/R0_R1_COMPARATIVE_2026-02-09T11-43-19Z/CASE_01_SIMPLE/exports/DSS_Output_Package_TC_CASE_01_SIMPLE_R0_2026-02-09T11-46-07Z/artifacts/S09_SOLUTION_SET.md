# SOLUTION_SET

{
  "count_rule": "3",
  "concepts": [
    {
      "concept_index": 1,
      "name": "Два SLA потока",
      "idea_1l": "Разделить запросы на критичные и обычные с разными SLA",
      "linked_form": "separation: condition",
      "linked_principles": [
        "CORE_OPERATOR: separation_condition"
      ],
      "linked_resources": [
        "Правила приоритета"
      ],
      "ikr_alignment_1l": "Скорость критичных сохраняется",
      "traceability": "separation: condition; resource: правила приоритета"
    },
    {
      "concept_index": 2,
      "name": "Сегментный приоритет",
      "idea_1l": "Приоритет по ценности клиента",
      "linked_form": "separation: condition",
      "linked_principles": [
        "CORE_OPERATOR: segmentation"
      ],
      "linked_resources": [
        "Типы клиентов"
      ],
      "ikr_alignment_1l": "Скорость для ключевых",
      "traceability": "resource: типы клиентов; contradiction element: скорость ответа"
    },
    {
      "concept_index": 3,
      "name": "Категорийная очередь",
      "idea_1l": "Очереди по категориям сложности",
      "linked_form": "separation: condition",
      "linked_principles": [
        "CORE_OPERATOR: separation_condition"
      ],
      "linked_resources": [
        "Категории запросов"
      ],
      "ikr_alignment_1l": "Снижение времени на простые",
      "traceability": "resource: категории запросов; contradiction element: скорость"
    }
  ]
}