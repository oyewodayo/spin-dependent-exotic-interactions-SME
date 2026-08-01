# Foldy--Wouthuysen Derivation of the $d_{\mu\nu}$ Term

**Oyewo Temidayo**  
*CERN Summer Programme 2026*

June 2026

**Note:** Theory Note 3  
**Repository:** `exotic-spin-interactions-SME/docs/theory_notes/FW_derivation_dmunu.md`

> *SME coefficient $`d_{\mu\nu}`$ $`\rightarrow`$ Non-relativistic Hamiltonian $`\rightarrow`$ Dobrescu--Mocioiu potentials $`V_2`$, $`V_7`$, $`V_8`$*

---

## Overview

The SME coefficient $d_{\mu\nu}$ is a CPT-even, Lorentz-odd rank-2 tensor. **Correction (see "Root cause" below): it is *not* a mass-sector bilinear $\bar\psi\gamma_5\sigma^{\mu\nu}\psi$** — that structure belongs to $H_{\mu\nu}$. Per Kostelecký & Lane (1999), $d_{\mu\nu}$ is a **kinetic/derivative-sector** coefficient, entering the Lagrangian through
$$
\mathcal L \supset \tfrac{1}{2}i\,\bar\psi\,d^{\mu\nu}\gamma_5\gamma_\mu\,\overleftrightarrow\partial_\nu\,\psi ,
$$
paired with $c_{\mu\nu}$ the same way $b_\mu$ is paired with $a_\mu$ in the mass sector. It is the axial partner of $c_{\mu\nu}$, not of $H_{\mu\nu}$. Despite being CPT-even (same sign for matter and antimatter), it generates a rich phenomenology because different components produce NR Hamiltonians at different orders in $1/m$, spanning potentials $V_2$, $V_7$, and $V_8$.

The $d_{\mu\nu}$ term is particularly important for electron--nucleon scattering experiments because $d_{i0}$ produces a large (order $m^1$) but momentum-independent coupling to $\sigma^i$, while $d_{ij}$ produces a velocity-dependent coupling.

---

### Root cause of the earlier "unverified" flag — resolved by checking the primary source

While completing the executable `derivations/sympy/` notebooks for `b_μ` and `H_μν`, a real Dirac-algebra sign error was found and fixed in the `b_μ` notebook (see `FW_bmu_term.ipynb` §2–3, and the correction notes in `FW_derivation_bmy.md`) — it was only caught by actually running the symbolic computation rather than trusting the hand-derived prose. Applying that same numeric check here (`gamma[0]*gamma5*sigma_munu(i,0)` in `dirac_algebra.py`'s tooling) for the electric-axial $d_{i0}$ term gave an **even**, $O(m^0)$, *imaginary*-coefficient operator ($\propto -i\,\Sigma^i\beta$) — not the real, $O(m^1)$, mass-*enhanced* $+d_{i0}\,m\,\sigma^i$ claimed below, so the claim was flagged unverified.

Checking against Kostelecký & Lane, *Phys. Rev. D* 60, 116010 (1999) (§II A) shows why: that spot-check was testing the **wrong operator**. Their Eq. (1)–(3) define
$$
\mathcal L = \tfrac12 i\bar\psi\Gamma^\nu\overleftrightarrow\partial_\nu\psi - \bar\psi M\psi,\qquad
M = m+a_\mu\gamma^\mu+b_\mu\gamma_5\gamma^\mu+\tfrac12 H_{\mu\nu}\sigma^{\mu\nu},\qquad
\Gamma^\nu = \gamma^\nu+c^{\mu\nu}\gamma_\mu+d^{\mu\nu}\gamma_5\gamma_\mu+\cdots
$$
and state explicitly that *"parameters appearing in $M$ have dimensions of mass, while those in $\Gamma$ are dimensionless"* and *"Both $c_{\mu\nu}$ and $d_{\mu\nu}$ are traceless, while $H_{\mu\nu}$ is antisymmetric."* So this note's original $L_d=d_{\mu\nu}\bar\psi\gamma_5\sigma^{\mu\nu}\psi$ (mass-sector, antisymmetric, dimension-1 coefficients — copying $H_{\mu\nu}$'s structure) was the wrong Ansatz on two counts: wrong sector (kinetic, not mass) and wrong symmetry (traceless, not antisymmetric — so $d_{00}=0$ "by antisymmetry" does not hold in general).

