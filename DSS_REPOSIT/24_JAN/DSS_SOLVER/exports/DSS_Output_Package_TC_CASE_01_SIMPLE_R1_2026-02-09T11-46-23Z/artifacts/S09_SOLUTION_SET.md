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
        "P1_SEGMENTATION"
      ],
      "linked_resources": [
        "Правила приоритета"
      ],
      "ikr_alignment_1l": "Скорость критичных сохраняется",
      "traceability": "principle: P1_SEGMENTATION; resource: правила приоритета"
    },
    {
      "concept_index": 2,
      "name": "Сегментный приоритет",
      "idea_1l": "Приоритет по ценности клиента",
      "linked_form": "separation: condition",
      "linked_principles": [
        "P2_CONDITIONALLY_PRIORITY"
      ],
      "linked_resources": [
        "Типы клиентов"
      ],
      "ikr_alignment_1l": "Скорость для ключевых",
      "traceability": "principle: P2_CONDITIONALLY_PRIORITY; resource: типы клиентов"
    },
    {
      "concept_index": 3,
      "name": "Категорийная очередь",
      "idea_1l": "Очереди по категориям сложности",
      "linked_form": "separation: condition",
      "linked_principles": [
        "P1_SEGMENTATION"
      ],
      "linked_resources": [
        "Категории запросов"
      ],
      "ikr_alignment_1l": "Снижение времени на простые",
      "traceability": "principle: P1_SEGMENTATION; resource: категории запросов"
    }
  ]
}