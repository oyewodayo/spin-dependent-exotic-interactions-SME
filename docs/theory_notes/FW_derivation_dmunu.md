# Foldy–Wouthuysen Derivation of the $d_{\mu\nu}$ Term

**Oyewo Temidayo**
*CERN Summer Programme 2026*

June 2026

**Note:** Theory Note 3
**Repository:** `exotic-spin-interactions-SME/docs/theory_notes/FW_derivation_dmunu.md`

> *SME coefficient $d_{\mu\nu}$ $\rightarrow$ Non-relativistic Hamiltonian $\rightarrow$ Dobrescu–Mocioiu potentials $V_2$, $V_7$, $V_8$ *

---

## Overview

The SME coefficient $d_{\mu\nu}$ is a CPT-even, Lorentz-odd rank-2 tensor. Per
Kostelecký & Lane (1999), it is a **kinetic/derivative-sector** coefficient —
the axial-tensor partner of $c_{\mu\nu}$, not of $H_{\mu\nu}$ — entering the
Lagrangian through

$$
\mathcal L_d = \tfrac12 i\,\bar\psi\,d^{\mu\nu}\gamma_5\gamma_\mu\,\overleftrightarrow\partial_\nu\,\psi .
$$

$d_{\mu\nu}$ is **traceless**, not antisymmetric like $H_{\mu\nu}$, so $d_{00}$
need not vanish. Despite being CPT-even (same sign for matter and antimatter),
it generates a rich phenomenology because different components produce
non-relativistic Hamiltonians at different orders in $1/m$, spanning
Dobrescu–Mocioiu potentials $V_2$, $V_7$, and $V_8$.

The $d_{\mu\nu}$ term is particularly relevant for electron–nucleon scattering
experiments: $d_{i0}$ produces a large (order $m^1$) but momentum-independent
coupling to $\sigma^i$, while $d_{ij}$ and $d_{00}$ produce momentum-dependent
couplings.

### Key Results

* $d_{i0}$: $H_{NR} = +d_{i0}\,m\,\sigma^i$ (order $m^1$, large but static)
  $\to V_2$ — matches Kostelecký & Lane (1999) Eq. (4) exactly, sign included
  (`FW_dmunu_term.ipynb`).
* $d_{ij}$: $H_{NR} = +d_{ij}\,p^j\,\sigma^i$ (order $m^0$ in velocity)
  $\to V_7, V_8$ — structure matches Eq. (4); overall sign not yet reproduced
  by this level of derivation (see "Open point" below).
* $d_{00}$: $H_{NR} = +d_{00}\,(\boldsymbol\sigma\cdot\mathbf p)$ (order $m^0$
  in momentum) $\to V_8$, via the FW $\mathcal O^2/2m$ expansion — structure
  matches Eq. (4); sign likewise open.
* CPT-even: no sign flip for antimatter; $A_\alpha$ is predicted near $0$,
  subject to the same sensitivity-gap caveat discussed in
  `FW_derivation_bmy.md` §4.2.

---

## The SME Lagrangian Term

### Covariant Form

Kostelecký & Lane (1999, §II A, Eqs. 1–3) place $d_{\mu\nu}$ in the *kinetic*
sector of the general SME Dirac Lagrangian,

$$
\mathcal L = \tfrac12 i\bar\psi\Gamma^\nu\overleftrightarrow\partial_\nu\psi - \bar\psi M\psi,\qquad
M = m+a_\mu\gamma^\mu+b_\mu\gamma_5\gamma^\mu+\tfrac12 H_{\mu\nu}\sigma^{\mu\nu},\qquad
\Gamma^\nu = \gamma^\nu+c^{\mu\nu}\gamma_\mu+d^{\mu\nu}\gamma_5\gamma_\mu+\cdots,
$$

so $d_{\mu\nu}$'s contribution is the derivative-coupling term above, not a
bare $\bar\psi\gamma_5\sigma^{\mu\nu}\psi$ mass-sector bilinear — that
structure belongs to $H_{\mu\nu}$, inside $M$. Kostelecký & Lane state
directly that parameters in $M$ carry mass dimension while those in
$\Gamma^\nu$ are dimensionless, and that $c_{\mu\nu}$ and $d_{\mu\nu}$ are
*traceless* — $H_{\mu\nu}$ is the antisymmetric one. $d_{00}$ therefore need
not vanish.

Varying with respect to $\bar\psi$ gives the modified free Dirac equation

$$
\big(i\gamma^\mu\partial_\mu + i\,d^{\mu\nu}\gamma_5\gamma_\mu\partial_\nu - m\big)\psi = 0 .
$$

