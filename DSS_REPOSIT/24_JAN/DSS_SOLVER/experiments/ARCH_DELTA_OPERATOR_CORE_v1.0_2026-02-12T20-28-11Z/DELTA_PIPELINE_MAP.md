# DELTA_PIPELINE_MAP

## Current pipeline (as-is)
S08 -> S09 -> S10 -> S11 -> S12

## Proposed pipeline (architecture delta only)
S08 -> **S08.5 Operator Extraction** -> **GateCR** -> S09 -> S10 -> S11 -> S12

## Delta statement
- Added one structural layer S08.5.
- Added one mandatory control gate GateCR before S09.
- No changes to definitions of S09–S12.
