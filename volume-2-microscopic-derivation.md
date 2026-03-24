# HPF Canonical Presentation Package — Volume II
## Microscopic Derivation, Executable Development Line, and Theorem-Work Spine
### Consolidated Final Package State — Updated Epoch 2026-03-20

**Role of this volume:** This volume carries the microscopic derivation line, the toy/executable progression, the grouped-\(L_2\) legality branch, the March 20 reversible-registry and continuation-ambiguity corrections, the v0.2.7 bridge recalibration, and the current theorem-work chain for microscopic legality.

---

# 1. Executive consolidation outcome

The microscopic package now separates cleanly into four layers:

## Tier A — framework authority above the microscopic line
- `HPF_Master_Canonical_Framework_Epoch_2026-03-19_v2.md`
- Volume I of this package

## Tier B — current microscopic synthesis and working status
- the March 19 microscopic-legality working paper,
- this consolidated Volume II.

## Tier C — live theorem-work notes
- corrected Selection Lemma,
- continuation-ambiguity reformulation of the microscopic ambiguity burden,
- Capacity-Margin Lemma,
- Aggregation-Law Adequacy Lemma,
- Operator-Richness Lemma.

## Tier D — executable line and calibration artifacts
- v0.1 through v0.1.3 historical microscopic line,
- v0.2.0 through v0.2.7 enriched-canon executable line,
- current bridge recalibration matrix / JSON output.

---

# 2. Microscopic program status that remains fixed

The substrate-side legality target remains

\[
F(x,t)=\frac{M_{\rm req}^{(\rm micro)}(x,t)}{M_{\rm free}^{(\rm micro)}(x,t)},
\qquad
L_{\rm QPRCA}(x,t)=1 \iff F(x,t)<1.
\]

At deepest intended form, this is an existence statement over legal local bounded bijections. That strongest form is still open, but the target is sharp.

The local toy/executable line continues to use the 4-bit site alphabet

\[
(n_L,n_R,b,q),
\]

with reversible block-rule structure and exact predecessor counting inside the tested family.

---

# 3. What the v0.1.x line established

## 3.1 v0.1
First executable legality harness.

Representative baseline:
- additive,
- \(M_{\rm cap}=4\), \(\mu_P=1.0\),
- acceptance \(=0.25\),
- mean \(F_{\rm block}\approx1.32157\),
- mean predecessor count \(=6.0\),
- exact total load conservation.

## 3.2 v0.1.1
Applicable-rule predecessor algebra made predecessor multiplicity variable.

Observed predecessor histogram:
- 6 \(\to\) 120 outputs,
- 7 \(\to\) 100 outputs,
- 8 \(\to\) 32 outputs,
- 9 \(\to\) 4 outputs.

Gain: predecessor burden became structure-sensitive.
Limitation: raw \(\log_2 |P|\) overweighted predecessor cost and dominated rejection.

## 3.3 v0.1.2
Normalized predecessor baseline:

\[
P_{\rm norm}(O)=
\frac{\log_2 |\mathcal P(O)|-\log_2 P_{\min}}
{\log_2 P_{\max}-\log_2 P_{\min}}.
\]

Observed structure:
- 8 \(\to\) 64 outputs,
- 9 \(\to\) 128 outputs,
- 10 \(\to\) 64 outputs,
- bounds \(P_{\min}=8\), \(P_{\max}=10\).

Representative baseline:
- additive,
- \(M_{\rm cap}=4\), \(\mu_P=1.0\),
- acceptance \(\approx0.4078125\),
- mean \(F_{\rm block}\approx1.04536\),
- mean predecessor count \(\approx9.1375\),
- dominant rejection almost entirely collision-led.

Consolidated judgment retained:
- v0.1.2 remains the cleanest balanced historical baseline.

## 3.4 v0.1.3
Refined non-predecessor channel branch.

Representative baseline:
- additive,
- \(M_{\rm cap}=4\), \(\mu_P=1.0\),
- acceptance \(\approx0.384375\),
- mean \(F_{\rm block}\approx1.07922\),
- mean predecessor count \(\approx9.0625\),
- rejection ecology: \(B=283\), \(R=108\), \(A=3\), \(C=0\), \(P=0\).