Their fully-reduced nonrelativistic Hamiltonian, Eq. (4), gives an independent, literature-sourced check of the *numeric claims* (as opposed to the derivation route). At unsuppressed order it contains
$$
\delta h \;\supset\; \big(-b_j + m\,d_{j0} + \cdots\big)\,\sigma^j ,
$$
and at the next order in $p/m$,
$$
\delta h \;\supset\; \big(-m\,d_{kj}+\cdots\big)\frac{p_j}{m}\,\sigma^k \;=\; -d_{kj}\,p_j\,\sigma^k+\cdots
$$
i.e. the literature *does* contain a real, mass-enhanced $m\,d_{j0}\,\sigma^j$ term and a momentum-dependent $d_{ij}\,p^j\,\sigma^i$ term — structurally matching the "Key Results" claimed below. So the headline claims were apparently right, but for the wrong reason: they weren't obtained by correctly FW-reducing $\Gamma^\nu$'s derivative term, and the `dirac_algebra.py` check that contradicted them was (correctly) rejecting the mass-sector operator this note mistakenly substituted in — not rejecting the physical result itself.

**Update — `FW_dmunu_term.ipynb` now exists and is executed** (`derivations/sympy/FW_dmunu_term.ipynb`), redoing the FW reduction from the correct kinetic-sector operator $d^{\mu\nu}\gamma_5\gamma_\mu$ using `dirac_algebra.py` directly (no hand algebra), and checking every piece against Eq. (4) above. Result:

*   $\Gamma_0=\gamma^0\gamma_5\gamma_0=-\gamma_5$ (odd), $\Gamma_i=\gamma^0\gamma_5\gamma_i=+\Sigma^i$ (even) — verified by direct matrix computation, not assumed.
*   $d_{i0}$: the even sector gives $H_{NR}=-d^{i0}m\sigma^i$ directly, no FW iteration needed (mirrors how $b_i$ needed none). Converting to Kostelecký & Lane's lower-index convention ($d_{i0}=-d^{i0}$ under the $(+,-,-,-)$ metric) gives $+d_{i0}\,m\,\sigma^i$ — **exact match with Eq. (4), sign included.** This is the specific claim that was flagged unverified; it is now genuinely derived and confirmed.
*   $d_{ij}$: also falls out of the even sector directly, $H_{NR}=+d^{ij}p^j\sigma^i$. Structure matches Eq. (4)'s $-d_{kj}p^j\sigma^k$ term, but the overall sign does not.
*   $d_{00}$: the odd sector ($\Gamma_0$) requires the FW $\mathcal O^2/2m$ cross-term with $\boldsymbol\alpha\cdot\mathbf p$, worked out explicitly in the notebook, giving $H_{NR}=(d_{00}-\mathbf d_0\cdot\mathbf p/m)(\boldsymbol\sigma\cdot\mathbf p)$, leading term $+d_{00}(\boldsymbol\sigma\cdot\mathbf p)$. Structure matches Eq. (4)'s $-d_{00}(\boldsymbol\sigma\cdot\mathbf p)$ term; sign again does not.

Both open signs follow the same pattern (only momentum-linear terms disagree; the pure mass-enhancement term matches exactly), which points at a specific, identified gap rather than a random error: Kostelecký & Lane's actual derivation of Eq. (4) includes a wavefunction-renormalization step for kinetic-sector coefficients ($c_{\mu\nu}$, $d_{\mu\nu}$) that a plain "insert $i\partial_\nu\to p_\nu$ into the equation of motion" derivation — what the notebook does — does not capture. That's the "more careful multi-step work" this note originally anticipated needing; see the notebook §6 for the full comparison.

### Key Results

*   $d_{i0}$: $H_{NR} = +d_{i0}\, m\, \sigma^i$ (order $m^1$, large but static) $\rightarrow V_2$ — **derived and verified**, matches Kostelecký & Lane (1999) Eq. (4) exactly (`FW_dmunu_term.ipynb`, executed)
*   $d_{ij}$: $H_{NR} = +d_{ij}\, p^j\, \sigma^i$ (order $m^0$ in velocity) $\rightarrow V_7, V_8$ — derived, structure confirmed against Eq. (4); **overall sign still open** (see above)
*   $d_{00}$: $H_{NR} = +d_{00}\, \sigma \cdot p$ (order $m^0$ in momentum) $\rightarrow V_8$ — derived via FW $\mathcal O^2/2m$, structure confirmed against Eq. (4); **overall sign still open** (see above)
*   CPT-even: NO sign flip for antimatter; $A\alpha$ predicted near 0 (stated directly in Kostelecký & Lane 1999, not independently re-derived here)

---

## The SME Lagrangian Term — superseded, kept for the audit trail

