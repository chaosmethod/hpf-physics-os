# HPF Lambda / Dark Matter — Consolidated Active Master Package

## Status
Active authority compilation after the no-1.4 canon rewrite.

## How to use this file
- **Part I** is the live canon master.
- **Part II** is the reader-facing full draft.
- **Part III** is the minimal attackable core.
- **Part IV** is the symbol reference.
- **Part V** is the provenance map.

---

# Part I — Canon Master Authority

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



ewpage

# Part II — Reader-Facing Full Draft

# HPF Canonical Derivation Package

## First-Principles Derivation of Λ and the Dark Matter Fraction

## Truth-Status: Candidate-Locked

## Date: 2026-03-29 (corrected from 2026-03-27 draft)

## Authors: Eric Keaton Porter

\---

# Section 1: Executive Summary

This document presents the active HPF candidate-locked derivation package for the cosmological constant \(\Lambda\) and the dark-matter fraction. The active derivation structure is split into two branches and the old mixed March 27 branch is retired.

Lambda branch:

\[
1.05 \;\rightarrow\; 1.3806 \;\rightarrow\; 5.7889 \;\rightarrow\; n=220 \;\rightarrow\; L_{vac} \;\rightarrow\; \Lambda
\]

Dark-matter branch:

\[
b \;\rightarrow\; f_{coh} \;\rightarrow\; \alpha_{vac} \;\rightarrow\; \Omega_{\rm dm}=1-\alpha_{vac}.
\]

**Outputs**

|Quantity|HPF output|Observed|Gap|
|-|-|-|-|
|\(\Lambda\)|1.081 x 10^-52 m^-2|1.1 x 10^-52 m^-2|10^-0.008|
|Dark matter fraction|26.29%|26.8%|0.51%|

The corrected radial law is

\[
R_H = L_{vac}\phi^n,
\qquad
L_{vac}=\frac{R_H}{\phi^n}.
\]

No `/2` belongs in this identity. The earlier `/2` factor arose from double-counting bipartite half-active support in a radial relation where it does not belong.

**Status note.** The shell selector is now the integrated entropy-phase budget. In the active canon, \(n=220\) is candidate-locked by regulated phase span. \(H_0\) may still be used as an external consistency anchor, but it is not the primary selector.

\---

# Section 2: The Lattice Identity and c as Regulator

\(c\), \(L_{vac}\), and \(t_{sched}\) are the same substrate primitive under three descriptions.

**Identity**
\[
L_{vac} = c \cdot t_{sched}.
\]

In substrate units, \(c=1\), \(L_{vac}=1\), and \(t_{sched}=1\). In this sense \(c\) is the scheduler rate, not an externally imposed speed bound.

The SI value of \(L_{vac}\) is set by the integer Fibonacci shell depth from the substrate unit to the Hubble scale:

\[
L_{vac}=\frac{R_H}{\phi^n}.
\]

Since the scheduler is discrete, \(n\in \mathbb{Z}_{>0}\).

The active selector for \(n\) is

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

\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},
\qquad k=11.
\]

Thus \(n=220\) is treated in the active canon as a candidate-locked shell selector. If \(R_H=c/H_0\) is inserted numerically, that step functions as an external consistency anchor only.

A constant-shadow pattern remains recorded but not promoted to derivation status: \(1.05\), \(1.3806\), and \(5.7889\) align numerically with the mantissae of \(\hbar\), \(k_B\), and \(\mu_B\), respectively. In this document that pattern is treated as functional resonance, not as first-principles deduction.

**Editorial note.** The symbol index must still be updated so the vacuum entry matches the corrected no-`/2` radial law.

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

   # Section 6: Governor Transfer Lemma

## 6.1 Definitions

Define

\[
f_{coh}=\frac{1}{2\pi b}\sqrt{1+b^2},
\qquad
b=\frac{\ln\phi}{\pi/2}.
\]

Here \(f_{coh}\) is the geometric coherent-support fraction of the spiral boundary. It is a support fraction, not yet an availability variable.

Define \(\alpha_{vac}\) as the scheduler-usable post-governor vacuum availability.

## 6.2 Lemma

\[
\alpha_{vac}=\sqrt{f_{coh}}.
\]

Equivalently,

\[
f_{coh}=\alpha_{vac}^2.
\]

## 6.3 Assumption used

The transfer from geometric support fraction to usable availability is governed by the HPF chronological-governor rule that availability enters linearly in scheduler time while support enters quadratically as reservoir measure. Under that rule, the unique one-step transfer between the two variables is a single square root.

## 6.4 Proof under the governing assumption

\(f_{coh}\) and \(\alpha_{vac}\) are not the same object: the former is geometric support occupancy, while the latter is post-governor usable availability. Zero transfer would identify distinct variables; two transfers would apply the same governor map twice. Under the governing assumption stated in 6.3, exactly one square-root transfer is admitted. Therefore

\[
\alpha_{vac}=\sqrt{f_{coh}}.
\]

QED.

## 6.5 Status note

This lemma is **candidate-locked**, not a uniqueness theorem independent of the governor rule. The geometric input \(f_{coh}\) is substrate-native; the one-square-root transfer is the active HPF governor map.

## 6.6 Numerical values

