# FORM_SELECTION

{
  "PRIMARY_FORM": "NONE",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "NONE"
    ],
    "WHY_NOT_X": [
      "Рост очереди"
    ],
    "WHY_NOT_Y": [
      "Ограничение по найму"
    ]
  },
  "TRIZ_CORE": {
    "CONTRADICTION_1L": "Скорость ответа должна быть высокой и не может быть высокой без найма.",
    "IKR_1L": "Ответы быстрые без найма и без ухудшения качества.",
    "physical_contradiction": {
      "object": "Процесс поддержки",
      "parameter": "скорость ответа",
      "state_a": "высокая",
      "state_not_a": "низкая"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "скорость ответа зависит от категории/сегмента",
      "expected_resolution": "критичные запросы обрабатываются быстро, остальные — по SLA"
    },
    "system_operator": {
      "system_present": "Очередь поддержки",
      "subsystem_present": "Категория запроса",
      "system_future": "Рост при фиксированной команде"
    },
    "transformation_model": {
      "changed_object": "правила обработки очереди",
      "new_state": "разделение по условию приоритета",
      "resolution_link": "скорость сохраняется для критичных без найма"
    },
    "non_obviousness_check": {
      "assumption_broken": "без условного разделения скорость нельзя сохранить",
      "why_not_obvious": "условное разделение меняет скорость без найма"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      "CORE_OPERATOR: separation_condition",
      "CORE_OPERATOR: segmentation"
    ],
    "ACTIONS": [
      "ввести разные SLA по категориям",
      "критичные запросы в отдельный поток"
    ]
  },
  "IKR_TEST": {
    "Q1": "Скорость ответа соблюдена",
    "Q2": "Рост выдержан без найма"
  },
  "CONFIDENCE": {
    "score": "0.5",
    "justification": "сегментация снижает нагрузку"
  }
}