Judgment retained:
- v0.1.3 is a richer non-predecessor ecological branch,
- but not a full replacement for v0.1.2.

---

# 4. Why the package moved beyond v0.1.x

The enriched March 19 rewrite imposed three new requirements that the historical v0.1.x line did not yet satisfy together:
- explicit legality / validity separation,
- explicit geometry-validity bridge stack,
- explicit derived-\(\zeta\) recovery from the modern layered canon.

That is why the package now treats v0.2.x as the live executable family.

---

# 5. Executable progression from v0.2.0 to v0.2.4

## 5.1 v0.2.0 — canonical enriched-canon executable
First executable reference aligned to Volume I logic.

What it carries:
- legality / validity separation,
- bridge stack \(U \to U_{\rm geom}^{(\rm NL)} \to \Lambda_{\rm geom} \to \chi^*_{\rm geom}\),
- separate \(\zeta\) and \(\chi^*_{\rm geom}\),
- current-canon treatment of route burden,
- first recovery-style projection back onto the older phase language.

## 5.2 v0.2.1 — first explicit derived-\(\zeta\) recovery line
The immediate recovery map introduced an effective-flux axis

\[
S_{\rm eff}=1+w_U U+w_{U_g}U_{\rm geom}^{(\rm NL)}+w_\Lambda \Lambda_{\rm geom}+w_{\rm loop}m_{\rm loop}+w_{\rm route}m_{\rm route}+w_F\Phi_F,
\]

with softened legality term

\[
\Phi_F=6[U_{\rm raw}-0.85]_+,
\]

followed by

\[
\zeta_{\rm derived}=1-\sigma(k(S_{\rm eff}-1.05)).
\]

Purpose: keep legality vs validity separation intact while restoring a smooth summary output.

## 5.3 v0.2.2 — grouped-\(L_2\) promotion
New live recommended combiner:

\[
F_{\rm grp-L2}=\frac{\sqrt{C^2+A^2}+P+\sqrt{B^2+R^2}}{M_{\rm free}}.
\]

Default 40-step comparison, seed 0:

### Baseline mode
- additive: acceptance \(\approx0.4078\), mean \(F\approx1.0454\), \(S_{\rm eff}=5.7889\), hard saturation,
- grouped-\(L_2\): acceptance \(\approx0.6172\), mean \(F\approx0.8563\), \(S_{\rm eff}\approx5.3325\), validity corridor,
- max: acceptance \(=1\), mean \(F\approx0.3178\), validity corridor.

### Refined mode
- additive: acceptance \(\approx0.3844\), mean \(F\approx1.0792\), hard saturation,
- grouped-\(L_2\): acceptance \(\approx0.7219\), mean \(F\approx0.8479\), validity corridor,
- max: acceptance \(=1\), mean \(F\approx0.3157\), validity corridor.

Interpretation:
- grouped-\(L_2\) removed immediate hard-collapse behavior produced by additive,
- acceptance rose strongly,
- but derived-\(\zeta\) still sat too deep in the corridor.

## 5.4 v0.2.3 — tuned effective-flux projection
Replaced linear map \(S_{\rm eff}=S_{\rm hard}S_{\rm raw}\) with power-compressed form

\[
S_{\rm eff}=S_{\rm onset}+(S_{\rm hard}-S_{\rm onset})S_{\rm raw}^{14},
\]

and softer logistic slope \(k=0.8\).

Results:
- default grouped-\(L_2\) runs moved to \(S_{\rm eff}\approx2.55\) rather than \(\approx5.33\),
- sweep band became roughly \(1.069 \lesssim S_{\rm eff} \lesssim 2.563\),
- onset and corridor were better represented.

But v0.2.3 introduced a topology problem:
- \(S_{\rm eff}\ge S_{\rm onset}=1.05\),
- so **stable_localized** became mathematically unreachable.

## 5.5 v0.2.4 — floor-fixed grouped-(L_2) derived-(\zeta) line
The piecewise anchored projection fixed the floor bug while preserving onset/corridor/hard ordering.

Recovered target cases:
- stable localized: `zeros`, baseline, \(M_{\rm cap}=6\), 1 step, \(\mu_P=0.5\),
  - \(S_{\rm eff}\approx0.547986\), \(\zeta\approx0.599075\),
