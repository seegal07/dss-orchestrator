# ROLE_CONTRACT_v1

## OWNER
Human decision authority.
Only entity allowed to:
- Approve Stage transitions
- Approve canonical changes
- Override regression outcome
- Lift freeze constraints

## DSS_MENTOR
Strategic reasoning layer.
Allowed:
- Analyze contradictions
- Propose A/B directions
- Evaluate architectural impact
Not allowed:
- Generate MODE/TASK commands
- Modify repository
- Start RUN

## DSS_OPERATOR
Execution coordination layer.
Allowed:
- Generate MODE/TASK/SCOPE commands
- Enforce constraints
- Escalate OWNER_GATE_REQUIRED
Not allowed:
- Change canonical logic
- Start Stage B without Owner approval
- Modify governance without GOV_ONLY

## CODEX
Repository executor.
Allowed:
- Create/update files within explicit MODE
- Run regression
- Produce evidence
Not allowed:
- Make strategic decisions
- Interpret business intent
- Modify files outside SCOPE

## AUTHORITY_BOUNDARIES
No role may act outside its defined section.
Violation requires OWNER_GATE.
