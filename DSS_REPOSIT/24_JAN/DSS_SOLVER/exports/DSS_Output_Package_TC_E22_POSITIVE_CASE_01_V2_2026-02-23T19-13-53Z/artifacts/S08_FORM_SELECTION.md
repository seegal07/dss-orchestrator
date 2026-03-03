# FORM_SELECTION

{
  "PRIMARY_FORM": "Form 5",
  "BOUNDARY_CHECK": {
    "note": "контроль против перерасхода"
  },
  "TRIZ_CORE": {
    "physical_contradiction": {
      "object": "запуск филиала",
      "parameter": "скорость/точность",
      "state_a": "быстро",
      "state_not_a": "без роста затрат"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "порог запуска",
      "expected_resolution": "ускорение без роста затрат"
    },
    "system_operator": {
      "subsystem_present": "подготовка",
      "system_present": "pipeline запуска",
      "supersystem_present": "сеть филиалов"
    },
    "transformation_model": {
      "changed_object": "условие запуска",
      "new_state": "через порог готовности",
      "resolution_link": "баланс скорости/затрат"
    },
    "non_obviousness_check": {
      "assumption_broken": "быстрее = дороже",
      "why_not_obvious": "при корректном пороге возможно иначе"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      1
    ],
    "ACTIONS": [
      "условный запуск"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES"
  },
  "CONFIDENCE": {
    "score": 1
  },
  "risk_1l": "риск неверного порога"
}