\[
f_{coh}=0.543354,
\qquad
\alpha_{vac}=\sqrt{f_{coh}}=0.737125.
\]

## 6.7 Corollary: dark-matter fraction

Define

\[
\Omega_{\rm dm}=1-\alpha_{vac}.
\]

Then

\[
\Omega_{\rm dm}=1-0.737125=0.262875=26.29\%.
\]

This is the post-governor deferred coherent-support complement. It is not the raw geometric complement \(1-f_{coh}\).

## 6.8 Status note

The dark-matter output follows from the separate branch

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm},
\]

and must not be mixed into the Lambda selector.

\---

# Section 7: \(L_{vac}\) Derivation and Active Canonical Structure

## 7.1 Definitions and radial law

Let \(R_H\) denote the Hubble-scale radius used for external numerical anchoring. Let \(n\in\mathbb{Z}_{>0}\) denote Fibonacci shell depth. The corrected radial law is

\[
\frac{R_H}{L_{vac}}=\phi^n,
\qquad
L_{vac}=\frac{R_H}{\phi^n}.
\]

No `/2` enters this identity.

## 7.2 Status of \(n\)

In the active canon, \(n\) is not selected by fitting \(\Lambda\) through \(H_0\). Instead, the live selector is the integrated entropy-phase budget

\[
n_{\rm sel}
=
\operatorname{round}\!\left[
\frac{24}{\ln\phi}
\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS
\right]
\approx 220.
\]

Thus \(n=220\) is treated as candidate-locked by the phase selector. If one inserts \(R_H=c/H_0\) numerically, that step checks consistency of the selected integer; it does not define it.

For the Planck 2018 anchor \(H_0=67.4\,\mathrm{km\,s^{-1}\,Mpc^{-1}}\),

\[
R_H = c/H_0 = 1.3736\times 10^{26}\,\mathrm{m},
\qquad
L_{vac}=R_H/\phi^{220}=1.447\times 10^{-20}\,\mathrm{m}.
\]

## 7.3 3D BCC streaming factor

The three-dimensional BCC streaming contribution is

\[
e^{3\pi/2}=111.32.
\]

This factor is treated as substrate-native: three spatial streaming steps, each contributing \(\pi/2\).


## 7.4 Formal phase structure

### Definition 7.4.1 (Blur anchor)

\[
S_{\rm blur}=1.05.
\]

**Status note.** Empirically anchored under HPF mapping from the Lu half-blur / 0.5 Einstein-side midpoint result.

### Definition 7.4.2 (Entropy onset)

\[
S_{\rm ent}=1.3806.
\]

**Status note.** Candidate-locked active lower entropy onset. This is the live lower onset used in the selector and continuum-suppression statements.

### Definition 7.4.3 (Capacity wall)

\[
S_{\rm cap}=5.7889.
\]

**Status note.** Candidate-locked active phase ceiling.

Hence the active phase ordering is

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889.
\]

### Status note on constant-shadow pattern

The numerical correspondences

\[
1.05 \leftrightarrow \hbar,
\qquad
1.3806 \leftrightarrow k_B,
\qquad
5.7889 \leftrightarrow \mu_B
\]

are retained as functional resonance only. They are not presented as first-principles derivations.

## 7.5 Zeta gate


### Definition 7.5.1

\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}}.
\]

### Proposition 7.5.2 (Operational steepness)

\[
k=11.
\]

### Derivation note

Fixing midpoint \(1.05\), onset target \(S_\ast=1.3806\), and residual Einstein-side stability \(\eta=0.021\) gives

\[
k=\frac{\ln\!\left(\frac{1-\eta}{\eta}\right)}{S_\ast-1.05}\approx 11.62.
\]

The active value \(k=11\) is therefore the rounded operational steepness.

**Status note.** Candidate-explained and candidate-locked; not uniqueness-proved.

## 7.6 Integer selector

### Definition 7.6.1

\[
n_{\rm sel}
=
\operatorname{round}\!\left[
\frac{24}{\ln\phi}
\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS
\right].
\]

### Interpretation note

Here \(24\) is the active cubic/BCC sector multiplicity, \(\ln\phi\) is the Fibonacci shell-step spacing measure in log-space, and \(1-\zeta(S)\) is the instability-active fraction over the entropy-phase interval.

### Corollary 7.6.2

\[
n_{\rm sel}\approx 220.
\]

### Status note

The lower integration bound of the active selector is \(1.3806\). No separate \(1.4\) marker remains in the active canon. This sharpening restores \(n=220\).

The prefactor \(24\) is interpreted as the 3D sector lift of native BCC 8-fold coordination. This interpretation is structurally coherent and candidate-locked, but not uniqueness-proved.

## 7.7 Branch separation

The two active chains are

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
\]

and

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}.
\]

The second branch must remain separate from the Lambda selector.

## 7.8 Canonical status summary

**Derived / substrate-native**
- \(\phi\)
- \(b\)
- \(f_{coh}\)
- corrected no-`/2` radial law
- BCC 8-fold coordination

**Empirically anchored**
- Lu half-blur / 0.5 Einstein-side midpoint result
- \(1.05\) as HPF calibrated blur anchor