- onset corridor: `zeros`, baseline, \(M_{\rm cap}=6\), 20 steps,
  - \(S_{\rm eff}=1.05\), \(\zeta=0.5\),
- validity corridor: `balanced_pairs`, baseline, \(M_{\rm cap}=4\), 80 steps,
  - \(S_{\rm eff}\approx2.004378\), \(\zeta\approx0.317886\),
- hard saturation: `single_L`, baseline, \(M_{\rm cap}=1.5\), 40 steps,
  - \(S_{\rm eff}=5.7889\), \(\zeta\approx0.022072\).

Current judgment at this stage:
- projection topology was repaired,
- but the microscopic burden channel and registry logic still needed one more round of cleanup.

## 5.6 theorem-spine clarification after v0.2.4
After the floor-fix, the theorem program was sharpened into an explicit spine:
- corrected Selection Lemma via \(F_{\min}\),
- bounded predecessor-pathology read,
- Capacity-Margin Lemma draft,
- Aggregation-Law Adequacy Lemma draft,
- explicit Operator-Richness bottleneck,
- first honest conditional sufficiency theorem rather than premature strongest-form closure.

This clarified the true frontier: the next issue was no longer just calibration of the derived-\(\zeta\) projection, but whether the live operator family and the active burden channels actually matched the intended reversible legality target.

## 5.7 v0.2.5 — reversible registry repair
Operator-richness analysis exposed a real registry defect in the then-live line: one named rule failed the file's own bijection check while the rest passed.

The immediate repair step was to replace that bad rule with a reversible equal-queue toggle so that the operator family became fully bijective as coded.

This fixed a genuine theorem-level problem, but it also exposed a deeper diagnostic issue:
- once the registry is fully reversible,
- the old raw predecessor-count burden goes flat by construction,
- because every output now has exactly one preimage per bijective rule.

So v0.2.5 repaired reversibility, but also showed that the existing predecessor-burden channel was no longer the right observable for the repaired registry.

## 5.8 continuation-ambiguity redefinition of the predecessor channel
The next correction was conceptual rather than cosmetic.

The old predecessor burden had been tied to output-side preimage multiplicity:

\[
P_{\rm norm}(O)=
\frac{\log_2 |\mathcal P(O)|-\log_2 P_{\min}}
{\log_2 P_{\max}-\log_2 P_{\min}}.
\]

That worked while predecessor counts varied across outputs, but it becomes trivial in a fully bijective finite registry.

The replacement channel therefore shifts from **raw predecessor count** to **input-conditioned continuation ambiguity** over the reversible operator family. The theorem-safe interpretation is:

> for a fixed local input, how many materially distinct reversible continuations remain available, and how evenly are they represented across the admissible local rule family?

Fix a local input block
\[
\psi_{\rm in}\in\mathcal S_{\rm loc},
\]
a finite admissible reversible family
\[
\mathcal O_{\rm rev}=\{\hat T_1,\dots,\hat T_N\},
\]
and let
\[
O_i:=\hat T_i(\psi_{\rm in}).
\]

Define a continuation-signature map
\[
\Sigma(O_i)
\]
that retains the physically relevant local continuation features rather than irrelevant rule labels. A theorem-safe minimal signature should track features such as:
- transport direction pattern,
- occupancy / collision resolution pattern,
- queue or reservoir engagement,
- blockage / scratch use,
- anisotropy class.

Two outputs are assigned to the same continuation class when
\[
O_i\sim O_j \iff \Sigma(O_i)=\Sigma(O_j).
\]

Let the resulting class weights be \(p_\kappa\). Then the effective continuation multiplicity is

\[
N_{\rm eff}^{(\rm cont)}(\psi_{\rm in})
=
\frac{1}{\sum_\kappa p_\kappa^2},
\]

and the normalized ambiguity burden is read through a logarithmic map of the form

\[
P_{\rm cont}(\psi_{\rm in})
=
\frac{\log N_{\rm eff}^{(\rm cont)}(\psi_{\rm in})}
{\log N_{{\rm eff,max}}^{(\rm cont)}+\varepsilon}.
\]

Interpretation:
- low burden when the reversible rules effectively agree on one continuation class,
- higher burden when legal reversible continuations split across several materially distinct continuation classes,
- nontrivial burden even when every coded rule is bijective.

