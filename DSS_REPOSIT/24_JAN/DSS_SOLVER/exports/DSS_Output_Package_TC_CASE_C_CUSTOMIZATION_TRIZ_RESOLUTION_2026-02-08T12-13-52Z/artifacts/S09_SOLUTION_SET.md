# SOLUTION_SET

{
  "count_rule": "3–5",
  "concepts": [
    {
      "concept_index": 1,
      "name": "Модуль расширений",
      "idea_1l": "Вынести кастомизацию в модульный слой",
      "linked_form": "Форма разделения",
      "linked_principles": [
        "Дробление"
      ],
      "linked_resources": [
        "Архитектура продукта"
      ],
      "ikr_alignment_1l": "Сохраняет ядро",
      "traceability": "principle:Дробление; separation:part-whole"
    },
    {
      "concept_index": 2,
      "name": "Контур кастомизации для сегмента",
      "idea_1l": "Разрешать кастомизацию только для сегмента с отдельным SLA",
      "linked_form": "Форма условий",
      "linked_principles": [
        "Разделение по условиям"
      ],
      "linked_resources": [
        "Политика кастомизации"
      ],
      "ikr_alignment_1l": "Ограничивает нагрузку",
      "traceability": "principle:Разделение по условиям; separation:condition"
    }
  ]
}