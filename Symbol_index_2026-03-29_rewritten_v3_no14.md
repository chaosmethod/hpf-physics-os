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
