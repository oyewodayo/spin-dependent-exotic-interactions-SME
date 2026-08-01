# Foldy--Wouthuysen Derivation of the $H_{\mu\nu}$ Term

**Oyewo Temidayo**
*CERN Summer Programme 2026*

June 2026

**Note:** Theory Note 2
**Repository:** `exotic-spin-interactions-SME/docs/theory_notes/FW_derivation_Hmunu.md`

> *`SME coefficient $`H_{\mu\nu}`$ $`\rightarrow`$ Non-relativistic Hamiltonian $`\rightarrow`$ Dobrescu--Mocioiu potentials $`V_3`$ and $`V_7`$`*

---

## Overview

The SME coefficient $H_{\mu\nu}$ is a rank-2 antisymmetric tensor coupling:

$$
L_H = -\frac{1}{2} H_{\mu\nu} \bar{\psi} \sigma^{\mu\nu} \psi
$$

where

$$
\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu].
$$

Unlike $b_\mu$, $H_{\mu\nu}$ is CPT-EVEN but Lorentz-odd. It does not change sign under CPT, meaning matter and antimatter couple identically at tree level. Its primary experimental signature is an anisotropy (direction-dependence) rather than a matter--antimatter asymmetry.

$H_{\mu\nu}$ has two distinct sectors: the magnetic-like spatial components $H_{ij}$ and the electric-like mixed components $H_{0i}$. These generate different DM potentials at different orders in the $1/m$ expansion, as derived below.
---

## Key Result

* $H_{ij}$ (magnetic-like):

$$
H_{NR} = -\mathcal{H}^k \sigma^k
$$

  where

$$
\mathcal{H}^k = \frac{1}{2}\varepsilon^{ijk} H_{ij}
$$

  $\rightarrow V_3$ (dipole-dipole)

* $H_{0i}$ (electric-like):

$$
H_{NR} = -\frac{1}{m}\sigma \cdot (p \times H_E)
$$

  $\rightarrow V_7$ (spin-velocity)

* CPT-even: same sign for matter and antimatter (no $A\alpha = 1$ signature)

* Experimental signature: sidereal variation, **not** matter-antimatter asymmetry

---

## The SME Lagrangian Term

### Covariant Form

The $H_{\mu\nu}$ Lagrangian term is:

$$ L_H = -\frac{1}{2} H_{\mu\nu} \bar{\psi} \sigma^{\mu\nu} \psi \qquad \text{where } \sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu, \gamma^\nu] $$

The tensor $H_{\mu\nu} = -H_{\nu\mu}$ is antisymmetric and real. It has 6 independent components:

* 3 magnetic-like:

$$ H_{ij} = \frac{1}{2}\varepsilon_{ijk} B_H^k $$

* 3 electric-like:

$$ H_{0i} = E_H^i $$

### CPT Properties

Under CPT:

$$ \bar{\psi}\sigma^{\mu\nu}\psi \rightarrow +\bar{\psi}\sigma^{\mu\nu}\psi $$

(CPT-even bilinear).

Therefore

$$ L_H \rightarrow -\frac{1}{2}H_{\mu\nu}\bar{\psi}\sigma^{\mu\nu}\psi, $$

the same sign as the original. $H_{\mu\nu}$ is CPT-even.

Under Lorentz transformations, since $H_{\mu\nu}$ is a fixed background tensor, it explicitly breaks Lorentz invariance but not CPT.

Under charge conjugation alone:

$$ \bar{\psi}^c\sigma^{\mu\nu}\psi^c = +\bar{\psi}\sigma^{\mu\nu}\psi $$

(C-even tensor current).

The antiparticle coupling is therefore the **same sign** as the particle:

$$ H_{NR}^{\text{antimatter}} = H_{NR}^{\text{matter}}. $$

This means $H_{\mu\nu}$ predicts

$$ A\alpha = 0 $$

in the absence of sensitivity differences.

---

## FW Transformation of $H_{\mu\nu}$

### Magnetic-like Components $H_{ij}$

For the spatial antisymmetric components, the relevant combination is

$$ \gamma^0\sigma^{ij} $$

where

