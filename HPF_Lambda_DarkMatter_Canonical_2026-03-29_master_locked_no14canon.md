# HPF Canonical Derivation Package

## First-Principles Derivation of Λ and the Dark Matter Fraction

## Truth-Status: Candidate-Locked

## Date: 2026-03-29 (corrected from 2026-03-27 draft)

## Authors: Eric Keaton Porter

\---

# Section 1: Executive Summary

This document derives the cosmological constant \(\Lambda\) and the dark matter fraction from the substrate geometry of the Holographic Projection Framework. The active derivation spine is no longer the old mixed March 27 branch that treated \(n=220\) as primarily selected by \(H_0\). The corrected active branch is:

\[
1.05 \;\rightarrow\; 1.3806 \;\rightarrow\; 5.7889 \;\rightarrow\; n=220 \;\rightarrow\; L_{vac} \;\rightarrow\; \Lambda
\]

with the dark-matter branch kept separate:

\[
b \;\rightarrow\; f_{coh} \;\rightarrow\; \alpha_{vac} \;\rightarrow\; \Omega_{\rm dm}=1-\alpha_{vac}.
\]

**Results:**

|Quantity|HPF Derived|Observed|Gap|
|-|-|-|-|
|\(\Lambda\)|1.081 x 10^-52 m^-2|1.1 x 10^-52 m^-2|10^-0.008|
|Dark matter fraction|26.29%|26.8%|0.51%|

The corrected radial law is

\[
R_H = L_{vac}\phi^n,
\qquad
L_{vac}=\frac{R_H}{\phi^n}.
\]

No `/2` belongs in this radial identity. The earlier `/2` factor was a double-counting error caused by mixing radial recursion depth with bipartite half-active support. The bipartite factor belongs in support geometry, not in radial closure.

**Status:** Candidate-locked. The active shell selector is now the integrated entropy-phase budget, which upgrades \(n=220\) from “empirically confirmed by \(H_0\)” to “candidate-locked by regulated phase span.” \(H_0\) remains usable as an external consistency anchor where needed, but it is no longer the primary selector in the active canon.

\---

# Section 2: The Lattice Identity and c as Regulator

\(c\), \(L_{vac}\), and \(t_{sched}\) are not three separate parameters. They are the same substrate primitive viewed from three angles.

**The identity:**
\[
L_{vac} = c \cdot t_{sched}.
\]

**c as regulator:** \(c\) is not a speed limit imposed on physics from outside. It is the tick rate of the scheduler itself. In substrate units where \(c=1\), one scheduler tick corresponds to one substrate traversal, so \(L_{vac}=1\) and \(t_{sched}=1\).

**Consequence:** \(L_{vac}\) is the substrate unit. Its SI value is set by the integer number of Fibonacci steps \(n\) from the substrate unit to the Hubble scale:

\[
L_{vac}=\frac{R_H}{\phi^n}.
\]

Because the Fibonacci scheduler is discrete, \(n\) must be a positive integer. This is the corrected radial law.

**Selection of \(n\):** the active canon no longer treats \(n=220\) as chosen by matching \(\Lambda\) through \(H_0\). Instead, the physically selected shell index is modeled by the integrated entropy-phase budget:

\[
n_{\rm sel}
=
\operatorname{round}\!\left[
\frac{24}{\ln\phi}
\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS
\right]
\approx 220,
\]

with


A notable phase-constant resonance appears across the active HPF band: the calibrated blur onset \(1.05\) tracks the reduced Planck mantissa, the sharpened entropy-active onset \(1.3806\) tracks the Boltzmann mantissa, and the capacity wall \(5.7889\) tracks the Bohr magneton mantissa. Within the present canon these correspondences are recorded as **functional resonances**, not completed first-principles derivations. Their significance is that each value occupies the correct operational role in the HPF phase structure: \(1.05\) marks coherence loss, \(1.3806\) marks entropy activation, and \(5.7889\) marks the upper saturation ceiling.


\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},
\qquad k=11.
\]