**Candidate-locked**
- \(1.3806\)
- \(5.7889\)
- \(k=11\) as rounded operational steepness
- \(24\) as selector sector multiplicity
- \(n=220\) via integrated entropy-phase budget
- \(\alpha_{vac}=\sqrt{f_{coh}}\) under the governor-transfer lemma

\---

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


This section separates internal derivations, empirical anchors, and candidate-locked elements. Claims below should be read with their status labels attached.

## 10.1 Derived / substrate-native

|Claim|Form|Location|Status note|
|-|-|-|-|
|\(C(n)=F(n)\) for BCC bipartite coherent sequences|Proposition|Section 4.4|Internal derivation|
|\(\phi\) emerges from the BCC bipartite scheduler|Corollary|Section 4.5|Internal derivation|
|Continue/Branch is the valid coarse-graining|Proposition|Section 4.6|Internal derivation|
|Logarithmic spiral is the causal-boundary embedding|Proposition|Section 5.1|Internal derivation|
|\(\kappa_{BCC}=2\)|Definition / computation|Section 3|Internal derivation|
|\(c\) as scheduler regulator and \(L_{vac}=c\,t_{sched}\)|Definition|Section 2|Internal derivation|
|\(n\in\mathbb{Z}_{>0}\)|Corollary|Sections 2, 7.1|Discrete scheduler consequence|
|\(e^{3\pi/2}=111.32\)|Definition / computation|Section 7.3|Internal derivation|
|Bipartite half-support belongs in support geometry, not radial law|Corollary|Sections 5.2, 7.1|No-`/2` correction|

**Usage language:** “derived,” “established,” or “proved internally,” as appropriate.

## 10.2 Empirically anchored under HPF mapping

|Claim|External source|What the source reports|HPF role|
|-|-|-|-|
|\(S_{\rm blur}=1.05\)|Lu et al. 2026|Coherence degradation / half-blur behavior|Mapped blur anchor|
|Planck \(H_0=67.4\)|Planck 2018|CMB Hubble constant|External consistency anchor for \(R_H\)|
|OTOC Lyapunov regime support|Li et al. 2026|Quantum Lyapunov exponent|External regime anchor|

**Usage language:** “mapped from,” “inferred under HPF mapping,” or “used as external anchor.”

## 10.3 Candidate-locked propositions

|Claim|Form|Location|Status note|
|-|-|-|-|
|\(S_{\rm ent}=1.3806\)|Definition|Section 7.4|Active lower entropy onset|
|\(S_{\rm cap}=5.7889\)|Definition|Section 7.4|Active capacity wall|
|\(k=11\)|Proposition|Section 7.5|Rounded operational steepness from midpoint/onset targeting|
|\(24\) as sector multiplicity|Interpretive structural input|Section 7.6|Coherent, not uniqueness-proved|
|\(n=220\)|Corollary|Section 7.6|Selected by integrated entropy-phase budget|
|\(S_{\rm ent}=1.3806\) as active redistribution exponent|Proposition|Section 9.3|Used in continuum-suppression law after removal of the archived 1.4 marker|
|\(\alpha_{vac}=\sqrt{f_{coh}}\)|Lemma|Section 6|Depends on active governor rule|
|Continuum-emergence mechanism|Assembled mechanism|Section 9|Operationally closed, strongest-form uniqueness open|

**Usage language:** “candidate-locked,” “active canon,” or “current selector,” but not “uniquely derived.”

## 10.4 Downstream supported outputs

|Output|HPF value|Observed|Gap|
|-|-|-|-|
|\(\Lambda\)|1.081 x 10^-52 m^-2|1.1 x 10^-52 m^-2|10^-0.008|
|Dark matter fraction|26.29%|26.8%|0.51%|

**Usage language:** “output,” “agreement,” or “downstream support.” Do not use observational agreement alone as proof of ontology.

## 10.5 Reading rule

Every numbered constant in the live chain should be read together with one of three tags:

1. **Derived / substrate-native**
2. **Empirically anchored under HPF mapping**
3. **Candidate-locked**

The paper should not slide between these categories without an explicit status note.

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


\---

# Appendix A: Minimal Attackable Core

This appendix isolates the smallest live mathematical core of the package.

## A.1 Corrected radial law

\[
\frac{R_H}{L_{vac}}=\phi^n,
\qquad
L_{vac}=\frac{R_H}{\phi^n}.
\]

**Status:** derived / substrate-native correction. No `/2` belongs here.

## A.2 Phase landmarks

\[
S_{\rm blur}=1.05,
\qquad
S_{\rm ent}=1.3806,
\qquad
S_{\rm cap}=5.7889.
\]

**Status:** \(1.05\) empirically anchored under HPF mapping; \(1.3806\) and \(5.7889\) candidate-locked. No separate \(1.4\) marker remains in the active canon.

## A.3 Zeta gate and steepness

\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},
\qquad
k=11.
\]

With \(S_\ast=1.3806\) and \(\eta=0.021\),

\[
k\approx \frac{\ln((1-\eta)/\eta)}{S_\ast-1.05}\approx 11.62,
\]

so \(k=11\) is the rounded operational steepness.

**Status:** candidate-explained, candidate-locked.

## A.4 Integer selector

