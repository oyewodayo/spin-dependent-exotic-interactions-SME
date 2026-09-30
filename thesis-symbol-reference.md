# Complete Symbol and Notation Reference for the Thesis

*Covers Chapters 1–5 of `thesis/`: Introduction, Theoretical Foundations, the SME↔DM Mapping, the Constraint Database, and Gap Analysis. Cross-checked against the current thesis text, `docs/theory_notes/`, and the executed `derivations/sympy/` notebooks. Where different chapters use different notation for the same quantity, both are given, with a note.*

---

## Greek Letters / Dirac Algebra (Ch. 2–3)

| Symbol | Meaning | Context |
|--------|---------|---------|
| $\gamma^\mu$ | Dirac gamma matrices ($\mu=0,1,2,3$) | Relativistic fermion field theory |
| $\gamma^0$ | Time-like gamma matrix | Block-diagonal: $\text{diag}(1,1,-1,-1)$ in Dirac representation |
| $\gamma_5$ | $i\gamma^0\gamma^1\gamma^2\gamma^3$ | Chiral matrix; off-diagonal in Dirac representation |
| $\beta$ | $\gamma^0$ | Used in Foldy-Wouthuysen expansion |
| $\alpha^i$ | $\gamma^0\gamma^i$ ($i=1,2,3$) | Velocity operator; off-diagonal in Dirac representation |
| $\Sigma^i$ | $\text{diag}(\sigma^i,\sigma^i)$ | 4×4 spin matrix |
| $\sigma^i$ | Pauli matrices ($i=1,2,3$) | 2×2 spin operators for non-relativistic fermions |
| $\boldsymbol\sigma$ | $(\sigma^1,\sigma^2,\sigma^3)$ | Pauli vector |
| $D_\mu$ | Gauge-covariant derivative | Appears in the general SME Lagrangian (Ch. 1 Eq. 2, Ch. 2 Eq. sme-general) |
| $\eta_\Gamma$ | CPT parity of a bilinear $\bar\psi\Gamma\psi$ | $+1$ for $\Gamma\in\{\mathbb 1,\gamma^\mu,\sigma^{\mu\nu}\}$, $-1$ for $\Gamma\in\{\gamma_5,\gamma_5\gamma^\mu\}$ (Ch. 2, §"CPT Properties: General Argument") — does **not** apply directly to derivative-coupled coefficients ($c_{\mu\nu}$, $d_{\mu\nu}$); see the $d_{\mu\nu}$ row in "CPT Transformation Signs" below |

---

## SME Coefficients (Ch. 1–3)

| Symbol | Type | CPT | Lorentz | Definition |
|--------|------|-----|---------|------------|
| $a_\mu$ | Vector | **Odd** | Odd | $\mathcal L_a = -a_\mu\bar\psi\gamma^\mu\psi$; $H_{NR}=-a_0$ at $m^0$, $-a_iv^i/m$ at $m^{-1}$; no spin-dependent leading term |
| $b_\mu$ | Vector | **Odd** | Odd | $\mathcal L_b = -b_\mu\,\bar\psi\,\gamma_5\gamma^\mu\,\psi$ |
| $b_i$ | Spatial component of $b_\mu$ | **Odd** | Odd | $i=1,2,3$; generates $-\mathbf b\cdot\boldsymbol\sigma$ (matter) |
| $b_0$ | Temporal component of $b_\mu$ | **Odd** | Odd | Generates $+b_0(\boldsymbol\sigma\cdot\mathbf p)/m$ |
| $c_{\mu\nu}$ | Tensor (kinetic sector) | **Even** | Odd | $\mathcal L_c = -c_{\mu\nu}\bar\psi\gamma^\mu D^\nu\psi$; direction-dependent kinetic-energy modification; possible subleading $V_2$-type role via the $g_sg_s$ channel |
| $H_{\mu\nu}$ | Antisymmetric tensor | **Even** | Odd | $\mathcal L_H = -\frac12 H_{\mu\nu}\,\bar\psi\,\sigma^{\mu\nu}\,\psi$ |
| $H_{ij}$ | Spatial components ($i,j=1,2,3$) | **Even** | Odd | Magnetic-like; generates $-\boldsymbol{\mathcal H}_B\cdot\boldsymbol\sigma$ |
| $H_{0i}$ | Mixed components | **Even** | Odd | Electric-like; generates $-\frac1m\boldsymbol\sigma\cdot(\mathbf p\times\mathbf H_E)$ |
| $\mathcal H_B^k$ | $\frac12\varepsilon^{ijk}H_{ij}$ | **Even** | Odd | Dual magnetic-like vector from $H_{ij}$ |
| $H_E^i$ | $H_{0i}$ | **Even** | Odd | Electric-like vector from $H_{0i}$ |
| $d_{\mu\nu}$ | Traceless tensor (kinetic sector) | **Even** | Odd | $\mathcal L_d = \tfrac12 i\,\bar\psi\,d^{\mu\nu}\gamma_5\gamma_\mu\,\overleftrightarrow\partial_\nu\,\psi$ |
| $d_{i0}$ | Mixed components | **Even** | Odd | Generates $+d_{i0}\,m\,\sigma^i$ ($m^1$ enhancement) |
| $d_{ij}$ | Spatial components | **Even** | Odd | Generates $+d_{ij}\,p^j\,\sigma^i$ (velocity-dependent) |
| $d_{00}$ | Temporal component | **Even** | Odd | Generates $+d_{00}\,(\boldsymbol\sigma\cdot\mathbf p)$ (momentum-dependent); **nonzero** (traceless, not antisymmetric) |
| $e_\mu,\,f_\mu$ | Dimensionless vectors (kinetic sector) | **Odd** | Odd | No spin-dependent term: $e_\mu$ enters only spin-independent terms; $f_\mu$ is absent from $H_{NR}$ at linear order and removable by field redefinition (Altschul 2006) |
| $g_{\lambda\mu\nu}$ | Dimensionless tensor (kinetic sector) | **Odd** | Odd | Reduced in Ch. 4; generates $V_2$, $V_7$, $V_8$ |