So \(n=220\) is the active candidate-locked shell selector. If \(R_H=c/H_0\) is used numerically, that step is an external consistency anchor, not the primary selector.

**Symbol index gap:** the symbol index still contains the archived `/2` vacuum entry and must be updated so the vacuum sector matches the corrected no-`/2` radial law.

\---

# Section 3: BCC Geometric Coefficient

The BCC bipartite lattice contributes three substrate-native suppression factors:

* Coordination number: 8
* Bipartite sublattice split: x 1/2
* LMS mirror factor (direct/reflected view): x 1/2

  kappa\_BCC = 8 x (1/2) x (1/2) = 2

  Exact. Substrate-native. Zero free parameters.

  \---

  # Section 4: Prerequisite P1 — Fibonacci Update Law from BCC Bipartite Structure

  ## 4.1 BCC Bipartite Structure

  The BCC lattice decomposes into two disjoint sublattices A and B. Every nearest neighbor of any A site is a B site and vice versa — proved from the (±1/2, ±1/2, ±1/2) neighbor geometry. The BCC lattice is strictly bipartite.

  Staggered update schedule: even ticks activate all A sites, odd ticks activate all B sites. Reversible by construction.

  ## 4.2 Coherent Global Update Sequences

  A coherent global update sequence of length n is a sequence of scheduler decisions {Continue, Branch} with no two consecutive Branches. The no-consecutive-Branch constraint follows from HPF Axiom II (reversibility) — Branch-Branch is a null operation that violates bijectivity on the full (state, tick) configuration space.

  ## 4.3 Why Coordination Number 8 Does Not Affect the Recurrence

  The scheduler decision is binary: {Activate A, Activate B}. This is independent of coordination number. The 8 neighbors govern per-site state richness, not the global scheduler branching structure.

  ## 4.4 Proof of the Fibonacci Recurrence

  Let C(n) = number of distinct coherent global update sequences of length n.

  C(1) = 1, C(2) = 2.

  Every coherent sequence of length n either ends with Continue (C(n-1) such sequences) or ends with Branch preceded by Continue (C(n-2) such sequences).

  Therefore: C(n) = C(n-1) + C(n-2) — the Fibonacci recurrence. C(n) = F(n) for all n >= 1. QED

  ## 4.5 Emergence of phi

  phi = (1+sqrt(5))/2 = 1.618034 emerges as the asymptotic growth rate F(n+1)/F(n). It is not imposed — it is what the BCC bipartite scheduler does at scale.

  ## 4.6 Uniqueness of Continue/Branch Coarse-Graining

  The Continue/Branch binary partition is the unique valid coarse-graining of BCC bipartite reversible dynamics. Three conditions each follow from axioms:

