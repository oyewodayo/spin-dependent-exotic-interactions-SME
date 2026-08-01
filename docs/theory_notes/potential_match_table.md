# SME Coefficient $\leftrightarrow$ Dobrescu--Mocioiu Potential Matching Table

**Oyewo Temidayo**  
*University of Ibadan Postgraduate*

June 2026

**Note:** Theory Note 4 --- Master Reference  
**Repository:** `exotic-spin-interactions-SME/docs/theory_notes/potential_matching_table.md`

> *Complete reference: all SME operators $`\rightarrow`$ NR Hamiltonians $`\rightarrow`$ DM potentials $`V_1`$--$`V_{16}`$ $`\rightarrow`$ SPINDEP coupling*

---

## Overview

This document is the master reference connecting SME operator coefficients to Dobrescu--Mocioiu (DM) potentials to SPINDEP coupling labels. It synthesises the three FW derivation notes (Theory Notes 1--3) into a single lookup table and adds the complete $V_1$--$V_{16}$ DM potential catalogue with their explicit forms.

The primary use of this table in the SPINDEP framework is to interpret measured values of $A\alpha$ in terms of bounds on specific SME coefficients, and to predict which DM potential a given SME background field would generate in a two-body interaction.

## Notation and Conventions

| **Symbol** | **Meaning** |
| :--- | :--- |
| $\sigma_{1,2}$ | Pauli matrices acting on particle 1 or 2 |
| $\hat{r} = r/\|r\|$ | Unit vector from source to field point |
| $\lambda = 1/m_\phi$ | Mediator Compton wavelength (interaction range parameter) |
| $v = v_{\text{rel}}$ | Relative velocity of the two particles |
| $f, \bar{f}$ | Matter fermion and antimatter fermion |
| $\mathcal{H}_B^k = \frac{1}{2}\varepsilon^{ijk}H_{ij}$ | Dual magnetic-like vector from $H_{\mu\nu}$ |
| $b_\mu, H_{\mu\nu}, d_{\mu\nu}$ | SME coefficients: CPT-odd vector; CPT-even tensor; CPT-even axial tensor |

## Complete Dobrescu--Mocioiu Potential Catalogue

The forms below
are transcribed directly from Cong et al. (2025), Eqs. (1)--(12) [equivalent
to Dobrescu & Mocioiu (2006), Eqs. (3.1)--(3.16)], with $\sigma_X\to\sigma_1$,
$\sigma_Y'\to\sigma_2$, and $y(r) = e^{-r/\lambda}/(4\pi)$, $\lambda = 1/m_\phi$.
$\hat{r}$ points from particle 2 to particle 1, $v$ is their relative velocity,
and $m$ is the fermion mass relevant to the term (see Cong et al. for the
fully general two-mass $m_X, m_Y$ bookkeeping). The differential operators
$(1 - r\,d/dr)$ and $(1 - r\,d/dr + \tfrac{1}{3}r^2 d^2/dr^2)$ act on $y(r)$;
evaluated explicitly they contribute the extra $1/(\lambda r)$, $1/(\lambda^2 r^2)$
terms seen in $V_3$ below (worked out fully) and analogously for $V_4$--$V_7$,
$V_{15}$, $V_{16}$ (left in operator form here — see Cong et al. Sec. V for the
fully evaluated closed forms once specialised to a given coupling channel).

$$
V_1 = \frac{1}{r}\, y(r) \qquad \text{(monopole--monopole, spin-independent)}
$$

$$
V_2 = \frac{1}{r}\,(\sigma_1\cdot\sigma_2)\, y(r) \qquad \text{(dipole--dipole / spin--spin)}
$$

$$
V_3 = \frac{1}{m^2 r^3}\left[\sigma_1\cdot\sigma_2\left(1 - r\frac{d}{dr}\right) - 3(\sigma_1\cdot\hat{r})(\sigma_2\cdot\hat{r})\left(1 - r\frac{d}{dr} + \frac{r^2}{3}\frac{d^2}{dr^2}\right)\right] y(r)
$$