$$ \sigma^{ij} = \frac{i}{2}[\gamma^i,\gamma^j]. $$

In the Dirac representation:

$$ \gamma^0\sigma^{ij} = \varepsilon^{ijk}\Sigma^k = \mathrm{diag} \left( \varepsilon^{ijk}\sigma^k, \varepsilon^{ijk}\sigma^k \right) $$

This is an even operator (block-diagonal).

In the upper components, contracting with $H_{ij}$:

$$ H_{H_{ij}}^{\uparrow} = -\frac{1}{2} H_{ij} \varepsilon^{ijk}\sigma^k = -\mathcal{H}_B^k \sigma^k $$

$$ H_{NR}(H_{ij}) = -\mathcal{H}_B \cdot \sigma $$

This is the standard spin--magnetic field coupling, here with the SME background $\mathcal{H}_B$ playing the role of a magnetic field.

It generates the dipole--dipole potential $V_3$ in the two-body interaction via the tensor exchange propagator.

### Electric-like Components $H_{0i}$

The mixed components $H_{0i}$ contribute through

$$ \gamma^0\sigma^{0i} = \gamma^0 \times \frac{i}{2} [\gamma^0,\gamma^i]. $$

In the Dirac representation:

$$ \gamma^0\sigma^{0i} = \frac{1}{2}\gamma^0[\gamma^0,\gamma^i] = -\alpha^i \quad (\text{off-diagonal}) $$

This is an **odd operator**; it mixes upper and lower spinor components.

At order $m^0$ it vanishes; the FW procedure generates a contribution at order $m^{-1}$:

$$ H_{NR}(H_{0i}) = -\frac{1}{m} \sigma \cdot (p \times H_E) $$

where

$$ H_E^i = H_{0i}. $$

This is a spin--orbit-type coupling that generates DM potential $V_7$.

---

## Two-Body Potential Matching

### $V_3$ from $H_{ij}$

The magnetic-like $H_{ij}$ term generates a dipole--dipole potential:

$$ V_3 = \frac{g^2}{4\pi} \left[ \sigma_1\cdot\sigma_2 - 3(\sigma_1\cdot\hat r)(\sigma_2\cdot\hat r) \right] \frac{e^{-r/\lambda}}{r} $$

where $g$ is identified with the effective $H_{ij}$ coupling.

Both particles 1 and 2 must carry a spin coupling for $V_3$ to contribute, consistent with the dipole--dipole form.

### $V_7$ from $H_{0i}$

The electric-like $H_{0i}$ term generates a spin--velocity potential:

$$ V_7 = \frac{g^2}{4\pi} \sigma_1\cdot(v\times\hat r) \frac{e^{-r/\lambda}}{r} $$

This is velocity-dependent and requires experimental setups sensitive to relative motion between the test masses.

---

## Summary Table

| **$H_{\mu\nu}$ sector** | **NR Hamiltonian**                     | **DM Potential** | **Order in $1/m$** | **Experimental signature**            |
| ----------------------- | -------------------------------------- | ---------------- | ------------------ | ------------------------------------- |
| $H_{ij}$ (magnetic)     | $-\mathcal{H}_B\cdot\sigma$            | $V_3$            | $m^0$ (leading)    | Sidereal variation in spin precession |
| $H_{0i}$ (electric)     | $-\frac{1}{m}\sigma\cdot(p\times H_E)$ | $V_7$            | $m^{-1}$           | Velocity/direction-dependent force    |

---

## References

1. Kostelecký, V.A. & Samuel, S. (1989). *Spontaneous breaking of Lorentz symmetry in string theory*. **Phys. Rev. D** 39, 683.

2. Bailey, Q.G. & Kostelecký, V.A. (2006). *Signals for Lorentz violation in post-Newtonian gravity*. **Phys. Rev. D** 74, 045001.

3. Dobrescu, B.A. & Mocioiu, I. (2006). *Spin-dependent macroscopic forces from new particle exchange*. **JHEP** 11, 005.

4. Kostelecký, V.A. & Lane, C.D. (1999). *Nonrelativistic quantum Hamiltonian for Lorentz violation*. **J. Math. Phys.** 40, 6245.