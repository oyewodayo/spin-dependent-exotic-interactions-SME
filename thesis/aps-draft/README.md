# APS / REVTeX draft

Journal-article version of the thesis, targeted at **Physical Review D**.

## Build

```bash
pdflatex main && pdflatex main
```

Two passes are required to resolve cross-references. No bibliography tool
is needed — references are a hand-rolled `thebibliography` block, matching
the thesis, so there is no `.bib` file and no BibTeX/biber step.

Requires `revtex4-2`, which ships with TeX Live 2019 and later
(`texlive-publishers` on Debian/Ubuntu).

## Layout options

The class line is set to `reprint` (two-column, journal appearance). For a
double-spaced single-column referee copy, change `reprint` to `preprint`
in `\documentclass`. Nothing else needs to change.

## Figures

Figures are read from `../main_figures/` via `\graphicspath`; nothing is
duplicated into this directory, so regenerating the thesis figures updates
this draft automatically. Five of the thesis's twenty figures are used:

| Figure | File |
|---|---|
| 1 | `constraint_atlas/constraint_V2+3.png` |
| 2 | `matter_antimatter/gAgA_V2_ep_Karshenboim2011_vs_Ficek2018.png` |
| 3 | `matter_antimatter/gAgA_V2_ee_Jiao2019_vs_Karshenboim2011.png` |
| 4 | `gap_analysis/pair_coverage_matrix.png` |
| 5 | `gap_analysis/matter_antimatter_ratio.png` |

## Relationship to the thesis

This is a condensation, not a reformatting. Five thesis chapters become
eight article sections; the literature review is folded into the
introduction, the per-potential constraint atlas (twelve figures) is
reduced to one representative panel, and the methods chapter is compressed
to what is needed to reproduce the result.

All numbers are taken from the same `results/tables/dataset_registry.csv`
that the thesis uses, and were verified against it: 273 compiled, 15
excluded, 258 analysed, 19 antimatter, eleven matched pairs.

Content in the thesis but **not** carried into the article: the full
derivation intermediate steps, the per-potential figure set, the
supplementary coverage appendix, and the notation glossary.

## Before submitting

- Confirm author list, order and corresponding author
- Confirm the affiliation and add ORCID iDs if available
- Add funding/acknowledgement text if required by the department
- Consider whether PRD or PRA is the better venue — the mapping is PRD in
  character, but the atomic-spectroscopy data sources lean PRA
