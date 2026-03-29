# HPF Canonical Repository

## Current working canonical state

This repository contains the current active HPF canon together with the active Lambda / dark-matter package, executable support artifacts, and provenance material.

The present working state uses the **no-1.4 active Lambda canon**. In this repo state:

- the corrected radial law is active: `R_H / L_vac = φ^n`
- no `/2` belongs in the active radial identity
- the active Lambda phase chain uses `1.05 -> 1.3806 -> 5.7889 -> n = 220 -> L_vac -> Λ`
- the dark-matter branch remains separate: `φ -> b -> f_coh -> α_vac -> Ω_dm`
- `n = 220` is treated as candidate-locked by the integrated entropy-phase budget, not primarily selected by `H_0`
- `k = 11`, `24`, `1.3806`, `5.7889`, `n = 220`, and `α_vac = sqrt(f_coh)` remain candidate-locked rather than uniqueness-proved

This README is meant to make the repo usable without reopening archived branches or mixing authority levels.

---

## Top authority files

### 1. Active Lambda / dark-matter canon authority
- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_no14canon.md`

This is the controlling authority file for the current Lambda / dark-matter package.

### 2. Serious-reader presentation draft
- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon.md`

This is the cleaned mathematical-reader draft intended for external serious review.

### 3. Minimal exposed mathematical core
- `HPF_Lambda_DarkMatter_attackable_core_2026-03-29_no14canon.md`

This is the stripped core designed to expose the active mathematical chain clearly and make attack points explicit.

### 4. Symbol control
- `Symbol_index_2026-03-29_rewritten_v3_no14.md`

This file should be used to prevent symbol drift.

### 5. Provenance / authority map
- `volume-3-provenance-map-updated_v2_no14.md`

This file records what is active, what is support, and what is historical.

---

## Framework canon files

These remain part of the broader HPF/QPRCA/UHET working canon and should stay in the repo:

- `volume-1-master-canon.md`
- `volume-2-microscopic-derivation.md`
- `volume-3-provenance-map-updated_v2_no14.md`
- `qprca-v0.2.8.py`

Role split:

- **Volume I** = framework / presentation canon
- **Volume II** = microscopic legality and executable-development canon
- **Volume III** = provenance, supersession, and package navigation
- **qprca-v0.2.8.py** = front active executable artifact

The Lambda / dark-matter package extends this framework canon downstream into the vacuum / cosmology sector; it does not replace the framework volumes.

---

## Recommended repo structure

### Canon/
Place the active authority documents here:

- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_no14canon.md`
- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon.md`
- `HPF_Lambda_DarkMatter_attackable_core_2026-03-29_no14canon.md`
- `Symbol_index_2026-03-29_rewritten_v3_no14.md`
- `volume-1-master-canon.md`
- `volume-2-microscopic-derivation.md`
- `volume-3-provenance-map-updated_v2_no14.md`

### Support/
Place formal supporting notes here:

- `HPF_Governor_Transfer_Theorem_Strengthening_2026-03-29.md`
- `existence-sensor-protocol-note.md`

### Support/Executable_Evidence/
Place machine-checkable artifacts here:

- `qprca-v0.2.8.py`
- `existence-sensor-report.json`
- `sigma-pressure-test.json`

### Archive/
Place superseded or transitional files here:

- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_fixed.md`
- `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass.md`
- `HPF_Lambda_DarkMatter_attackable_core_2026-03-29.md`
- `Symbol_index_2026-03-29_rewritten_v2.md`
- `volume-3-provenance-map-updated.md`
- old figure drafts and temporary image-generation outputs

---

## Current active Lambda / dark-matter chain

### Lambda branch

`1.05 -> 1.3806 -> 5.7889 -> n = 220 -> L_vac -> Λ`

Interpretation:

- `1.05` = empirical blur anchor under HPF mapping
- `1.3806` = active lower entropy / instability onset
- `5.7889` = active capacity wall
- `n = 220` = candidate-locked shell selector from integrated entropy-phase budget
- `L_vac = R_H / φ^220`
- `Λ` is downstream of the active selector chain

### Dark-matter branch

`φ -> b -> f_coh -> α_vac -> Ω_dm`

Interpretation:

- `b = ln φ / (π/2)`
- `f_coh` = coherent support fraction
- `α_vac = sqrt(f_coh)` = candidate-locked governor transfer
- `Ω_dm = 1 - α_vac`

These two branches must remain separate in the active canon.

---

## Active truth-status discipline

Every major quantity should be read under one of three labels:

### Derived / substrate-native
Examples include:
- `φ`
- `b`
- `f_coh`
- corrected no-`/2` radial law
- BCC coordination structure

### Empirically anchored under HPF mapping
Examples include:
- `1.05` as the blur anchor
- external observational values used only as anchors or consistency checks

### Candidate-locked
Examples include:
- `1.3806`
- `5.7889`
- `k = 11`
- `24`
- `n = 220`
- `α_vac = sqrt(f_coh)`

Do not slide between these categories in prose.

---

## What is explicitly retired from active canon

The following are not part of the current active Lambda / dark-matter canon:

- the old `/2` radial law
- the old mixed Lambda / DM selector chain
- primary selection of `n = 220` by matching `Λ` through `H_0`
- use of `1.4` as an active operational canon value in the Lambda chain

Historical files may still contain those elements. Treat them as archived unless rewritten into the no-1.4 authority set.

---

## Reading order

For a full read:

1. `volume-1-master-canon.md`
2. `volume-2-microscopic-derivation.md`
3. `volume-3-provenance-map-updated_v2_no14.md`
4. `Symbol_index_2026-03-29_rewritten_v3_no14.md`
5. `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_no14canon.md`
6. `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon.md`
7. `HPF_Lambda_DarkMatter_attackable_core_2026-03-29_no14canon.md`
8. support notes and executable evidence as needed

For a quick serious-reader handoff:

1. `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon.md`
2. `HPF_Lambda_DarkMatter_attackable_core_2026-03-29_no14canon.md`
3. `Symbol_index_2026-03-29_rewritten_v3_no14.md`

For internal canon control:

1. `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_no14canon.md`
2. `volume-3-provenance-map-updated_v2_no14.md`
3. `Symbol_index_2026-03-29_rewritten_v3_no14.md`

---

## Practical usage rule

If there is ever a conflict:

1. the **master locked no14** file wins
2. then the **final reader pass no14**
3. then the **attackable core no14**
4. then the **symbol index / provenance map**
5. then support notes and executable evidence
6. archived files lose unless explicitly re-promoted

---

## Current repo purpose

This repository is not just a paper dump. Its working purpose is to preserve:

- the live HPF regulatory framework
- the microscopic legality / executable line
- the active vacuum-sector Lambda / dark-matter branch
- the authority structure needed to prevent canon drift
- the support and executable artifacts needed for stress testing and reproducibility

---

## Current status in one paragraph

The repo currently presents HPF as a regulatory framework with MDEA routing and QPRCA substrate authority, together with an active candidate-locked vacuum-sector package in which the corrected no-`/2` radial law, the active entropy-phase selector, and the separated dark-matter governor-transfer branch are all preserved under explicit truth-status discipline. The current working repo state is the no-1.4 Lambda canon, with support and executable artifacts retained but demoted below primary canon authority.
