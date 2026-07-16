# Foldy--Wouthuysen Derivation of the $d_{\mu\nu}$ Term

**Oyewo Temidayo**  
*CERN Summer Programme 2026*

June 2026

**Note:** Theory Note 3  
**Repository:** `exotic-spin-interactions-SME/docs/theory_notes/FW_derivation_dmunu.md`

> *SME coefficient $`d_{\mu\nu}`$ $`\rightarrow`$ Non-relativistic Hamiltonian $`\rightarrow`$ Dobrescu--Mocioiu potentials $`V_2`$, $`V_7`$, $`V_8`$*

---

## Overview

The SME coefficient $d_{\mu\nu}$ is a CPT-even, Lorentz-odd rank-2 tensor coupling involving $\gamma_5$: $L_d = d_{\mu\nu}\,\bar{\psi}\,\gamma_5\,\sigma^{\mu\nu}\,\psi$. It is the 'axial tensor' partner of $H_{\mu\nu}$. Despite being CPT-even (same sign for matter and antimatter), it generates a rich phenomenology because different components produce NR Hamiltonians at different orders in $1/m$, spanning potentials $V_2$, $V_7$, and $V_8$.

The $d_{\mu\nu}$ term is particularly important for electron--nucleon scattering experiments because $d_{i0}$ produces a large (order $m^1$) but momentum-independent coupling to $\sigma^i$, while $d_{ij}$ produces a velocity-dependent coupling and $d_{00}$ gives a momentum-dependent spin coupling.

---

**Unresolved — flagged, not yet fixed (this revision):** while completing the executable `derivations/sympy/` notebooks for `b_μ` and `H_μν`, a real Dirac-algebra sign error was found and fixed in the `b_μ` notebook (see `FW_bmu_term.ipynb` §2–3, and the correction notes in `FW_derivation_bmy.md`) — it was only caught by actually running the symbolic computation rather than trusting the hand-derived prose. Applying that same numeric check here (`gamma[0]*gamma5*sigma_munu(i,0)` in `dirac_algebra.py`'s tooling) for the electric-axial $d_{i0}$ term gives an **even**, $O(m^0)$, *imaginary*-coefficient operator ($\propto -i\,\Sigma^i\beta$) — not the real, $O(m^1)$, mass-*enhanced* $+d_{i0}\,m\,\sigma^i$ claimed below. The claimed order-$m^1$ enhancement does not fall out of the same direct $\gamma^0\Gamma$ projection that correctly reproduced the $b_\mu$ and $H_{\mu\nu}$ results, and re-deriving it properly needs more careful multi-step work than could be verified in this pass. **Treat the "Key Results" below as unverified pending a dedicated `FW_dmunu_term.ipynb` notebook** (not yet created) that checks each claim numerically the way the other two notebooks now do — do not cite the $d_{i0}\to V_2$ mass-enhancement claim in the thesis until that verification is done.

### Key Results (unverified — see caveat above)

*   $d_{i0}$: $H_{NR} = +d_{i0}\, m\, \sigma^i$ (order $m^1$, large but static) $\rightarrow V_2$
*   $d_{ij}$: $H_{NR} = +d_{ij}\, p^j\, \sigma^i$ (order $m^0$ in velocity) $\rightarrow V_7, V_8$
*   $d_{00}$: $H_{NR} = +d_{00}\, \sigma \cdot p$ (order $m^0$ in momentum) $\rightarrow V_8$
*   CPT-even: NO sign flip for antimatter; $A\alpha$ predicted near 0

---

## The SME Lagrangian Term

### Covariant Form

The $d_{\mu\nu}$ Lagrangian is:

$$
L_d = d_{\mu\nu}\, \bar{\psi}\, \gamma_5\, \sigma^{\mu\nu}\, \psi \qquad \text{where } \sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu]
$$

$d_{\mu\nu} = -d_{\nu\mu}$ is real and antisymmetric with 6 independent components: three $d_{i0}$ (electric-axial) and three $d_{ij}$ (magnetic-axial). Additionally $d_{00} = 0$ by antisymmetry.

*Note:* in some SME references, $d_{\mu\nu}$ absorbs additional factors. Throughout this note we follow the convention of Kostelecký & Lane (1999).

### CPT Properties

Under CPT: $\bar{\psi}\gamma_5\sigma^{\mu\nu}\psi \rightarrow +\bar{\psi}\gamma_5\sigma^{\mu\nu}\psi$ (the combination $\gamma_5\sigma^{\mu\nu}$ is CPT-even). Therefore $L_d$ is CPT-even. Under C: the bilinear $\bar{\psi}^c\gamma_5\sigma^{\mu\nu}\psi^c = +\bar{\psi}\gamma_5\sigma^{\mu\nu}\psi$ (same sign). The $d_{\mu\nu}$ contribution to $g_{\text{coupling}}$ is therefore the same for matter and antimatter.

## FW Derivation by Component

### Electric-axial components $d_{i0}$

