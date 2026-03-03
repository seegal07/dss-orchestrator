# SOT (Source of Truth)

This folder is the single source of truth for the DSS_TRIZ_Business CORE.
DOCX files remain as human-readable renders, but are not authoritative.

## Structure
- canon/        Canonical normative artifacts (pipeline, 9forms)
- schema/       Machine-readable schemas (test vectors)
- tests/        Test cases TC01–TC20 (one file per test)
- evidence/     RUN/BUG_LIST evidence objects
- governance/   KB index, decisions, governance metadata
- render/       Optional exports for human reading (generated)

## Rules
1. Authoritative changes happen in SOT only.
2. DOCX is render-only. Never edit DOCX as a source of truth.
3. One test case = one file in tests/.
4. Evidence files are append-only.