### CPT Properties

Kostelecký & Lane state explicitly that the field operators for
$a_\mu,b_\mu,e_\mu,f_\mu,g_{\lambda\mu\nu}$ are CPT-odd, and the rest —
including $c_{\mu\nu}$, $d_{\mu\nu}$, $H_{\mu\nu}$ — are CPT-even.
$d_{\mu\nu}$'s contribution to the effective coupling is therefore the same
for matter and antimatter; no sign flip is expected in the SPINDEP asymmetry
parameter $A_\alpha$ from this coefficient (subject to the sensitivity-gap
caveat in `FW_derivation_bmy.md` §4.2, which applies uniformly to every
CPT-even coefficient).

---

## FW Derivation by Component

Going to momentum space ($i\partial_\mu\to p_\mu$, metric $(+,-,-,-)$, so
$p_0=E$, $p_j=-p^j$ for physical momentum $p^j$):

$$
\big(\gamma^\mu p_\mu + d^{\mu\nu}p_\nu\,\gamma_5\gamma_\mu - m\big)\psi = 0 .
$$

Multiplying by $\gamma^0$ and solving for $E\psi=H\psi$ gives the free part
$H_0=\boldsymbol\alpha\cdot\mathbf p+\beta m$, plus the $d_{\mu\nu}$
correction

$$
H_d = -\,d^{\mu\nu}p_\nu\,\Gamma_\mu, \qquad \Gamma_\mu := \gamma^0\gamma_5\gamma_\mu \ \ (\text{lower-index } \mu).
$$

Direct computation (`dirac_algebra.py`, `derivations/sympy/FW_dmunu_term.ipynb`) gives

$$
\Gamma_0=-\gamma_5 \ \ (\text{odd}), \qquad \Gamma_i=+\Sigma^i \ \ (i=1,2,3;\ \text{even}).
$$

### Electric-axial and magnetic-axial components: $d_{i0}$, $d_{ij}$

Because $\Gamma_i=+\Sigma^i$ is already even, the $\mu=i$ piece of $H_d$
contributes directly to $H_{NR}$ with no FW iteration needed — exactly as
$b_i$ does for $b_\mu$ (`FW_derivation_bmy.md` §3.2a). Substituting $E\to m$
(the leading-order energy eigenvalue) and projecting onto the upper block,

$$
H_{NR}^{\text{even}} = \sum_i\Big({-d^{i0}m + \sum_j d^{ij}p^j}\Big)\sigma^i .
$$

Converting to Kostelecký & Lane's lower-index convention under the
$(+,-,-,-)$ metric ($d_{i0}=-d^{i0}$ for one lowered timelike index,
$d_{ij}=d^{ij}$ for two lowered spacelike indices):

$$
H_{NR}(d_{i0}) = +d_{i0}\,m\,\sigma^i, \qquad\qquad H_{NR}(d_{ij}) = +d_{ij}\,p^j\,\sigma^i .
$$

The $d_{i0}$ result matches Kostelecký & Lane's own nonrelativistic
Hamiltonian (their Eq. 4) exactly, including the sign. It is large (enhanced
by $m$) but does not produce a spatial gradient, so it does not contribute to
a force law directly; in a two-body interaction it contributes to $V_2$ as a
background spin-polarising field, with correspondingly tight experimental
bounds — current constraints from atomic magnetometry give
$|d_{i0}| < 10^{-25}$ GeV (Heckel et al. 2008).

The $d_{ij}$ result matches Eq. (4) in structure — a velocity-dependent
coupling to the spin, generating DM potentials $V_7,V_8$ — but this
derivation does not reproduce its overall sign relative to Eq. (4). See
"Open point" below.

### Pure temporal $d_{00}$ (and $d_{0j}$)

$\Gamma_0=-\gamma_5$ is odd, so this piece must instead be combined with the
leading odd operator $\boldsymbol\alpha\cdot\mathbf p$ through the standard
FW $\mathcal O^2/2m$ reduction, exactly as $b_0$ is treated for $b_\mu$. At
leading order the odd operator is

$$
\mathcal O_d = \big(d^{00}m - d^{0j}p^j\big)\gamma_5 ,
$$

and the FW cross term with $\boldsymbol\alpha\cdot\mathbf p$ gives, in closed
form,

$$
H_{NR}^{\text{odd}} = \Big(d_{00} - \frac{\mathbf d_0\cdot\mathbf p}{m}\Big)(\boldsymbol\sigma\cdot\mathbf p)
\;\xrightarrow{\text{leading order}}\;
H_{NR}(d_{00}) = +d_{00}\,(\boldsymbol\sigma\cdot\mathbf p) .
$$