$$
\hphantom{V_3} = \frac{e^{-r/\lambda}}{4\pi m^2}\left\{\sigma_1\cdot\sigma_2\left[\frac{1}{r^3}+\frac{1}{\lambda r^2}\right] - (\sigma_1\cdot\hat{r})(\sigma_2\cdot\hat{r})\left[\frac{3}{r^3}+\frac{3}{\lambda r^2}+\frac{1}{\lambda^2 r}\right]\right\} \qquad \text{(tensor dipole--dipole)}
$$

$$
V_{4,5} = -\frac{1}{2mr^2}(\sigma_1 \pm \sigma_2)\cdot(v\times\hat{r})\left(1 - r\frac{d}{dr}\right) y(r) \qquad \text{(spin--velocity; $+$ = $V_4$, $-$ = $V_5$)}
$$

$$
V_{6,7} = -\frac{1}{2mr^2}\Big[(\sigma_1\cdot v)(\sigma_2\cdot\hat{r}) \pm (\sigma_1\cdot\hat{r})(\sigma_2\cdot v)\Big]\left(1 - r\frac{d}{dr}\right) y(r) \qquad \text{($+$ = $V_6$, $-$ = $V_7$)}
$$

$$
V_8 = \frac{1}{r}(\sigma_1\cdot v)(\sigma_2\cdot v)\, y(r) \qquad \text{(velocity--velocity)}
$$

$$
V_{9,10} = -\frac{1}{2mr^2}(\sigma_1 \pm \sigma_2)\cdot\hat{r}\left(1 - r\frac{d}{dr}\right) y(r) \qquad \text{(monopole--dipole; $+$ = $V_9$, $-$ = $V_{10}$)}
$$

$$
V_{11} = -\frac{1}{mr^2}(\sigma_1\times\sigma_2)\cdot\hat{r}\left(1 - r\frac{d}{dr}\right) y(r) \qquad \text{(spin cross-product; \emph{not} $L\cdot S$ spin-orbit)}
$$

$$
V_{12,13} = \frac{1}{2r}(\sigma_1 \pm \sigma_2)\cdot v\, y(r) \qquad \text{($+$ = $V_{12}$, $-$ = $V_{13}$)}
$$

$$
V_{14} = \frac{1}{r}(\sigma_1\times\sigma_2)\cdot v\, y(r)
$$

$$
V_{15} = -\frac{3}{2m^2r^3}\Big\{[\sigma_1\cdot(v\times\hat{r})](\sigma_2\cdot\hat{r}) + (\sigma_1\cdot\hat{r})[\sigma_2\cdot(v\times\hat{r})]\Big\}\left(1 - r\frac{d}{dr} + \frac{r^2}{3}\frac{d^2}{dr^2}\right) y(r)
$$

$$
V_{16} = -\frac{1}{2mr^2}\Big\{[\sigma_1\cdot(v\times\hat{r})](\sigma_2\cdot v) + (\sigma_1\cdot v)[\sigma_2\cdot(v\times\hat{r})]\Big\}\left(1 - r\frac{d}{dr}\right) y(r)
$$

