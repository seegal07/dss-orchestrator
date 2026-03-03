# GATEPFL_SUMMARY_EXTRACTOR_CONTRACT_v0.1
Status: ACTIVE (tooling contract)
Scope: Stage A summary tooling only

## Truth-source
- Step2 truth-source for GatePFL extraction is `gate_log.json`.

## Parser rule
- Regex parsing is forbidden.
- JSON parsing only.

## Required behavior
- Tool must read `gate_log.json`, find `gate_id=="GatePFL"`, and write:
  - `GatePFL_result`
  - `GatePFL_reason`
  into `SUMMARY.json` per variant.

## Guardrail
- If `GatePFL` exists in `gate_log.json` and extracted `result` or `reason` is `null`,
  tool must fail loudly (non-zero exit / explicit error).

## Usage
```bash
python3 /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/harness/utils/gatepfl_summary_extractor_v0_1.py \
  --pack-path /Users/oleksiichaika/Desktop/DSS_REPOSIT/24_JAN/DSS_SOLVER/experiments/<PACK_DIR>
```

## Anti-pattern
- Do not inline ad-hoc parsers for GatePFL extraction in run commands.
- Use this versioned tool to generate/patch `SUMMARY.json` deterministically.
