# FORM_SELECTION

{
  "PRIMARY_FORM": "Form 5",
  "BOUNDARY_CHECK": {
    "note": "ok"
  },
  "TRIZ_CORE": {
    "physical_contradiction": {
      "object": "branch decisions",
      "parameter": "autonomy level",
      "state_a": "high local autonomy",
      "state_not_a": "strict central control"
    },
    "separation": {
      "separation_type": "condition",
      "what_changes": "autonomy depends on risk category",
      "expected_resolution": "high-risk decisions escalated, low-risk decisions local"
    },
    "system_operator": {
      "subsystem_present": "local manager",
      "system_present": "branch governance",
      "supersystem_present": "network policy"
    },
    "transformation_model": {
      "changed_object": "approval routing",
      "new_state": "risk-tier routing",
      "resolution_link": "reduces overload while keeping control"
    },
    "non_obviousness_check": {
      "assumption_broken": "without condition separation_type autonomy and control cannot coexist",
      "why_not_obvious": "condition separation_type changes autonomy depends on risk category expected_resolution"
    }
  },
  "PRINCIPLES_TO_ACTION": {
    "PRINCIPLES": [
      1
    ],
    "ACTIONS": [
      "tiered routing"
    ]
  },
  "IKR_TEST": {
    "Q1": "YES"
  },
  "CONFIDENCE": {
    "score": 1
  }
}