**Convention note:** the $b_\mu$ term's operator ordering matters. This thesis uses $\gamma_5\gamma^\mu$ (not $\gamma^\mu\gamma_5$) throughout — Ch. 1 Eq. 2, Ch. 2 Eq. sme-minimal, and `FW_derivation_bmy.md` all agree on this. Since $\{\gamma_5,\gamma^\mu\}=0$, the two orderings are exact negatives of each other; `derivations/sympy/FW_bmu_term.ipynb` implements the opposite ordering internally and so reports the opposite sign for $H_{NR}(b_i)$ — a bookkeeping artifact of that convention, not an independent result (see the notebook's own convention note).

---

## Dobrescu–Mocioiu (DM) Coupling Constants and Potentials (Ch. 1–4)

| Symbol | Meaning |
|--------|---------|
| $g_s$ | Scalar coupling constant |
| $g_p$ | Pseudoscalar coupling constant |
| $g_V$ | Vector coupling constant |
| $g_A$ | Axial-vector coupling constant |
| $V(\mathbf r)=\sum_{i=1}^{16}V_i(\mathbf r)$ | Complete DM potential decomposition (Ch. 1 Eq., Ch. 2 §"Complete Catalogue") |

Ch. 2 gives the full closed-form $V_1$–$V_{16}$ catalogue (transcribed from Cong et al. 2025); the four potentials actually derived from SME coefficients in Ch. 3 are:

| Potential | Name | Closed form (Ch. 2) | SME Source (Ch. 3) |
|--------|------|------|------------|
| $V_2$ | Spin-spin | $-g_A^{(1)}g_A^{(2)}\,\frac{1}{4\pi}\,(\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2)\,\frac{e^{-r/\lambda}}{r}$ | $b_i$, $d_{i0}$ |
| $V_3$ | Dipole-dipole | $\frac{g^2}{4\pi}[\boldsymbol\sigma_1\cdot\boldsymbol\sigma_2 - 3(\boldsymbol\sigma_1\cdot\hat{\mathbf r})(\boldsymbol\sigma_2\cdot\hat{\mathbf r})]\frac{e^{-r/\lambda}}{r}$ | $H_{ij}$ |
| $V_7$ | Spin-velocity | Ch. 3's single-vertex form: $\frac{g^2}{4\pi}\boldsymbol\sigma_1\cdot(\mathbf v\times\hat{\mathbf r})\frac{e^{-r/\lambda}}{r}$. Ch. 2's closed two-body form: $V_{6,7}=-\frac{1}{2mr^2}[(\boldsymbol\sigma_1\cdot\mathbf v)(\boldsymbol\sigma_2\cdot\hat{\mathbf r})\pm(\boldsymbol\sigma_1\cdot\hat{\mathbf r})(\boldsymbol\sigma_2\cdot\mathbf v)](1-r\,d/dr)y(r)$ | $b_0$, $H_{0i}$, $d_{ij}$ |
| $V_8$ | Velocity-velocity | $\frac1r(\boldsymbol\sigma_1\cdot\mathbf v)(\boldsymbol\sigma_2\cdot\mathbf v)\,y(r)$ | $b_0$, $d_{ij}$, $d_{00}$ |
| $V_{9+10}$ | Monopole-dipole | $-\frac{g_pg_s}{8\pi m}(\boldsymbol\sigma\cdot\hat{\mathbf r})\left(\frac1{r^2}+\frac1{\lambda r}\right)e^{-r/\lambda}$ (Ch. 1's worked example; matches Ch. 2's general $V_{9,10}$ specialised to one spin) | Not derived from an SME coefficient in Ch. 3; appears as a database category in Ch. 4 |

