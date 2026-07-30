"""
asymmetry_calc.py
==================
Compute the CPT asymmetry parameter

    A_alpha = (g_matter - g_antimatter) / (g_matter + g_antimatter)

across all compiled matter/antimatter pairs.

Thin wrapper around the real implementation in the SPINDEP
computational framework, vendored here as a git submodule at
`spindep-framework/` (pinned to a specific commit -- see
`.gitmodules` and `git submodule status`).

After cloning this repo, initialise the submodule with:
    git submodule update --init --recursive

IMPORTANT CAVEAT (see docs/theory_notes/potential_match_table.md and
FW_derivation_bmy.md Sec. 4.2): `coupling_abs` in the dataset registry is
an experimental *upper bound*, always positive, not a signed measured
coupling. |A_alpha| -> 1 whenever one bound is far tighter than the
other, regardless of the true CPT status of the underlying physics. Do
not read a high |A_alpha| value alone as evidence of CPT violation.
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

from spindep.src.asymmetry import compute_asymmetry  # noqa: E402

__all__ = ["compute_asymmetry"]


if __name__ == "__main__":
    import pandas as pd

    summary_path = _SPINDEP_ROOT / "spindep" / "results" / "tables" / "asymmetry_summary.csv"
    summary = pd.read_csv(summary_path)

    print(f"Loaded {len(summary)} matter/antimatter pairs from {summary_path.name}\n")
    cols = ["coupling", "potential", "sector", "mean_abs_A", "chi2_weighted", "p_value_weighted"]
    print(summary[cols].sort_values("mean_abs_A", ascending=False).to_string(index=False))

    print(f"\nMean |A_alpha| across all pairs: {summary['mean_abs_A'].mean():.4f}")
    print(f"Pairs with |A_alpha| > 0.95:      {(summary['mean_abs_A'] > 0.95).sum()} / {len(summary)}")
    print("\nSee the caveat in this file's module docstring before interpreting")
    print("these values as evidence of CPT violation vs. a sensitivity gap.")
