# S08_5_OPERATOR_OUTPUT

operator_selected: DEPENDENCY_INVERSION
detected_conflict_types: [B]
dominant_conflict_type: B
transformed_conflict_frame: Запуск возможен только после предзапусковой верификации команды и спроса.
what_changed_structurally: Необратимые затраты запрещены до прохождения порога готовности.
mechanism_1l: Запуск филиала разрешён только после проверки (команда>=N и спрос>=M) до любых необратимых затрат; иначе стоп.
search_loop: TRUE
structural_resolution_confirmed: TRUE
separation_illusion_test: FALSE
assisted_matrix:
  - question_id: CR_Q1
    answer: YES
  - question_id: CR_Q2
    answer: YES
  - question_id: CR_Q3
    answer: YES
  - question_id: CR_Q4
    answer: YES
  - question_id: CR_Q5
    answer: YES