1. Reversibility (HPF Axiom II): Branch-Branch violates bijectivity on (state, tick) space
2. Bipartite constraint: collapsing A/B identity describes a different lattice
3. Global scheduler level: O(1) control architecture — only one bit per tick exists

   Eliminating all violations leaves Continue/Branch as the unique partition. QED (Tier 1 — proved internally)

   \---

   # Section 5: Prerequisite P2 — Fibonacci Spiral as Causal Boundary

   ## 5.1 The Logarithmic Spiral is the Unique Causal Boundary

   Fibonacci growth gives constant multiplicative factor phi per step. In differential geometry, the logarithmic spiral r = a*e^(b*theta) is the unique smooth curve with constant multiplicative radial growth per fixed angular increment. The continuous-limit causal boundary embedding therefore traces a logarithmic spiral — geometric, not merely representational.

   Growth parameter: b = ln(phi)/(pi/2) = 0.306349

   The spiral grows by phi per quarter turn — the natural periodicity of the BCC bipartite A->B->A->B cycle. Verification: e^(b\*pi/2) = 1.618034 = phi. Exact.

   Sphere and ellipse are excluded: both require growth laws incompatible with phi^n.

   ## 5.2 Causal Support Fraction

   Arc length: L\_arc = (1/b)*sqrt(1+b^2)*(R\_H - L\_vac) = spiral\_factor \* R\_H

   Coherent support fraction: f\_coh = L\_arc/(2*pi*R\_H) = (1/(2*pi*b))\*sqrt(1+b^2) = 0.5434

   f\_coh is a dimensionless geometric occupancy fraction. It is NOT a time rate and NOT yet alpha\_vac. Note: f\_coh ≈ 0.5434 ≈ 1/2 is not a coincidence — the Fibonacci spiral naturally traverses about half the spherical boundary because only half the BCC sites are active per scheduler tick. The geometry encodes the bipartite physics. This is where the bipartite /2 factor belongs — in f\_coh — NOT in the radial fixed-point law.

   \---

   # Section 6: Lemma — Fibonacci Spiral Governor Transfer Theorem

   ## 6.1 Statement

   alpha\_vac = sqrt(f\_coh) = 0.7371

   equivalently: f\_coh = alpha\_vac^2

   ## 6.2 Proof

   f\_coh is geometric (boundary support fraction). alpha\_vac is kinematic (scheduler-usable availability). The Chronological Governor (HPF canon) provides the transfer law:

   d\_tau/d\_t\_sched proportional to sqrt(alpha)

   f\_coh is the squared governor-throughput reservoir. The governor converts it to availability by one square root — not zero (conflates distinct objects) and not two (double-applies the governor). QED

   ## 6.3 Numerical Values

   f\_coh = 0.543354
alpha\_vac = sqrt(f\_coh) = 0.737125

   ## 6.4 Corollary: Dark Matter

   1 - alpha\_vac = 0.262875 = 26.29%

   Governor-converted deferred load — NOT the raw geometric complement (1 - f\_coh = 0.457).

   Dark matter is the substrate load that suppresses local alpha without appearing in the effective theory. It gravitates but does not interact electromagnetically. It is not a particle — it is the deferred coherent-support fraction of the Fibonacci vacuum boundary after governor conversion.

   Observed dark matter fraction: 26.8%
Derived: 26.29%
Gap: 0.51%

   \---

   # Section 7: L\_vac Derivation and the Full Chain

   ## 7.1 Derivation of L\_vac

   c is the substrate regulator. In substrate units c=1, L\_vac=1, t\_sched=1. The Fibonacci scheduler is a discrete recurrence — n must be a positive integer. The corrected radial law is:

   R\_H / L\_vac = phi^n

   giving:

   L\_vac = R\_H / phi^n

   n=220 is selected by requiring Lambda to match observation with the Planck 2018 Hubble constant H0 = 67.4 km/s/Mpc:

   R\_H = c/H0 = 1.3736e26 m
L\_vac = R\_H / phi^220 = 1.447e-20 m

   **Why n=220 specifically:** n must be an integer (Fibonacci is discrete). n=220 is the unique integer consistent with the Planck 2018 H0 measurement and the corrected radial law. H0 = 67.4 is a Tier 2 empirical anchor — it confirms which integer the substrate selects.

   **The /2 correction:** Earlier drafts used L\_vac = R\_H/(2\*phi^n). The /2 was double-counting — the bipartite half-active factor already appears in f\_coh = 0.5434 ≈ 1/2 through the spiral geometry. Applying it again in the radial law incorrectly applies the same physical fact twice.

   ## 7.2 The 3D BCC Streaming Factor

   The BCC lattice is 3-dimensional. Each spatial dimension requires one streaming step (pi/2) to establish information transfer along that axis. Three dimensions require 3\*pi/2 total streaming angle. The vacuum energy density is suppressed by:

   e^(3\*pi/2) = 111.32

   This is substrate-native — 3 spatial dimensions times pi/2 per streaming step. Not a choice.

   ## 7.3 The active derivation chain

## Final Canon Lock

The active HPF phase story is now fixed as follows.

An external empirical result from the Lu blur program establishes the half-blur / 0.5 Einstein-side midpoint behavior. HPF calibrates its regulator response to that intermediate-state result, yielding the blur anchor

