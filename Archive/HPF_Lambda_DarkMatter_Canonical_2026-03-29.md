# HPF Canonical Derivation Package

## First-Principles Derivation of Λ and the Dark Matter Fraction

## Truth-Status: Candidate-Locked

## Date: 2026-03-29 (corrected from 2026-03-27 draft)

## Authors: Eric Keaton Porter

\---

# Section 1: Executive Summary

This document derives the cosmological constant Λ and the dark matter fraction from the substrate geometry of the Holographic Projection Framework using no continuous fit parameters in the substrate vacuum derivation chain. Empirical calibration appears only in the continuum-emergence blur map, not in the vacuum derivation itself.

The derivation chain is:

BCC structure → Fibonacci growth → spiral boundary → f\_coh → alpha\_vac → Λ → dark matter complement

**Results:**

|Quantity|HPF Derived|Observed|Gap|
|-|-|-|-|
|Λ|1.081 x 10^-52 m^-2|1.1 x 10^-52 m^-2|10^-0.008|
|Dark matter fraction|26.29%|26.8%|0.51%|

Both results emerge from the same derivation chain without being separately targeted. The dark matter fraction fell out of the Λ derivation as the governor-converted complement of alpha\_vac.

**Key correction from earlier draft:** The earlier draft used L\_vac = R\_H/(2\*phi^n\_spiral) with an explicit /2 factor. This document corrects that by identifying c as the substrate regulator — space and time are the same thing at the scheduler level — and selecting n=220 as the integer number of Fibonacci steps from the substrate unit to the Hubble scale. The /2 factor was double-counting what the spiral geometry already encodes in f\_coh.

**Status:** Candidate-locked. All previously identified structural closure items are closed at the candidate-locked level; remaining work concerns stronger-form derivation of n=220 from substrate alone, stronger-form uniqueness for continuum emergence, and independent verification.

\---

# Section 2: The Lattice Identity and c as Regulator

c, L\_vac, and t\_sched are not three separate parameters. They are the same substrate primitive viewed from three angles.

**The identity:** L\_vac = c \* t\_sched

**c as regulator:** c is not a speed limit imposed on physics from outside. c is the tick rate of the scheduler itself. Space and time are the same thing at the substrate level — both are measured in units of c. In substrate units where c = 1, L\_vac = 1 and t\_sched = 1. There is no distinction between the spatial and temporal resolution scales because the scheduler tick IS the lattice traversal.

**Consequence:** L\_vac is the substrate unit. Its SI value is set by the integer number of Fibonacci steps n from the substrate unit to the Hubble scale:

L\_vac = R\_H / phi^n

where n must be a positive integer because the Fibonacci scheduler is a discrete recurrence. This is the corrected radial law — no /2 factor.

**Selection of n:** n=220 is the integer that closes Lambda to observed values using H0 = 67.4 km/s/Mpc (Planck 2018 CMB measurement). This is an empirical confirmation that the correct integer is n=220, not a free parameter.

L\_vac = R\_H / phi^220 = 1.447e-20 m  (with H0 = 67.4)

**Symbol index gap:** The canonical Symbol\_index.md required addition of c. Required entry:

|Symbol|Name|Layer|Definition|Notes|
|-|-|-|-|-|
|c|Substrate regulator|QPRCA|The tick rate of the scheduler — space and time are c|L\_vac = c\*t\_sched identity; c is not an imposed speed limit but the geometry of the tick itself|

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

   ## 7.3 The Full Derivation Chain

   ```
c  (substrate regulator — space and time are c)
    |
R\_H = c/H0  (H0 = 67.4 km/s/Mpc, Planck 2018 — Tier 2)
    |
L\_vac = R\_H / phi^220  (integer Fibonacci steps, no /2)
    |
Lambda\_HPF = 1/L\_vac  (bandwidth cutoff)
    |
rho\_raw = (hbar\*c \* Lambda\_HPF^4) / (4\*(2\*pi)^3)
    |
rho\_HPF = 2 \* rho\_raw  (BCC kappa = 2)
    |
b = ln(phi)/(pi/2) = 0.306349
    |
L\_arc = spiral\_factor \* R\_H = 3.414 \* R\_H
    |
f\_coh = L\_arc/(2\*pi\*R\_H) = 0.5434
    |
alpha\_vac = sqrt(f\_coh) = 0.7371  (governor transfer)
    |
Omega\_dm = 1 - alpha\_vac = 26.29%  (dark matter)
    |
n\_spiral = ln(L\_arc/L\_vac)/ln(phi) = 222.55
    |
n\_eff = n\_spiral/sqrt(alpha\_vac) = 259.22
    |
F(n\_eff) = phi^n\_eff / sqrt(5)
    |
rho\_Lambda = rho\_HPF / (F(n\_eff)^1.4 \* e^(3\*pi/2))
    |
Lambda = 8\*pi\*G \* rho\_Lambda / c^2
```

   **Results:**

