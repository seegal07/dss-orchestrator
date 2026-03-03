# OPERATOR_CORE_SPEC_v1.1

Status: ACTIVE SoT (architecture lock)

## 1) Purpose & product class
DSS Operator Core defines operator-driven structural transformation as a mandatory layer before decision completion.
This layer is not a decision protocol and not an idea generation layer.
Its function is to force structural reframing of contradiction X/Y before concept expansion.

## 2) Pipeline insertion
- Insert **S08.5 Operator Extraction Layer** between S08 and S09.
- Introduce **GateCR** as mandatory control gate after S08.5.
- Rule:
  - If GateCR = PASS -> S09 allowed.
  - If GateCR = SOFT_FAIL -> S09 allowed with `COMPROMISE_MODE=TRUE`.
  - If GateCR = HARD_FAIL -> S09–S14 = NOT_RUN and output canonical literal defined in routing rules.

## 3) Deterministic Operator Selection Table
Operator set:
- Separation
- Mediator
- Level Shift
- Dependency Inversion

Dominant conflict type classification and priority:
1. **B: causal dependency** -> Dependency Inversion
2. **A: time conflict** -> Separation
3. **C: interaction/mediator conflict** -> Mediator
4. **D: scale/level conflict** -> Level Shift

Priority enforcement rule:
- If multiple conflict types are detected, selected operator MUST follow: **B > A > C > D**.

## 4) Operator application definition
Counts as “structure changed” only if at least one is true:
- dependency direction in X→Y relation is changed,
- conflict locus (time/place/level) is changed,
- interaction topology changes (mediator introduction/removal/rebinding),
- system level of control/constraint is shifted.

Does NOT count as structure change:
- parameter tuning,
- delayed pain,
- redistributed harm without topology/dependency change.

## 5) Mechanism ownership rule
- System enforces operator framing and structural checks.
- Decision Owner writes mechanism inside the enforced structural frame.
- System does not generate mechanism content beyond structural framing constraints.

## 6) GateCR Validation Matrix
Mandatory checks:
1. Where conflict existed before transformation.
2. Where conflict exists after transformation.
3. Whether time/place/level of conflict changed.
4. Whether original X→Y dependency still holds in the same form.
5. Whether risk is shifted to time / third party / hidden obligation.

## 7) Separation Illusion Test
A candidate fails Separation Illusion Test if any applies:
- conflict is postponed only in time,
- conflict is displaced to external actor with no structural control change,
- hidden obligation replaces explicit contradiction,
- net contradiction remains unchanged under original boundary.

## 8) Outcomes logic
- **PASS**: structural transformation confirmed; contradiction relation changed.
- **SOFT_FAIL**: partial structural shift; contradiction weakened but not structurally removed.
- **HARD_FAIL**: no structural transformation; contradiction preserved/repackaged.

Transitions:
- PASS -> S09 allowed.
- SOFT_FAIL -> S09 allowed + `COMPROMISE_MODE=TRUE` mandatory.
- HARD_FAIL -> S09 NOT_RUN, S10 NOT_RUN, S11 NOT_RUN, S12 NOT_RUN, S13 NOT_RUN, S14 NOT_RUN with canonical hard-fail literal.

## 9) Traceability requirements
Each mechanism entering S09+ must reference:
- `operator_used`
- contradiction `X/Y`
- `what_changed_structurally` (explicit structural delta)

Traceability is mandatory for audit and gate evidence.

## 10) What we do NOT change
- No changes to DCF/SDP specs.
- No activation of 40 principles.
- No activation of 9 forms.
- No semantic changes to Gate9–Gate12.

## 11) Phase-bound qualifier
- The no-code restriction is applied to **fixation phase only**.
- Integration patch is allowed in **E12** when authorized.