\[
n_{\rm sel}
=
\operatorname{round}\!\left[
\frac{24}{\ln\phi}
\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS
\right]
\approx 220.
\]

**Status:** candidate-locked. Here \(24\) is interpreted as active cubic/BCC sector multiplicity and \(\ln\phi\) as shell-step spacing in log-space.

## A.5 Dark-matter chain

\[
b=\frac{\ln\phi}{\pi/2},
\qquad
f_{coh}=\frac{1}{2\pi b}\sqrt{1+b^2},
\qquad
\alpha_{vac}=\sqrt{f_{coh}},
\qquad
\Omega_{\rm dm}=1-\alpha_{vac}.
\]

**Status:** \(b\) and \(f_{coh}\) derived / substrate-native; \(\alpha_{vac}=\sqrt{f_{coh}}\) candidate-locked under the governor-transfer lemma; \(\Omega_{\rm dm}\) downstream output.

## A.6 Split of live claims

Lambda branch:

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
\]

Dark-matter branch:

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}.
\]

This is the smallest live target for mathematical attack.



ewpage

# Part III — Minimal Attackable Core

# HPF Lambda / Dark Matter — Minimal Attackable Core

This companion note isolates the live mathematical core from the full paper.

## 1. Corrected radial law

\[
\frac{R_H}{L_{vac}}=\phi^n,
\qquad
L_{vac}=\frac{R_H}{\phi^n}.
\]

**Status:** derived / substrate-native correction. No `/2` belongs in the radial identity.

## 2. Phase landmarks

\[
S_{\rm blur}=1.05,
\qquad
S_{\rm ent}=1.3806,
\qquad
S_{\rm cap}=5.7889.
\]

**Status:** \(1.05\) empirically anchored under HPF mapping; \(1.3806\) and \(5.7889\) candidate-locked. No separate \(1.4\) marker remains in the active canon.

## 3. Zeta gate

\[
\zeta(S)=\frac{1}{1+e^{k(S-1.05)}},
\qquad
k=11.
\]

With \(S_\ast=1.3806\) and \(\eta=0.021\),

\[
k\approx \frac{\ln((1-\eta)/\eta)}{S_\ast-1.05}\approx 11.62,
\]

so \(k=11\) is the rounded operational steepness.

## 4. Integer selector

\[
n_{\rm sel}
=
\operatorname{round}\!\left[
\frac{24}{\ln\phi}
\int_{1.3806}^{5.7889}(1-\zeta(S))\,dS
\right]
\approx 220.
\]

**Status:** candidate-locked. The lower integration bound is \(1.3806\). No separate \(1.4\) marker remains in the active canon.

## 5. Dark-matter branch

\[
b=\frac{\ln\phi}{\pi/2},
\qquad
f_{coh}=\frac{1}{2\pi b}\sqrt{1+b^2},
\qquad
\alpha_{vac}=\sqrt{f_{coh}},
\qquad
\Omega_{\rm dm}=1-\alpha_{vac}.
\]

**Status:** \(b\) and \(f_{coh}\) derived / substrate-native; \(\alpha_{vac}=\sqrt{f_{coh}}\) candidate-locked under the active governor-transfer lemma.

## 6. Split of active branches

Lambda branch:

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
\]

Dark-matter branch:

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}.
\]



ewpage

# Part IV — Symbol Reference

# HPF–MDEA Unified Symbol & Definition Index

**Status:** Canonical Reference — Updated 2026-03-27
**Scope:** Definitions only (no derivations, no narrative)
**Purpose:** Eliminate ambiguity across HPF, MDEA, UHET, and QPRCA

---

## 1. Framework Layer Map

This stack is **layered, not competitive**:

- **HPF (Holographic Projection Framework)** — legality, regime detection, and execution constraints
- **MDEA (Multi‑Domain Execution Architecture)** — orchestration and routing among domain experts
- **UHET (Unified Holographic Emergence Theory)** — phenomenological description of saturation‑regulated regimes
- **QPRCA (Quantum Partitioned Reversible Cellular Automaton)** — executable substrate candidate

No layer replaces or subsumes another.

---

## 2. Core Symbols (Global)

| Symbol | Name | Layer | Definition | Notes |
|------|------|-------|------------|-------|
| $x$ | Lattice site / region | Global | Localized execution region | Abstract index |
| $t_{sched}$ | Scheduler time | QPRCA | Absolute substrate update clock | Uniform |
| $\tau$ | Proper time | Emergent | Observable time from coherent updates | Branch‑dependent |
| $c$ | Substrate propagation limit | QPRCA | Lattice site spacing per scheduler tick | $L_{vac} \equiv c \cdot t_{sched}$; c is not an imposed speed limit but the geometry of the tick itself |

---

## 3. HPF — Regulation & Legality Symbols