**Note on $V_7$/$V_8$:** the per-coefficient matching sections in `FW_derivation_bmy.md` / `FW_derivation_dmunu.md` write these as single-vertex, schematic expressions (e.g. an anticommutator $\{(\boldsymbol\sigma\cdot\mathbf v), e^{-r/\lambda}/r\}$ for $V_8$) rather than the fully closed two-body forms above. Cite the Ch. 2 closed form when the exact functional form is asked for.

**Other DM potentials appearing only in Ch. 4's database (not derived in Ch. 3):** $V_1$ (monopole-monopole), $V_{1a}$, $V_{2+3}$, $V_{4+5}$, $V_{9+10}$, $V_{12+13}$ — these are combined labels used because the underlying experiments don't distinguish the adjacent catalogue potentials individually (e.g. $V_{2+3}$ = a dataset sensitive to both $V_2$ and $V_3$ without separating them). $V_6$, $V_{14}$ have no classified dataset in the compiled database at all.

---

## Operators and Hamiltonians (Ch. 1–3)

| Symbol | Meaning | Expression |
|--------|---------|------------|
| $H_0$ | Free Dirac Hamiltonian | $H_0 = \boldsymbol\alpha\cdot\mathbf p + \beta m$ |
| $H$ | Full Hamiltonian (free + perturbation) | Rigorous form (Ch. 2–3): $H = \beta m + \varepsilon_{\text{even}} + \varepsilon_{\text{odd}}$. Ch. 1's introductory sketch instead writes $H=\boldsymbol\alpha\cdot\mathbf p+\beta m+\delta H_{\mathrm{SME}}$ — same content, less formal split |
| $H_{NR}$ | Non-relativistic Hamiltonian | After Foldy-Wouthuysen transformation |
| $H_{\mathrm{spin}}^{\mathrm{eff}}$ | Spin-dependent part of $H_{NR}$ | Ch. 1's informal name for what Ch. 3 computes coefficient-by-coefficient |
| $H_b$ | $b_\mu$ contribution | $b_\mu\gamma^0\gamma_5\gamma^\mu$ |
| $H_d$ | $d_{\mu\nu}$ contribution | $-d^{\mu\nu}p_\nu\,\Gamma_\mu$ |
| $\Gamma_\mu$ | $\gamma^0\gamma_5\gamma_\mu$ | $\Gamma_0 = -\gamma_5$ (odd), $\Gamma_i = +\Sigma^i$ (even) |
| $\varepsilon_{\text{even}}$ | Even operator | Commutes with $\beta$ |
| $\varepsilon_{\text{odd}}$ | Odd operator | Anticommutes with $\beta$ |
| $S$ | FW generator | $S = -i\beta\varepsilon_{\text{odd}}/(2m)$ |
| (master expansion) | Order-$1/m$ FW result | $H' \approx \beta m + \varepsilon_{\text{even}} + \dfrac{\beta\varepsilon_{\text{odd}}^2}{2m} - \dfrac{[\varepsilon_{\text{odd}},\varepsilon_{\text{even}}]}{4m} + O(m^{-2})$ |

---

## Physical Quantities

