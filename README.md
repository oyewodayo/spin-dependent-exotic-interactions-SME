# Exotic Spin-Dependent Interactions: A Unified SME Constraint Framework

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: MSc Research](https://img.shields.io/badge/Status-MSc%20Research-blue)]()
[![Institution: University of Ibadan](https://img.shields.io/badge/Institution-University%20of%20Ibadan-green)]()

---

## Overview

This repository documents the theoretical derivations, computational 
tools, constraint compilations, and analysis code for my MSc thesis 
in Theoretical Physics at the University of Ibadan, Nigeria.

**Thesis Title:**
> *Unified Constraint Framework for Exotic Spin-Dependent Interactions:
> Matter–Antimatter Sector Comparison*

**Student:** Oyewo Temidayo Solomon  
**Supervisor:** Professor O.E. Oyewande  
**Program:** MSc Theoretical Physics  
**Institution:** University of Ibadan, Nigeria  
**Duration:** March – September 2026  
**Contact:** oyewodayo@gmail.com

---

## Research Motivation

Exotic spin-dependent interactions mediated by ultralight bosons 
(axions, dark photons, Z′ bosons) represent a frontier in testing 
physics beyond the Standard Model (BSM). These interactions are 
motivated by fundamental open questions including:

- The strong-CP problem
- The nature of dark matter
- CPT symmetry violation
- Quantum theories of gravity

Despite over 100 experiments compiled through 2024 (Cong et al., 
Rev. Mod. Phys. 97, 025005, 2025), **no unified framework** 
systematically translates between different theoretical formalisms 
or compares matter-sector versus antimatter-sector constraints.

This project addresses that gap.

---

## Research Objectives

### Primary Objective
Develop a unified constraint framework that translates between the 
Standard Model Extension (SME) and the Dobrescu–Mocioiu exotic 
potential formulations, enabling systematic comparison of 
matter-sector and antimatter-sector bounds to test CPT symmetry.

### Specific Aims

**Aim 1 — Theoretical Derivation: SME → Exotic Potential Mapping**
- Apply Foldy–Wouthuysen transformation to the SME-modified fermion 
  Lagrangian
- Extract non-relativistic Hamiltonian including CPT-odd operators
- Match resulting potentials to the Dobrescu–Mocioiu basis ($$V_1–V_{16}$$)
- Derive closed-form translation formulas for $b_\mu$, $H_{\mu\nu}$, $d_{\mu\nu}$

Focus potentials: $V_2$, $V_3$, $V_7$, $V_8$ (matching what `docs/theory_notes/` actually derives; $V_{14}$ previously listed here does not appear in any derivation and was removed — no SME coefficient among $b_\mu, H_{\mu\nu}, d_{\mu\nu}$ has been shown to map to it)


**Aim 2 — Constraint Compilation and Cross-Platform Analysis**
- Build a comprehensive database of published constraints (2006–2024)
- Standardise all platforms to common units and coordinate systems
- Separate matter-sector vs antimatter-sector bounds
- Perform statistical CPT consistency tests via χ² analysis

**Aim 3 — Gap Analysis and Experimental Roadmap**
- Map constraint coverage across (potential, range, particle species)
- Identify unexplored parameter space in the antimatter sector
- Calculate precision requirements for detecting CPT-violating 
  asymmetries at naturalness scale

---

## Theoretical Framework

### Standard Model Extension (SME)
The SME is an effective field theory framework for Lorentz and CPT 
violation. The CPT-odd fermion sector Lagrangian includes:
$\mathcal{L}_{\mathrm{SME}} \supset b_{\mu}\,\bar{\psi}\gamma^{\mu}\gamma^{5}\psi$

where $b_\mu$ is a fixed CPT-violating background 4-vector.

### Dobrescu–Mocioiu Classification
The complete set of 16 non-relativistic potentials ($$V_{1}–V_{16}$$) 
categorises all single-boson-mediated spin-dependent interactions 
between spin-1/2 fermions, organised by discrete symmetry 
properties (C, P, T).

### Foldy–Wouthuysen Transformation
The standard technique for extracting the non-relativistic limit 
of relativistic quantum field theories. The derivation pipeline is:
```
SME Lagrangian → Modified Dirac Equation → FW Transformation 
→ H_NR (non-relativistic) → Matching → Dobrescu–Mocioiu Vi
```

### CPT Symmetry Test
The asymmetry parameter used in this work is:

$$A_{\alpha} = \frac{g_{\alpha}^{f} - g_{\alpha}^{\bar{f}}}{g_{\alpha}^{f} + g_{\alpha}^{\bar{f}}}$$

A large χ² (relative to dof) flags a statistically significant matter-antimatter
asymmetry — consistent with, though not on its own proof of, CPT violation (see
the caveat below: SPINDEP compares one-sided experimental bounds, not signed
measurements, so a sensitivity gap between experiments produces the same
signature). A small χ² is consistent with CPT symmetry within current
experimental precision.

---

## Repository Structure
```
exotic-spin-interactions-SME/
│
├── README.md                  # This file
├── LICENSE                    # MIT License
├── .gitignore                 # Python, LaTeX, Mathematica ignores
│
├── docs/                      # Documentation and notes
│   ├── theory_notes/
│   │   ├── FW_derivation_bmy.md
│   │   ├── FW_derivation_Hmunu.md
│   │   ├── FW_derivation_dmunu.md   # d_i0 -> V2 claim flagged unverified
│   │   └── potential_match_table.md
│   └── SPINDEP_one_pager.pdf  # one-page project summary for external review
│
├── derivations/               # Symbolic computation notebooks
│   └── sympy/
│       ├── FW_bmu_term.ipynb      # executed; see corrections in cells
│       ├── FW_Hmunu_term.ipynb    # executed
│       ├── dirac_algebra.py
│       └── pauli_matrices.py
│       # FW_dmunu_term.ipynb not yet created -- see caveat in
│       # FW_derivation_dmunu.md before relying on its claims
│
├── spindep-framework/         # Git SUBMODULE (not vendored/duplicated code) -- the actual
│                              # SPINDEP computational engine: dataset parser, unit
│                              # conversion, chi-squared statistics, constraint plotting,
│                              # the compiled dataset registry, and a GUI. Pinned to a
│                              # specific commit on the spindep_gui branch; update via
│                              # `git submodule update --remote` when the tool changes.
│
├── analysis/                  # Thin wrapper scripts around spindep-framework's real code
│   │                          # (import from the submodule; see each script's docstring)
│   ├── requirements.txt       # Python dependencies
│   ├── constraint_plots.py    # Coupling constant vs range plots (real, executable)
│   ├── chi_square_tests.py    # CPT consistency tests (real, executable)
│   ├── asymmetry_calc.py      # A_α parameter calculation (real, executable)
│   ├── unit_conversion.py     # Standardise units across platforms (real, executable)
│   └── notebooks/             # Interactive exploration -- not yet created; the SPINDEP
│                              # GUI (spindep-framework/gui/) currently serves this role
│
├── figures/                   # Generated publication-quality figures -- reproducible by
│   │                          # running analysis/constraint_plots.py (needs the submodule
│   │                          # initialised, see Installation below)
│   ├── constraint_atlas/      # 11 per-potential + 1 combined atlas plot
│   ├── matter_antimatter/     # 10 comparison plots (one per matched pair)
│   └── gap_analysis/          # 3 white-space identification plots
│
└── thesis/                    # Flat by design, to match the Overleaf project layout
    ├── main.tex                 # Master document -- \subfile{}s the 5 chapters below in
    │                            # order, with correct auto-numbering and one shared,
    │                            # deduplicated bibliography. Compile THIS for the real thesis.
    ├── 01_introduction.tex             # Chapter 1
    ├── 02_theoretical_foundations.tex  # Chapter 2: general SME, DM catalogue, FW method
    ├── 03_sme_dm_mapping.tex           # Chapter 3: explicit b_mu/H_munu/d_munu -> DM mapping
    ├── 04_constraint_database.tex      # Chapter 4: 273-dataset compilation + 10 matched pairs
    └── 05_gap_analysis.tex             # Chapter 5: coverage gaps + experimental strategy
                                 # Each chapter file also compiles standalone on its own
                                 # (via the `subfiles` package) for individual review.
                                 Note that this research work and the documentation here are work in progress. Updating and reviews and consistently been carried out until final satisfactaction. Your feedback is welcome. Thank you
```

---

## Installation and Usage

### Prerequisites
```bash
# Python environment
python >= 3.9
pip install -r analysis/requirements.txt

# For Mathematica notebooks
Wolfram Mathematica >= 12.0

# For LaTeX compilation
TeX Live or MiKTeX (full installation recommended)
```

### Setting Up the Python Environment
```bash
# Clone the repository AND its spindep-framework submodule
git clone --recurse-submodules https://github.com/oyewodayo/exotic-spin-interactions-SME.git
cd exotic-spin-interactions-SME

# If you already cloned without --recurse-submodules:
#   git submodule update --init --recursive

# Create virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r analysis/requirements.txt
```

### Running the Analysis
```bash
# Generate constraint plots
python analysis/constraint_plots.py

# Run CPT chi-square tests
python analysis/chi_square_tests.py

# Calculate asymmetry parameters
python analysis/asymmetry_calc.py
```

### Python Dependencies
```
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
pandas>=2.0.0
sympy>=1.12
jupyter>=1.0.0
seaborn>=0.12.0
```

---

## Key Results (Updated as Research Progresses)

### SME → Dobrescu-Mocioiu Translation Table

The table below matches the notes actually in `docs/theory_notes/`: $b_\mu$ (spatial) maps to $V_2$ (spin-spin, not the monopole-dipole form an earlier pass mislabeled it as), $b_\mu$ (temporal) maps to $V_7,V_8$, and $H_{\mu\nu}$ maps to $V_3$/$V_7$. The $d_{\mu\nu}$ row is marked unverified rather than derived, since that derivation hasn't yet been checked against the same Dirac-algebra tooling used for $b_\mu$ and $H_{\mu\nu}$ (see `FW_derivation_dmunu.md`).

| SME Coefficient | Target Potential | Coupling Relation | Status |
|----------------|-----------------|-------------------|--------|
| $b_\mu$ (spatial)  | $V_2$ (spin-spin) | $b_i \leftrightarrow g_A/2$ | Derived and verified (`FW_bmu_term.ipynb`, executed) |
| $b_\mu$ (temporal) | $V_7, V_8$ | $b_0 \sim (\sigma\cdot p)/m$ | Derived and verified |
| $H_{\mu\nu}$          | $V_3$ (from $H_{ij}$), $V_7$ (from $H_{0i}$) | $H_{ij}\sim g_T$ × tensor | Derived and verified (`FW_Hmunu_term.ipynb`, executed) |
| $d_{\mu\nu}$           | $V_2$ (from $d_{i0}$, claimed), $V_7,V_8$ (from $d_{ij}$, claimed) |$d_{ij} \sim g_{s} g_{A} / m$| **Unverified** — no executed notebook yet; the $d_{i0}\to V_2$ mass-enhancement claim did not reproduce under the same numeric check that caught the $b_\mu$ sign error |

### Matter-Antimatter Comparison Summary

Populated from `spindep-framework/spindep/results/tables/asymmetry_summary.csv` (see `analysis/asymmetry_calc.py`, which imports the submodule -- run `git submodule update --init --recursive` first). Numeric coupling-bound magnitudes aren't reproduced here (only $A_\alpha$, which the summary table stores directly) — see the CSV / `dataset_registry.csv` for the underlying bounds.

| Potential | Matter source | Antimatter source | Sector | $A_\alpha$ | Status |
|-----------|---------------|--------------------|--------|-----------|--------|
| $V_2$ ($g_Ag_A$)   | Karshenboim2011 | Ficek2018       | e-$\bar p$ | 0.9998 | Compiled |
| $V_2$ ($g_Ag_A$)   | Ficek2017       | Karshenboim2011 | e-e        | 0.9892 | Compiled |
| $V_{2+3}$ ($g_Ag_A$) | Ficek2017     | Fadeev2022      | e-e        | 0.9539 | Compiled |
| $V_{2+3}$ ($g_pg_p$) | Fadeev2022    | Fadeev2022      | e-e        | 0.9535 | Compiled |
| $V_{2+3}$ ($g_Vg_V$) | Fadeev2022    | Fadeev2022      | e-e        | 0.9535 | Compiled |
| $V_3$        | — | — | — | Planned (no compiled pair yet) |
| $V_7$        | — | — | — | Planned (no compiled pair yet) |
| $V_8$        | — | — | — | Planned (no compiled pair yet) |

**Caveat:** per `docs/theory_notes/potential_match_table.md`, a high $A_\alpha$ here is *consistent with* CPT violation but equally explained by a sensitivity gap between the matter- and antimatter-sector experiments — it is not, by itself, evidence of either. This holds even after correcting for the strongest statistical objection to the naive test: treating all 300 interpolated grid points per pair as independent degrees of freedom. `spindep-framework`'s `statistics.py` now estimates an effective dof from the autocorrelation length of the residuals (typically 6–21 per pair, not 300) and recomputes the p-value against it — every pair remains significant at effectively p≈0 even under that correction, which shifts the open question from "is the dof count wrong" to "why does the gap persist after correcting it."

---

## Progress Log

| Phase | Duration | Status | Notes |
|-------|----------|--------|-------|
| Literature Review | Weeks 1–4 | In progress | Cong et al. 2025 studied |
| FW: $b_\mu$ derivation | Week 5 | Complete | Executed and verified in `FW_bmu_term.ipynb`; a Dirac-algebra sign error was caught by running the computation and fixed |
| FW: $H_{\mu\nu}$ derivation | Week 6–7 | Complete | Executed and verified in `FW_Hmunu_term.ipynb` |
| FW: $d_{\mu\nu}$ derivation | Week 7–8 | Needs re-verification | Claimed results don't reproduce under the same numeric check that caught the $b_\mu$ error — see `FW_derivation_dmunu.md` |
| Constraint compilation | Weeks 9–14 | Substantially complete | 273 datasets, 10 matched pairs, 12+10+3 figures; reproducible via the `spindep-framework` submodule — see `analysis/` and `figures/` |
| Gap analysis | Weeks 15–18 | Figures compiled | `figures/gap_analysis/` (lambda coverage, matter/antimatter ratio, pair coverage matrix); written analysis not yet drafted |
| Thesis writing | Weeks 19–24 | In progress | Chapters 1–5 drafted (`thesis/`); Chapter 6 (conclusion) not yet started |

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
  author  = {Dobrescu, B.A. and Mocioiu, I.},
  title   = {Spin-dependent macroscopic forces from new particle exchange},
  journal = {JHEP},
  volume  = {0811},
  pages   = {005},
  year    = {2006}
}

@article{Kostelecky1999,
  author  = {Kosteleck\'{y}, V.A. and Lane, C.},
  title   = {Nonrelativistic quantum Hamiltonian for Lorentz violation},
  journal = {Phys. Rev. D},
  volume  = {60},
  pages   = {116010},
  year    = {1999}
}

@article{Fadeev2019,
  author  = {Fadeev, P. and others},
  title   = {Revisiting spin-dependent forces mediated by new bosons},
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

This project is licensed under the MIT License — see the 
[LICENSE](LICENSE) file for details.

---

## Citation

If you use any part of this work in your research, please cite:
```bibtex
@mastersthesis{Oyewo2026,
  author  = {Oyewo Temidayo Solomon},
  title   = {Unified Constraint Framework for Exotic Spin-Dependent 
             Interactions: Matter-Antimatter Sector Comparison},
  school  = {University of Ibadan},
  year    = {2026},
  note    = {MSc Thesis, Department of Physics}
}
```

---

## Acknowledgements

I am grateful to my supervisor **Professor O.E. Oyewande** for 
guidance and support throughout this research. This work draws 
heavily on the theoretical frameworks established by Kostelecký 
& Lane (1999), Dobrescu & Mocioiu (2006), and Fadeev et al. (2019), 
and the comprehensive experimental review by Cong et al. (2025).

---

*Last updated: July 2026*