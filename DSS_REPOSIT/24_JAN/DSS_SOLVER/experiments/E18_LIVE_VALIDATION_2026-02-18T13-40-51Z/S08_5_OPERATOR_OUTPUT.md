# S08_5_OPERATOR_OUTPUT

operator_selected: DEPENDENCY_INVERSION
detected_conflict_types: [B]
dominant_conflict_type: B
transformed_conflict_frame: Локальное исключение из CRM-порядка разрешается только при риске провала ивента и автоматически закрывается по порогу подтверждений.
what_changed_structurally: Решение об отклонении от CRM сделано условным и обратимым по явному триггеру, а не произвольным.
mechanism_1l: Если подтверждено <15, приоритетом становится обзвон ранее зарегистрированных неявившихся лидов; при >=15 — возврат в стандарт CRM.
search_loop: TRUE
structural_resolution_confirmed: true
separation_illusion_test: false
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