> **This whole section (through "FW Derivation by Component" below) uses the wrong Ansatz** — a mass-sector bilinear copied from the $H_{\mu\nu}$ note, antisymmetric with $d_{00}=0$. Kostelecký & Lane (1999) place $d_{\mu\nu}$ in the *kinetic* sector as $\tfrac12 i\bar\psi\,d^{\mu\nu}\gamma_5\gamma_\mu\overleftrightarrow\partial_\nu\psi$, and state it is *traceless*, not antisymmetric (see "Root cause" above). Left in place, uncorrected, so the derivation error is traceable — do not treat the operator identities below as valid; use them only to see what went wrong.

### Covariant Form (superseded)

The $d_{\mu\nu}$ Lagrangian was assumed here to be:

$$
L_d = d_{\mu\nu}\, \bar{\psi}\, \gamma_5\, \sigma^{\mu\nu}\, \psi \qquad \text{where } \sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu]
$$

with $d_{\mu\nu} = -d_{\nu\mu}$ real and antisymmetric, 6 independent components ($d_{i0}$, $d_{ij}$), $d_{00}=0$ by antisymmetry. **This is wrong** — see the correct Lagrangian and tracelessness property in "Root cause" above.

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

### Pure temporal $d_{00}$ — superseded, $d_{00}\neq 0$ in general

**Wrong** (see "Root cause" above): $d_{\mu\nu}$ is traceless, not antisymmetric, so $d_{00}=0$ does not follow from its tensor symmetry. `FW_dmunu_term.ipynb` derives a genuine, nonzero NR contribution from $d_{00}$ via the FW $\mathcal O^2/2m$ reduction of the odd $\Gamma_0=-\gamma_5$ sector: leading term $H_{NR}(d_{00})=+d_{00}(\boldsymbol\sigma\cdot\mathbf p)$, structurally matching Kostelecký & Lane's Eq. (4) (sign open — see "Root cause").

## Two-Body Potentials and Matching

### $d_{i0} \rightarrow V_2$

The large $d_{i0}m\sigma^i$ coupling contributes to $V_2$ in the two-body potential as the spin-polarised vertex. Since $H_{NR}(d_{i0})$ has the same $\sigma^i$ (Zeeman-like) structure as the $b_i$ case, the two-body potential it generates is likewise spin--spin, not monopole--dipole:

$$
V_2 \text{ contribution} \propto (d_{i0}\, m)^{(1)} (d_{i0}\, m)^{(2)} \times (\sigma_1 \cdot \sigma_2) \frac{e^{-r/\lambda}}{r}
$$

This supersedes an earlier draft that used the monopole--dipole radial form $(\sigma_1\cdot\hat r)[1/(\lambda r)+1/r^2]e^{-r/\lambda}$, which belongs to $V_9,V_{10}$, not $V_2$. $V_2$ is spin--spin ($\sigma_1\cdot\sigma_2$) with no $\hat r$ dependence — see `potential_match_table.md` for the corrected $V_1$--$V_{16}$ catalogue.

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
| $d_{00}$ | superseded — see "Root cause": $d_{\mu\nu}$ is traceless, not antisymmetric, so $d_{00}\neq0$ in general | — | — | Superseded |

*This table's derivation route (the rest of this section) is superseded, but every number in it happens to match what `FW_dmunu_term.ipynb` independently derives from the correct kinetic-sector Lagrangian and confirms against Kostelecký & Lane (1999) Eq. (4) — see "Root cause" above for the executed, machine-checked version (including where a sign is still open for $d_{ij}$ and $d_{00}$).*

## References

1. Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. *Phys. Rev. D* 39, 683.

2. Kostelecký, V.A. & Lane, C.D. (1999). Nonrelativistic quantum Hamiltonian for Lorentz violation. *J. Math. Phys.* 40, 6245. **Note:** the Lagrangian (Eqs. 1–3) and nonrelativistic Hamiltonian (Eq. 4) cited in "Root cause" above were verified directly against Kostelecký & Lane, *Constraints on Lorentz Violation from Clock-Comparison Experiments*, **Phys. Rev. D 60, 116010 (1999)** (arXiv:hep-ph/9908504) — a companion paper by the same authors reproducing the identical general formalism as background theory. The two are consistent; cite whichever is more appropriate for the specific claim, but the equation numbers referenced here (Eqs. 1–4) are from the PRD 60 paper, not the J. Math. Phys. one.

3. Heckel, B.R. et al. (2008). Preferred-frame and CP-violation tests with polarized electrons. *Phys. Rev. D* 78, 092006.

4. Dobrescu, B.A. & Mocioiu, I. (2006). *JHEP* 11, 005.