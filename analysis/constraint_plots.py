"""
constraint_plots.py
====================
Coupling-constant vs. interaction-range (lambda) constraint plots:
per-potential atlas panels, the combined 16-panel constraint atlas, and
matter/antimatter comparison figures.

Thin wrapper around the real implementation in the SPINDEP
computational framework, vendored here as a git submodule at
`spindep_framework/` (pinned to a specific commit -- see
`.gitmodules` and `git submodule status`). Regenerates the figures
already checked into `../figures/` from the live dataset registry (so
they can be reproduced/verified, not just viewed as static images).

After cloning this repo, initialise the submodule with:
    git submodule update --init --recursive
"""

import sys
from pathlib import Path

_SPINDEP_ROOT = Path(__file__).resolve().parents[1] / "spindep_framework"
if not _SPINDEP_ROOT.exists():
    raise ImportError(
        f"spindep_framework submodule not found at {_SPINDEP_ROOT}.\n"
        "Run: git submodule update --init --recursive"
    )
if str(_SPINDEP_ROOT) not in sys.path:
    sys.path.insert(0, str(_SPINDEP_ROOT))

from spindep.src.constraint_plots import (  # noqa: E402
    plot_single_potential,
    plot_constraint_atlas,
    plot_matter_antimatter_comparison,
    run_constraint_plots,
)
from spindep.src.parser import discover_datasets  # noqa: E402

__all__ = [
    "plot_single_potential",
    "plot_constraint_atlas",
    "plot_matter_antimatter_comparison",
    "run_constraint_plots",
]

THIS_REPO_FIGURES = Path(__file__).resolve().parents[1] / "figures"


if __name__ == "__main__":
    import pandas as pd

    dataset_root = _SPINDEP_ROOT / "spindep" / "datasets" / "normalized"
    datasets = discover_datasets(dataset_root)
    print(f"Discovered {len(datasets)} datasets from {dataset_root}")

    summary = pd.read_csv(_SPINDEP_ROOT / "spindep" / "results" / "tables" / "asymmetry_summary.csv")
    summary_rows = summary.to_dict("records")

    out_dir = THIS_REPO_FIGURES / "_regenerated"
    out_dir.mkdir(parents=True, exist_ok=True)

    run_constraint_plots(
        datasets=datasets,
        summary_rows=summary_rows,
        plots_dir=_SPINDEP_ROOT / "spindep" / "results" / "plots",
        figures_dir=out_dir,
    )
    print(f"\nRegenerated into {out_dir} -- compare against the checked-in")
    print(f"figures in {THIS_REPO_FIGURES} to verify reproducibility, then")
    print("remove the _regenerated/ scratch directory.")
