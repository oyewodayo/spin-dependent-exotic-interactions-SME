# Foldy–Wouthuysen derivation: the $g_{\lambda\mu\nu}$ term

Companion to `FW_derivation_bmy.md`, `FW_derivation_Hmunu.md` and
`FW_derivation_dmunu.md`. Symbolic derivation in
`derivations/sympy/FW_gmunu_term.ipynb`.

Conventions: Dirac/Pauli representation, metric $(+,-,-,-)$, $\hbar=c=1$,
$\gamma_5=i\gamma^0\gamma^1\gamma^2\gamma^3$, as in `dirac_algebra.py`.

## Summary

| family | $H_{\rm NR}$ | DM potential | $1/m$ order | matter–antimatter (CPT-conjugate) |
|---|---|---|---|---|
| $g_{[kl]0}$ | $-m\,\tilde{\mathbf g}\cdot\boldsymbol\sigma$ | $V_2$ | $m^{+1}$ (mass-enhanced) | $g^{\bar f}=-g^f$ |
| $g_{[0k]0}$ | $+\boldsymbol\sigma\cdot(\mathbf p\times\mathbf g_{00})$ | $V_7$ | $m^{0}$ | $g^{\bar f}=-g^f$ |
| $g_{[kl]j}$ | $+\tfrac12\varepsilon_{klm}g_{mlj}\,p^j\,\sigma^k$ | $V_7,V_8$ | $m^{0}$ (vel.) | $g^{\bar f}=-g^f$ |
| $g_{[0k]j}$ | — | — | — | no contribution at this order |

with $\tilde g_j\equiv\tfrac12\varepsilon_{jkl}g_{kl0}$ and
$(\mathbf g_{00})_k\equiv g_{k00}$, and $\mathbf p$ the physical momentum ($p^j$).

All three contributing families reproduce Kostelecký & Lane's non-relativistic
Hamiltonian term by term, signs included.

## Why this coefficient completes the mapping

Of the eight minimal and near-minimal SME fermion-sector coefficients, only
four generate spin-dependent terms in the non-relativistic Hamiltonian.
Splitting Kostelecký & Lane's $h$ into top-level terms, every term carrying a
factor of $\boldsymbol\sigma$ contains only $b_\mu$, $d_{\mu\nu}$,
$g_{\lambda\mu\nu}$ and $H_{\mu\nu}$. The coefficients $a_\mu$, $c_{\mu\nu}$
and $e_\mu$ appear exclusively in spin-independent terms, and $f_\mu$ does not
appear in $h$ at all through third order in $1/m$.

Since the Dobrescu–Mocioiu basis is spin-dependent apart from $V_1$, those four
exhaust the coefficients with an image in it. With $g_{\lambda\mu\nu}$ derived,
the SME$\to$DM mapping is **closed rather than partial**.

## Lagrangian placement

From Kostelecký & Lane Eq. (1),

$$\Gamma_\nu=\gamma_\nu+c_{\mu\nu}\gamma^\mu+d_{\mu\nu}\gamma_5\gamma^\mu
+e_\nu+if_\nu\gamma_5+\tfrac12 g_{\lambda\mu\nu}\sigma^{\lambda\mu}.$$

So $g_{\lambda\mu\nu}$ is a **kinetic-sector** coefficient, like $c_{\mu\nu}$
and $d_{\mu\nu}$ and unlike the mass-sector $b_\mu$ and $H_{\mu\nu}$. It is
antisymmetric in its first two indices (because $\sigma^{\lambda\mu}$ is); the
third index is the derivative index. It is CPT-odd and dimensionless.

Only the $\nu=0$ slice $\{g_{010},g_{020},g_{030},g_{120},g_{130},g_{230}\}$
enters $\Gamma_0$, which is verified directly in the notebook.

## Field redefinition