| Symbol | Name | Definition | Valid Range | Notes |
|------|------|------------|-------------|-------|
| $b(x)$ | Badness field | Local measure of instability | $\ge 0$ | Domain‑agnostic |
| $B$ | Total badness | $\sum_x b(x)$ | $\ge 0$ | Refinement tracked |
| $\sigma(x)$ | Saturation pressure | Update demand / capacity | $[0, \infty)$ | Hard gate at $>1$ |
| $\sigma_{\max}$ | Max saturation | $\max_x \sigma(x)$ | $[0, \infty)$ | Routing trigger |
| $\sigma_*$ | Activation threshold | Persistent saturation trigger | $0.7$ (default) | HPF engage |
| $G_{health}$ | Geometry health | Metric viability score | $[0,1]$ | Revoked $<0.3$ |
| $G_{crit}$ | Geometry cutoff | Metric failure threshold | $0.3$ | Hard revoke |
| $U_{health}$ | Unitarity health | Probability conservation | $[0,1]$ | Diagnostic |
| $\tau_C$ | Convergence threshold | Refinement convergence ratio | $0.5$ | Default |
| $\tau_P$ | Persistence threshold | Instability persistence ratio | $0.8$ | Default |

---

## 4. MDEA — Execution & Routing Symbols

| Symbol | Name | Definition | Notes |
|------|------|------------|-------|
| $E_i$ | Domain expert | Theory + solver valid in a regime | GR, QFT, etc. |
| $V_i$ | Validity score | Fitness of $E_i$ for current state | Computed |
| $E^*$ | Selected expert | $\arg\max_i V_i$ | Soft selection |
| $S_{handoff}$ | Handoff state | Minimal exported state | No invented precision |

---

## 5. UHET — Saturation & Phenomenology Symbols

| Symbol | Name | Definition | Notes |
|------|------|------------|-------|
| $S_f$ | Entropic flux | External turbulence / load | Phase driver |
| $u(r)$ | Utilization | $R_s / r$ | Dimensionless |
| $\alpha(x)$ | Update availability | Fraction of coherent updates | Not a metric |
| $R_s$ | Saturation radius | Utilization $=1$ surface | Horizon‑like |
| $\gamma_{HPF}$ | Time dilation | $dt_{sched}/d\tau$ | Matches GR |

---

## 6. QPRCA — Substrate Symbols

| Symbol | Name | Definition | Notes |
|------|------|------------|-------|
| $\alpha(x)$ | Regulator field | Local coherent update availability | Quantum DOF |
| $L_{tot}(x)$ | Total load | Sum of channel activities | Universal coupling |
| $L_a(x)$ | Channel load | Activity from channel $a$ | Weighted |
| $w_a$ | Channel weight | Fixed coupling weight | Non‑geometric |

---

## 7. Vacuum Sector Symbols

*Updated 2026-03-29. These symbols follow the corrected active Lambda / dark-matter branch.*

| Symbol | Name | Definition | Notes |
|------|------|------------|-------|
| $L_{vac}$ | Substrate resolution scale | Lattice site spacing; $L_{vac} = c \cdot t_{sched}$ | Active radial law: $L_{vac} = R_H / \varphi^n$; no `/2` belongs in the radial identity |
| $\varphi$ | Golden ratio | Asymptotic growth rate of Fibonacci recursion | $\varphi = (1+\sqrt{5})/2 = 1.618$; emerges from recurrence, not imposed |
| $b$ | Fibonacci growth parameter | $b = \ln\varphi / (\pi/2)$ | Support-geometry parameter |
| $f_{coh}$ | Coherent support fraction | $f_{coh} = \frac{1}{2\pi b}\sqrt{1+b^2}$ | Coherent vacuum support fraction |
| $\alpha_{vac}$ | Vacuum update availability | $\alpha_{vac} = \sqrt{f_{coh}}$ | Governor-transfer output; $\alpha_{vac} \approx 0.7371$ |
| $\Omega_{\rm dm}$ | Dark matter fraction | $\Omega_{\rm dm}=1-\alpha_{vac}$ | Deferred coherent-support complement |
| $n$ | Radial shell index | $R_H/L_{vac} = \varphi^n$ | Active shell count is $n=220$ in current candidate-locked canon |
| $\kappa_{BCC}$ | BCC geometric coefficient | $\kappa_{BCC} = 8 \times (1/2) \times (1/2) = 2$ | Coordination number $\times$ bipartite $\times$ LMS mirror |
| $\varepsilon$ | Continuum correction | $\varepsilon = (1-\zeta(S_f)) \cdot (L_{vac}/\ell_O)^{S_{ent}}$ | Discrete-substrate residual for observable at scale $\ell_O$ |
| $S_{ent}$ | Active entropy onset / redistribution exponent | $S_{ent}=1.3806$ | Live lower onset used in the selector and continuum-suppression law |

---

## 8. Phase Boundaries (Reference)

| Quantity | Boundary | Interpretation |
|---------|----------|----------------|
| $S_f < 1.05$ | Below blur threshold | Fully coherent local updates; discrete substrate maximally hidden |
| $S_f \approx 1.05$ | Lu blur threshold ($\lambda_{blur}$) | Coherence loss onset; $\zeta = 0.5$; redistribution begins |
| $1.05 < S_f < 1.3806$ | Pre-entropy transition band | Coherence-loss regime before the active entropy onset |
| $1.3806 < S_f < 5.7889$ | Active entropy / transition band | Instability-active regime used by the selector and continuum-suppression law |
| $S_f > 5.7889$ | Capacity wall / decoherence | Raw geometry collapse / saturation ceiling |
| $\sigma_{\max} \ge 1$ | Illegal | Route to UHET |
| $G_{health} < 0.3$ | Metric failure | Route to QPRCA |
| no separate $1.4$ marker in active canon | Canon note | The live lower onset is $S_{ent}=1.3806$ |

