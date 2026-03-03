# CONSISTENCY_CHECKS_v0.1

- GateCR tri-state consistency (E23B): `['soft_fail', 'soft_fail', 'soft_fail']`
- E23B_R1: GateCR=soft_fail, compromise_mode=True, rule_ok=True
- E23B_R2: GateCR=soft_fail, compromise_mode=True, rule_ok=True
- E23B_R3: GateCR=soft_fail, compromise_mode=True, rule_ok=True
- compromise_mode activation rule: `PASS`
- HARD_FAIL downstream stop check: no HARD_FAIL observed in this protocol.
- ZERO_LOGIC_CHANGE=YES
- FILES_TOUCHED: NONE
