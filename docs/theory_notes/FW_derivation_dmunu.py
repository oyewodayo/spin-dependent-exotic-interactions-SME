---
title: "Foldy–Wouthuysen Derivation of the d_μν Term"
author: "Oyewo Temidayo"
affiliation: "CERN Summer Programme 2026"
date: "June 2026"
note: "Theory Note 3"
repository: "exotic-spin-interactions-SME/docs/theory_notes/FW_derivation_dmunu.md"
---

> *SME coefficient d_μν → Non-relativistic Hamiltonian → Dobrescu–Mocioiu potentials V₂, V₇, V₈*

---

## 1. Overview

The SME coefficient d_μν is a CPT-even, Lorentz-odd rank-2 tensor coupling involving γ_5: L_d = d_μν ψ̅ γ_5 σ^μν ψ. It is the 'axial tensor' partner of H_μν. Despite being CPT-even (same sign for matter and antimatter), it generates a rich phenomenology because different components produce NR Hamiltonians at different orders in 1/m, spanning potentials V₂, V₇, and V₈.

The d_μν term is particularly important for electron—nucleon scattering experiments because d_{i0} produces a large (order m¹) but momentum-independent coupling to σ^i, while d_{ij} produces a velocity-dependent coupling and d_{00} gives a momentum-dependent spin coupling.

  ———————————————————————————————————
  **Key Results**

  d_{i0}: H_NR = +d_{i0} m σ^i (order m¹, large but static) → V₂

  d_{ij}: H_NR = +d_{ij} p^j σ^i (order m⁰ in velocity) → V₇, V₈

  d_{00}: H_NR = +d_{00} σ·p (order m⁰ in momentum) → V₈

  CPT-even: NO sign flip for antimatter; Aα predicted near 0
  ———————————————————————————————————

## 2. The SME Lagrangian Term

### 2.1 Covariant Form

The d_μν Lagrangian is:

$$
L_d = d_μν ψ̅ γ_5 σ^μν ψ where σ^μν = (i/2)[γ^μ, γ^ν]
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(2.1)*

d_μν = −d_νμ is real and antisymmetric with 6 independent components: three d_{i0} (electric-axial) and three d_{ij} (magnetic-axial). Additionally d_{00} = 0 by antisymmetry.

Note: in some SME references, d_μν absorbs additional factors. Throughout this note we follow the convention of Kostelecký & Lane (1999).

### 2.2 CPT Properties

Under CPT: ψ̅γ_5σ^μνψ → +ψ̅γ_5σ^μνψ (the combination γ_5σ^μν is CPT-even). Therefore L_d is CPT-even. Under C: the bilinear ψ̅^cγ_5σ^μνψ^c = +ψ̅γ_5σ^μνψ (same sign). The d_μν contribution to g_coupling is therefore the same for matter and antimatter.

## 3. FW Derivation by Component

### 3.1 Electric-axial components d_{i0}

The combination relevant to d_{i0} is γ^0γ_5σ^{i0} = γ^0γ_5(i/2)[γ^i,γ^0]. In the Dirac representation:
$$
γ^0γ_5σ^{i0} = +mΣ^i = diag(+mσ^i, +mσ^i)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.1)*

This is an even operator at order m¹. The NR Hamiltonian from d_{i0} is therefore:
$$
H_NR(d_{i0}) = +d_{i0} m σ^i
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.2 —- LARGE TERM)*

This term is large (enhanced by m) but does not produce a spatial gradient and therefore does not contribute to a force law directly. In a two-body interaction, it contributes to V₂ as a background spin-polarising field. Experimental bounds on d_{i0} from torsion balance experiments are correspondingly tight.

### 3.2 Magnetic-axial components d_{ij}

For the spatial antisymmetric components d_{ij}, the relevant combination is:
$$
γ^0γ_5σ^{ij} = (i/2)γ^0γ_5[γ^i,γ^j]
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.3)*

Expanding in the Dirac representation and using γ_5γ^i = γ^5γ^i, one obtains an odd matrix at zeroth order that becomes even at order m⁻¹ after the FW transformation. The result involves the momentum operator:
$$
H_NR(d_{ij}) = +d_{ij} p^j σ^i [summed over i,j]
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(3.4)*

This is a velocity-dependent (momentum-dependent) coupling to the spin. It generates DM potentials V₇ (antisymmetric in σ·v form) and V₈ (anticommutator of σ and v).

### 3.3 Pure temporal d_{00} = 0

By antisymmetry of d_μν, d_{00} = 0 identically. The notation d_{00} in some references refers to the trace d_μμ ≡ g^{μν}d_{μν} which is separately zero for an antisymmetric tensor. No NR contribution.

## 4. Two-Body Potentials and Matching

### 4.1 d_{i0} → V₂

The large d_{i0}mσ^i coupling contributes to V₂ in the two-body potential as the spin-polarised vertex:
$$
V₂ contribution ∝ (d_{i0} m) × g_2 × (σ_1·r̂)[1/(λr) + 1/r²] e^{-r/λ}
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.1)*

The large m factor means even very small d_{i0} coefficients produce potentially observable effects. Current bounds from atomic magnetometry constrain |d_{i0}| \< 10⁻²⁵ GeV (Heckel et al. 2008).

### 4.2 d_{ij} → V₇ and V₈

The velocity-dependent d_{ij} term generates:
$$
V₇ ∝ d_{ij} σ^i v^j e^{-r/λ}/r
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.2a)*
$$
V₈ ∝ d_{ij} {(σ·v), e^{-r/λ}/r} (anticommutator)
$$
&nbsp;&nbsp;&nbsp;&nbsp;*(4.2b)*

## 5. Summary Table

  ——————————————— —————————— —————————— ————————— —————————————————————
  **d_μν component**             **NR Hamiltonian**    **DM Potential(s)**   **Order in 1/m**   **Notes**

  **d_{i0} (electric-axial)**   +d_{i0} m σ^i       **V₂**                m¹ (large!)        Enhanced by fermion mass; tight bounds

  **d_{ij} (magnetic-axial)**   +d_{ij} p^j σ^i    **V₇, V₈**            m⁰ in velocity     Velocity-dependent; needs moving sources

  **d_{00}**                    = 0 by antisymmetry   None                  —                Identically zero
  ——————————————— —————————— —————————— ————————— —————————————————————

## 6. References

- Kostelecký, V.A. & Samuel, S. (1989). Spontaneous breaking of Lorentz symmetry in string theory. Phys. Rev. D 39, 683.

- Kostelecký, V.A. & Lane, C.D. (1999). Nonrelativistic quantum Hamiltonian for Lorentz violation. J. Math. Phys. 40, 6245.

- Heckel, B.R. et al. (2008). Preferred-frame and CP-violation tests with polarized electrons. Phys. Rev. D 78, 092006.

- Dobrescu, B.A. & Mocioiu, I. (2006). JHEP 11, 005.