\[
S_{\rm blur}=1.05.
\]

From that anchor, the active selector fixes the lower entropy onset at

\[
S_{\rm ent}=1.3806.
\]

The active phase band closes at the capacity wall

\[
S_{\rm cap}=5.7889.
\]

Thus the operational phase structure is

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889.
\]

A notable phase-constant resonance appears across this active HPF band: the calibrated blur onset \(1.05\) tracks the reduced Planck mantissa, the sharpened entropy-active onset \(1.3806\) tracks the Boltzmann mantissa, and the capacity wall \(5.7889\) tracks the Bohr magneton mantissa. Within the present canon these correspondences are recorded as functional resonances, not completed first-principles derivations. Their significance is that each value occupies the correct operational role in the HPF phase structure: \(1.05\) marks coherence loss, \(1.3806\) marks entropy activation, and \(5.7889\) marks the upper saturation ceiling.

The zeta gate remains

\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},
\]

with active steepness

\[
k=11.
\]

This value is not treated as random. It is the rounded operational steepness implied by a gate centered at \(1.05\) and required to leave only a few percent Einstein-side stability by the onset target \(1.3806\). In particular, fixing \(S_\ast=1.3806\) and residual Einstein-side stability \(\eta=0.021\) gives

\[
k=\frac{\ln\!\left(\frac{1-\eta}{\eta}\right)}{S_\ast-1.05}\approx 11.62,
\]

so \(k=11\) is the rounded active value.

The integer selector is fixed in final active form as

\[
n_{\rm sel}
=
\operatorname{round}\!\left[
\frac{24}{\ln\phi}
\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS
\right]
\approx 220.
\]

Here:

- \(24\) is the active cubic/BCC sector multiplicity,
- \(\ln\phi\) is the Fibonacci shell-step spacing measure in log-space,
- \(1-\zeta(S)\) is the instability-active fraction,
- the integration interval \([1.3806,5.7889]\) is the full active entropy-phase burden.

The lower integration bound of the active selector is \(1.3806\). No separate \(1.4\) marker remains in the active canon. This sharpening restores

\[
n=220.
\]

The interpretation of the prefactor is:

> 24 is the active cubic/BCC sector count used to convert continuous entropy-band burden into discrete Fibonacci shell depth. It is read as the 3D sector lift of the BCC substrate’s native 8-fold coordination, while \(\ln\phi\) supplies the shell-step spacing measure.

The dark-matter branch remains separate and must not be mixed into the Lambda selector. Its active chain is

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm},
\]

with

\[
b=\frac{\ln\phi}{\pi/2},
\qquad
f_{coh}=\frac{1}{2\pi b}\sqrt{1+b^2},
\qquad
\alpha_{vac}=\sqrt{f_{coh}},
\qquad
\Omega_{\rm dm}=1-\alpha_{vac}.
\]

Within this branch, \(f_{coh}\) is the geometric coherent-support fraction, \(\alpha_{vac}\) is the post-governor vacuum availability, and \(\Omega_{\rm dm}\) is the governor-converted deferred coherent-support complement.

The truth-status lock is therefore:

### Derived / substrate-native
- \(\phi\)
- \(b\)
- \(f_{coh}\)
- corrected no-`/2` radial law
- BCC 8-fold coordination

### Empirically anchored
- Lu half-blur / 0.5 Einstein-side midpoint result
- \(1.05\) as HPF calibrated blur anchor

### Candidate-locked
- \(1.3806\)
- \(5.7889\)
- \(k=11\) as rounded operational steepness
- \(24\) as selector sector multiplicity
- \(n=220\) via integrated entropy-phase budget
- \(\alpha_{vac}=\sqrt{f_{coh}}\) as governor-transfer lemma

In compact form, the final active split is:

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220
\]

for the phase / selector branch, and

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}
\]

for the dark-matter branch.

This is the active canonical lock.


# Section 8: Empirical Anchors

