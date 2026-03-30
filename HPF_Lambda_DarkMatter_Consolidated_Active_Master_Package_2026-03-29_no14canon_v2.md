# HPF Lambda / Dark Matter Consolidated Active Master Package

**Date:** 2026-03-29  
**Package state:** active no-1.4 canon, v2  
**Purpose:** single handoff entry for the current working canonical repo.

## Primary authority

- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_no14canon.md`

## Reader-facing technical draft

- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon_with_selector_robustness.md`

## Minimal exposed core

- `HPF_Lambda_DarkMatter_attackable_core_2026-03-29_no14canon.md`

## Anti-drift support

- `Symbol_index_2026-03-29_rewritten_v3_no14.md`
- `volume-3-provenance-map-updated_v2_no14.md`

## Support notes

- `HPF_Governor_Transfer_Theorem_Strengthening_2026-03-29.md`
- `HPF_Lambda_selector_local_robustness_note_2026-03-29.md`
- `existence-sensor-protocol-note.md`

## Executable evidence

- `qprca-v0.2.8.py`
- `existence-sensor-report.json`
- `sigma-pressure-test.json`

## Current active branch summary

### Lambda branch

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
\]

with the active selector
\[
\operatorname{round}\!\left[\frac{24}{\ln\phi}\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS\right] \approx 220,
\qquad
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},\ k=11.
\]

### Dark matter branch

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}
\]

kept fully separate from the Lambda selector.

## Current robustness status

The active package now includes a local robustness note for the shell selector. Current status:

- broad tolerance in gate steepness \(k\)
- moderate tolerance in phase-bound placement
- narrow / rigid shell-conversion direction
- connected local 4-parameter robustness region detected
- no uniqueness or universality theorem claimed from this result alone

## Repository guidance

Use the master locked file for canon authority. Use the updated final reader pass for serious technical reading. Use the attackable core when you want the smallest exposed mathematical target. Use the support notes and executable evidence as subordinate justification, not as top-level canon.
