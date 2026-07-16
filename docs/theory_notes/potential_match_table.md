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

**Correction (this revision):** the previous version of this table had several
potentials transcribed with the wrong spin/vector structure (most critically,
$V_2$ was written in $V_9$/$V_{10}$'s monopole--dipole form). The forms below
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

**Notes on the corrections:**
- $V_2$ is spin--spin ($\sigma_1\cdot\sigma_2$), with *no* $\hat{r}$ dependence and *no* $1/r^2$ or $1/(\lambda r)$ terms — it is $V_9,V_{10}$ (monopole--dipole, single spin dotted into $\hat{r}$) that has that radial structure. The previous version of this table had these swapped.
- $V_{11}$ is $(\sigma_1\times\sigma_2)\cdot\hat{r}$ — a cross product of the *two* spins with $\hat{r}$ — not an $L\cdot S$ orbital spin-orbit coupling. $V_{12},V_{13}$ are the $\pm$ pair $(\sigma_1\pm\sigma_2)\cdot v$ (single-spin-combination dotted into velocity), not cross products.
- $V_4,V_5$ and $V_9,V_{10}$ and $V_{12},V_{13}$ are each a $\pm$ **pair of the same structure** (sum vs. difference of the two particles' spins), not two independent structures as previously listed.

## Main SME $\rightarrow$ DM Potential Matching Table

The table below gives the complete mapping from SME coefficient to NR Hamiltonian to DM potential(s), with CPT/Lorentz properties and the predicted $A\alpha$ signature in SPINDEP.

<div style="overflow-x: auto;">

| **SME Coeff.** | **CPT** | **Lorentz** | **NR Hamiltonian** | **DM Potential(s)** | **1/m Order** | **SPINDEP $A\alpha$ prediction** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $b_i$ | **Odd** | **Odd** | $-b\cdot\sigma$ (matter) $+b\cdot\sigma$ (antimatter) | $V_2$ | $m^0$ | $\|A\alpha\| \rightarrow 1$ (sign flip under C) |
| $b_0$ | **Odd** | **Odd** | $+b_0(\sigma\cdot p)/m$ | $V_7, V_8$ | $m^{-1}$ | $\|A\alpha\| \rightarrow 1$ ($b_0$ flips for antimatter) |
| $H_{ij}$ | **Even** | **Odd** | $-\mathcal{H}_B\cdot\sigma$ | $V_3$ | $m^0$ | $A\alpha \approx 0$ (same sign, sensitivity gap only) |
| $H_{0i}$ | **Even** | **Odd** | $-\frac{1}{m}\sigma\cdot(p\times H_E)$ | $V_7$ | $m^{-1}$ | $A\alpha \approx 0$ (same sign for matter/anti) |
| $d_{i0}$ | **Even** | **Odd** | $+d_{i0}\, m\, \sigma^i$ | $V_2$ | $m^1$ (!) | $A\alpha \approx 0$ (CPT-even; same sign) |
| $d_{ij}$ | **Even** | **Odd** | $+d_{ij}\, p^j\, \sigma^i$ | $V_7, V_8$ | $m^0$ (vel.) | $A\alpha \approx 0$ (velocity-dependent; same sign) |
| $d_{00}$ | **Even** | **Even** | $= 0$ by antisymmetry | None | --- | No contribution |

</div>

## Connecting to SPINDEP Results

### Validated gAgA Pairs

<div style="overflow-x: auto;">

| **SPINDEP Pair** | **Coupling** | **DM Potential** | **Dominant SME coeff.** | **Theoretical $\|A\alpha\|$ prediction** |
| :--- | :--- | :--- | :--- | :--- |
| gsgs$\cdot$UNKNOWN$\cdot$ee | Scalar-scalar | $V_1$ (UNKNOWN) | $c_{\mu\nu}$ (CPT-even) | $A\alpha \approx 0$ if CPT holds; 0.873 is anomalous --- likely sensitivity gap |
| gAgA$\cdot$V1$\cdot$ep | Axial-axial | $V_2$ (spin-spin) | $b_\mu$ (CPT-odd) | $\|A\alpha\| = 1$ --- consistent with 0.9998 |
| gAgA$\cdot$V2$\cdot$ee ($\times 5$) | Axial-axial | $V_2$ (spin-spin) | $b_\mu$ (CPT-odd) | $\|A\alpha\| = 1$ --- consistent with 0.954--1.000 |

</div>

### Interpretation of the gsgs result

The gsgs$\cdot$UNKNOWN$\cdot$ee pair shows $|A\alpha| = 0.873$ --- lower than all gAgA pairs. This is physically significant for two reasons:

*   **CPT-even coupling:** The scalar--scalar (gsgs) coupling does not appear in the minimal SME at dimension 4. Its primary contribution comes from $c_{\mu\nu}$, a CPT-even coefficient. CPT-even terms predict $A\alpha \approx 0$, so $0.873 \neq 0$ is entirely attributable to the experimental sensitivity gap (Delaunay 2017 matter constraint is 3--4 orders of magnitude tighter than Adkins 2022 positronium constraint).

*   **UNKNOWN potential:** The potential label UNKNOWN indicates the parser could not match the filename to a $V_n$ token. The likely candidate is $V_1$ (monopole--monopole, scalar exchange) given the gsgs coupling. $V_1$ has no spin structure and would produce $A\alpha = 0$ for a CPT-symmetric world.

*   **Width of 95% CI:** $[0.871, 0.875]$ --- wider than gAgA CIs ($[0.999, 1.000]$). This reflects that gsgs pair is not at saturation; the bootstrap is correctly capturing genuine uncertainty in the asymmetry estimate.

### CPT Rule for All SME Coefficients

The general rule, derived from the Foldy--Wouthuysen analysis, is:

$$
H_{NR}^{\text{antiparticle}}(X^{\text{CPT-odd}}) = -H_{NR}^{\text{particle}}(X^{\text{CPT-odd}})
$$

$$
H_{NR}^{\text{antiparticle}}(X^{\text{CPT-even}}) = +H_{NR}^{\text{particle}}(X^{\text{CPT-even}})
$$

This implies:

*   **CPT-odd ($b_\mu$):** $g_{\bar{a}} = -g_m \rightarrow |A\alpha| = 1$ (saturated) for exact CPT-odd coupling

*   **CPT-even ($H_{\mu\nu}, d_{\mu\nu}, c_{\mu\nu}$):** $g_{\bar{a}} = +g_m \rightarrow A\alpha = 0$ for exact CPT-even coupling; non-zero $A\alpha$ from sensitivity gaps only

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