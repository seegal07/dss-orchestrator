# FORM_SELECTION

{
  "PRIMARY_FORM": "Form 5",
  "BOUNDARY_CHECK": {
    "note": "контроль против перерасхода"
  },
  "TRIZ_CORE": {
    "physical_contradiction": {
      "object": "запуск филиала",
      "parameter": "точность/время",
      "state_a": "высокая точность",
      "state_not_a": "короткое время запуска"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "условие допуска",
      "expected_resolution": "контроль trade-off"
    },
    "system_operator": {
      "subsystem_present": "подготовка",
      "system_present": "pipeline запуска",
      "supersystem_present": "сеть филиалов"
    },
    "transformation_model": {
      "changed_object": "условие допуска",
      "new_state": "через критерий готовности",
      "resolution_link": "баланс точности и времени"
    },
    "non_obviousness_check": {
      "assumption_broken": "выше точность всегда без влияния на время",
      "why_not_obvious": "в реальности есть trade-off"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      1
    ],
    "ACTIONS": [
      "условный допуск"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES"
  },
  "CONFIDENCE": {
    "score": 1
  },
  "risk_1l": "риск неверного критерия"
}