---
title: "Foldy–Wouthuysen Derivation of the bμ Term"
author: "Oyewo Temidayo"
affiliation: "University of Ibadan"
date: "June 2026"
note: "Theory Note 1"
---

> *SME coefficient b_μ → Non-relativistic Hamiltonian → Dobrescu–Mocioiu potential V₂*

---

## 1. Overview and Physical Motivation

The SME coefficient bμ (sometimes written b_μ or b^f_μ for fermion f) parametrises CPT-odd, Lorentz-violating interactions of the form −bμ ψ̅ γ_5 γ^μ ψ in the SME Lagrangian. This term is CPT-odd because under CPT: ψ → iγ^0γ^2ψ* and the combination ψ̅γ_5γ^μψ changes sign. It is the leading CPT-violating operator relevant to spin-dependent exotic interactions because it couples to the fermion spin directly through the γ_5 structure.

The goal of this derivation is to take the fully relativistic SME Lagrangian term and obtain the non-relativistic (NR) Hamiltonian via the Foldy—Wouthuysen (FW) transformation. The NR Hamiltonian is then matched to the Dobrescu—Mocioiu (DM) catalogue to identify which potential(s) V_n it generates in a two-body interaction.

> [!NOTE]
> **Key Result**
> The b_i (spatial) component generates V₂ at leading order m⁰: H_NR = −b_i σ^i (matter), +b_i σ^i (antimatter) — see §4.
> The b_0 (temporal) component generates V₇, V₈ at subleading order m⁻¹: H_NR = +b_0 (σ·p)/m
> This sign flip is the qualitative CPT-odd signature of b_μ. It does **not** by itself predict |Aα| → 1 in SPINDEP's output — that requires the separate sensitivity-gap argument in §4.2, since the framework compares independent one-sided bounds, not signed couplings.

## 2. The SME Lagrangian Term

### 2.1 Covariant Form

The CPT-odd Lorentz-violating modification to the free Dirac Lagrangian in the minimal SME is:

$$
L_b = -b_μ ψ̅ γ_5 γ^μ ψ
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(2.1)*

The full equation of motion (Dirac equation modified by the SME term) is:
$$
(iγ^μ∂_μ - m - b_μγ_5γ^μ)ψ = 0
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(2.2)*

### 2.2 CPT Properties

Under the CPT transformation, the spinor transforms as ψ → iγ^0γ^2ψ*_CPT (up to a phase). The relevant bilinear transforms as:
$$
CPT[ψ̅γ_5γ^μψ] = -ψ̅γ_5γ^μψ
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(2.3)*

So L_b → +b_μψ̅γ_5γ^μψ under CPT, which differs from the original −b_μψ̅γ_5γ^μψ by a sign — confirming b_μ is CPT-odd. A non-zero b_μ therefore breaks CPT symmetry.

Under charge conjugation C alone (which maps particles to antiparticles):
$$
C[ψ̅γ_5γ^μψ] = +ψ̅γ_5γ^μψ (C is even for axial current)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(2.4a)*

However, the COUPLING changes sign because the antiparticle b_μ coefficient is −b_μ relative to the particle. This is the origin of the matter—antimatter sign flip in the NR Hamiltonian, derived explicitly in §4.

## 3. Foldy—Wouthuysen Transformation

### 3.1 Purpose and Method

The Foldy—Wouthuysen (FW) transformation is a sequence of unitary transformations on the Dirac Hamiltonian that systematically decouples the upper (particle) and lower (antiparticle) two-component spinors in powers of 1/m. At each order, 'odd' operators (those mixing upper and lower) are eliminated, leaving a block-diagonal Hamiltonian in the upper components.

The standard Dirac Hamiltonian in an external perturbation ε is written H = βm + ε_even + ε_odd, where β = γ^0 and ε_even, ε_odd commute and anticommute with β respectively. The FW transformation is:
$$
U_FW = exp(βε_odd/2m) → H' = U† H U - i U† ∂_t U
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.1)*