This change aligns the microscopic line better with the broader HPF use of participation-ratio effective multiplicities in other ambiguity channels. Canon-level prose should therefore stop calling the live \(P\)-channel simply “predecessor burden”; it is now better read as **microscopic continuation ambiguity burden** or **local operator ambiguity burden**.

## 5.9 v0.2.6 — continuation-ambiguity executable patch
The executable line was then patched so the active \(P\)-channel measures continuation ambiguity instead of raw predecessor count.

This produced the first important positive result after the registry repair:
- the \(P\)-channel becomes alive again under a fully reversible registry,
- stable-localized becomes reachable again,
- corridor behavior survives,
- but the old bridge proxy now needed recalibration because mean-\(F\) alone became too lossy.

So v0.2.6 established the correct new microscopic burden concept, but not yet the final bridge behavior.

## 5.10 v0.2.7 — bridged continuation-ambiguity line
The next and current executable correction was to recalibrate the bridge itself while keeping the two-wall architecture intact.

The crucial change was not merely threshold retuning. The bridge's coarse legality proxy was strengthened by adding legality-tail information, so hard-edge cases are distinguished by actual violation/excess structure rather than washed out by the mean.

The active coarse legality-pressure proxy is

\[
F_{\rm bridge}
=
\operatorname{clip}\!\left[
U
+0.35\,\nu_F
+0.50\,\overline{(F-1)_+}
\right]_{[0,1]},
\]

where:
- \(U\) is the mean closure-load proxy,
- \(\nu_F\) is the fraction of block updates with \(F_{\rm block}\ge 1\),
- \(\overline{(F-1)_+}\) is the mean legality excess above the hard wall.

The current recalibrated derived axis is then

\[
S_{\rm raw}
=
0.12\,U
+0.12\,\Lambda_{\rm geom}
+0.10\,U_{\rm geom}^{(\rm NL)}
+0.60\,\nu_F
+1.40\,\overline{(F-1)_+}
+0.10(1-a)
+0.25R,
\]

followed by the same floor-fixed projection back to \(S_{\rm eff}\).

This preserves the canonical stack

\[
U \to U_{\rm geom}^{(\rm NL)} \to \Lambda_{\rm geom} \to \chi_{\rm geom}^*,
\qquad
F \to L_{\rm QPRCA},
\]

without collapsing legality into validity.

Observed current recheck reading:
- stable localized: recovered,
- onset corridor: recovered,
- validity corridor: recovered,
- hard saturation: recovered.

Current anchor values:
- stable localized: \(S_{\rm eff}=0.600637\),
- onset corridor: \(S_{\rm eff}=1.050000\),
- validity corridor: \(S_{\rm eff}=2.212534\),
- hard saturation: \(S_{\rm eff}=5.788900\).

Current judgment:
- the reversible-registry defect has been repaired,
- the predecessor-burden concept has been replaced by a continuation-ambiguity burden that survives full reversibility,
- the bridge has been recalibrated accordingly,
- and the active executable state is now the bridged continuation-ambiguity line rather than the older raw predecessor-count line.

---

# 6. The corrected theorem-work chain

## 6.1 Corrected Selection Lemma
The first draft was circular. The corrected object is

\[
F_{\min}(\psi_{\rm in})=\min_{\hat T\in\mathcal O_{\rm QPRCA}}F(\psi_{\rm in};\hat T).
\]

Corrected statement:

\[
F_{\min}(\psi_{\rm in})<1 \Rightarrow \exists \hat T\in\mathcal O_{\rm QPRCA}\text{ with }F(\psi_{\rm in};\hat T)<1.
\]

This is the non-circular selection bridge.

## 6.2 Historical predecessor-pathology evidence retained for lineage
Before the reversible-registry repair, executable sweep evidence supported the weaker claim that worst-form universal predecessor saturation was not observed in the tested finite family:
- predecessor counts only took values in \(\{8,9,10\}\),
- no tested input block had all candidate outputs pinned at \(P_{\max}=10\),
- half the 256 local blocks showed a rule-insensitive surcharge at \(9\),
- the other half retained an \(8/10\) split across tested rules.

Interpretation:
- worst-form universal predecessor collapse was not observed,
- but this is now a **historical** diagnostic tied to the older raw predecessor-count observable rather than the final microscopic burden primitive.

