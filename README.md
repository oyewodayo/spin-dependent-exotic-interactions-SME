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
- Match resulting potentials to the Dobrescu–Mocioiu basis (V1–V16)
- Derive closed-form translation formulas for $b_\mu$, $H_{\mu\nu}$, $d_{\mu\nu}$

Focus potentials: $V_2$, $V_3$, $V_7$, $V_{14}$


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
$$\mathcal{L}_{\mathrm{SME}} \supset b_{\mu} \bar{\psi} \gamma^{\mu} \gamma^{5} \psi$$

where b_μ is a fixed CPT-violating background 4-vector.

### Dobrescu–Mocioiu Classification
The complete set of 16 non-relativistic potentials (V1–V16) 
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

$$A_{\alpha} = \frac{g_{\alpha} f - g_{\alpha} \bar{f}}{g_{\alpha} f + g_{\alpha} \bar{f}}$$


A large χ² across experiments indicates CPT violation.  
A small χ² confirms CPT symmetry within experimental precision.

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
│   ├── theory_notes/          # Handwritten scan PDFs, typed notes
│   │   ├── FW_derivation_bmу.md
│   │   ├── FW_derivation_Hmunu.md
│   │   ├── FW_derivation_dmunu.md
│   │   └── potential_matching_table.md
│   ├── references/            # Annotated bibliography
│   │   └── bibliography.md
│   └── timeline/              # Research progress tracking
│       └── progress_log.md
│
├── derivations/               # Symbolic computation notebooks
│   ├── mathematica/
│   │   ├── FW_bmу_term.nb
│   │   ├── FW_Hmunu_term.nb
│   │   ├── FW_dmunu_term.nb
│   │   └── potential_matching.nb
│   └── sympy/
│       ├── FW_bmу_term.ipynb
│       ├── FW_Hmunu_term.ipynb
│       ├── dirac_algebra.py
│       └── pauli_matrices.py
│
├── constraints/               # Experimental constraint database
│   ├── data/
│   │   ├── matter_sector/
│   │   │   ├── NV_centres.csv
│   │   │   ├── torsion_balances.csv
│   │   │   └── atomic_magnetometers.csv
│   │   └── antimatter_sector/
│   │       ├── BASE_antiproton.csv
│   │       ├── ALPHA_antihydrogen.csv
│   │       └── positronium_hfs.csv
│   ├── schema.md              # Database column definitions
│   └── sources.md             # Data provenance and references
│
├── analysis/                  # Python analysis scripts
│   ├── requirements.txt       # Python dependencies
│   ├── constraint_plots.py    # Coupling constant vs range plots
│   ├── chi_square_tests.py    # CPT consistency tests
│   ├── asymmetry_calc.py      # A_α parameter calculation
│   ├── unit_conversion.py     # Standardise units across platforms
│   └── notebooks/
│       ├── 01_data_exploration.ipynb
│       ├── 02_constraint_atlas.ipynb
│       └── 03_CPT_comparison.ipynb
│
├── figures/                   # Generated publication-quality figures
│   ├── constraint_atlas/      # 16-panel Vi constraint plots
│   ├── matter_antimatter/     # Comparison plots
│   └── gap_analysis/          # White space identification plots
│
└── thesis/                    # Thesis writing (LaTeX)
    ├── main.tex
    ├── chapters/
    │   ├── 01_introduction.tex
    │   ├── 02_theory.tex
    │   ├── 03_FW_derivations.tex
    │   ├── 04_constraints.tex
    │   └── 05_conclusion.tex
    ├── figures/               # Symlinked from ../figures/
    └── references.bib
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
# Clone the repository
git clone https://github.com/YourUsername/exotic-spin-interactions-SME.git
cd exotic-spin-interactions-SME

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

| SME Coefficient | Target Potential | Coupling Relation | Status |
|----------------|-----------------|-------------------|--------|
| b_μ (spatial)  | V2 (dipole-dipole) | b_i ~ g_A × σ_source | ✅ Derived |
| b_μ (temporal) | V9+10 (monopole-dipole) | b_0 ~ g_p g_s / m | ✅ Derived |
| H_μν           | V3, V14 | H_ij ~ g_T × tensor | 🔄 In Progress |
| d_μν           | V7 (spin-velocity) | d_ij ~ g_s g_A / m | 📋 Planned |

### Matter-Antimatter Comparison Summary

| Potential | Best Matter Bound | Best Antimatter Bound | Asymmetry A_α | Status |
|-----------|------------------|----------------------|---------------|--------|
| V2        | — | — | — | 📋 Planned |
| V3        | — | — | — | 📋 Planned |
| V7        | — | — | — | 📋 Planned |
| V14       | — | — | — | 📋 Planned |

*Tables will be populated as constraints are compiled.*

---

## Progress Log

| Phase | Duration | Status | Notes |
|-------|----------|--------|-------|
| Literature Review | Weeks 1–4 | 🔄 In Progress | Cong et al. 2025 studied |
| FW: b_μ derivation | Week 5 | ✅ Complete | Verified vs K&L 1999 |
| FW: H_μν derivation | Week 6–7 | 🔄 In Progress | — |
| FW: d_μν derivation | Week 7–8 | 📋 Planned | — |
| Constraint compilation | Weeks 9–14 | 📋 Planned | — |
| Gap analysis | Weeks 15–18 | 📋 Planned | — |
| Thesis writing | Weeks 19–24 | 📋 Planned | — |

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

*Last updated: April 2026*