**Structural notes:**
- $V_2$ is spin--spin ($\sigma_1\cdot\sigma_2$), with *no* $\hat{r}$ dependence and *no* $1/r^2$ or $1/(\lambda r)$ terms — it is $V_9,V_{10}$ (monopole--dipole, single spin dotted into $\hat{r}$) that has that radial structure, a distinct class.
- $V_{11}$ is $(\sigma_1\times\sigma_2)\cdot\hat{r}$ — a cross product of the *two* spins with $\hat{r}$ — not an $L\cdot S$ orbital spin-orbit coupling. $V_{12},V_{13}$ are the $\pm$ pair $(\sigma_1\pm\sigma_2)\cdot v$ (single-spin-combination dotted into velocity), not cross products.
- $V_4,V_5$ and $V_9,V_{10}$ and $V_{12},V_{13}$ are each a $\pm$ **pair of the same structure** (sum vs. difference of the two particles' spins), not independent structures.

## Main SME $\rightarrow$ DM Potential Matching Table

The table below gives the complete mapping from SME coefficient to NR Hamiltonian to DM potential(s), with CPT/Lorentz properties and the naive predicted $A\alpha$ signature.

A caveat on the "prediction" column below: it is tempting to substitute an exact, signed CPT-odd relation ($g_{\bar f}=-g_f$) directly into the SPINDEP formula $A_\alpha=(g_f-g_{\bar f})/(g_f+g_{\bar f})$ and conclude $|A\alpha|\to 1$. That substitution does not hold — the denominator vanishes and the expression diverges instead (verified with `sympy.limit` in `derivations/sympy/pauli_matrices.py`). More importantly, SPINDEP's actual inputs are independent, always-positive experimental *upper bounds*, not a signed measured coupling, so the signed substitution does not describe what is actually computed. Comparing two positive bounds of very different tightness drives $|A\alpha|\to 1$ regardless of CPT status — a sensitivity-gap effect. The predictions below should therefore be read as "**consistent with**," not "**caused by**," the stated CPT parity; see `FW_derivation_bmy.md` §4.2 for the full argument.

<div style="overflow-x: auto;">

| **SME Coeff.** | **CPT** | **Lorentz** | **NR Hamiltonian** | **DM Potential(s)** | **1/m Order** | **SPINDEP $A\alpha$ prediction** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $b_i$ | **Odd** | **Odd** | $-b\cdot\sigma$ (matter) $+b\cdot\sigma$ (antimatter) | $V_2$ | $m^0$ | Consistent with $\|A\alpha\|$ near 1, but equally consistent with a sensitivity gap (no sign-flip evidence from $A\alpha$ alone) |
| $b_0$ | **Odd** | **Odd** | $+b_0(\sigma\cdot p)/m$ | $V_7, V_8$ | $m^{-1}$ | Same caveat as $b_i$ |
| $H_{ij}$ | **Even** | **Odd** | $-\mathcal{H}_B\cdot\sigma$ | $V_3$ | $m^0$ | $A\alpha \approx 0$ expected if bounds are comparably sensitive; a sensitivity gap can still produce $\|A\alpha\|$ near 1 despite CPT-even physics |
| $H_{0i}$ | **Even** | **Odd** | $-\frac{1}{m}\sigma\cdot(p\times H_E)$ | $V_7$ | $m^{-1}$ | Same caveat as $H_{ij}$ |
| $d_{i0}$ | **Even** | **Odd** | $+d_{i0}\, m\, \sigma^i$ | $V_2$ | $m^1$ (!) | Same caveat as $H_{ij}$; **derived and verified** against Kostelecký & Lane (1999) Eq. 4 |
| $d_{ij}$ | **Even** | **Odd** | $+d_{ij}\, p^j\, \sigma^i$ | $V_7, V_8$ | $m^0$ (vel.) | Same caveat as $H_{ij}$; structure confirmed, overall sign open |
| $d_{00}$ | **Even** | **Odd** | $+d_{00}\,(\sigma\cdot p)$ | $V_8$ | $m^0$ (mom.) | Same caveat as $H_{ij}$; structure confirmed, overall sign open |

</div>

**Note on $d_{\mu\nu}$'s Lagrangian sector:** $d_{\mu\nu}$ is a *kinetic*-sector coefficient, paired with $c_{\mu\nu}$ and entering as $\tfrac12i\bar\psi\,d^{\mu\nu}\gamma_5\gamma_\mu\overleftrightarrow\partial_\nu\psi$ (Kostelecký & Lane, 1999) — not a mass-sector bilinear like $H_{\mu\nu}$'s $\bar\psi\gamma_5\sigma^{\mu\nu}\psi$. It is *traceless*, not antisymmetric, so $d_{00}$ need not vanish. Derived from this Lagrangian (`derivations/sympy/FW_dmunu_term.ipynb`), $d_{i0}\to V_2$ matches Kostelecký & Lane's own nonrelativistic Hamiltonian (their Eq. 4) exactly, and $d_{ij}\to V_7,V_8$ / $d_{00}\to V_8$ match in structure with an overall sign this equation-of-motion-level derivation leaves open — see `FW_derivation_dmunu.md` for the full account.

**Note on "consistent with" vs. "caused by":** because every SPINDEP $A\alpha$ value is a ratio of two independent one-sided bounds, an observed value near $\pm 1$ can arise either from a genuine CPT-odd signal *or* from nothing more than one experiment being much more sensitive than the other. Distinguishing the two requires independent information about the relative precision of the matter- and antimatter-sector measurements being compared — it cannot be read off $A\alpha$ alone. This applies uniformly to every row above, CPT-odd or CPT-even.

## Connecting to SPINDEP Results

### Validated gAgA Pairs

<div style="overflow-x: auto;">

| **SPINDEP Pair** | **Coupling** | **DM Potential** | **Dominant SME coeff.** | **Observed $\|A\alpha\|$ — consistent with, not proof of** |
| :--- | :--- | :--- | :--- | :--- |
| gsgs$\cdot$V1$\cdot$ee | Scalar-scalar | $V_1$ (confirmed; see below) | $c_{\mu\nu}$ (CPT-even) | $0.873$: consistent with a sensitivity-gap-dominated CPT-even channel |
| gAgA$\cdot$V1$\cdot$ep | Axial-axial | $V_2$ (spin-spin) | $b_\mu$ (CPT-odd) | $0.9998$: consistent with a CPT-odd sign flip, but equally consistent with a pure sensitivity gap |
| gAgA$\cdot$V2$\cdot$ee ($\times 5$) | Axial-axial | $V_2$ (spin-spin) | $b_\mu$ (CPT-odd) | $0.954$--$1.000$: same caveat as above |

</div>

### Interpretation of the gsgs result

The gsgs$\cdot$V1$\cdot$ee pair shows $|A\alpha| = 0.873$ --- lower than all gAgA pairs. Two notes:

*   **CPT-even coupling:** The scalar--scalar (gsgs) coupling does not appear in the minimal SME at dimension 4. Its primary contribution comes from $c_{\mu\nu}$, a CPT-even coefficient. A value below the gAgA pairs is *consistent with* a CPT-even channel and a sizeable sensitivity gap (Delaunay 2017 matter constraint is 3--4 orders of magnitude tighter than Adkins 2022 positronium constraint) — but, per the correction above, the gAgA pairs' higher values are *equally* explainable by a sensitivity gap alone, so the comparison between rows in this table cannot by itself distinguish "CPT-odd" from "CPT-even, larger sensitivity gap."

*   **Potential confirmed as $V_1$:** this pair's filenames (`Delaunay_2017`, `Adkins_2022_eeplus`) carry no potential-number token, so the parser records them as `UNKNOWN` by default. Both source papers were checked directly to resolve this: Delaunay, Frugiuele, Fuchs & Soreq (2017), *Phys. Rev. D* 96, 115002, constrain a spin-independent scalar interaction between electrons, and Adkins, Cassidy & Pérez-Ríos (2022), *Phys. Rept.* 975, 1, report a bound on the analogous spin-independent $g_s^eg_s^{e^+}$ coupling from positronium spectroscopy — both a direct match to $V_1$'s monopole--monopole, spin-independent definition. The classification is applied via `FILENAME_POTENTIAL_OVERRIDES` in `spindep/src/parser.py`, not by editing the raw source files. $V_1$ has no spin structure and would produce $A\alpha = 0$ for a CPT-symmetric world *if* the compared bounds were of comparable sensitivity. A further eleven filenames sit under a `# V1 / scalar exchange datasets` comment in the same override table without the potential-side fix applied — see `thesis/05_gap_analysis.tex` §5.4 for the list; these remain `UNKNOWN` pending the same source-verification step.

*   **Width of 95% CI:** $[0.871, 0.875]$ --- wider than gAgA CIs ($[0.999, 1.000]$). This reflects that the gsgs pair's bootstrap has more relative spread; it is not, by itself, evidence about CPT parity.

### CPT Rule for All SME Coefficients

The general rule, derived from the Foldy--Wouthuysen analysis, is:

$$
H_{NR}^{\text{antiparticle}}(X^{\text{CPT-odd}}) = -H_{NR}^{\text{particle}}(X^{\text{CPT-odd}})
$$

$$
H_{NR}^{\text{antiparticle}}(X^{\text{CPT-even}}) = +H_{NR}^{\text{particle}}(X^{\text{CPT-even}})
$$

This is a statement about a single, hypothetical *signed* coupling and its antiparticle counterpart. It does **not**, by itself, imply anything about the ratio of two independent experimental upper bounds:

*   **CPT-odd ($b_\mu$):** for an exact signed relation $g_{\bar a} = -g_m$, the SPINDEP formula $A_\alpha=(g_m-g_{\bar a})/(g_m+g_{\bar a})$ is undefined (0/0 in the exactly-equal-magnitude case) or diverges (for any small mismatch) — it does **not** evaluate to a bounded $|A\alpha|=1$. What actually produces $|A\alpha|\to 1$ in real SPINDEP output is two independent *positive* bounds of very different tightness, which happens regardless of CPT parity.

*   **CPT-even ($H_{\mu\nu}, d_{\mu\nu}, c_{\mu\nu}$):** $g_{\bar a} = +g_m$ for an exact signed relation gives $A\alpha = 0$ only if $g_m$ and $g_{\bar a}$ are numerically equal — again a statement about a hypothetical signed measurement, not about independent one-sided bounds, which will show whatever sensitivity gap exists between the two experiments regardless of the true CPT-even relation.

In short: **$A\alpha$ computed from upper bounds cannot currently distinguish CPT violation from an experimental sensitivity gap.** Doing so would require either (a) bounds of demonstrably comparable sensitivity, or (b) actual central-value measurements with symmetric errors instead of one-sided limits.

## Additional SME Coefficients (for completeness)

### $a_\mu$ (CPT-odd, Lorentz-odd)

The $a_\mu$ term $L_a = a_\mu\bar{\psi}\gamma^\mu\psi$ produces $H_{NR} = -a_0$ at order $m^0$ (scalar energy shift) and $-a_i v^i / m$ at order $m^{-1}$ (velocity-dependent). It does not generate a spin-dependent potential at leading order and therefore does not appear in the DM catalogue directly. It is CPT-odd, so antimatter picks up opposite sign: relevant for clock comparisons (ALPHA, BASE) but not for torsion-balance spin-dependent constraints.

### $c_{\mu\nu}$ (CPT-even, Lorentz-odd)

The $c_{\mu\nu}$ term $L_c = c_{\mu\nu}\bar{\psi}\gamma^\mu i\partial^\nu\psi$ generates momentum-dependent (direction-dependent) energy shifts. It is CPT-even. In the NR limit it contributes a direction-dependent kinetic energy modification that mimics a preferred-frame effect. For spin-dependent interactions it generates $V_2$-type couplings at subleading order. The gsgs sector may be sensitive to $c_{\mu\nu}$ if the mediator couples through the scalar current.

### $e_\mu, f_\mu$ (CPT-odd, higher dimension)

Dimension-4+ operators $e_\mu$ and $f_\mu$ are CPT-odd but velocity-dependent (odd under C but even under P). They contribute to $V_8$ and higher DM potentials. They are not yet constrained by SPINDEP pairs but will become accessible when gVgV and gpgp pairs are analysed with the v2.0 parser.

## References

1. Dobrescu, B.A. & Mocioiu, I. (2006). Spin-dependent macroscopic forces from new particle exchange. *JHEP* 11, 005. arXiv:hep-ph/0605342

2. Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. *Phys. Rev. D* 39, 683.

3. Kostelecký, V.A. & Lane, C.D. (1999). Nonrelativistic quantum Hamiltonian for Lorentz violation. *J. Math. Phys.* 40, 6245.

4. Kostelecký, V.A. & Mewes, M. (2001). CPT violation and the standard model. *Phys. Rev. D* 66, 056005.

5. Foldy, L.L. & Wouthuysen, S.A. (1950). On the Dirac theory of spin-1/2 particles. *Phys. Rev.* 78, 29.

6. Bailey, Q.G. & Kostelecký, V.A. (2006). Signals for Lorentz violation in post-Newtonian gravity. *Phys. Rev. D* 74, 045001.

7. Fadeev, P. et al. (2022). Revisiting spin-dependent forces mediated by new bosons. *Phys. Rev. A* 99, 022113.

8. Heckel, B.R. et al. (2008). Preferred-frame and CP-violation tests with polarized electrons. *Phys. Rev. D* 78, 092006.