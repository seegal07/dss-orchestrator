# OPERATOR_OUTPUT

{
  "operator_selected": "DEPENDENCY_INVERSION",
  "detected_conflict_types": [
    "B"
  ],
  "dominant_conflict_type": "B",
  "transformed_conflict_frame": "Сначала фильтрация кандидата по верифицированной пригодности, затем оффер в лимите срока/бюджета.",
  "what_changed_structurally": "Оффер теперь зависит от верифицированного прохождения Sintegrum и двух интервью, а не только от скорости закрытия вакансии.",
  "mechanism_1l": "Если Sintegrum >=8 и оба интервью PASS, делаем оффер; иначе стоп и новый поиск.",
  "structural_resolution_confirmed": true,
  "separation_illusion_test": false,
  "search_loop": true,
  "assisted_matrix": [
    {
      "question_id": "CR_Q1",
      "answer": "YES"
    },
    {
      "question_id": "CR_Q2",
      "answer": "YES"
    },
    {
      "question_id": "CR_Q3",
      "answer": "YES"
    },
    {
      "question_id": "CR_Q4",
      "answer": "YES"
    },
    {
      "question_id": "CR_Q5",
      "answer": "YES"
    }
  ]
}