Expanding to order 1/m, the transformed Hamiltonian is:
$$
H' ≈ βm + ε_even + βε_odd²/(2m) - [ε_odd, ε_even]/(4m) + O(m⁻²)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.2)*

### 3.2 Application to the b_μ Term

The b_μ Hamiltonian (from L_b, taking the upper-sign convention) is:
$$
H_b = b_μγ^0γ_5γ^μ = b_0γ^0γ_5γ^0 + b_iγ^0γ_5γ^i
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.3)*

Using the Dirac representation where γ^0 = diag(1,1,−1,−1) and γ_5 = off-diagonal:

#### 3.2a Spatial components b_i

For the spatial components (i = 1,2,3), the term γ^0γ_5γ^i is an 'even' operator (block-diagonal) in the Dirac representation. Verified directly with `dirac_algebra.py` (see `derivations/sympy/`, using this note's own Lagrangian ordering γ_5γ^μ), the operator identity is:
$$
γ^0γ_5γ^i = -Σ^i = -\,\mathrm{diag}(σ^i, σ^i)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.4)*

where Σ^i is the 4×4 spin matrix. This carries a minus sign relative to the naive guess $+Σ^i$ because $γ_5$ and $γ^i$ anticommute; skipping that minus sign and then reinstating it by hand at the next step is a bookkeeping trap this note fell into in an earlier draft — (3.4)-(3.5) below now follow in one direct step with no unexplained sign flip. In the upper 2×2 block:
$$
H_NR(b_i) = -b · σ (matter)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.5 — KEY RESULT)*

This is already in the Pauli non-relativistic form and requires no further FW iteration to leading order in 1/m. The b_i term is therefore exact at order m⁰ in the NR expansion.

**On the sign convention:** this result depends on the ordering of $γ_5$ and $γ^μ$ in the Lagrangian bilinear, and the two forms $\bar\psi\gamma_5\gamma^\mu\psi$ and $\bar\psi\gamma^\mu\gamma_5\psi$ are exact negatives of each other (since $\{\gamma_5,\gamma^\mu\}=0$). This note follows $\mathcal L_b=-b_\mu\bar\psi\gamma_5\gamma^\mu\psi$ (§2.1), matching the standard SME mass-operator form $M=m+a_\mu\gamma^\mu+b_\mu\gamma_5\gamma^\mu+\tfrac12H_{\mu\nu}\sigma^{\mu\nu}$ used throughout Kostelecký's papers, including Kostelecký & Lane (1999) as cited here — the same convention used in `thesis/01_introduction.tex` Eq. (2). `derivations/sympy/FW_bmu_term.ipynb` uses the opposite ordering ($\gamma^\mu\gamma_5$) and consequently reports $H_{NR}(b_i)=+b\cdot\sigma$ for matter — an artifact of that convention choice, not a disagreement about the underlying physics or a computational error in either document. Cite the result from this note (§3.2a, §4) rather than the notebook's raw sign when writing up the thesis, or flip the notebook's convention to match before citing it directly.

#### 3.2b Temporal component b_0

The temporal component produces an 'odd' operator:
$$
γ^0γ_5γ^0 = γ_5 = off-diagonal
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.7)*

Since this is odd, it does not contribute at m⁰. At order m⁻¹, using the FW expansion (3.2), the odd operator generates:
$$
H_NR(b_0) = β(γ_5 b_0)²/(2m) + ... → +b_0(σ·p)/m + O(m⁻²)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.8)*

This is velocity-dependent and matches DM potentials V₇ and V₈.

## 4. Charge Conjugation and the Antimatter Sign Flip

### 4.1 C-transformation of the Spinor

Under charge conjugation C, the Dirac spinor transforms as:
$$
ψ → ψ^c = Cγ^0ψ* where C = iγ^2γ^0 (Dirac convention)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.1)*

