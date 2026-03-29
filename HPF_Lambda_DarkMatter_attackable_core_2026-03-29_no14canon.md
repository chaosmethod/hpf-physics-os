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
