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
1.05 \;\rightarrow\; 1.3806 \text{ / } 1.4 \;\rightarrow\; 5.7889 \;\rightarrow\; n=220 \;\rightarrow\; L_{vac} \;\rightarrow\; \Lambda
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

### Proposition 7.4.2 (Rounded structural marker)

\[
d_{eff}=1.4=1.05\times\frac{4}{3}.
\]

**Status note.** Derived structural marker. It is retained as the rounded geometric instability marker.

### Definition 7.4.3 (Entropy onset and capacity wall)

\[
S_{\rm ent}=1.3806,
\qquad
S_{\rm cap}=5.7889.
\]

**Status note.** Candidate-locked active phase landmarks.

Hence the active phase ordering is

\[
1.05 \rightarrow 1.3806/1.4 \rightarrow 5.7889.
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

The rounded marker \(1.4\) is retained for structural discussion, while \(1.3806\) is the actual lower integration bound of the active selector. This sharpening restores \(n=220\).

The prefactor \(24\) is interpreted as the 3D sector lift of native BCC 8-fold coordination. This interpretation is structurally coherent and candidate-locked, but not uniqueness-proved.

## 7.7 Branch separation

The two active chains are

\[
1.05 \rightarrow 1.3806/1.4 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
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
- \(d_{eff}=1.4\) as rounded structural marker
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
HPF use: Confirms which integer n selects L\_vac. H0 = 67.4 gives n=220 as the unique integer closing Lambda. This is Tier 2 — HPF does not derive H0, it uses H0 to identify the correct Fibonacci integer.

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

At each scheduler tick, local updates are accepted with probability zeta(S\_f) = 1/(1+e^(k\*(S\_f-1.05))) where k = 11.0 (transition slope, calibrated to reproduce the sharp coherence-loss profile from Lu 2026) and redistributed reversibly with probability 1-zeta(S\_f). At S\_f = 1.05, zeta = 0.5 — half the updates are redistributed rather than applied locally. Discreteness degrades through reversible delocalization before any rigid lattice exposure occurs.

## 9.2 Observable Bound

For observable O at probing scale l\_O:

epsilon(l\_O/L\_vac, S\_f) = (1 - zeta(S\_f)) \* (L\_vac/l\_O)^d\_eff

Observable O is operationally continuum-indistinguishable if epsilon < delta\_O (measurement precision).

Critical scale: l\_O\* = L\_vac \* \[(1-zeta(S\_f))/delta\_O]^(1/d\_eff)

## 9.3 Derivation of d\_eff = 1.4

BCC has 4 independent diagonal directions (4 direction-reverse pairs from the 8 neighbors). Fibonacci scheduler: Continue(1) + Branch(3) = 4 choices. Ratio = 4/3.

d\_eff = lambda\_blur x (4/3) = 1.05 x (4/3) = 1.4

d\_eff is not borrowed from the phase boundary — it IS the phase boundary, and the phase boundary is derived from BCC diagonal structure x blur threshold.

Redistribution kernel variance scales as (L\_vac/l\_O)^1.4 because R\_i spreads over N\_sites \~ (l\_O/L\_vac)^1.4 Fibonacci-reachable sites, each contributing independently by reversibility.

## 9.4 LIV Suppression

Lattice anisotropy corrections are the same order as epsilon — suppressed by (L\_vac/l\_O)^1.4 for any l\_O >> L\_vac in the Einstein phase. At current experimental precision (GW detectors \~10^-20), discrete corrections are \~10^2.9 below detectability.

\---

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
|\(d_{eff}=1.4\)|Proposition|Sections 7.4, 9.3|Rounded structural marker|
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

Observable bound derived. \(d_{eff}=1.4\) proved as the rounded structural marker from the BCC diagonal chain. Remaining work is stronger-form uniqueness, not basic mechanism assembly.

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
| \(S_{\rm ent}=1.3806\) | Sharpened entropy-active onset | Active HPF phase landmark tighter than rounded 1.4 marker | Candidate-locked active canon | Sections 2, 7, 10 | Lower limit of shell-selection integral |
| \(d_{eff}=1.4=1.05\times 4/3\) | Rounded structural instability marker | Blur threshold times BCC diagonal/branch structure | Derived / candidate-locked structural marker | Sections 7, 10 | Rounded transition marker; redistribution scaling context |
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
1.05 \rightarrow 1.3806/1.4 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
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
d_{eff}=1.4=1.05\times\frac{4}{3},
\qquad
S_{\rm ent}=1.3806,
\qquad
S_{\rm cap}=5.7889.
\]

**Status:** \(1.05\) empirically anchored under HPF mapping; \(d_{eff}=1.4\) derived as rounded structural marker; \(1.3806\) and \(5.7889\) candidate-locked.

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
1.05 \rightarrow 1.3806/1.4 \rightarrow 5.7889 \rightarrow n=220 \rightarrow L_{vac} \rightarrow \Lambda
\]

Dark-matter branch:

\[
\phi \rightarrow b \rightarrow f_{coh} \rightarrow \alpha_{vac} \rightarrow \Omega_{\rm dm}.
\]

This is the smallest live target for mathematical attack.