The charge-conjugated spinor describes the antiparticle with the same momentum but opposite charge. Crucially, the SME coefficient b_μ is a fixed background field that does NOT transform under C — it is an external source. Therefore the Lagrangian density for the antiparticle becomes:
$$
L_b(ψ^c) = +b_μψ̅^cγ_5γ^μψ^c = +b_μ (ψ̅γ_5γ^μψ)*
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.2)*

The sign flip from −b_μ (particle) to +b_μ (antiparticle) follows from the anticommutativity of the C matrix with γ_5. Explicitly:
$$
Cγ_5γ^μ C⁻¹ = −(γ_5γ^μ)* → ψ̅^cγ_5γ^μψ^c = −(ψ̅γ_5γ^μψ)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.3)*

Combined with the −b_μ in the Lagrangian, the antiparticle coupling has overall +b_μ. Therefore:
$$
H_NR^antiparticle(b_i) = +b · σ
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.4)*

### 4.2 Implication for the Asymmetry Parameter

The two-body interaction potential for a matter—antimatter pair is proportional to the product of the single-particle NR Hamiltonians. For the b_i term:
$$
V_pair ∝ H_NR^matter × H_NR^antimatter ∝ (-b·σ_1)(+b·σ_2)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.5)*

This gives a potential that changes sign relative to the matter—matter case (where both factors carry −b·σ). The coupling constant g measured from matter—matter experiments and from matter—antimatter experiments therefore differ by a sign, yielding g_matter = −g_antimatter *for a hypothetical, exactly-known, signed coupling*. Substituting into the SPINDEP asymmetry parameter:
$$
Aα = (g_m - g_ā) / (g_m + g_ā) = (g - (-g)) / (g + (-g)) = 2g/0 → ∞
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.6)*

This is a genuine divergence — the denominator vanishes identically — not a value that "saturates at 1", as an earlier draft of this note claimed. (Verified directly with `sympy.limit` in `derivations/sympy/pauli_matrices.py`.) An exact CPT-odd sign flip of a *signed* coupling makes Eq. (4.6) formally undefined, not bounded.

The resolution is that Eq. (4.6) does not describe what SPINDEP actually computes. SPINDEP's `g_matter`/`g_antimatter` inputs are the `coupling_abs` columns of independent experimental datasets — **always-positive upper bounds** from separate experiments (see `spindep/README.md`), not a signed measurement of one real underlying coupling. For any two independent positive bounds $g_1, g_2$, the ratio $(g_1-g_2)/(g_1+g_2)$ approaches $\pm 1$ whenever one bound is far tighter than the other — **regardless of whether the underlying physics is CPT-odd or CPT-even.** This is a generic property of comparing two positive numbers of very different size (a sensitivity-gap effect), not a signature of the b_μ mechanism specifically. `derivations/sympy/pauli_matrices.py` now demonstrates this explicitly: substituting $g_{\text{tight}} = r\, g_{\text{loose}}$ and taking $r\to 0^+$ gives $A_\alpha \to 1$ with no CPT content at all.

Consequently, the observed $|A\alpha| \approx 1.000$ across gAgA pairs in SPINDEP is **consistent with**, but not **evidence for**, a nonzero $b_\mu$: the same numerical pattern is exactly what independent bounds of very different sensitivity would produce even under exact CPT symmetry. Distinguishing the two would require comparing bounds of comparable sensitivity, or using actual signed measured values (with symmetric uncertainties) rather than one-sided upper limits.

## 5. Matching to Dobrescu—Mocioiu Potentials

### 5.1 From Single-Particle to Two-Body Potential

