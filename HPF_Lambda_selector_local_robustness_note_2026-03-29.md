# HPF Lambda Selector Local Robustness Note (2026-03-29)

---

# Appendix B: Local robustness of the active shell selector

This appendix records the current local perturbation results for the active shell selector
\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},\qquad
n_{\rm sel}=\operatorname{round}\!\left[\frac{24}{\ln\phi}\int_{S_{\rm lo}}^{S_{\rm hi}}(1-\zeta(S))\,dS\right],
\]
with active baseline
\[
S_{\rm lo}=1.3806,\qquad S_{\rm hi}=5.7889,\qquad k=11,\qquad \frac{24}{\ln\phi}.
\]

The purpose of this appendix is narrow. It does **not** prove uniqueness. It records that the active selector occupies a genuine connected local robustness region in the scanned neighborhood and that its anisotropy is now explicit.

## B.1 Analytic control form

The selector integral may be written in closed form as
\[
I(S_{\rm lo},S_{\rm hi},k)
=
\int_{S_{\rm lo}}^{S_{\rm hi}}(1-\zeta(S))\,dS
=
\left[S+\frac{1}{k}\ln\!\bigl(1+e^{-k(S-1.05)}\bigr)\right]_{S_{\rm lo}}^{S_{\rm hi}}.
\]
Hence
\[
I
=
(S_{\rm hi}-S_{\rm lo})
+\frac{1}{k}\ln\!\frac{1+e^{-k(S_{\rm hi}-1.05)}}{1+e^{-k(S_{\rm lo}-1.05)}}.
\]
This makes the observed mechanism transparent: the dominant contribution is the interval budget \((S_{\rm hi}-S_{\rm lo})\), while the \(k\)-dependent term is a small tail correction once the lower bound already lies well to the right of the midpoint anchor at \(1.05\).

## B.2 Baseline evaluation

The baseline numerical evaluation gives

- raw selector value: \(X\approx 219.7422\)
- rounded shell count: \(n_{\rm sel}=220\)
- half-integer margin: \(\approx 0.2422\)

So the baseline is not sitting on a rounding cliff. It lies safely inside the \(220\) bucket.

## B.3 Phase A: one-parameter perturbations

Local one-parameter scans show:

- **Lower bound \(S_{\rm lo}\)**: moderately robust local interval preserving \(220\), roughly centered on the active baseline and spanning about \(\Delta S\sim 0.02\) in the tested neighborhood.
- **Upper bound \(S_{\rm hi}\)**: narrow but clean interval-budget tolerance, also with a preservation width of about \(\Delta S\sim 0.02\) in the tested neighborhood.
- **Gate steepness \(k\)**: highly robust across the tested scan \(k\in[10,13]\); all sampled values preserved \(n_{\rm sel}=220\).
- **Shell-conversion prefactor**: structurally rigid; small perturbations leave the \(220\) bucket much sooner than comparable perturbations in \(k\) or in either phase bound.

The correct summary language is therefore:

> The selector appears locally robust in gate steepness, moderately robust in phase-bound placement, and rigid in the shell-conversion prefactor.

## B.4 Phase B: paired scans

The decisive two-dimensional result is the \((S_{\rm lo},S_{\rm hi})\) scan.

### \((S_{\rm lo},S_{\rm hi})\) plane

In the scanned local box, the \(220\)-preserving region is:

- connected
- free of scattered islands
- shaped as a **tilted band**, not a knife-edge ridge
- centered on a line of slope \(\approx +1\)

This means that if \(S_{\rm lo}\) is shifted upward, the selector may remain in the same integer bucket provided \(S_{\rm hi}\) is shifted upward by nearly the same amount. The mechanism is therefore an interval-budget control law rather than a gate-shape tuning artifact.

### \((S_{\rm lo},k)\) and \((S_{\rm hi},k)\) planes

The mixed scans with \(k\) produce broad rectangular strips that span the full tested \(k\)-range. This confirms that the gate steepness is spectator-like over the scanned neighborhood and is not a load-bearing fine-tuning knob in the active selector.

## B.5 Phase C: full local four-parameter cube

A full local scan over \((S_{\rm lo},S_{\rm hi},k,\epsilon)\) in the tested neighborhood yields:

- total sampled grid points: **47,628**
- \(n_{\rm sel}=220\) hits: **2,415**
- hit fraction: **\(\approx 5.07\%\)**
- connected components: **1**
- internal voids / holes: **none detected**
- half-margin inside region: from about **0.001** at the boundary to about **0.499** in the core
- baseline neighborhood half-margin: **\(\approx 0.2422\)**

The correct geometric description is:

> The selector occupies a genuine connected local robustness volume in \((S_{\rm lo},S_{\rm hi},k,\epsilon)\)-space. Its robustness is anisotropic: broad in gate steepness, moderate along the phase-budget interval directions, and narrow in the shell-conversion prefactor direction.

A good visual analogy is a slanted slab or thick sheet: diagonally oriented in the \((S_{\rm lo},S_{\rm hi})\) plane, fully extended across the scanned \(k\)-range, and relatively thin in the prefactor direction.

## B.6 Status note

These perturbation results strengthen the active selector in a specific and limited sense.

They support the claim that:

1. the active shell selector is **not** a narrow \(k=11\) fine-tuning artifact,
2. the dominant mechanism is the regulated interval budget together with the shell-conversion factor, and
3. the active baseline lies in a genuine connected local basin rather than on an isolated floating-point knife-edge.

They do **not** yet prove:

- global uniqueness of the selector,
- substrate-class universality beyond the scanned local neighborhood,
- or independence from the sector-conversion prefactor.

The correct strength statement is therefore:

> Within the scanned local neighborhood, the selector is dominated by the macroscopic interval budget and is largely insensitive to gate steepness, while the shell-conversion prefactor remains the stiffest direction.
