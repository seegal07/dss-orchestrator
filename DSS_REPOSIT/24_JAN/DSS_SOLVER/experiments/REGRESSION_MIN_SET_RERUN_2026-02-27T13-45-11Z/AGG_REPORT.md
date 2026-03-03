# REGRESSION_MIN_SET_RERUN REPORT
RUN_ROOT: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z

overall_pass: False

## Per-pack observed vs expected

### POSITIVE_A
- source_pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_CASE_01_RUN_V4_2026-02-24T15-27-32Z
- expected: {"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"}
- observed: {"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"}
- harness_crash: True
- GatePFL (gate_log primary): E22_V1=None/None; E22_V2=None/None; E22_V3=None/None
- anchors: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/01_POSITIVE_A/REPORT.md
- deviation_fields: checkpoints, Step1, Step2

### POSITIVE_B
- source_pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_B_CASE_01_RUN_V2_2026-02-24T11-18-23Z
- expected: {"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"}
- observed: {"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"}
- harness_crash: True
- GatePFL (gate_log primary): E22_V1=None/None; E22_V2=None/None; E22_V3=None/None
- anchors: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/02_POSITIVE_B/REPORT.md
- deviation_fields: checkpoints, Step1, Step2

### POSITIVE_C
- source_pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_C_CASE_01_RUN_V1_2026-02-24T15-41-33Z
- expected: {"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"}
- observed: {"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"}
- harness_crash: True
- GatePFL (gate_log primary): E22_V1=None/None; E22_V2=None/None; E22_V3=None/None
- anchors: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/03_POSITIVE_C/REPORT.md
- deviation_fields: checkpoints, Step1, Step2

### NEGATIVE
- source_pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_RUN_V8_SLOT_INVARIANCE_2026-02-23T15-24-39Z
- expected: {"checkpoints": "PASS/PASS", "Step1": "FAIL", "Step2": "NOT_APPLICABLE"}
- observed: {"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"}
- harness_crash: True
- GatePFL (gate_log primary): E22_V1=None/None; E22_V2=None/None; E22_V3=None/None
- anchors: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/04_NEGATIVE/REPORT.md
- deviation_fields: checkpoints, Step1, Step2

### RESOLVED_HISTORY (former KNOWN_ISSUE / PAUSE)
- source_pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/E22_POSITIVE_C_CASE_01_RUN_V3_2026-02-25T11-50-52Z
- expected: {"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"}
- observed: {"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"}
- harness_crash: True
- GatePFL (gate_log primary): E22_V1=None/None; E22_V2=None/None; E22_V3=None/None
- anchors: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/05_RESOLVED_HISTORY_former_KNOWN_ISSUE_PAUSE/REPORT.md
- deviation_fields: checkpoints, Step1, Step2

### LIVE_PROTOCOL_READINESS_CONTROL
- source_pack: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/LIVE_OWNER_CASE_STAGEA_PROTOCOL_V0_1_AFTER_MINPATCH2_2026-02-26T09-27-55Z
- expected: {"checkpoints": "PASS"}
- observed: {"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"}
- harness_crash: True
- GatePFL (gate_log primary): LIVE_OWNER_PROTOCOL_V1=None/None
- anchors: /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/06_LIVE_PROTOCOL_READINESS_CONTROL/REPORT.md
- deviation_fields: checkpoints

## Deviations (evidence-first)
- POSITIVE_A: expected={"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"} observed={"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"} anchors={'report': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/01_POSITIVE_A/REPORT.md', 'checkpoints': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/01_POSITIVE_A/CHECKPOINTS.json', 'summary': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/01_POSITIVE_A/SUMMARY.json'}
- POSITIVE_B: expected={"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"} observed={"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"} anchors={'report': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/02_POSITIVE_B/REPORT.md', 'checkpoints': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/02_POSITIVE_B/CHECKPOINTS.json', 'summary': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/02_POSITIVE_B/SUMMARY.json'}
- POSITIVE_C: expected={"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"} observed={"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"} anchors={'report': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/03_POSITIVE_C/REPORT.md', 'checkpoints': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/03_POSITIVE_C/CHECKPOINTS.json', 'summary': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/03_POSITIVE_C/SUMMARY.json'}
- NEGATIVE: expected={"checkpoints": "PASS/PASS", "Step1": "FAIL", "Step2": "NOT_APPLICABLE"} observed={"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"} anchors={'report': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/04_NEGATIVE/REPORT.md', 'checkpoints': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/04_NEGATIVE/CHECKPOINTS.json', 'summary': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/04_NEGATIVE/SUMMARY.json'}
- RESOLVED_HISTORY (former KNOWN_ISSUE / PAUSE): expected={"checkpoints": "PASS/PASS", "Step1": "PASS", "Step2": "PASS"} observed={"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"} anchors={'report': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/05_RESOLVED_HISTORY_former_KNOWN_ISSUE_PAUSE/REPORT.md', 'checkpoints': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/05_RESOLVED_HISTORY_former_KNOWN_ISSUE_PAUSE/CHECKPOINTS.json', 'summary': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/05_RESOLVED_HISTORY_former_KNOWN_ISSUE_PAUSE/SUMMARY.json'}
- LIVE_PROTOCOL_READINESS_CONTROL: expected={"checkpoints": "PASS"} observed={"checkpoints": "FAIL/FAIL", "Step1": "NOT_RUN", "Step2": "NOT_RUN"} anchors={'report': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/06_LIVE_PROTOCOL_READINESS_CONTROL/REPORT.md', 'checkpoints': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/06_LIVE_PROTOCOL_READINESS_CONTROL/CHECKPOINTS.json', 'summary': '/Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/REGRESSION_MIN_SET_RERUN_2026-02-27T13-45-11Z/06_LIVE_PROTOCOL_READINESS_CONTROL/SUMMARY.json'}
