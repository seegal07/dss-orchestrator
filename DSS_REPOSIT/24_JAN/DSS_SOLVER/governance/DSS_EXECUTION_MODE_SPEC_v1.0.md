# DSS_EXECUTION_MODE_SPEC_v1.0
## Execution Mode Control Layer

### 1. Purpose
Define mandatory execution modes for DSS_TRIZ-2 / DSS-3.
Prevent unintended activation of DCF, replay, or live dialogue.

---

### 2. Mandatory MODE Header

Every command must start with:

MODE: <one of the allowed modes>

If MODE is missing -> DO NOTHING.

---

### 3. Allowed Modes

MODE: ARCHITECTURE_ONLY  
- No live interaction  
- No DCF  
- No SDP  
- No case loading

MODE: OFFLINE_SIMULATION  
- Can load case  
- Can simulate steps  
- No live questioning  
- No DCF auto-activation

MODE: LIVE_CLIENT  
- Dialogue allowed  
- Clarification Loop allowed  
- SDP enabled  
- DCF allowed (if triggered)

MODE: REPLAY_FREEZE  
- Load frozen case only  
- No new client input  
- No DCF auto-activation unless explicitly requested

MODE: GOVERNANCE_UPDATE  
- Only documentation changes  
- No pipeline execution

---

### 4. DCF Activation Rule

DCF may activate ONLY IF:

MODE == LIVE_CLIENT  
AND  
SDP == TRUE

If MODE != LIVE_CLIENT -> DCF_DISABLED = TRUE

---

### 5. Freeze Replay Protection

If case loaded from CASE_FREEZE.md:
DCF auto-activation is forbidden
unless explicit flag:

ALLOW_DCF_ON_REPLAY = TRUE

---

### 6. Logging Requirement

Every run must log:

EXECUTION_MODE = <mode>
CASE_SOURCE = <path or NONE>
DCF_STATUS = ENABLED / DISABLED
SDP_STATUS = TRUE / FALSE

---

### 7. Status

Normative governance layer.
Does not modify:
- TRIZ core
- Gate logic
- DCF generator
- Enforcement logic

---