| Symbol | Meaning |
|--------|---------|
| $m$ | Fermion mass |
| $m_\phi$ | Mediator (boson) mass |
| $\lambda$ | Interaction range: $\lambda=\hbar/(m_\phi c)=1/m_\phi$ in natural units |
| $\mathbf p$ | Momentum operator: $-i\nabla$ |
| $\mathbf v$ | Velocity. Single-particle NR relation $\mathbf v=\mathbf p/m$; in the two-body DM potentials, $\mathbf v=\mathbf v_{\text{rel}}$, the relative velocity of the pair |
| $\hat{\mathbf r}$ | Unit separation vector |
| $r$ | Distance between particles |
| $E$ | Energy eigenvalue (leading order: $m$) |
| $\langle\sigma_i\rangle_{\text{source}}$ | Macroscopic spin expectation of a polarised source, used in $b_i\leftrightarrow(g_A/2)\langle\sigma_i\rangle_{\text{source}}$ (Ch. 3 §"Matching to Dobrescu–Mocioiu Potentials") |

---

## The Asymmetry Parameter $A_\alpha$

Now standardized across the whole thesis on the $f/\bar f$ (fermion/antifermion) convention introduced in Ch. 1, matching the notation already used elsewhere for the general CPT rule ($H_{NR}^{\bar f}$, etc.):

$$
A_\alpha = \frac{g_\alpha^f-g_\alpha^{\bar f}}{g_\alpha^f+g_\alpha^{\bar f}}, \qquad \alpha\in\{s,p,V,A\}
$$

