# S08_5_OPERATOR_OUTPUT

## Required fields
- operator_selected
- detected_conflict_types
- dominant_conflict_type
- transformed_conflict_frame
- what_changed_structurally
- structural_resolution_confirmed
- separation_illusion_test
- assisted_matrix
- search_loop
- gatecr_status
- hard_fail_message

## CONTROL TEST — search_loop flag (MUST SET TRUE/FALSE)

Purpose:
This flag is NOT about “iteration during thinking”.
It is ONLY about whether your proposed mechanism relies on a STOP/RESTART/RE-SEARCH/RETURN loop to function.
If YES → it is a risk-shift into time/idle/uncertainty and PASS is forbidden.

Set `search_loop: TRUE` if the mechanism contains ANY of the following (explicitly or implicitly):
1) stop / pause / wait / freeze / postpone until something happens
2) restart / “start over” / reset / relaunch
3) “go back”, “return to previous step”, “re-evaluate and repeat”
4) “if not found / if not working → search again / try another option / iterate until success”
5) conditional loop: “repeat the search/selection cycle until criteria met”

Set `search_loop: FALSE` only if the mechanism is one-pass and completes WITHOUT:
- waiting for a future condition,
- restarting the process,
- returning to earlier steps,
- or repeating a search/selection loop.

Quick self-check (answer YES/NO):
Q1: Does my mechanism include “if it fails → we will try again / search again / restart / go back”?
Q2: Does it rely on downtime / waiting / postponement as part of how it works?

If Q1=YES OR Q2=YES → `search_loop: TRUE`.
Otherwise → `search_loop: FALSE`.