The combination relevant to $d_{i0}$ is $\gamma^0\gamma_5\sigma^{i0} = \gamma^0\gamma_5\frac{i}{2}[\gamma^i,\gamma^0]$. In the Dirac representation:

$$
\gamma^0\gamma_5\sigma^{i0} = +m\Sigma^i = \mathrm{diag}(+m\sigma^i, +m\sigma^i)
$$

This is an even operator at order $m^1$. The NR Hamiltonian from $d_{i0}$ is therefore:

$$
H_{NR}(d_{i0}) = +d_{i0}\, m\, \sigma^i
$$

This term is large (enhanced by $m$) but does not produce a spatial gradient and therefore does not contribute to a force law directly. In a two-body interaction, it contributes to $V_2$ as a background spin-polarising field. Experimental bounds on $d_{i0}$ from torsion balance experiments are correspondingly tight.

### Magnetic-axial components $d_{ij}$

For the spatial antisymmetric components $d_{ij}$, the relevant combination is:

$$
\gamma^0\gamma_5\sigma^{ij} = \frac{i}{2}\gamma^0\gamma_5[\gamma^i,\gamma^j]
$$

Expanding in the Dirac representation and using $\gamma_5\gamma^i = \gamma^5\gamma^i$, one obtains an odd matrix at zeroth order that becomes even at order $m^{-1}$ after the FW transformation. The result involves the momentum operator:

$$
H_{NR}(d_{ij}) = +d_{ij}\, p^j\, \sigma^i \quad \text{[summed over } i,j\text{]}
$$

This is a velocity-dependent (momentum-dependent) coupling to the spin. It generates DM potentials $V_7$ (antisymmetric in $\sigma \cdot v$ form) and $V_8$ (anticommutator of $\sigma$ and $v$).

### Pure temporal $d_{00} = 0$

By antisymmetry of $d_{\mu\nu}$, $d_{00} = 0$ identically. The notation $d_{00}$ in some references refers to the trace $d_{\mu\mu} \equiv g^{\mu\nu}d_{\mu\nu}$ which is separately zero for an antisymmetric tensor. No NR contribution.

## Two-Body Potentials and Matching

### $d_{i0} \rightarrow V_2$

The large $d_{i0}m\sigma^i$ coupling contributes to $V_2$ in the two-body potential as the spin-polarised vertex. Since $H_{NR}(d_{i0})$ has the same $\sigma^i$ (Zeeman-like) structure as the $b_i$ case, the two-body potential it generates is likewise spin--spin, not monopole--dipole:

$$
V_2 \text{ contribution} \propto (d_{i0}\, m)^{(1)} (d_{i0}\, m)^{(2)} \times (\sigma_1 \cdot \sigma_2) \frac{e^{-r/\lambda}}{r}
$$

**Correction (this revision):** this previously used the monopole--dipole radial form $(\sigma_1\cdot\hat r)[1/(\lambda r)+1/r^2]e^{-r/\lambda}$, which belongs to $V_9,V_{10}$, not $V_2$. $V_2$ is spin--spin ($\sigma_1\cdot\sigma_2$) with no $\hat r$ dependence — see `potential_match_table.md` for the corrected $V_1$--$V_{16}$ catalogue.

The large $m$ factor means even very small $d_{i0}$ coefficients produce potentially observable effects. Current bounds from atomic magnetometry constrain $|d_{i0}| < 10^{-25}$ GeV (Heckel et al. 2008).

### $d_{ij} \rightarrow V_7$ and $V_8$

The velocity-dependent $d_{ij}$ term generates:

$$
V_7 \propto d_{ij}\, \sigma^i\, v^j\, e^{-r/\lambda}/r
$$

$$
V_8 \propto d_{ij}\, \{(\sigma \cdot v),\, e^{-r/\lambda}/r\} \quad \text{(anticommutator)}
$$

## Summary Table

| **$d_{\mu\nu}$ component** | **NR Hamiltonian** | **DM Potential(s)** | **Order in $1/m$** | **Notes** |
| :--- | :--- | :--- | :--- | :--- |
| $d_{i0}$ (electric-axial) | $+d_{i0}\, m\, \sigma^i$ | $V_2$ | $m^1$ (large!) | Enhanced by fermion mass; tight bounds |
| $d_{ij}$ (magnetic-axial) | $+d_{ij}\, p^j\, \sigma^i$ | $V_7, V_8$ | $m^0$ in velocity | Velocity-dependent; needs moving sources |
| $d_{00}$ | $= 0$ by antisymmetry | None | --- | Identically zero |

## References

1. Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. *Phys. Rev. D* 39, 683.

2. Kostelecký, V.A. & Lane, C.D. (1999). Nonrelativistic quantum Hamiltonian for Lorentz violation. *J. Math. Phys.* 40, 6245.

3. Heckel, B.R. et al. (2008). Preferred-frame and CP-violation tests with polarized electrons. *Phys. Rev. D* 78, 092006.

4. Dobrescu, B.A. & Mocioiu, I. (2006). *JHEP* 11, 005.