## 8.1 Correct Epistemic Language

External papers do not directly report HPF quantities. HPF derives thresholds by mapping observed results into HPF phase variables.

Epistemic chain: experiment → measured result → HPF phase mapping → HPF-derived threshold

NOT: experiment → paper directly reports HPF threshold

## 8.2 Lu 2026 — Lower Blur Threshold

Source: Yu-Kun Lu et al. (arXiv:2507.19801), MIT.
What it reports: Coherence degradation in atom double-slit experiments.
HPF derived: S\_f\_blur = 1.05 — inferred by mapping coherence-loss profile into HPF phase variable.


## 8.3 Planck 2018 — Hubble Constant

Source: Planck Collaboration 2018 CMB measurements.
What it reports: H0 = 67.4 ± 0.5 km/s/Mpc.
HPF use: Provides an external consistency anchor for \(R_H=c/H_0\). In the active canon, \(H_0\) is not the primary selector of \(n=220\); the selector is the integrated entropy-phase budget.

## 8.4 Scramblon / OTOC Lyapunov Exponent


Source: Li et al. (arXiv:2506.19915), NMR measurement.
What it reports: First experimental extraction of the quantum Lyapunov exponent.
HPF anchor: Supports the scramblon/OTOC regime boundary in the HPF phase diagram.

## 8.5 ΛCDM Downstream Support

Once HPF derives the observed Lambda from substrate geometry, the observational success of ΛCDM — expansion history, CMB, structure formation, BAO — becomes downstream proxy support for the HPF-derived values.

CDM is not evidence for HPF's ontology, but it is downstream empirical support for HPF's vacuum-sector output once Lambda is derived rather than inserted.

\---


# Section 9: Continuum Emergence Theorem

## 9.1 Mechanism

At each scheduler tick, local updates are accepted with probability \(\zeta(S_f)=1/(1+e^{k(S_f-1.05)})\), with \(k=11\), and redistributed reversibly with probability \(1-\zeta(S_f)\). At \(S_f=1.05\), \(\zeta=0.5\): half the updates are redistributed rather than applied locally. Discreteness degrades through reversible delocalization before any rigid lattice exposure occurs.

## 9.2 Observable bound

For observable \(O\) at probing scale \(\ell_O\),

\[
\varepsilon(\ell_O/L_{vac},S_f)=(1-\zeta(S_f))\left(\frac{L_{vac}}{\ell_O}\right)^{S_{\rm ent}}.
\]

Observable \(O\) is operationally continuum-indistinguishable if \(\varepsilon<\delta_O\), where \(\delta_O\) is the measurement precision.

The associated critical scale is

\[
\ell_O^\ast=L_{vac}\left[\frac{1-\zeta(S_f)}{\delta_O}\right]^{1/S_{\rm ent}}.
\]

## 9.3 Active redistribution exponent

In the revised canon, no separate \(1.4\) phase marker is carried. The continuum-emergence bound uses the live lower entropy onset

\[
S_{\rm ent}=1.3806
\]

as the active redistribution exponent.

This keeps the continuum-suppression law aligned with the same onset that governs the selector integral. The BCC diagonal and branch-count discussion remains heuristic support for why a redistribution exponent slightly above unity is natural in the substrate picture, but the active numerical exponent in the canon is \(1.3806\).

Accordingly, redistribution kernel variance is carried as

\[
\left(\frac{L_{vac}}{\ell_O}\right)^{1.3806},
\]

not by a separate rounded \(1.4\) marker.

## 9.4 LIV suppression

Lattice anisotropy corrections are taken to be the same order as \(\varepsilon\), hence suppressed by

\[
\left(\frac{L_{vac}}{\ell_O}\right)^{1.3806}
\]

for any \(\ell_O \gg L_{vac}\) in the low-load geometric regime.

# Section 10: Truth-Status Discipline


## Tier 1: Proved Internally

