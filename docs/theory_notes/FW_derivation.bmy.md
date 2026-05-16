
## SME Coefficient → Dobrescu–Mocioiu Potential Matching Table

---

### Overview

The Dobrescu–Mocioiu (DM) potentials $V_1$–$V_{16}$ classify all possible nonrelativistic spin-dependent interactions between two spin-1/2 fermions mediated by a single boson exchange. The table below gives the explicit mapping from each SME coefficient to the DM potential(s) it generates, the leading order in $1/m$ at which it appears, and its CPT/Lorentz properties.

---

### Notation

| Symbol | Meaning |
|---|---|
| $\boldsymbol{\sigma}_{1,2}$ | Pauli matrices acting on particle 1 or 2 |
| $\hat{\mathbf{r}} = \mathbf{r}/r$ | Unit vector from source to field point |
| $\lambda = 1/m_\phi$ | Mediator Compton wavelength (interaction range) |
| $\mathbf{v}$ | Relative velocity of the particles |
| $f, \bar{f}$ | Matter fermion, antimatter fermion |

---

### The 16 Dobrescu–Mocioiu Potentials (Reference)

$$V_1 = \frac{e^{-r/\lambda}}{r}$$

$$V_2 = \boldsymbol{\sigma}_1\cdot\hat{\mathbf{r}}\left(\frac{1}{\lambda r}+\frac{1}{r^2}\right)\frac{e^{-r/\lambda}}{r}$$

$$V_3 = \boldsymbol{\sigma}_1\cdot\boldsymbol{\sigma}_2\frac{e^{-r/\lambda}}{r} - \frac{1}{3}(\boldsymbol{\sigma}_1\cdot\hat{\mathbf{r}})(\boldsymbol{\sigma}_2\cdot\hat{\mathbf{r}})\left(3+\frac{3}{\lambda r}+\frac{1}{\lambda^2 r^2}\right)\frac{e^{-r/\lambda}}{r}$$

$$V_4 = \left[(\boldsymbol{\sigma}_1\cdot\hat{\mathbf{r}})(\boldsymbol{\sigma}_2\cdot\hat{\mathbf{r}}) - \frac{1}{3}\boldsymbol{\sigma}_1\cdot\boldsymbol{\sigma}_2\right]\frac{e^{-r/\lambda}}{r}$$

$$V_5 = \boldsymbol{\sigma}_1\cdot(\hat{\mathbf{r}}\times\mathbf{v})\frac{e^{-r/\lambda}}{r}$$

$$V_6 = (\boldsymbol{\sigma}_1\cdot\mathbf{v})(\boldsymbol{\sigma}_2\cdot\mathbf{v})\frac{e^{-r/\lambda}}{r}$$

$$V_7 = \boldsymbol{\sigma}_1\cdot(\mathbf{v}\times\hat{\mathbf{r}})\frac{e^{-r/\lambda}}{r}$$

$$V_8 = \left\{\boldsymbol{\sigma}_1\cdot\mathbf{v},\,\frac{e^{-r/\lambda}}{r}\right\}$$

$$V_{14} = (\boldsymbol{\sigma}_1\cdot\hat{\mathbf{r}})(\boldsymbol{\sigma}_2\cdot\mathbf{v})\frac{e^{-r/\lambda}}{r}$$

(Remaining $V_9$–$V_{16}$ involve higher-order spin-velocity combinations; their SME mappings are noted where applicable.)

---

### Main Matching Table

