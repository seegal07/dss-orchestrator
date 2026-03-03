# FORM_SELECTION

{
  "PRIMARY_FORM": "Форма противоречия",
  "BOUNDARY_CHECK": {
    "NEAREST_FORMS": [
      "Форма условий",
      "Форма контроля"
    ],
    "WHY_NOT_X": [
      "Нельзя увеличивать часы CEO"
    ],
    "WHY_NOT_Y": [
      "Нельзя превышать 8 инцидентов/мес"
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
      "what_changes": "Автономия включается только при выполнении условий риска",
      "expected_resolution": "Рост при жёстких лимитах инцидентов и потерь"
    },
    "system_operator": {
      "system_present": "Сеть филиалов",
      "system_past": "Централизованный контроль",
      "supersystem_present": "Рынок"
    },
    "transformation_model": {
      "changed_object": "Политика автономии",
      "new_state": "Условная автономия по риск‑коридору",
      "resolution_link": "Снимает конфликт рост/инциденты"
    },
    "non_obviousness_check": {
      "assumption_broken": "assumption_broken=separation_type condition allows autonomy only under risk limits"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      "Разделение по условиям",
      "Лимитирование"
    ],
    "ACTIONS": [
      "Коридор автономии по риску",
      "Автономия только при инцидентах ≤8/мес и потере ≤€15k"
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