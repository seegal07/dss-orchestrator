from TRIZ_CORE_ENGINE.api import validate_triz_core


def _base_tc():
    return {
        "full_vector": {
            "step_8": {
                "TRIZ_CORE": {
                    "physical_contradiction": {
                        "object": "feature",
                        "parameter": "customization",
                        "state_a": "high",
                        "state_not_a": "low",
                    },
                    "separation": {
                        "separation_type": "condition",
                        "what_changes": "only for segment",
                        "expected_resolution": "limit overload",
                    },
                    "system_operator": {
                        "system_present": "product",
                        "system_past": "product",
                        "supersystem_present": "market",
                    },
                    "transformation_model": {
                        "changed_object": "core layer",
                        "new_state": "separated extension",
                        "resolution_link": "removes conflict",
                    },
                    "non_obviousness_check": {
                        "assumption_broken": "customization must touch core",
                    },
                }
            }
        }
    }


def test_missing_physical_contradiction_invalid():
    tc = _base_tc()
    tc["full_vector"]["step_8"]["TRIZ_CORE"].pop("physical_contradiction")
    res = validate_triz_core(tc, None, None)
    assert res["status"] == "INVALID"


def test_missing_separation_invalid():
    tc = _base_tc()
    tc["full_vector"]["step_8"]["TRIZ_CORE"].pop("separation")
    res = validate_triz_core(tc, None, None)
    assert res["status"] == "INVALID"


def test_missing_non_obviousness_invalid():
    tc = _base_tc()
    tc["full_vector"]["step_8"]["TRIZ_CORE"].pop("non_obviousness_check")
    res = validate_triz_core(tc, None, None)
    assert res["status"] == "INVALID"


def test_minimal_full_set_valid():
    tc = _base_tc()
    res = validate_triz_core(tc, None, None)
    assert res["status"] == "VALID"