## 6.3 Current theorem-safe ambiguity reformulation
After the registry is repaired to full bijectivity, raw predecessor count is no longer the correct primitive burden notion. The theorem-facing question therefore becomes:

> for a given local input, does the reversible operator family collapse effectively to one continuation class, or does it retain a nontrivial continuation-ambiguity burden?

The corresponding weak-form boundedness question is no longer about bounded raw predecessor counts. It is about bounded

\[
N_{\rm eff}^{(\rm cont)}(\psi_{\rm in})
\]

and the resulting normalized ambiguity burden \(P_{\rm cont}(\psi_{\rm in})\).

Current truth-safe status:
- the executable line already uses a continuation-ambiguity replacement rather than raw predecessor count,
- the exact continuation-signature map \(\Sigma\) remains candidate-locked rather than fully closed,
- predecessor-only trapped-case counts remain useful as historical evidence about the older line, but they should not be treated as the final theorem object under the repaired registry.

## 6.4 Capacity-Margin Lemma (draft)
Working claim:
Once universal predecessor trapping is excluded, remaining illegality near threshold is primarily a **margin problem**, not a pure selection impossibility.

Supporting structure:
- finite operator family implies attained minimum burden,
- increasing free margin strictly lowers additive \(F\) for fixed channel burdens,
- disappearance of predecessor-only failures by \(M_{\rm cap}=6\) supports capacity recoverability.

Current status:
- proposed / partially supported by executable sweep.

## 6.5 Aggregation-Law Adequacy Lemma (draft)
Current sharp question:
Does the present aggregate law track genuine bounded reversible impossibility, or does it over-reject skewed but still executable local updates?

This is now the main theorem-level bottleneck after predecessor pathology and capacity-margin interpretation were partially separated.

A valid legality combiner should be:
- monotone in true burden channels,
- sensitive to rising total strain,
- but not so strict that skewed-yet-executable states are systematically mislabeled illegal.

This is why grouped-\(L_2\) promotion matters architecturally: it is not just a numerics tweak but an active adequacy test on the legality combiner.

## 6.5A Operator-Richness Lemma (checkpoint status)
The theorem spine still needs one explicit bridge between formal minimization and operational availability:

> Is the minimizing object in \(F_{\min}\) ranging over a genuinely available local update family, or only over a formal comparison set?

The current executable line now supports a better answer than before:
- the registry is finite and explicit,
- the minimizer is automatically attained,
- the coded rule family is nontrivial rather than single-branch,
- and the old non-bijective defect that undermined registry honesty has been repaired.

What still remains open is stronger constitutive richness:
- whether the present rule family spans enough of the intended local transport / queue / storage / rerouting possibilities,
- whether the continuation-signature classes are already sharp enough,
- and whether the present finite registry is representative enough for stronger sufficiency claims.

Current status:
- **finite operational minimization is real,**
- **full operator-richness closure is not yet complete.**

## 6.6 Resulting sufficiency-program wording
The package can now honestly say:

> The first microscopic legality lemma has been corrected into a non-circular selection form using \(F_{\min}\). Preliminary executable sweeps indicate that worst-form predecessor saturation traps are absent in the current operator family, but predecessor burden remains capable of triggering rejection under tight free-margin conditions. Capacity-margin collapse is real, and aggregation adequacy remains open. Thus the sufficiency program remains alive, but strongest-form closure is still premature.

---

# 7. Current best executable reference rule

For the current package state:
- **historical stable baseline:** v0.1.2,
- **current active enriched-canon branch:** v0.2.7 bridged continuation-ambiguity line.

That distinction matters. v0.1.2 is still the cleanest historical microscopic baseline, but it is no longer the most up-to-date executable line for the enriched canon.

---

# 8. Immediate next technical work

1. broader aggregation stress sweeps across grouped-\(L_2\), additive, and other overlap-aware candidate combiners,
2. broader v0.2.7 trajectory validation,
3. constitutive sharpening of continuation-signature classes and operator-family richness beyond the present finite registry,
4. constitutive sharpening of blockage/reservoir/anisotropy channels,
5. promotion of the current bridge recalibration from support-model status toward a more principled lower-wall constitutive law.
