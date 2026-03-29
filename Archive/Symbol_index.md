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

*Added 2026-03-27. These symbols appear in the Lambda and dark matter derivation package.*

| Symbol | Name | Definition | Notes |
|------|------|------------|-------|
| $L_{vac}$ | Substrate resolution scale | Lattice site spacing; $L_{vac} = c \cdot t_{sched}$ | Current instrumental limit $\sim 10^{-19}$ m; substrate-derived value $= R_H / (2\varphi^{n_{spiral}}) = 1.465 \times 10^{-20}$ m |
| $\varphi$ | Golden ratio | Asymptotic growth rate of BCC bipartite coherent update sequences | $\varphi = (1+\sqrt{5})/2 = 1.618...$; emerges from Fibonacci recurrence, not imposed |
| $b$ | Fibonacci spiral growth parameter | $b = \ln\varphi / (\pi/2)$ | Sets the causal boundary spiral geometry |
| $f_{coh}$ | Coherent support fraction | $f_{coh} = L_{arc} / (2\pi R_H)$ | Fraction of spherical vacuum boundary coherently supportable per tick |
| $\alpha_{vac}$ | Vacuum update availability | $\alpha_{vac} = \sqrt{f_{coh}}$ | Derived via governor transfer law; $\alpha_{vac} \approx 0.7371$ |
| $n_{spiral}$ | Fibonacci recursion depth | $n_{spiral} = \ln(L_{arc}/L_{vac}) / \ln\varphi$ | Number of coherent update steps from $L_{vac}$ to $R_H$ along spiral |
| $\kappa_{BCC}$ | BCC geometric coefficient | $\kappa_{BCC} = 8 \times (1/2) \times (1/2) = 2$ | Coordination number $\times$ bipartite $\times$ LMS mirror |
| $\varepsilon$ | Continuum correction | $\varepsilon = (1-\zeta(S_f)) \cdot (L_{vac}/\ell_O)^{d_{eff}}$ | Discrete-substrate residual for observable at scale $\ell_O$ |
| $d_{eff}$ | Effective redistribution dimension | $d_{eff} = \lambda_{blur} \times (4/3) = 1.4$ | Derived from BCC 4-diagonal structure $\times$ blur threshold |

---

## 8. Phase Boundaries (Reference)

| Quantity | Boundary | Interpretation |
|---------|----------|----------------|
| $S_f < 1.05$ | Below blur threshold | Fully coherent local updates; discrete substrate maximally hidden |
| $S_f \approx 1.05$ | Lu blur threshold ($\lambda_{blur}$) | Coherence loss onset; $\zeta = 0.5$; redistribution begins | 
| $S_f < 1.4$ | Einstein phase | Laminar geometry; GR valid effective expert |
| $1.4 < S_f < 5.79$ | Quantum phase | Turbulent geometry |
| $S_f > 5.79$ | Decoherence | Raw geometry collapse |
| $\sigma_{\max} \ge 1$ | Illegal | Route to UHET |
| $G_{health} < 0.3$ | Metric failure | Route to QPRCA |
| $d_{eff} = \lambda_{blur} \times (4/3)$ | Phase boundary relationship | $S_f = 1.4$ and $S_f = 1.05$ are not independent — derived from same BCC diagonal structure |

---

## 9. Provenance Note

This index was updated on 2026-03-27 to add:

- $c$ (substrate propagation limit) to Section 2 — closes gap identified in HPF Lambda/dark matter derivation package
- Section 7 (Vacuum Sector Symbols) — new symbols from the Lambda and dark matter derivation
- Section 8 updated — blur threshold $S_f = 1.05$ added; phase boundary relationship $d_{eff} = \lambda_{blur} \times (4/3)$ documented

The Lambda and dark matter derivation package is: `HPF_Lambda_DarkMatter_Canonical_2026-03-27.md`

Prior version of this index was standalone in the old repo structure. This version should travel with the Volume I–III canonical package.

---

This index defines symbols only. All derivations live in their respective documents.

---

**End of Canonical Index**