Because $\Gamma_0\neq\gamma_0$, the naive step of multiplying the equation of
motion by $\gamma^0$ and reading off $E\psi=H\psi$ is not available — it is the
error corrected in `FW_derivation_dmunu.md`. Kostelecký & Lane remove the
time-derivative coupling at the Lagrangian level with $\psi=A\chi$,

$$A=1-\tfrac12\gamma^0(\Gamma_0-\gamma_0),\qquad
\bar A=1-\tfrac12(\Gamma_0-\gamma_0)\gamma^0,$$

chosen so that $\bar A\,\Gamma_0 A=\gamma_0$ — verified symbolically. Note this
is *not* the condition $A^\dagger A=\gamma^0\Gamma_0$; the criterion is that the
redefined Lagrangian's $\partial_0\chi$ dependence be that of the ordinary Dirac
Lagrangian. The relativistic Hamiltonian is then

$$H=-\gamma^0\bar A\,\Gamma_j A\,p^j+\gamma^0\bar A M A,$$

which is Hermitian, as checked in the notebook.

Unlike $d_{\mu\nu}$, the $g$ vertex does not break hermiticity even without the
redefinition — the $\sigma^{\lambda\mu}$ structure populates $\Gamma_0$
differently. The redefinition is still correct to apply, but it is not
load-bearing here.

## Momentum convention

Kostelecký & Lane's lower-index $p_j$ is the **covariant** component
$p_j=-p^j$, not the physical three-momentum their prose describes. This is
fixed by their own free-particle term

$$m\mathcal P_0:=-p_j\gamma^0\gamma^j,$$

which evaluates to $-\boldsymbol\alpha\cdot\mathbf p$; recovering the required
free Dirac Hamiltonian $+\boldsymbol\alpha\cdot\mathbf p+\beta m$ therefore
forces $p_j=-p^j$.

The same convention was established independently in
`FW_derivation_dmunu.md`. That it is also what makes the $g$ sector agree —
having been fixed there without reference to $g$ — is an independent
confirmation of the reading.

## Matter–antimatter behaviour

In hole theory, an antiparticle of momentum $\mathbf p$ and spin $\mathbf s$ is
the absence of a negative-energy solution with momentum $-\mathbf p$ and spin
$-\mathbf s$, and has the opposite energy. A CPT test compares the particle
with its CPT-conjugate state, an antiparticle of the same momentum and
reversed spin:

$$H^{\bar f}_{NR}(\mathbf p,\boldsymbol\sigma)=-H_{\rm lower}(-\mathbf p,\boldsymbol\sigma).$$

Applied family by family:

- $g_{[kl]0}$: **flipped**, $g^{\bar f}=-g^f$.
- $g_{[0k]0}$: **flipped**, $g^{\bar f}=-g^f$.
- $g_{[kl]j}$: **flipped**, $g^{\bar f}=-g^f$.

All three contributing families flip, as the CPT-odd character of
$g_{\lambda\mu\nu}$ requires. At the same physical spin, all three give
identical particle and antiparticle shifts, which is Kostelecký & Lane's
antiparticle rule $g\to+g$.

The momentum reversal is essential. $g_{[0k]0}$ and $g_{[kl]j}$ are linear in
$\mathbf p$. Taking minus the lower block at the *same* momentum (as an
earlier version of this note did) wrongly suggests that these two families do
not flip, and led to an incorrect "per index family" conclusion.
`derivations/sympy/FW_antiparticle_all_coefficients.ipynb` checks every SME
coefficient family both ways, against CPT parity and against the
Kostelecký–Lane rule.

The relation concerns the underlying couplings. A flip makes the signed
$A_\alpha$ diverge, not approach 1, and SPINDEP's $A_\alpha$ values, built from
independent one-sided bounds, cannot reveal it: a sensitivity gap produces
$|A_\alpha|\approx1$ regardless of the underlying physics.

## Reference

Kostelecký, V.A. & Lane, C.D. (1999). *Nonrelativistic quantum Hamiltonian for
Lorentz violation*. **J. Math. Phys.** 40, 6245.
