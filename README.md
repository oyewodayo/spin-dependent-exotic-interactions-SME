# Exotic Spin-Dependent Interactions: A Unified SME Constraint Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: MSc Research](https://img.shields.io/badge/Status-MSc%20Research-blue)]()
[![Institution: University of Ibadan](https://img.shields.io/badge/Institution-University%20of%20Ibadan-green)]()

---

## Overview

This repository holds the derivations, notes, thesis source and analysis
wrappers for my MSc thesis in Theoretical Physics at the University of
Ibadan, Nigeria. The computational pipeline (SPINDEP) and the compiled
constraint database live in a separate repository,
[spindep-framework](https://github.com/oyewodayo/spindep-framework), which is
included here as a git submodule.

**Thesis title:**
> *Unified Constraint Framework for Exotic Spin-Dependent Interactions:
> Matter–Antimatter Sector Comparison*

**Student:** Oyewo Temidayo Solomon  
**Supervisor:** Professor O. E. Oyewande  
**Programme:** MSc Theoretical Physics  
**Institution:** University of Ibadan, Nigeria  
**Duration:** March – September 2026  
**Contact:** oyewodayo@gmail.com

---

## Research Motivation

Light bosons predicted in many extensions of the Standard Model (axion-like
particles, dark photons, Z′ bosons) produce spin-dependent forces between
fermions. These forces bear on several open questions:

- the strong-CP problem
- the nature of dark matter
- CPT symmetry
- quantum theories of gravity

Cong et al. (Rev. Mod. Phys. 97, 025005, 2025) review more than a hundred
experiments that bound these forces. Two formalisms are in use: the Standard
Model Extension (SME), which describes Lorentz and CPT violation through
background coefficients, and the Dobrescu–Mocioiu (DM) potentials, the basis
in which most experiments report their limits. There has been no systematic
translation between the two, and matter-sector and antimatter-sector bounds
have not been compared side by side. This project does both.

---

## Research Objectives

### Main objective
Build a framework that translates between the SME and the Dobrescu–Mocioiu
potentials, and use it to compare matter-sector and antimatter-sector bounds
as a test of CPT symmetry.

### Specific aims

**Aim 1 — SME → DM mapping**
- Apply the Foldy–Wouthuysen reduction to the SME fermion Lagrangian.
- Extract the non-relativistic Hamiltonian, including the CPT-odd terms.
- Match each spin-dependent term to a DM potential.
- Cover every minimal-SME coefficient with a spin-dependent term:
  $b_\mu$, $d_{\mu\nu}$, $g_{\lambda\mu\nu}$ and $H_{\mu\nu}$.

**Aim 2 — Constraint compilation and matter–antimatter comparison**
- Compile published constraint curves into one database.
- Put every curve on common units (coupling against range $\lambda$ in metres).
- Separate matter-sector from antimatter-sector bounds and match them in pairs.
- Test each pair with an asymmetry parameter and a χ² comparison.

**Aim 3 — Gap analysis**
- Map coverage across potential, interaction range and fermion sector.
- Identify where antimatter data are missing.
- Say which measurements would turn the comparison into a real CPT test.

---

## Theoretical Framework

### Standard Model Extension
The SME is an effective field theory for Lorentz and CPT violation. Its
minimal fermion sector adds background coefficients to the Dirac Lagrangian
through two matrices,

$$M = m + a_\mu\gamma^\mu + b_\mu\gamma_5\gamma^\mu + \tfrac12 H_{\mu\nu}\sigma^{\mu\nu},$$

$$\Gamma^\nu = \gamma^\nu + c_{\mu}{}^{\nu}\gamma^\mu + d_{\mu}{}^{\nu}\gamma_5\gamma^\mu + e^\nu + i f^\nu\gamma_5 + \tfrac12 g^{\lambda\mu\nu}\sigma_{\lambda\mu}.$$

### Dobrescu–Mocioiu potentials
Sixteen non-relativistic potentials, $V_1$–$V_{16}$, cover every
spin-dependent interaction between two spin-½ fermions from single-boson
exchange, sorted by their C, P and T properties.

### Foldy–Wouthuysen reduction
```
SME Lagrangian → modified Dirac equation → FW reduction
→ non-relativistic Hamiltonian → match to DM potentials
```
The reduction follows Kostelecký & Lane (J. Math. Phys. 40, 6245, 1999). Their
Hamiltonian writes momenta with lower indices, $p_j = -p^j$; reading it that
way is what makes every term agree with the derivations here.

### Matter–antimatter comparison
For each matched pair of bounds on the same coupling and potential, SPINDEP
interpolates both curves onto a common grid in $\lambda$ and evaluates

$$A_{\alpha}(\lambda) = \frac{g_{\alpha}^{f}(\lambda) - g_{\alpha}^{\bar{f}}(\lambda)}{g_{\alpha}^{f}(\lambda) + g_{\alpha}^{\bar{f}}(\lambda)}.$$

Both inputs are one-sided upper limits, not signed measurements. If each
limit is a sensitivity times a common coupling, $U = s\,g_\star$, the coupling
cancels:

$$A_U = \frac{s_f - s_{\bar f}}{s_f + s_{\bar f}}.$$

A large $|A_\alpha|$ therefore measures how much tighter one experiment is
than the other. On its own it cannot separate CPT violation from a
sensitivity gap. A genuine test needs signed shifts or likelihoods from the
antimatter experiments.

---

## Repository Structure
```
exotic-spin-interactions-SME/
│
├── README.md
├── LICENSE                        # MIT
├── .gitignore
│
├── docs/
│   ├── theory_notes/
│   │   ├── FW_derivation_bmy.md       # b_mu
│   │   ├── FW_derivation_Hmunu.md     # H_munu
│   │   ├── FW_derivation_dmunu.md     # d_munu, including the covariant-momentum reading
│   │   ├── FW_derivation_gmunu.md     # g_lambdamunu
│   │   └── potential_match_table.md   # full SME -> DM table and the matched pairs
│   ├── SPINDEP_one_pager.tex          # one-page project summary
│   └── SPINDEP_one_pager.pdf
│
├── derivations/sympy/                 # executed SymPy notebooks behind every mapping
│   ├── FW_bmu_term.ipynb
│   ├── FW_Hmunu_term.ipynb
│   ├── FW_dmunu_term.ipynb
│   ├── FW_gmunu_term.ipynb
│   ├── FW_antiparticle_all_coefficients.ipynb   # particle vs antiparticle, all 16 families
│   ├── FW_bmu_asymmetry.pdf, FW_Hmunu_CPT_comparison.pdf, FW_dmunu_term.pdf
│   ├── dirac_algebra.py
│   └── pauli_matrices.py
│
├── spindep-framework/             # git submodule: the SPINDEP pipeline, the compiled
│                                  # dataset registry and the GUI
│
├── analysis/                      # small scripts that call the submodule
│   ├── requirements.txt       # what these scripts and the SymPy notebooks need
│   ├── constraint_plots.py        # regenerates the figures below
│   ├── chi_square_tests.py        # worked χ² example for one pair, checked against the summary table
│   ├── asymmetry_calc.py          # prints A_alpha, its interval and Z for all 15 pairs
│   └── unit_conversion.py         # audits the range units of every dataset
│
├── figures/                       # PNG copies of the pipeline figures
│   ├── constraint_atlas/          # one panel per potential plus the combined atlas
│   ├── matter_antimatter/         # one comparison plot per matched pair (15)
│   └── gap_analysis/              # coverage by range, sector and potential
│
└── thesis/
    ├── project/                   # the thesis (report class)
    │   ├── main.tex
    │   ├── 00_abstract.tex, 00_acknowledgements.tex, 00_certification.tex, 00_dedication.tex
    │   ├── 01_introduction.tex
    │   ├── 02_literature_review.tex
    │   ├── 03_materials_and_methods.tex
    │   ├── 04_results_and_discussion.tex
    │   ├── 05_conclusions.tex
    │   ├── 06_references.tex
    │   └── 07_appendices.tex      # notation, computational resources, extra coverage figures
    ├── aps-draft/                 # journal version for Physical Review D (REVTeX)
    │   ├── main.tex
    │   └── README.md
    └── main_figures/              # figures used by both the thesis and the APS draft
```

---

## Installation and Usage

### Prerequisites
- Python 3.9 or later
- A LaTeX distribution (TeX Live or MiKTeX) with `revtex4-2` for the APS draft

### Setting up
```bash
# Clone this repository together with the spindep-framework submodule
git clone --recurse-submodules https://github.com/oyewodayo/spin-dependent-exotic-interactions-SME.git
cd spin-dependent-exotic-interactions-SME

# If you cloned without --recurse-submodules:
#   git submodule update --init --recursive

python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

pip install -r analysis/requirements.txt   # the scripts below and the SymPy notebooks
```

### Running the analysis
```bash
python analysis/asymmetry_calc.py      # A_alpha, interval and Z for every pair
python analysis/chi_square_tests.py    # one pair from raw curves, compared with the table
python analysis/unit_conversion.py     # range-unit audit
python analysis/constraint_plots.py    # regenerates the figures into figures/_regenerated/
```

To rerun the full pipeline and rebuild the registry and summary table, see the
README in `spindep-framework/`.

### Building the documents
```bash
(cd thesis/project   && pdflatex main && pdflatex main)
(cd thesis/aps-draft && pdflatex main && pdflatex main)
(cd docs             && pdflatex SPINDEP_one_pager)
```

---

## Key Results

### SME → Dobrescu–Mocioiu dictionary

$b_\mu$, $d_{\mu\nu}$, $g_{\lambda\mu\nu}$ and $H_{\mu\nu}$ are the only
minimal-SME fermion coefficients with spin-dependent terms through third
order in $1/m$. $a_\mu$, $c_{\mu\nu}$ and $e_\mu$ give spin-independent terms
only, and $f_\mu$ does not enter at linear order (Kostelecký & Lane 1999,
J. Math. Phys. 40, 6245, Eq. 26). All four reductions below agree with that
paper term by term; `docs/theory_notes/potential_match_table.md` gives the
explicit Hamiltonian for each row.

| SME coefficient | CPT | DM potential | Order in $1/m$ | Notebook |
|-----------------|-----|--------------|----------------|----------|
| $b_i$ | odd | $V_2$ | $m^0$ | `FW_bmu_term.ipynb` |
| $b_0$ | odd | $V_7$, $V_8$ | $m^{-1}$ | `FW_bmu_term.ipynb` |
| $H_{ij}$ | even | $V_3$ | $m^0$ | `FW_Hmunu_term.ipynb` |
| $H_{0i}$ | even | $V_7$ | $m^{-1}$ | `FW_Hmunu_term.ipynb` |
| $d_{i0}$ | even | $V_2$ | $m^{+1}$ | `FW_dmunu_term.ipynb` |
| $d_{ij}$ | even | $V_7$, $V_8$ | $m^0$ (momentum) | `FW_dmunu_term.ipynb` |
| $d_{00}$ | even | $V_8$ | $m^0$ (momentum) | `FW_dmunu_term.ipynb` |
| $g_{[kl]0}$ | odd | $V_2$ | $m^{+1}$ | `FW_gmunu_term.ipynb` |
| $g_{[0k]0}$ | odd | $V_7$ | $m^0$ (momentum) | `FW_gmunu_term.ipynb` |
| $g_{[kl]j}$ | odd | $V_7$, $V_8$ | $m^0$ (momentum) | `FW_gmunu_term.ipynb` |

$e_\mu$, $f_\mu$ and $g_{\lambda\mu\nu}$ lie outside the renormalisable SME
proper (Colladay & Kostelecký 1998). They are kept because they can be
appreciable for composite particles such as nucleons (Kostelecký & Lane 1999,
Phys. Rev. D 60, 116010).

**Particle and antiparticle.** Compared between CPT-conjugate states (same
momentum, reversed spin), the CPT-odd $b_\mu$ and $g_{\lambda\mu\nu}$ terms
change sign and the CPT-even $d_{\mu\nu}$ and $H_{\mu\nu}$ terms do not.
Compared at the same physical spin, every one of these relations reverses.
`FW_antiparticle_all_coefficients.ipynb` checks both statements for all 16
coefficient families.

### Constraint database

| Quantity | Count |
|----------|-------|
| Datasets compiled | 283 |
| Datasets analysed | 247 (36 held out, each with a recorded reason) |
| Antimatter-sector datasets | 22 (9 $e$–$\bar p$, 6 muonium, 5 positronium, 1 $\bar p$He, 1 $dd\mu^+$) |
| Matter-sector datasets | 225 |
| Matched matter–antimatter pairs | 15 (13 independent) |

Seven of the twelve potentials and six of the eleven fermion-sector pairs have
no antimatter data at all. The $e$–$N$, $n$–$N$ and $p$–$N$ sectors hold 117
matter datasets between them and no antimatter counterpart.

### Matched pairs

From `spindep-framework/results/tables/asymmetry_summary.csv`. "ee" compares
$e$–$e$ with $e$–$e^+$; "ep" compares $e$–$p$ with $e$–$\bar p$. The interval
is the 95% bootstrap interval on the mean $|A_\alpha|$, and $Z$ is the
one-sided Gaussian significance after the χ² is rescaled to the effective
degrees of freedom.

| Coupling | Potential | Sector | Matter source | Antimatter source | Mean $\|A_\alpha\|$ | 95% interval | dof$_\text{eff}$ | $Z$ |
|---|---|---|---|---|---|---|---|---|
| $g_Ag_A$ | $V_3$ | ep | Cong2025 | Fadeev2022 | 1.0000 | [1.0000, 1.0000] | 8 | 51.1 |
| $g_Ag_A$ | $V_2$ | ep | Cong2025 | Ficek2018 | 0.9999 | [0.9999, 0.9999] | 21 | 34.4 |
| $g_Ag_A$ | $V_2$ | ep | Karshenboim2011 | Ficek2018 | 0.9998 | [0.9998, 0.9998] | 17 | 38.8 |
| $g_Ag_A$ | $V_2$ | ee | Ficek2017 | Karshenboim2011 | 0.9892 | [0.9886, 0.9896] | 21 | 48.2 |
| $g_Ag_A$ | $V_3$ | ee | Ficek2017 | Fadeev2022 | 0.9539 | [0.9518, 0.9557] | 6 | 38.5 |
| $g_pg_p$ | $V_3$ | ee | Fadeev2022 | Fadeev2022 | 0.9535 | [0.9516, 0.9552] | 6 | 37.1 |
| $g_Vg_V$ | $V_3$ | ee | Fadeev2022 | Fadeev2022 | 0.9535 | [0.9516, 0.9552] | 6 | 37.1 |
| $g_pg_p$ | $V_3$ | ep | Cong2025 | Ficek2018 | 0.9304 | [0.9293, 0.9314] | 6 | 34.3 |
| $g_Ag_A$ | $V_3$ | ep | Cong2025 | Ficek2018 | 0.9303 | [0.9292, 0.9313] | 6 | 34.3 |
| $g_sg_s$ | $V_1$ | ee | Delaunay2017 | Adkins2022 | 0.8727 | [0.8686, 0.8770] | 21 | 25.7 |
| $g_Ag_A$ | $V_3$ | ep | Fadeev2022 | Ficek2018 | 0.8237 | [0.8168, 0.8299] | 6 | 37.3 |
| $g_Ag_A$ | $V_3$ | ep | Fadeev2022 | Fadeev2022 | 0.8044 | [0.8024, 0.8063] | 8 | 43.8 |
| $g_Vg_V$ | $V_3$ | ep | Fadeev2022 | Ficek2018 | 0.7994 | [0.7971, 0.8015] | 7 | 31.8 |
| $g_pg_p$ | $V_3$ | ep | Fadeev2022 | Ficek2018 | 0.7994 | [0.7971, 0.8015] | 7 | 31.8 |
| $g_Ag_A$ | $V_2$ | ee | Jiao2019 | Karshenboim2011 | 0.3336 | [0.3197, 0.3474] | 9 | 5.1 |

The two $g_pg_p$/$g_Vg_V$ rows that repeat exactly use the same pair of
source curves, which is why 15 pairs give 13 independent comparisons.

Every pair is significant ($Z$ from 5.1 to 51) even after the autocorrelation
correction, which cuts the 300 grid points per pair down to 6–21 effective
degrees of freedom. That significance is about the size of the sensitivity
gap, not about CPT. The data show this directly: each of the four pairs built
on the 2025 hydrogen bounds (Cong2025) has a twin that uses an older matter
bound for the same antimatter curve, and in every case the tighter matter
bound gives the larger asymmetry.

---

## Progress Log

| Phase | Period | Status | Notes |
|-------|--------|--------|-------|
| Literature review | Weeks 1–4 | Complete | Built on Cong et al. (2025) and the primary SME and DM papers |
| FW reduction: $b_\mu$ | Week 5 | Complete | `FW_bmu_term.ipynb` |
| FW reduction: $H_{\mu\nu}$ | Weeks 6–7 | Complete | `FW_Hmunu_term.ipynb` |
| FW reduction: $d_{\mu\nu}$ | Weeks 7–8 | Complete | `FW_dmunu_term.ipynb`; agrees with Kostelecký & Lane once $p_j = -p^j$ |
| FW reduction: $g_{\lambda\mu\nu}$ | Weeks 8–9 | Complete | `FW_gmunu_term.ipynb` |
| Particle–antiparticle check | Week 9 | Complete | `FW_antiparticle_all_coefficients.ipynb`, all 16 families |
| Constraint compilation | Weeks 9–14 | Complete | 283 datasets, 247 analysed, 15 matched pairs (`spindep-framework`) |
| Gap analysis | Weeks 15–18 | Complete | `figures/gap_analysis/`; thesis Chapter 4 |
| Thesis and journal draft | Weeks 19–26 | Complete, under review | `thesis/project/`, `thesis/aps-draft/` |

---

## Key References
```bibtex
@article{Cong2025,
  author  = {Cong, Lei and others},
  title   = {Spin-dependent exotic interactions},
  journal = {Rev. Mod. Phys.},
  volume  = {97},
  pages   = {025005},
  year    = {2025}
}

@article{Dobrescu2006,
  author  = {Dobrescu, B. A. and Mocioiu, I.},
  title   = {Spin-dependent macroscopic forces from new particle exchange},
  journal = {JHEP},
  volume  = {11},
  pages   = {005},
  year    = {2006}
}

@article{KosteleckyLane1999JMP,
  author  = {Kosteleck\'{y}, V. A. and Lane, C. D.},
  title   = {Nonrelativistic quantum Hamiltonian for Lorentz violation},
  journal = {J. Math. Phys.},
  volume  = {40},
  pages   = {6245},
  year    = {1999}
}

@article{KosteleckyLane1999PRD,
  author  = {Kosteleck\'{y}, V. A. and Lane, C. D.},
  title   = {Constraints on Lorentz violation from clock-comparison experiments},
  journal = {Phys. Rev. D},
  volume  = {60},
  pages   = {116010},
  year    = {1999}
}

@article{Colladay1998,
  author  = {Colladay, D. and Kosteleck\'{y}, V. A.},
  title   = {Lorentz-violating extension of the standard model},
  journal = {Phys. Rev. D},
  volume  = {58},
  pages   = {116002},
  year    = {1998}
}

@article{Fadeev2019,
  author  = {Fadeev, P. and others},
  title   = {Revisiting spin-dependent forces mediated by new bosons:
             Potentials in the coordinate-space representation for
             macroscopic- and atomic-scale experiments},
  journal = {Phys. Rev. A},
  volume  = {99},
  pages   = {022113},
  year    = {2019}
}

@article{Smorra2017,
  author  = {Smorra, C. and others},
  title   = {A parts-per-billion measurement of the antiproton
             magnetic moment},
  journal = {Nature},
  volume  = {550},
  pages   = {371},
  year    = {2017}
}

@article{Ahmadi2017,
  author  = {Ahmadi, M. and others},
  title   = {Observation of the 1S-2S transition in trapped
             antihydrogen},
  journal = {Nature},
  volume  = {541},
  pages   = {506},
  year    = {2017}
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE)
file for details.

---

## Citation

If you use any part of this work, please cite:
```bibtex
@mastersthesis{Oyewo2026,
  author  = {Oyewo, Temidayo Solomon},
  title   = {Unified Constraint Framework for Exotic Spin-Dependent
             Interactions: Matter-Antimatter Sector Comparison},
  school  = {University of Ibadan},
  year    = {2026},
  note    = {MSc Thesis, Department of Physics}
}
```

---

## Acknowledgements

I am grateful to my supervisor, **Professor O. E. Oyewande**, for guidance and
support throughout this research. The work builds on the frameworks of
Colladay & Kostelecký (1998), Kostelecký & Lane (1999), Dobrescu & Mocioiu
(2006) and Fadeev et al. (2019), and on the experimental review by Cong et al.
(2025).
