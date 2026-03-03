# SOLUTION_SET

{
  "count_rule": "2",
  "concepts": [
    {
      "concept_index": 1,
      "name": "Двухконтурная автономия по риску",
      "idea_1l": "Решения низкого риска остаются автономными; решения высокого риска требуют контроля",
      "linked_form": "separation: condition",
      "linked_principles": [
        "CORE_OPERATOR: separation_condition"
      ],
      "linked_resources": [
        "Порог потерь 15k €/30 дней"
      ],
      "ikr_alignment_1l": "Сохраняет скорость и контроль",
      "traceability": "separation: condition; principle: Разделение по условию"
    },
    {
      "concept_index": 2,
      "name": "Классификация сделок по риску",
      "idea_1l": "Классы сделок получают разные правила автономии",
      "linked_form": "separation: condition",
      "linked_principles": [
        "CORE_OPERATOR: segmentation"
      ],
      "linked_resources": [
        "Базовая линия инцидентов 8/мес"
      ],
      "ikr_alignment_1l": "Снижает инциденты без остановки роста",
      "traceability": "separation: condition; principle: Дробление"
    },
    {
      "concept_index": 3,
      "name": "Адаптивные лимиты автономии",
      "idea_1l": "Лимиты автономии зависят от порога риска и соблюдения IKR",
      "linked_form": "separation: condition",
      "linked_principles": [
        "CORE_OPERATOR: separation_condition"
      ],
      "linked_resources": [
        "Порог потерь 15k €/30 дней"
      ],
      "ikr_alignment_1l": "Сохраняет рост и контроль",
      "traceability": "contradiction: автономия/контроль; resource: порог потерь; barrier: одновременно высокая автономия и контроль"
    }
  ]
}