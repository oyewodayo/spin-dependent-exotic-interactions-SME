"""
chi_square_tests.py
====================
CPT consistency tests: weighted chi-squared comparison of matter and
antimatter coupling-constant bounds.

Thin wrapper around the real implementation in the SPINDEP
computational framework, included here as a git submodule at
`spindep-framework/` (pinned to a specific commit -- see
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

_SPINDEP_ROOT = Path(__file__).resolve().parents[1] / "spindep-framework"
if not _SPINDEP_ROOT.exists():
    raise ImportError(
        f"spindep-framework submodule not found at {_SPINDEP_ROOT}.\n"
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


def _load_pair(registry, coupling, matter_filename, antimatter_filename):
    """Load a matter/antimatter dataset pair and convert lambda to metres.

    The same file name can appear under more than one coupling folder
    (gVgV and gpgp share the Fadeev 2022 curves), so the coupling is part
    of the lookup. Registry paths are relative to the spindep-framework
    root.
    """
    rows = registry[registry["coupling"] == coupling]
    m_row = rows.loc[rows["filename"] == matter_filename].iloc[0]
    a_row = rows.loc[rows["filename"] == antimatter_filename].iloc[0]

    df_m, _, _ = convert_lambda_to_metres(
        load_dataset(_SPINDEP_ROOT / m_row["filepath"]), m_row["filename"])
    df_a, _, _ = convert_lambda_to_metres(
        load_dataset(_SPINDEP_ROOT / a_row["filepath"]), a_row["filename"])
    return df_m, df_a


if __name__ == "__main__":
    import pandas as pd

    registry = pd.read_csv(_SPINDEP_ROOT / "results" / "tables" / "dataset_registry.csv")

    # Worked example: gpgp, V3, e-e against e-e+ (both from Fadeev et al. 2022).
    # This is also the pair used for SPINDEP's null test and signal injection.
    df_m, df_a = _load_pair(registry, "gpgp",
                            "3Fadeev_2022_4_m_abs_ee", "3Fadeev_2022_2_m_abs_ebare")

    # Same grid size as the pipeline, so the numbers match the summary table.
    result = chi_squared_from_datasets(df_m, df_a, n_points=300)
    print("Pair: gpgp, V3, e-e vs e-e+ (Fadeev et al. 2022)\n")
    print(f"  chi2_weighted        = {result['chi2_weighted']:.1f}  (on {result['dof_weighted']} grid points)")
    print(f"  dof_effective        = {result['dof_effective']}  (autocorr_length = {result['autocorr_length']:.1f})")
    print(f"  chi2 (effective dof) = {result['chi2_weighted_eff']:.1f}")
    print(f"  log10 p (effective)  = {result['log10_pval_weighted_eff']:.1f}")
    print(f"  Z (effective)        = {result['z_weighted_eff']:.1f}")
    print(f"  mean |A_alpha|       = {result['mean_abs_A']:.4f}  "
          f"95% CI [{result['aalpha_ci_low']:.4f}, {result['aalpha_ci_high']:.4f}]")
    print()
    print("Cross-check against the pipeline's summary table "
          "(spindep-framework/results/tables/asymmetry_summary.csv):")
    summary = pd.read_csv(_SPINDEP_ROOT / "results" / "tables" / "asymmetry_summary.csv")
    row = summary[(summary.coupling == "gpgp") & (summary.potential == "V3")
                  & (summary.sector == "ee")].iloc[0]
    print(f"  recorded mean |A_alpha| = {row['mean_abs_A']:.4f}, "
          f"Z (effective) = {row['z_weighted_eff']:.1f}")