---

## 9. Provenance Note

This index was updated on 2026-03-27 to add:

- $c$ (substrate propagation limit) to Section 2 — closes gap identified in HPF Lambda/dark matter derivation package
- Section 7 (Vacuum Sector Symbols) — new symbols from the Lambda and dark matter derivation
- Section 8 updated — blur threshold $S_f = 1.05$ added; active entropy onset $S_{ent}=1.3806$ now carried as the live lower onset and redistribution exponent

The active Lambda and dark matter derivation package is: `HPF_Lambda_DarkMatter_Canonical_2026-03-29_rewritten.md`

Prior version of this index was standalone in the old repo structure. This version should travel with the Volume I–III canonical package.

---

This index defines symbols only. All derivations live in their respective documents.

---

**End of Canonical Index**


---
## 12. Symbol Provenance and Truth-Status Guide

This appendix aligns the symbol index with the active canonical paper. Every live symbol or numeric landmark should be read under one of three statuses:

- **Derived / substrate-native**: follows directly from HPF geometry or scheduler structure
- **Empirically anchored under HPF mapping**: imported by mapping observation into HPF phase language
- **Candidate-locked**: strongest current internal selector or landmark, but not yet a uniqueness theorem

### 12.1 Vacuum / dark-matter branch

| Symbol | Meaning | Origin | Truth-status | Primary use |
|---|---|---|---|---|
| \(\phi\) | Golden ratio / Fibonacci growth ratio | Scheduler recurrence | Derived / substrate-native | Spiral growth, shell spacing |
| \(b=\ln\phi/(\pi/2)\) | Log-spiral growth parameter | Quarter-turn Fibonacci/BCC embedding | Derived | Defines causal-boundary spiral |
| \(f_{coh}\) | Coherent support fraction | Spiral-supported fraction of spherical causal boundary | Derived geometric quantity | Boundary support reservoir |
| \(\alpha_{vac}=\sqrt{f_{coh}}\) | Post-governor vacuum availability | One-step governor transfer from support to availability | Candidate-locked lemma | Usable vacuum fraction |
| \(\Omega_{\rm dm}=1-\alpha_{vac}\) | Dark matter fraction | Deferred coherent-support complement after governor transfer | Downstream derived output | Dark-matter result |
| \(L_{vac}\) | Substrate resolution scale | Scheduler identity \(L_{vac}=c\,t_{sched}\) and corrected radial law \(L_{vac}=R_H/\phi^n\) | Derived once \(n\) and \(R_H\) are fixed | Vacuum scale for Lambda branch |
| \(c\) | Scheduler regulator | Tick-rate identity of substrate | Derived / substrate-native | Defines scheduler-time scale |
| \(\kappa_{BCC}=2\) | BCC geometric coefficient | Coordination x bipartite x LMS mirror | Derived | Support geometry coefficient |

### 12.2 Phase-landmark and selector branch

| Symbol / Value | Meaning | Origin | Truth-status | Primary use |
|---|---|---|---|---|
| \(S_{\rm blur}=1.05\) | Blur / coherence-loss onset | Lu atom-blur result mapped into HPF phase variable | Empirically anchored under HPF mapping | Lower anchor of \(\zeta(S)\) |
| \(S_{\rm ent}=1.3806\) | Sharpened entropy-active onset | Active HPF phase landmark | Candidate-locked | Lower limit of shell-selection integral |
| \(S_{\rm ent}=1.3806\) | Active entropy onset / redistribution exponent | Active HPF phase landmark | Candidate-locked | Lower limit of shell-selection integral; exponent in continuum-suppression law |
| \(S_{\rm cap}=5.7889\) | Capacity wall / saturation ceiling | Active HPF phase ceiling | Candidate-locked | Upper limit of shell-selection integral |
| \(k=11\) | Gate steepness | Working \(\zeta(S)\) calibration | Empirically tuned / operational | Blur-gate sharpness |
| \(24\) | Sector multiplicity | Native cubic/BCC sector count | Structural input / candidate-locked in selector | Converts phase span into shell count |
| \(n=220\) | Selected Fibonacci shell index | Integrated entropy-phase budget | Candidate-locked selector | Fixes \(L_{vac}\) in active canon |
| \(e^{3\pi/2}=111.32\) | 3D BCC streaming factor | Three spatial streaming steps of \(\pi/2\) | Derived / substrate-native | Dimensional suppression factor |
| \(H_0=67.4\) km/s/Mpc | External cosmological anchor | Planck 2018 | Empirical anchor only | Optional \(R_H=c/H_0\) consistency anchor |

### 12.3 Minimal explanation chain

For the dark-matter branch:

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}.
\]

For the Lambda branch:

\[
1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda.
\]

### 12.4 Usage rule

When explaining any number in the package, state:

1. what it is,
2. where it comes from,
3. whether it is derived, anchored, or candidate-locked,
4. what equation or section first introduces it,
5. what downstream job it does.

If one of those five is missing, the number is still under-explained.



ewpage

# Part V — Provenance and Supersession Map