| SME Coeff. | CPT | Lorentz | NR Hamiltonian (upper components) | DM Potential(s) | Leading Order | CPT signature |
|---|---|---|---|---|---|---|
| $b_i$ | Odd | Odd | $-b_i\sigma^i$ | $V_2$ (monopole-dipole, long-range limit) | $m^0$ | Sign flips: matter $-\mathbf{b}\cdot\boldsymbol{\sigma}$, antimatter $+\mathbf{b}\cdot\boldsymbol{\sigma}$ |
| $b_0$ | Odd | Odd | $+b_0\frac{\boldsymbol{\sigma}\cdot\mathbf{p}}{m}$ | $V_7$, $V_8$ | $m^{-1}$ | Sign flips for antimatter |
| $H_{ij}$ (magnetic-like) | Even | Odd | $-\mathcal{H}_B^k\sigma^k$ where $\mathcal{H}^k = \frac{1}{2}\epsilon^{ijk}H_{ij}$ | $V_3$ (dipole-dipole) | $m^0$ | Same sign for matter and antimatter |
| $H_{0i}$ (electric-like) | Even | Odd | $-\frac{1}{m}\boldsymbol{\sigma}\cdot(\mathbf{p}\times\mathbf{H}_E)$ | $V_7$ | $m^{-1}$ | Same sign for matter and antimatter |
| $d_{i0}$ | Even | Odd | $+d_{i0}m\,\sigma^i$ | $V_2$ (uniform, static) | $m^1$ (large but tiny coeff.) | Same sign for matter and antimatter |
| $d_{ij}$ | Even | Odd | $+d_{ij}p^j\sigma^i$ | $V_7$, $V_8$ | $m^0$ in velocity | Same sign; velocity-dependent |
| $d_{00}$ | Even | Even | $+d_{00}\boldsymbol{\sigma}\cdot\mathbf{p}$ | $V_8$ | $m^0$ in velocity | Same sign for matter and antimatter |

---

### CPT Rule for Antimatter

The sign flip for CPT-odd coefficients follows from the charge-conjugation operation on the FW-transformed spinor. For any CPT-odd SME coefficient $X$, the transformed Hamiltonian for an antiparticle acquires an overall minus sign relative to the particle case:

$$H^\text{NR}_\text{antiparticle}(X^\text{CPT-odd}) = -H^\text{NR}_\text{particle}(X^\text{CPT-odd})$$

For CPT-even coefficients:

$$H^\text{NR}_\text{antiparticle}(X^\text{CPT-even}) = +H^\text{NR}_\text{particle}(X^\text{CPT-even})$$

This is the theoretical basis for your asymmetry parameter:

$$A_\alpha = \frac{g_\alpha^f - g_\alpha^{\bar{f}}}{g_\alpha^f + g_\alpha^{\bar{f}}}$$

For a pure $b_\mu$ background: $g^{\bar{f}} = -g^f$, so $A_\alpha = \infty$ (or saturates to $\pm 1$ in the bounded definition). This is consistent with your measured $|A_\alpha| \approx 1$ across all $g_Ag_A$ pairs.

---

### Connecting Your Asymmetry Results to This Table

| Your pair | Coupling | DM Potential | Dominant SME coefficient | Expected $A_\alpha$ from theory |
|---|---|---|---|---|
| $g_sg_s$ / UNKNOWN / ee | Scalar-scalar | $V_1$ | None in minimal SME (requires $c_{\mu\nu}$) | Should be 0 if CPT holds; your 0.873 is anomalous |
| $g_Ag_A$ / V1 / ep | Axial-axial | $V_2$ | $b_\mu$ (CPT-odd) | $|A_\alpha| = 1$ — consistent with your 0.9998 |
| $g_Ag_A$ / V2 / ee | Axial-axial | $V_2$ | $b_\mu$ (CPT-odd) | $|A_\alpha| = 1$ — consistent with your 1.000 |

The $g_sg_s$ / UNKNOWN result at $|A_\alpha| = 0.873$ rather than 1 is the most interesting datum: it is lower than all $g_Ag_A$ pairs, which is consistent with the UNKNOWN potential not being purely CPT-odd. The large uncertainty ratio (matter $\sigma = 9.1\%$ vs antimatter $\sigma = 25.5\%$) suggests the antimatter constraint curve has more curvature variation — meaning fewer data points constrain that range, which inflates the weighted chi-squared denominator and drives the asymmetry away from exactly 1.

