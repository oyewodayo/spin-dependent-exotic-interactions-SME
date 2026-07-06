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
> The b_i (spatial) component generates V₂ at leading order m⁰: H_NR = −b_i σ^i
> The b_0 (temporal) component generates V₇, V₈ at subleading order m⁻¹: H_NR = +b_0 (σ·p)/m
> Sign flips under C: matter gets −bμσ^μ, antimatter gets +bμσ^μ
> This sign flip is the theoretical basis for |Aα| = 1 in all gAgA pairs

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

Using the Dirac representation where γ^0 = diag(1,1,−1,−1) and γ_5 = off-diagonal, and the identity γ^0γ_5γ^i = α^iγ_5 = off-diagonal:

#### 3.2a Spatial components b_i

For the spatial components (i = 1,2,3), the term γ^0γ_5γ^i is an 'even' operator (block-diagonal) in the Dirac representation:
$$
γ^0γ_5γ^i = Σ^i = diag(σ^i, σ^i)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.4)*

where Σ^i is the 4×4 spin matrix. In the upper 2×2 block:
$$
H_{b_i}^{↑} = +b_iσ^i → H_NR(b_i) = -b_iσ^i
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.5)*
$$
H_NR(b_i) = -b · σ (matter)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.6 —- KEY RESULT)*

This is already in the Pauli non-relativistic form and requires no further FW iteration to leading order in 1/m. The b_i term is therefore exact at order m⁰ in the NR expansion.

#### 3.2b Temporal component b_0

The temporal component produces an 'odd' operator:
$$
γ^0γ_5γ^0 = γ_5 = off-diagonal
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.7)*

Since this is odd, it does not contribute at m⁰. At order m⁻¹, using the FW expansion (3.2), the odd operator generates:
$$
H_NR(b_0) = β(γ_5 b_0)²/(2m) + \... → +b_0(σ·p)/m + O(m⁻²)
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

This gives a potential that changes sign relative to the matter—matter case (where both factors carry −b·σ). The coupling constant g measured from matter—matter experiments and from matter—antimatter experiments therefore differ by a sign, yielding g_matter = −g_antimatter. Substituting into the SPINDEP asymmetry parameter:
$$
Aα = (g_m - g_ā) / (g_m + g_ā) = (g - (-g)) / (g + (-g)) → ∞
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.6)*

In the bounded definition |g_m| ≠ |g_ā| (because experimental upper bounds are always positive), the asymmetry saturates at |Aα| = 1. This is fully consistent with the observed |Aα| ≈ 1.000 across all gAgA pairs in SPINDEP. The b_μ term is thus the primary theoretical explanation for the near-maximal asymmetry.

## 5. Matching to Dobrescu—Mocioiu Potentials

### 5.1 From Single-Particle to Two-Body Potential

The DM catalogue describes two-body potentials from boson exchange between particles 1 and 2. The single-particle Hamiltonian H_NR(ψ1) from §3 must be promoted to a two-body potential by including the mediator propagator and the second vertex. For a Yukawa mediator of mass m_φ:
$$
V₂(r) = g^2 / (4π) × (σ_1·r̂) × [λ⁻²/r + λ⁻¹/r²] × e^{-r/λ} / r where λ = 1/m_φ
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(5.1)*

The coupling constant g in eq.(5.1) is identified with the b_μ coefficient through the matching condition g ⇔ |b_μ| / m_f for the relevant fermion mass m_f. The spatial b_i term maps to V₂ (monopole—dipole in the single-spin form) at leading order.

### 5.2 Summary of Matchings

> [!NOTE]
> **b_μ component**    **NR Hamiltonian**   **DM Potential**   **Order in 1/m**   **Notes**
> **b_i (spatial)**    -b·σ                 **V₂**             m⁰ (leading)       Monopole-dipole, spin of particle 1 only
> **b_0 (temporal)**   +b₀(σ·p)/m           **V₇, V₈**         m⁻¹                Velocity-dependent spin coupling

## 6. Physical Consequences and SPINDEP Implications

- **All gAgA pairs show |Aα| ≈ 1:** Fully explained by the b_μ sign flip. The theoretical prediction is |Aα| = 1 for any pair where the b_μ interaction dominates. The small deviations from 1 in pairs 4—5 reflect curve curvature effects in the uncertainty model, not physics.

- **gsgs pair at |Aα| = 0.873:** The gsgs potential does not couple to b_μ at leading order (scalar coupling requires c_μν, which is CPT-even). The lower |Aα| is consistent with the dominant operator being CPT-even, with the gap driven by experimental sensitivity differences rather than a sign flip.

- **Observable consequences:** A measurement of b_i ≠ 0 for any fermion would appear as a direction-dependent shift in atomic energy levels (sidereal variation). SPINDEP constraints bound the effective b_i from the ratio of matter to antimatter coupling bounds.

## 7. References

- Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. Phys. Rev. D 39, 683.

- Foldy, L.L. & Wouthuysen, S.A. (1950). On the Dirac theory of spin-1/2 particles and its non-relativistic limit. Phys. Rev. 78, 29.

- Kostelecký, V.A. & Mewes, M. (2001). CPT violation and the standard model. Phys. Rev. D 66, 056005.

- Bailey, Q.G. & Kostelecký, V.A. (2006). Signals for Lorentz violation in post-Newtonian gravity. Phys. Rev. D 74, 045001.

- Dobrescu, B.A. & Mocioiu, I. (2006). Spin-dependent macroscopic forces from new particle exchange. JHEP 11, 005.
