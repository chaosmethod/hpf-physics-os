# HPF v0.2.8 Existence-Sensor Protocol Note (2026-03-20)

## Scope

This note defines the theorem-safe executable protocol for testing whether the microscopic legality aggregate can function as a **non-circular existence sensor** on the current finite reversible rule family.

The immediate executable target is:

> On the sanitized reversible subregistry, does \(F_{\min}(\psi_{\rm in}) < 1\) track the existence of at least one actually available legal reversible continuation?

This is **not** a universal sufficiency theorem. It is an executable test on the present finite reversible family.

## Pre-run locks

Before the full sweep, the following are fixed:

1. **Sanitized reversible subregistry**
   - Extracted dynamically from the v0.2.7 file's own bijection audit.
   - No legacy non-bijective rules are included.

2. **Candidate minimal Sigma-equivalence**
   - Continuation signature:
     \[
     \Sigma=(T_{\rm out}, C_{\rm mode}, R_{\rm eng})
     \]
   - `T_out`: categorical transport outcome
   - `C_mode`: categorical collision / occupancy handling mode
   - `R_eng`: categorical non-transport resource engagement

3. **Adversarial Sigma pressure test**
   - A small edge-case inspection is run before the full sweep.
   - Sigma may be revised after this pre-lock adversarial check and before the main run.

4. **Threshold asymmetry**
   - False positives are the critical failure mode.
   - A false positive means \(F_{\min}<1\) while no legal continuation exists, so the putative existence sensor overstates legality in the exact direction that would mislead the sufficiency program.

## Pass / fail interpretation

### Strong pass
- Zero false positives
- Zero false negatives
on the tested sanitized reversible family.

### Conditional pass
- Zero false positives
- Low false negatives with explainable structure tied to registry poverty or Sigma coarseness.

### Failure
- Any persistent false positives
- Or substantial false negatives that cannot be localized cleanly.

## Scope limitations

A clean result here does **not** prove:

- strongest-form operator richness
- universal microscopic legality sufficiency
- lower-wall constitutive derivation
- external empirical validation
- that this Sigma partition is uniquely correct or best

A clean result would support the Selection-Lemma program **for this Sigma, this aggregation law, and this sanitized finite reversible registry**.

## Current implementation choices

This v0.2.8 wrapper:
- loads the uploaded v0.2.7 executable directly
- dynamically extracts the reversible family from the file's own bijection check
- computes continuation classes under the minimal Sigma map
- separates:
  - `exists_legal_continuation`
  - `F_min`
- emits both a Sigma pressure-test JSON and an existence-sensor report JSON