The channel index $\alpha$ is dropped when clear from context (Ch. 3's coefficient-by-coefficient sections write just $g_f/g_{\bar f}$), and Ch. 4 promotes the same quantity to a function of $\lambda$, $A_\alpha(\lambda)$, evaluated on a grid for each matched dataset pair. (This replaced an earlier inconsistency where Ch. 3 and Ch. 4 used $g_m/g_{\bar a}$ for the same quantity — now unified to $g_f/g_{\bar f}$ throughout.)

**Physical content, true regardless of which chapter states it:**
- Under exact CPT symmetry, $A_\alpha=0$ for every channel (Ch. 1).
- For a genuinely CPT-odd, exactly signed coupling ($g_{\bar f}=-g_f$), the formula's denominator vanishes identically — $A_\alpha$ **diverges**, it does not saturate at 1 (Ch. 3, confirmed with `sympy.limit`).
- What SPINDEP actually computes uses one-sided experimental **upper bounds**, not signed measurements, for both $g_f$ and $g_{\bar f}$. A ratio of two independent positive bounds of very different tightness approaches $\pm1$ regardless of the true CPT parity of the underlying physics — a sensitivity-gap effect (Ch. 1, 3, 4 all state this).
- Statistical significance (Z from 5.1 to 51 after the Ch. 4 autocorrelation correction) is **not** the same claim as evidence for CPT violation — every one of the fifteen matched pairs in Ch. 4 is significant, yet none can currently be read as CPT-violation evidence rather than a sensitivity gap (Ch. 4 §"Interpretation").

---

## Statistical / Database Notation (Ch. 4)

| Symbol | Meaning |
|--------|---------|
| `{V}{Author}{Year}_m_abs_{sector}.csv` | Filename convention for a compiled constraint dataset: potential label, source, and fermion sector encoded in the name |
| `ee`, `eebar`, `ep`, `epbar`, `emu`, `emubar`, `nn`, `np`, `pp`, … | Fermion-sector labels; `bar`-suffixed sectors are antimatter (e.g. `eebar` = electron–positron) |
| `UNKNOWN` | Potential label the parser could not resolve from a filename; retained rather than dropped or guessed, so the classification gap stays visible |
| $g_Ag_A$, $g_pg_s$, $g_sg_s$, $g_Vg_V$, $g_Ag_V$, $g_pg_p$ | Coupling-family classification tags for a dataset (which coupling type each side of the interaction uses), not a literal numeric product |
| $\chi^2$ | Chi-squared statistic; computed two ways in Ch. 4 (uniform 10% fractional uncertainty, and a curvature-weighted per-point uncertainty) |
| $\mathrm{dof}_{\text{eff}}$ | Effective degrees of freedom, corrected for autocorrelation among the 300 interpolated grid points (found to be 6–21, vs. the naive 300) |
| $p_{\text{eff}}$ | Significance recomputed against $\mathrm{dof}_{\text{eff}}$ |
| $\overline{\lvert A_\alpha\rvert}$ | Mean absolute asymmetry across the grid for one matched pair |
| 95% CI | Bootstrap (2000 resamples) confidence interval on $\overline{\lvert A_\alpha\rvert}$ |

---

## Important Signs and Their Meanings

| Sign/Expression | Meaning | Why |
|-----------------|---------|-----|
| $-\mathbf b\cdot\boldsymbol\sigma$ | Matter NR Hamiltonian for $b_i$ | $\gamma^0\gamma_5\gamma^i = -\Sigma^i$ |
| $+\mathbf b\cdot\boldsymbol\sigma$ | Antimatter NR Hamiltonian for $b_i$, CPT-conjugate state (spin reversed) | Hole theory with $\mathbf p\to-\mathbf p$, $\mathbf s\to-\mathbf s$; CPT-odd. At the same physical spin: $-\mathbf b\cdot\boldsymbol\sigma$ (Kostelecký & Lane rule $b\to+b$) |
| $+b_0(\boldsymbol\sigma\cdot\mathbf p)/m$ | NR Hamiltonian for $b_0$ | Odd operator becomes even via FW at $m^{-1}$ |
| $-\boldsymbol{\mathcal H}_B\cdot\boldsymbol\sigma$ | NR Hamiltonian for $H_{ij}$ | Standard Zeeman coupling; CPT-even |
| $-\frac1m\boldsymbol\sigma\cdot(\mathbf p\times\mathbf H_E)$ | NR Hamiltonian for $H_{0i}$ | Odd operator at $m^{-1}$ via FW |
| $+d_{i0}\,m\,\sigma^i$ | NR Hamiltonian for $d_{i0}$ | **Verified**: matches Kostelecký & Lane Eq. 4 exactly, sign included |
| $+d_{ij}\,p^j\,\sigma^i$ | NR Hamiltonian for $d_{ij}$ | Structure confirmed; **sign open** |
| $+d_{00}\,(\boldsymbol\sigma\cdot\mathbf p)$ | NR Hamiltonian for $d_{00}$ | Structure confirmed; **sign open** |
| $A_\alpha \to \infty$ | **Formal** result for exact signed CPT-odd relation | Denominator $g+(-g)=0$ |
| $A_\alpha \to \pm 1$ | **Actual** result from one-sided bounds | Sensitivity-gap effect; **not** CPT evidence |

---

## Commutation/Anticommutation Relations

| Relation | Meaning |
|----------|---------|
| $\{\gamma_5,\gamma^\mu\}=0$ | $\gamma_5$ anticommutes with all gamma matrices |
| $\gamma^0\gamma_5\gamma^i = -\Sigma^i$ | Spatial $b_i$ term is **even** (block-diagonal) |
| $\gamma^0\gamma_5\gamma^0 = \gamma_5$ | Temporal $b_0$ term is **odd** (off-diagonal) |
| $\gamma^0\sigma^{ij} = \varepsilon^{ijk}\Sigma^k$ | $H_{ij}$ term is **even** |
| $\gamma^0\sigma^{0i} = -\alpha^i$ | $H_{0i}$ term is **odd** |
| $\Gamma_0 = -\gamma_5$ | $d_{\mu\nu}$ temporal piece is **odd** |
| $\Gamma_i = +\Sigma^i$ | $d_{\mu\nu}$ spatial piece is **even** |
| $\varepsilon_{\text{even}}$ commutes with $\beta$ | Definition of an even operator |
| $\{\varepsilon_{\text{odd}},\beta\}=0$ | Odd operator anticommutes with $\beta$ |

---

## CPT Transformation Signs

| Coefficient | How CPT parity is established | Sign / Result |
|----------------|----------|-------------|
| $b_\mu$ | Bilinear rule: $\mathrm{CPT}[\bar\psi\gamma_5\gamma^\mu\psi]=-\bar\psi\gamma_5\gamma^\mu\psi$ | **CPT-odd** — Lagrangian changes sign |
| $H_{\mu\nu}$ | Bilinear rule: $\mathrm{CPT}[\bar\psi\sigma^{\mu\nu}\psi]=+\bar\psi\sigma^{\mu\nu}\psi$ | **CPT-even** — Lagrangian unchanged |
| $c_{\mu\nu}$ | Bilinear rule: vector ($-$) times derivative ($-$) | **CPT-even** |
| $d_{\mu\nu}$ | Bilinear rule: axial vector ($-$) times derivative ($-$) | **CPT-even** |
| $a_\mu$ | Bilinear rule: vector ($-$) | **CPT-odd** |
| $e_\mu,f_\mu,g_{\lambda\mu\nu}$ | Bilinear rule: scalar/pseudoscalar/tensor ($+$) times derivative ($-$) | **CPT-odd** |
| $b_\mu$ (charge conjugation) | $C[\bar\psi\gamma_5\gamma^\mu\psi]=+\bar\psi\gamma_5\gamma^\mu\psi$ (axial current C-even) | $C$ alone gives no sign difference; at the same physical spin the antiparticle has the same $b_\mu$ (Kostelecký & Lane: $b\to+b$). The CPT-odd flip appears between CPT-conjugate states |
| $H_{\mu\nu}$ (charge conjugation) | $C[\bar\psi\sigma^{\mu\nu}\psi]=-\bar\psi\sigma^{\mu\nu}\psi$ (tensor current C-odd) | Opposite sign at the same physical spin ($H\to-H$); same sign between CPT-conjugate states (CPT-even) |
| $d_{\mu\nu}$ (antiparticle) | Kostelecký & Lane: $d\to-d$ at the same physical spin | Same sign between CPT-conjugate states (CPT-even) |

CPT parities of the bilinears $\bar\psi\Gamma\psi$: scalar $+$, pseudoscalar $+$, vector $-$, axial vector $-$, tensor $+$ (Peskin & Schroeder 1995, §3.6); each derivative contributes a further $-$. This reproduces Kostelecký & Lane's classification for all eight coefficients. The matter–antimatter relations are verified for every coefficient family in `derivations/sympy/FW_antiparticle_all_coefficients.ipynb`.

**Correction from an earlier draft of this reference:** $d_{\mu\nu}$'s CPT-even property must **not** be attributed to a bilinear $\bar\psi\gamma_5\sigma^{\mu\nu}\psi$ — that is not $d_{\mu\nu}$'s Lagrangian (it isn't any of the three coefficients' Lagrangian; $H_{\mu\nu}$'s is $\bar\psi\sigma^{\mu\nu}\psi$, without the $\gamma_5$). Citing $\gamma_5\sigma^{\mu\nu}$ for $d_{\mu\nu}$ reproduces exactly the wrong mass-sector operator that `docs/theory_notes/FW_derivation_dmunu.md` used to (incorrectly) assume before it was corrected against Kostelecký & Lane (1999). (An earlier version of this table also claimed that $a_\mu$ and $d_{\mu\nu}$ could not be classified by the bilinear rule. They can, once the vector bilinear is given CPT parity $-$ and the derivative is counted.)

---

## Key Takeaways

1. **$b_\mu$ and $g_{\lambda\mu\nu}$ sign flip**: between CPT-conjugate states (antiparticle spin reversed), matter gets $-\mathbf b\cdot\boldsymbol\sigma$ and antimatter $+\mathbf b\cdot\boldsymbol\sigma$ (genuine CPT-odd signature). All three contributing $g$ families flip likewise. At the same physical spin the shifts coincide (Kostelecký & Lane rule).

2. **$H_{\mu\nu}$, $d_{\mu\nu}$, $c_{\mu\nu}$ same sign**: CPT-conjugate matter and antimatter states get the same coupling (CPT-even). At the same physical spin the spin-dependent $H$ and $d$ terms reverse sign.

3. **$A_\alpha$ ambiguity**: The ratio of one-sided upper bounds gives $|A_\alpha|\to1$ from sensitivity gaps, **not** necessarily from CPT violation — true at the formal level (Ch. 1, 3) and confirmed empirically across all fifteen matched pairs in the compiled database (Ch. 4), including the spin-independent $g_sg_s$ pair, whose asymmetry is comparable to that of the spin-dependent $g_Ag_A$ pairs.

4. **Statistical significance ≠ CPT evidence**: every matched pair in Ch. 4 is significant at effectively $p\to0$ after the autocorrelation correction, but significance answers "is this asymmetry real," not "is this asymmetry caused by CPT violation" — the sensitivity-gap explanation is not ruled out by significance alone.

5. **$d_{i0}$ mass enhancement**: $+d_{i0}\,m\,\sigma^i$ is **verified** and matches Kostelecký & Lane's Eq. (4) exactly, sign included.

6. **$d_{ij}, d_{00}$ sign**: Structure is correct, but **overall sign is open** pending a wavefunction-renormalization treatment of the kinetic sector.

7. **The central empirical limitation (Ch. 4–5)**: of 283 compiled datasets, 247 enter the analysis and only 22 of those touch an antimatter sector ($e$-$\bar p$, $e$-$\bar\mu$ from muonium, $e$-$e^+$, $\bar p$-He, $dd\mu^+$). That is why only fifteen matter–antimatter pairs (thirteen independent) can be matched, and why none of the sensitivity-gap-vs-CPT-violation ambiguities above can yet be resolved from the existing database.