The DM catalogue describes two-body potentials from boson exchange between particles 1 and 2. The single-particle Hamiltonian H_NR(ψ1) from §3 is the same "$-b\cdot\sigma$" Zeeman-like structure that an axial-vector-boson exchange produces at *each* vertex (cf. axial-vector/axial-vector coupling in Cong et al. 2025, Eq. 47). Promoting to the two-body potential — i.e. matching the exchange of the same axial-vector mediator between *both* fermions — therefore gives the spin-spin form:
$$
V_2(r) = -g_A^{(1)} g_A^{(2)} \frac{1}{4\pi} (\sigma_1\cdot\sigma_2) \frac{e^{-r/\lambda}}{r} \quad \text{where } \lambda = 1/m_\phi
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(5.1)*

An earlier draft of Eq. (5.1) gave $V_2$ in the monopole--dipole functional form $(\sigma_1\cdot\hat r)[\lambda^{-2}/r+\lambda^{-1}/r^2]e^{-r/\lambda}/r$ — that form belongs to $V_9,V_{10}$ (single spin dotted into $\hat r$), not $V_2$. The correct $V_2$ is spin--spin ($\sigma_1\cdot\sigma_2$), with no $\hat r$ dependence and no $1/r^2$ term; see `potential_match_table.md` for the full corrected $V_1$--$V_{16}$ catalogue transcribed from Cong et al. (2025).

The coupling constant $g_A$ in eq. (5.1) is identified with the b_μ coefficient through the matching condition $g_A \Leftrightarrow |b_\mu| / m_f$ for the relevant fermion mass $m_f$. The spatial $b_i$ term maps to $V_2$ (spin--spin) at leading order — each fermion contributes one $-b\cdot\sigma$ vertex, and the product of the two single-particle Hamiltonians yields the $\sigma_1\cdot\sigma_2$ structure.

### 5.2 Summary of Matchings

> [!NOTE]
> | **b_μ component** | **NR Hamiltonian** | **DM Potential** | **Order in 1/m** | **Notes** |
> | --- | --- | --- | --- | --- |
> | **b_i (spatial)** | -b·σ | **V₂** | m⁰ (leading) | Spin--spin ($\sigma_1\cdot\sigma_2$); both particles' spins couple |
> | **b_0 (temporal)** | +b₀(σ·p)/m | **V₇, V₈** | m⁻¹ | Velocity-dependent spin coupling |

## 6. Physical Consequences and SPINDEP Implications

- **All gAgA pairs show |Aα| ≈ 1:** This is *consistent with* a b_μ sign flip, but — per the corrected §4.2 above — is equally well explained by a sensitivity gap between the matter- and antimatter-sector bounds, with no CPT violation required. The two explanations cannot be distinguished from the asymmetry value alone; it would require checking whether the matter and antimatter bounds being compared are of comparable experimental precision. The small deviations from 1 in pairs 4—5 reflect curve curvature effects in the uncertainty model, not necessarily physics.

- **gsgs pair at |Aα| = 0.873:** The gsgs potential does not couple to b_μ at leading order (scalar coupling requires c_μν, which is CPT-even), so a value below 1 is consistent with no CPT-odd contribution. But note this is the *same type* of argument as the gAgA case above: a lower or higher |Aα| here is also compatible with a smaller sensitivity gap between the two experiments, independent of the CPT status of the dominant operator.

- **Observable consequences:** A measurement of b_i ≠ 0 for any fermion would appear as a direction-dependent shift in atomic energy levels (sidereal variation). SPINDEP constraints bound the effective b_i from the ratio of matter to antimatter coupling bounds.

## 7. References

- Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. Phys. Rev. D 39, 683.

- Foldy, L.L. & Wouthuysen, S.A. (1950). On the Dirac theory of spin-1/2 particles and its non-relativistic limit. Phys. Rev. 78, 29.

- Kostelecký, V.A. & Mewes, M. (2001). CPT violation and the standard model. Phys. Rev. D 66, 056005.

- Bailey, Q.G. & Kostelecký, V.A. (2006). Signals for Lorentz violation in post-Newtonian gravity. Phys. Rev. D 74, 045001.

- Dobrescu, B.A. & Mocioiu, I. (2006). Spin-dependent macroscopic forces from new particle exchange. JHEP 11, 005.