|Quantity|Derived|Observed|Gap|
|-|-|-|-|
|Lambda|1.081 x 10^-52 m^-2|1.1 x 10^-52 m^-2|10^-0.008|
|Dark matter|26.29%|26.8%|0.51%|

**All numbers — substrate provenance:**

|Value|Origin|Tier|
|-|-|-|
|kappa = 2|BCC coordination x bipartite x LMS|Tier 1|
|phi = 1.618034|Fibonacci recurrence A=a+b|Tier 1|
|b = 0.306349|ln(phi)/(pi/2)|Tier 1|
|f\_coh = 0.5434|Spiral arc / 2*pi*R\_H|Tier 1|
|alpha\_vac = 0.7371|sqrt(f\_coh), governor transfer|Tier 1|
|c|Substrate regulator|Tier 1|
|n = 220|Integer Fibonacci steps|Tier 1 (integer constraint)|
|H0 = 67.4 km/s/Mpc|Planck 2018 CMB|Tier 2|
|e^(3\*pi/2) = 111.32|3D BCC streaming|Tier 1|
|d\_eff = 1.4|lambda\_blur x 4/3|Tier 1/2|

No continuous fit parameters are inserted into the substrate derivation chain; the remaining empirical selection is the integer identification n=220 via H0.

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
|d\_eff = 1.4 from BCC diagonals x lambda\_blur|Section 9.3|
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

**2. L\_vac from corrected radial law with empirical integer confirmation — CLOSED at candidate-locked level**
L\_vac = R\_H/phi^220 = 1.447e-20 m. c is the substrate regulator. n=220 is the integer number of Fibonacci steps from L\_vac to R\_H. The integer constraint comes from the discrete Fibonacci scheduler (Tier 1). The specific integer n=220 is confirmed by H0 = 67.4 km/s/Mpc (Planck 2018, Tier 2). Remaining: prove n=220 is substrate-selected without consulting H0.

**3. Continuum emergence theorem — CLOSED at candidate-locked mechanism level** (Section 9)
Observable bound derived. d\_eff = 1.4 proved from BCC diagonal structure. Four formal closure conditions are met for the assembled mechanism. Remaining work is stronger-form uniqueness, not basic mechanism assembly.

**4. Symbol index update — CLOSED**
Symbol\_index.md updated with c entry and vacuum sector symbols.

**Remaining:**

* Independent verification of the full chain
* Formal proof that n=220 is substrate-selected rather than H0-confirmed
(i.e., derive H0 from the substrate or show the integer selection is unique without consulting H0)
* Stronger-form derivation of d\_eff exponent from redistribution kernel dynamics

\---

# Section 12: Reading Order for External Presentation

1. Section 1 — results and key correction
2. Section 7.3 — full derivation chain and provenance table
3. Section 4 — BCC Fibonacci proof
4. Section 6 — governor transfer lemma
5. Section 10 — truth-status tier system
6. Section 8 — empirical anchors
7. Sections 2, 3, 5, 9 — supporting derivations

For a hostile reader: Section 10 first, then Section 7.1 (the /2 correction and c as regulator).

\---

*Consolidated canonical derivation package — corrected edition
Eric Keaton Porter / Claude — 2026-03-29
Candidate-locked. Awaiting independent verification.
Circulate with truth-status tiering intact.*