$d_{00}$ does not vanish, consistent with $d_{\mu\nu}$ being traceless rather
than antisymmetric. This result matches Eq. (4) in structure, again with an
open overall sign, and generates DM potential $V_8$.

### Open point: the sign of the momentum-dependent terms

The $d_{i0}$ mass-enhancement term matches Kostelecký & Lane's Eq. (4)
exactly, sign included. The two momentum-dependent pieces, $d_{ij}$ and
$d_{00}$, match in operator structure but not in overall sign. The mismatch
is systematic — only the momentum-linear terms disagree, while the pure
mass-enhancement term is exact — which points to a specific missing
ingredient rather than a random error: Kostelecký & Lane's full derivation of
Eq. (4) includes a wavefunction-renormalization step for kinetic-sector
coefficients ($c_{\mu\nu}$, $d_{\mu\nu}$), since the modified kinetic term
shifts the canonical normalization of the plane-wave states. The plain
"substitute $i\partial_\nu\to p_\nu$ into the equation of motion" derivation
used here does not include that step. Repeating the derivation with
wavefunction renormalization included is the natural next piece of work on
this coefficient; until then, $d_{ij}\to V_7,V_8$ and $d_{00}\to V_8$ should
be cited with their magnitude and operator structure established, but their
overall sign noted as open.

---

## Two-Body Potentials and Matching

### $d_{i0} \rightarrow V_2$

The large $d_{i0}m\sigma^i$ coupling contributes to $V_2$ in the two-body
potential as the spin-polarised vertex. Since $H_{NR}(d_{i0})$ has the same
$\sigma^i$ (Zeeman-like) structure as the $b_i$ case, the two-body potential
it generates is likewise spin–spin, not monopole–dipole:

$$
V_2 \text{ contribution} \propto (d_{i0}\, m)^{(1)} (d_{i0}\, m)^{(2)} \times (\sigma_1 \cdot \sigma_2) \frac{e^{-r/\lambda}}{r} .
$$

$V_2$ is spin–spin ($\sigma_1\cdot\sigma_2$) with no $\hat r$ dependence — see
`potential_match_table.md` for the full $V_1$–$V_{16}$ catalogue.

### $d_{ij} \rightarrow V_7$ and $V_8$, $d_{00} \rightarrow V_8$

The velocity-dependent $d_{ij}$ term generates

$$
V_7 \propto d_{ij}\, \sigma^i\, v^j\, e^{-r/\lambda}/r , \qquad
V_8 \propto d_{ij}\, \{(\sigma \cdot v),\, e^{-r/\lambda}/r\} \quad \text{(anticommutator)},
$$

and $d_{00}$ contributes an additional $V_8 \propto d_{00}\,(\sigma\cdot v)\, e^{-r/\lambda}/r$ term.

## Summary Table

| **$d_{\mu\nu}$ component** | **NR Hamiltonian** | **DM Potential(s)** | **Order in $1/m$** | **Notes** |
| :--- | :--- | :--- | :--- | :--- |
| $d_{i0}$ (electric-axial) | $+d_{i0}\, m\, \sigma^i$ | $V_2$ | $m^1$ (large!) | Enhanced by fermion mass; matches Eq. (4) exactly, including sign; tight bounds |
| $d_{ij}$ (magnetic-axial) | $+d_{ij}\, p^j\, \sigma^i$ | $V_7, V_8$ | $m^0$ in velocity | Velocity-dependent; structure confirmed, overall sign open |
| $d_{00}$ | $+d_{00}\, (\sigma\cdot p)$ | $V_8$ | $m^0$ in momentum | Nonzero because $d_{\mu\nu}$ is traceless, not antisymmetric; structure confirmed, sign open |

## References

1. Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. *Phys. Rev. D* 39, 683.

2. Kostelecký, V.A. & Lane, C.D. (1999). *Constraints on Lorentz Violation from Clock-Comparison Experiments*. **Phys. Rev. D** 60, 116010. (Companion paper: Kostelecký & Lane, *Nonrelativistic quantum Hamiltonian for Lorentz violation*, J. Math. Phys. 40, 6245 (1999), reproduces the identical general formalism.)

3. Heckel, B.R. et al. (2008). Preferred-frame and CP-violation tests with polarized electrons. *Phys. Rev. D* 78, 092006.

4. Dobrescu, B.A. & Mocioiu, I. (2006). *JHEP* 11, 005.