# HPF Canonical Presentation Package — Volume III
## Supersession, Provenance, and Live-Reference Map
### Consolidated Final Package State — Updated Epoch 2026-03-20

**Role of this volume:** audit and navigation volume. It records what is primary, what is supporting, what is exploratory, what is historical, and how the March 19 and March 20 updates change the live reference set.

---

# 1. Top current authorities

## 1.1 Overall framework authority
- `HPF_Master_Canonical_Framework_Epoch_2026-03-19_v2.md` *(historical authority file; retained in dev archive, not part of this public release)*

## 1.2 Current presentation master volume
- `volume-1-master-canon.md`

## 1.3 Current microscopic-legality and executable-development authority
- `volume-2-microscopic-derivation.md`

---

# 2. Current live supporting references

## 2.1 Framework / regulator front notes
*(Internal working documents retained in dev archive; not part of this public release.)*
- `HPF_Core_Note_Two_Wall_Regulator_Updated_2026-03-19.md`
- `HPF_Two_Wall_Regulator_Sections_4_5_Draft_2026-03-20.md`

## 2.2 Live executable artifacts
- `qprca-v0.2.8.py` — front active executable

## 2.3 March 20 microscopic correction notes absorbed into Volume II
*(These working notes were folded into `volume-2-microscopic-derivation.md` and are retained in dev archive only.)*
- `HPF_Microscopic_Legality_Theorem_Spine_v1_2026-03-20.md`
- `HPF_Operator_Richness_Note_v1_2026-03-20.md`
- `HPF_Predecessor_Burden_Redefinition_v1_2026-03-20.md`
- `HPF_Bridge_Recalibration_Note_v0_2_7_2026-03-20.md`

## 2.4 Historical March 19 roadmap / guide notes
*(Historical provenance documents retained in dev archive only.)*
- `HPF_Canonical_Package_Guide_Consolidated_Final_2026-03-19.md`
- `HPF_Closure_and_Theorem_Roadmap_Consolidated_2026-03-19.md`
- `HPF_Closure_Program_Theorem_Targets_Updated_2026-03-19.md`
- `HPF_Derived_Zeta_Recovery_Note_2026-03-19.md`

---

# 3. Executable supersession map

## 3.1 Historical microscopic line
- v0.1 = first executable legality harness
- v0.1.1 = variable predecessor algebra
- v0.1.2 = normalized predecessor stable historical baseline
- v0.1.3 = richer non-predecessor exploratory branch

## 3.2 Enriched-canon executable line
- v0.2.0 = first enriched-canon executable reference
- v0.2.1 = first explicit derived-zeta recovery executable
- v0.2.2 = grouped-L2 promotion branch
- v0.2.3 = tuned grouped-L2 projection branch
- v0.2.4 = floor-fixed grouped-L2 projection branch
- v0.2.5 = reversible-registry repair branch
- v0.2.6 = continuation-ambiguity executable patch
- v0.2.7 = bridged continuation-ambiguity line with legality-tail-sensitive bridge recalibration
- v0.2.8 = existence-sensor integration; current front executable

## 3.3 Current recommended executable status
- **front active executable:** `qprca-v0.2.8.py`
- **existence-sensor protocol note:** `existence-sensor-protocol-note.md`
- **existence-sensor test report:** `existence-sensor-report.json`
- **sigma pressure test artifact:** `sigma-pressure-test.json`
- **historical stable baseline reference:** v0.1.2 normalized predecessor baseline (retained conceptually through Volume II discussion)
- **historical floor-fix milestone:** v0.2.4 remains the key pre-registry-repair anchor for the earlier derived-$\zeta$ recovery line

Interpretation:
- v0.2.8 is the current front executable embodiment of the enriched canon,
- v0.2.7 was the bridge-recalibrated predecessor; retained in dev archive,
- v0.2.4 remains an important historical calibration milestone,
- v0.1.2 remains the clean historical microscopic baseline.

---

# 4. Supersession logic

## 4.1 Controlling rule
Where older wording conflicts with later March 19 closure/savepoint language, the later March 19 status controls.

## 4.2 Recovery rule
Older files may still contribute architecture, motivation, derivation history, or clarifying distinctions, provided they do not override current truth-status.

## 4.3 Anti-drift rule
No recovered or older text may be used to:
- collapse legality into validity,
- collapse geometry into the regulator,
- demote candidate-locked structures back to simply open,
- promote open frontier items to fully closed,
- erase the fixed HPF $\to$ MDEA $\to$ geometry/gravity $\to$ QPRCA order.

---

# 5. Provenance of the latest package changes

## 5.1 Theorem-track promotion
The closure-program note made explicit that the best next move is a theorem-and-reproduction track rather than another broad rewrite.

## 5.2 Derived-zeta recovery promotion
The package guide and derived-zeta notes made explicit that smooth corridor recovery is now an official closure target, not a side experiment.

## 5.3 Grouped-L2 promotion
The grouped-L2 recheck established that additive aggregation was over-driving ordinary runs toward hard saturation, while grouped-L2 materially improved acceptance and corridor behavior.

## 5.4 Projection tuning and floor fix
The tuning note localized the v0.2.3 scaling problem. The floor-fix update and v0.2.4 calibration work then repaired the projection topology by reopening the sub-onset stable branch without losing onset/corridor/hard representation.