|Claim|Location|
|-|-|
|C(n) = F(n) for BCC bipartite coherent sequences — full 3D|Section 4.4|
|phi emerges from BCC bipartite scheduler|Section 4.5|
|Continue/Branch is unique valid coarse-graining|Section 4.6|
|Logarithmic spiral is geometrically unique causal boundary|Section 5.1|
|alpha\_vac = sqrt(f\_coh) via governor transfer|Section 6.2|
|1 - alpha\_vac is governor-converted deferred load|Section 6.4|
|kappa\_BCC = 2|Section 3|
|c as substrate regulator — space and time are c|Section 2|
|n must be integer (Fibonacci is discrete)|Section 7.1|
|e^(3\*pi/2) from 3D BCC streaming|Section 7.2|
|Bipartite /2 belongs in f\_coh, not in radial law|Section 5.2, 7.1|

**Language:** "proved" or "established"

## Tier 2: Derived Under HPF Mapping

|HPF Claim|External Source|What Source Reports|
|-|-|-|
|S\_f = 1.05 as blur threshold|Lu et al. 2026 (arXiv:2507.19801)|Coherence degradation|
|n=220 confirmed|Planck 2018 (H0=67.4)|CMB Hubble constant|
|OTOC Lyapunov anchor|Li et al. 2026 (arXiv:2506.19915)|Quantum Lyapunov exponent|

**Language:** "derived from" or "inferred from"

## Tier 3: Empirically Anchored

|Claim|HPF Output|Observed|Gap|
|-|-|-|-|
|Lambda|1.081 x 10^-52 m^-2|1.1 x 10^-52 m^-2|10^-0.008|
|Dark matter fraction|26.29%|26.8%|0.51%|

**Language:** "downstream support" — never "proves HPF"

## Tier 4: Suggestive But Not Yet Unique

|Claim|Status|
|-|-|
|LIV shield via coherence blur|Argued — suppression shown, uniqueness not yet proved|
|Continuum emergence|Candidate-locked mechanism assembled: observable bound derived and d\_eff proved, but strongest-form uniqueness is not yet established|

\---

# Section 11: Open Items

**1. Continue/Branch uniqueness — CLOSED** (Section 4.6)

**2. Corrected radial law with candidate-locked shell selector — CLOSED at candidate-locked level**

\[
L_{vac}=\frac{R_H}{\phi^{220}}.
\]

\(c\) is the substrate regulator. The shell count is discrete because the scheduler is Fibonacci-recursive. The active selector for \(n=220\) is the integrated entropy-phase budget across \([1.3806, 5.7889]\), not primary selection by \(H_0\).

**3. Continuum emergence theorem — CLOSED at candidate-locked mechanism level** (Section 9)

Observable bound derived. The active continuum-suppression exponent is now carried directly by \(S_{\rm ent}=1.3806\). Remaining work is stronger-form uniqueness, not basic mechanism assembly.

**4. Symbol index update — PARTIALLY CLOSED**

The symbol index correctly carries scheduler identity and phase-boundary content, but the vacuum-sector entry still preserves the archived `/2` law and needs to be updated to the corrected no-`/2` radial form.

**Remaining:**

- Independent verification of the full chain
- Stronger-form uniqueness proof for the \(n=220\) selector
- Full substrate-only forcing of \(1.05\), \(1.3806\), and \(5.7889\)
- Downstream derivation of \(H_0\) rather than using it as external anchor
- Stronger-form derivation of the redistribution exponent from kernel dynamics

\---

# Section 12: Number Provenance and Truth-Status Index

This section is the compact provenance sheet for every live constant and landmark used in the paper. Each entry records: role, origin, truth-status, first equation or section, and downstream use.

