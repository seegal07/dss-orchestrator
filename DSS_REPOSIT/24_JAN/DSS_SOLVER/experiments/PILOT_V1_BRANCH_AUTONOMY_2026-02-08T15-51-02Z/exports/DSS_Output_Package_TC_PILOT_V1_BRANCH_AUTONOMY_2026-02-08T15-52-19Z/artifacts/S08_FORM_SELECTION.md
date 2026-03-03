# FORM_SELECTION

{
  "PRIMARY_FORM": "Форма противоречия",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "Форма регламентов",
      "Форма контроля"
    ],
    "WHY_NOT_X": [
      "Нельзя замораживать рост"
    ],
    "WHY_NOT_Y": [
      "Нельзя увеличивать нагрузку CEO"
    ]
  },
  "TRIZ_CORE": {
    "physical_contradiction": {
      "object": "Автономия филиала",
      "parameter": "Степень автономии",
      "state_a": "Высокая",
      "state_not_a": "Низкая"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "Автономия включается только при выполнении условий зрелости",
      "expected_resolution": "Рост при контролируемых инцидентах"
    },
    "system_operator": {
      "system_present": "Сеть филиалов",
      "system_past": "Централизованный контроль",
      "supersystem_present": "Рынок"
    },
    "transformation_model": {
      "changed_object": "Политика автономии",
      "new_state": "Условная автономия по правилам допуска",
      "resolution_link": "Снимает конфликт между ростом и ошибками"
    },
    "non_obviousness_check": {
      "assumption_broken": "assumption_broken=separation_type condition allows autonomy only when maturity conditions are met"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      "Разделение по условиям",
      "Лимитирование"
    ],
    "ACTIONS": [
      "Коридор автономии по допуску",
      "Автономия только для зрелых филиалов"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES",
    "Q2": "YES"
  },
  "CONFIDENCE": {
    "score": 2,
    "justification": "Separation по условиям"
  }
}