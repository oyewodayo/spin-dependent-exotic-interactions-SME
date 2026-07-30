"""
chi_square_tests.py
====================
CPT consistency tests: weighted chi-squared comparison of matter and
antimatter coupling-constant bounds.

Thin wrapper around the real implementation in the SPINDEP
computational framework, vendored here as a git submodule at
`spindep_framework/` (pinned to a specific commit -- see
`.gitmodules` and `git submodule status`). The chi-squared machinery
(weighted chi-squared, effective-DOF correction, bootstrap CI on
|A_alpha|) lives there; updating the pinned commit is an explicit
`git submodule update --remote` + commit, so this repo never drifts
out of sync silently.

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

from spindep.src.statistics import (  # noqa: E402
    chi_squared_sensitivity,
    chi_squared_weighted,
    chi_squared_from_datasets,
    effective_dof,
    bootstrap_aalpha_ci,
)
from spindep.src.parser import load_dataset  # noqa: E402
from spindep.src.unit_conversion import convert_lambda_to_metres  # noqa: E402

__all__ = [
    "chi_squared_sensitivity",
    "chi_squared_weighted",
    "chi_squared_from_datasets",
    "effective_dof",
    "bootstrap_aalpha_ci",
]


def _load_pair(registry, matter_filename, antimatter_filename):
    """Load and unit-convert a matter/antimatter dataset pair by filename,
    looking up their paths in the real dataset registry."""
    m_row = registry.loc[registry["filename"] == matter_filename].iloc[0]
    a_row = registry.loc[registry["filename"] == antimatter_filename].iloc[0]

    df_m, _, _ = convert_lambda_to_metres(load_dataset(m_row["filepath"]), m_row["filename"])
    df_a, _, _ = convert_lambda_to_metres(load_dataset(a_row["filepath"]), a_row["filename"])
    return df_m, df_a


if __name__ == "__main__":
    import pandas as pd

    registry = pd.read_csv(_SPINDEP_ROOT / "spindep" / "results" / "tables" / "dataset_registry.csv")

    # Real pair: gpgp . V2+3 . e-e vs e+e- (Fadeev et al. 2022) -- also the
    # pair examined via SPINDEP's null-test / injection framework.
    df_m, df_a = _load_pair(registry, "3Fadeev_2022_4_m_abs_ee", "3Fadeev_2022_2_m_abs_ebare")

    result = chi_squared_from_datasets(df_m, df_a, n_boot=500)
    print("Pair: gpgp . V2+3 . e-e vs e-e+ (Fadeev et al. 2022)\n")
    print(f"  chi2_weighted      = {result['chi2_weighted']:.1f}  (dof={result['dof_weighted']})")
    print(f"  p-value (weighted) = {result['pval_weighted']:.3e}")
    print(f"  dof_effective      = {result['dof_effective']}  (autocorr_length={result['autocorr_length']:.1f})")
    print(f"  mean |A_alpha|     = {result['mean_abs_A']:.4f}  "
          f"95% CI [{result['aalpha_ci_low']:.4f}, {result['aalpha_ci_high']:.4f}]")
    print()
    print("Cross-check against the precomputed summary table "
          "(spindep_framework/spindep/results/tables/asymmetry_summary.csv):")
    summary = pd.read_csv(_SPINDEP_ROOT / "spindep" / "results" / "tables" / "asymmetry_summary.csv")
    row = summary[(summary.coupling == "gpgp") & (summary.potential == "V2+3") & (summary.sector == "ee")].iloc[0]
    print(f"  recorded mean |A_alpha| = {row['mean_abs_A']:.4f}, "
          f"chi2_weighted = {row['chi2_weighted']:.1f}")
