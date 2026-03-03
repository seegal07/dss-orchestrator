# PHASE0_OUTPUT

{
  "phase0_enabled": true,
  "phase0_verdict": "PASS",
  "phase0_reason_code": "NONE",
  "canonical_hash": "55f193122fe192dd5560ab2ef1c022e19412fb879472c41046026396ed16203f",
  "canonical_hash_v0": "55f193122fe192dd5560ab2ef1c022e19412fb879472c41046026396ed16203f",
  "s2a_hash": "939e10ddd0fd626d4f73eabc735866cf8e958dfcba65609a504c3ce68eb8c865",
  "canonical_hash_text": "738efc33d0bf536d03a18c796bdfba87514361059f3688d63bf05c0664e9b83c",
  "canonical_slots_v0": {
    "scope": "правило запуска новых филиалов в Европе",
    "X_direction": "accelerate",
    "X_delta_direction": "accelerate",
    "X_metric_polarity": "HIGHER_IS_BETTER",
    "X_metric": "точность",
    "X_object": "филиалов",
    "Y_direction": "increase",
    "Y_delta_direction": "unknown",
    "Y_metric_polarity": "LOWER_IS_BETTER",
    "Y_metric": "время",
    "Y_object": "запуска",
    "constraints": [
      "не раздувать исследовательский бюджет/срок"
    ],
    "trace_markers": [
      "MISSING_SLOT:Y_delta_direction"
    ]
  },
  "raw_hash": "cbbae6e80f35e1a7f02a411685d9236b3dd8e1547c26f8355be122a9a1bce70c",
  "trace_count": 4,
  "confidence_summary": "HIGH",
  "canonical_scope": "правило запуска новых филиалов в Европе",
  "canonical_X": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
  "canonical_Y": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
  "canonical_constraints": [
    "не раздувать исследовательский бюджет/срок"
  ],
  "canonical_conflict_type_candidate_trace": null,
  "phase0_trace": [
    {
      "raw_fragment": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
      "interpreted_parameter": "Ускорить запуск филиалов в Европе и повысить точность CAPEX/OPEX+PMF до запуска.",
      "reasoning_trace": "X:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
      "interpreted_parameter": "Не увеличивать чрезмерно время и стоимость подготовки запуска.",
      "reasoning_trace": "Y:normalize_whitespace",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "правило запуска новых филиалов в Европе",
      "interpreted_parameter": "правило запуска новых филиалов в Европе",
      "reasoning_trace": "scope:scope_projection",
      "confidence_level": "HIGH"
    },
    {
      "raw_fragment": "['не раздувать исследовательский бюджет/срок']",
      "interpreted_parameter": [
        "не раздувать исследовательский бюджет/срок"
      ],
      "reasoning_trace": "constraints:stable_list_sort",
      "confidence_level": "HIGH"
    }
  ]
}