# OPERATOR_OUTPUT

{
  "operator_selected": "DEPENDENCY_INVERSION",
  "detected_conflict_types": [
    "B"
  ],
  "dominant_conflict_type": "B",
  "transformed_conflict_frame": "Запуск отделен от необратимых затрат до прохождения порога готовности.",
  "what_changed_structurally": "Необратимые затраты зависят от верификации команды и спроса.",
  "mechanism_1l": "Запуск филиала разрешён только после проверки (команда>=N и спрос>=M) до любых необратимых затрат; иначе стоп.",
  "search_loop": true,
  "structural_resolution_confirmed": true,
  "separation_illusion_test": false,
  "assisted_matrix": {
    "-": {
      "question_id": "CR_Q5",
      "answer": "YES"
    }
  },
  "gatecr_status_mirror": "NOT_APPLICABLE"
}