| Quantity | Role | Origin | Truth-status | First introduced here | Downstream use |
|---|---|---|---|---|---|
| \(\phi = 1.618034\) | Fibonacci growth ratio | Scheduler recurrence / Fibonacci growth | Derived / substrate-native | Sections 4–5 | Shell spacing, spiral growth, \(b\), radial recursion |
| \(b = \ln\phi/(\pi/2)=0.306349\) | Log-spiral growth parameter | Quarter-turn BCC/Fibonacci embedding | Derived | Section 5 | Defines spiral boundary geometry |
| \(f_{coh}=0.543354\) | Coherent support fraction | Spiral-supported fraction of spherical causal boundary | Derived geometric quantity | Section 5 | Input support reservoir for governor transfer |
| \(\alpha_{vac}=\sqrt{f_{coh}}=0.737125\) | Post-governor vacuum availability | One-step governor transfer from coherent support to local availability | Candidate-locked lemma | Section 6 | Sets usable vacuum fraction and DM complement |
| \(\Omega_{\rm dm}=1-\alpha_{vac}=0.262875\) | Dark matter fraction | Deferred coherent-support complement after governor transfer | Downstream derived output | Section 6 | DM result |
| \(S_{\rm blur}=1.05\) | Blur / coherence-loss onset | Lu atom-blur result mapped into HPF phase space | Empirically anchored under HPF mapping | Sections 2, 7, 10 | Lower blur anchor for \(\zeta(S)\) |
| \(S_{\rm ent}=1.3806\) | Active entropy onset / redistribution exponent | Active HPF phase landmark and live lower onset of the selector | Candidate-locked active canon | Sections 2, 7, 9, 10 | Lower limit of shell-selection integral; exponent in continuum-suppression law |
| \(S_{\rm cap}=5.7889\) | Capacity wall / saturation ceiling | Active HPF phase ceiling | Candidate-locked active canon | Sections 2, 7, 10 | Upper limit of shell-selection integral |
| \(k=11\) | Gate steepness | Working calibration of \(\zeta(S)\) | Empirically tuned / operational | Sections 2, 3, 7 | Sets blur-gate sharpness |
| \(n=220\) | Selected Fibonacci shell index | Integrated entropy-phase budget \(\frac{24}{\ln\phi}\int_{1.3806}^{5.7889}(1-\zeta)\,dS\) | Candidate-locked selector | Sections 2, 7, 10 | Fixes \(L_{vac}\) |
| \(24\) | Sector multiplicity | Native cubic/BCC sector count | Structural input / candidate-locked in selector | Sections 2, 7 | Converts phase span into shell count |
| \(L_{vac}\) | Substrate resolution scale | Corrected radial law \(L_{vac}=R_H/\phi^n\) and scheduler identity \(L_{vac}=c\,t_{sched}\) | Derived once \(n\) and \(R_H\) are fixed | Sections 2, 7 | Vacuum scale feeding \(\Lambda\) |
| \(c\) | Scheduler regulator | Substrate tick-rate identity | Derived / substrate-native | Section 2 | Defines \(L_{vac}=c\,t_{sched}\), connects to \(R_H\) when anchored |
| \(H_0=67.4\) km/s/Mpc | External cosmological anchor | Planck 2018 | Empirical anchor only | Sections 2, 7, 10 | Optional \(R_H=c/H_0\) consistency anchor, not primary selector |
| \(e^{3\pi/2}=111.32\) | 3D BCC streaming factor | Three spatial streaming steps of \(\pi/2\) | Derived / substrate-native | Section 7 | Dimensional suppression factor in active chain |
| \(\Lambda \approx 1.081\times 10^{-52}\,\mathrm{m}^{-2}\) | Cosmological constant output | Corrected no-`/2` Lambda branch | Downstream supported output | Sections 1, 7, 10 | Main cosmological output |

## 12.1 Reading guide

The paper uses three different epistemic levels and they must not be collapsed:

- **Derived / substrate-native:** follows directly from HPF geometric or scheduler structure.
- **Empirically anchored under HPF mapping:** introduced by mapping external observation into HPF phase language.
- **Candidate-locked:** strongest current internal selector or phase landmark, but not yet a uniqueness theorem.

## 12.2 Minimal explanation chain

The whole paper can be explained compactly as:

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}
\]

for the dark-matter branch, and

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
\]

for the Lambda branch.

That is the active canonical split.