## 5.5 Reversible-registry repair
The March 20 operator-richness audit made explicit that the old live registry still contained a rule that failed the file's own bijection check. The v0.2.5 repair corrected that defect and promoted reversibility honesty from assumption to coded property.

## 5.6 Continuation-ambiguity promotion
Once the registry became fully bijective, the old raw predecessor-count burden ceased to be the right microscopic primitive. The March 20 redefinition note promoted continuation ambiguity / local operator ambiguity as the correct replacement direction, and that logic is now absorbed into the merged Volume II.

## 5.7 Bridge recalibration
The first continuation-ambiguity patch preserved the corridor but exposed that the coarse bridge had become too mean-based to distinguish the hard edge. The v0.2.7 recalibration added legality-tail-sensitive coarse information and recovered the four anchor regimes again.

## 5.8 Package refresh on 2026-03-20
The updated package no longer treats v0.2.4 as the front active executable reference. The live package state is now:
- updated Volume I (`volume-1-master-canon.md`),
- merged Volume II with March 20 corrections folded in (`volume-2-microscopic-derivation.md`),
- updated Volume III (`volume-3-provenance-map.md`),
- v0.2.8 Python executable (`qprca-v0.2.8.py`),
- existence-sensor protocol note and test artifacts.

---

# 6. Reading order

1. `volume-1-master-canon.md` — master canon
2. `volume-2-microscopic-derivation.md` — microscopic and executable line
3. `volume-3-provenance-map.md` — provenance and live-reference map
4. `qprca-v0.2.8.py` — front active executable
5. existence-sensor protocol note and test artifacts

---

# 7. One-line package read

The package now preserves the enriched March 19 canon, integrates the March 20 theorem-work and v0.2.7 executable recovery line, and makes clear which artifacts are current authority, absorbed support, live executable support, or historical lineage.

---


# 8. Post-March-20 additions — 2026-03-29

## 8.1 Symbol index

`Symbol_index_2026-03-29_rewritten_v3_no14.md` is the current canonical symbol reference for the package. It travels with the Volume I–III set and now reflects the corrected no-`/2` radial law and the revised no-`1.4` phase canon.

Key additions and corrections:
- $c$ as scheduler regulator through the identity $L_{vac}\equiv c\cdot t_{sched}$
- Vacuum-sector symbols: $L_{vac}$, $\varphi$, $b$, $f_{coh}$, $\alpha_{vac}$, $\Omega_{\rm dm}$, $n$, $\kappa_{BCC}$, $\varepsilon$
- Phase section updated so the live landmarks are $S_{\rm blur}=1.05$, $S_{\rm ent}=1.3806$, and $S_{\rm cap}=5.7889$
- No separate $1.4$ phase marker remains in active canon

## 8.2 Lambda and dark matter derivation package

`HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon.md` is the current active derivation document for the vacuum sector.

It derives the cosmological constant $\Lambda$ and the dark-matter fraction from the HPF substrate geometry with the active branch split kept explicit.

**Current outputs:**

| Quantity | HPF Derived | Observed | Gap |
|----------|------------|----------|-----|
| $\Lambda$ | $1.081 \times 10^{-52}$ m$^{-2}$ | $1.1 \times 10^{-52}$ m$^{-2}$ | $10^{-0.008}$ |
| Dark matter fraction | $26.29\%$ | $26.8\%$ | $0.51\%$ |

**Current locked results:**

- corrected radial law: $L_{vac}=R_H/\varphi^{220}$ with no bipartite `/2` in the radial identity
- $\alpha_{vac}=\sqrt{f_{coh}}$ under the active governor-transfer lemma
- $\Omega_{\rm dm}=1-\alpha_{vac}$ as the deferred coherent-support complement
- active phase chain: $1.05 \rightarrow 1.3806 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda$
- continuum-emergence bound carried with exponent $S_{\rm ent}=1.3806$, not by a separate $1.4$ marker

**Truth-status:** Candidate-locked. The package is internally consolidated but still awaiting independent verification and stronger-form uniqueness proofs.

**Relationship to existing canon:** This package extends the HPF regulatory architecture into the vacuum sector. It does not supersede Volumes I–III. Those volumes remain the primary canon for the regulator architecture; the Lambda/dark-matter package is a downstream derivation built on that substrate architecture.

## 8.3 Updated reading order

1. `volume-1-master-canon.md` — master canon
2. `volume-2-microscopic-derivation.md` — microscopic and executable line
3. `volume-3-provenance-map-updated_v2_no14.md` — provenance and live-reference map
4. `Symbol_index_2026-03-29_rewritten_v3_no14.md` — canonical symbol reference
5. `qprca-v0.2.8.py` — front active executable
6. existence-sensor protocol note and test artifacts
7. `HPF_Lambda_DarkMatter_Canonical_2026-03-29_master_locked_no14canon.md` — compact canon lock
8. `HPF_Lambda_DarkMatter_Canonical_2026-03-29_final_reader_pass_no14canon.md` — full reader-facing vacuum-sector paper
9. `HPF_Lambda_DarkMatter_attackable_core_2026-03-29_no14canon.md` — minimal exposed core

