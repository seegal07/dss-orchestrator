# OPERATOR_OUTPUT

{
  "operator_selected": "DEPENDENCY_INVERSION",
  "detected_conflict_types": [
    "B",
    "A"
  ],
  "dominant_conflict_type": "B",
  "transformed_conflict_frame": "Сначала проверка пригодности кандидата, затем оффер в лимите срока/бюджета",
  "what_changed_structurally": "Оффер зависит от верифицированной пригодности кандидата, иначе стоп и новый поиск",
  "structural_resolution_confirmed": true,
  "separation_illusion_test": false,
  "search_loop": true,
  "assisted_matrix": [
    {
      "question_id": "Q1",
      "answer": "YES"
    },
    {
      "question_id": "Q2",
      "answer": "YES"
    },
    {
      "question_id": "Q3",
      "answer": "YES"
    },
    {
      "question_id": "Q4",
      "answer": "YES"
    },
    {
      "question_id": "Q5",
      "answer": "YES"
    }
  ],
  "gatecr_status": "PASS",
  "hard_fail_message": "",
  "operator_prompt": {
    "source": "synthetic"
  }
}