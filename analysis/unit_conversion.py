"""
unit_conversion.py
===================
Standardise units across constraint-database platforms.

This is a thin wrapper around the real implementation in the SPINDEP
computational framework, vendored here as a git submodule at
`spindep-framework/` (pinned to a specific commit -- see
`.gitmodules` and `git submodule status`). The logic lives there
(not duplicated here) so this repo and the framework never drift out
of sync silently; updating the pinned commit is an explicit
`git submodule update --remote` + commit.

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

from spindep.src.unit_conversion import (  # noqa: E402
    detect_unit_factor,
    convert_lambda_to_metres,
    audit_units,
)

__all__ = ["detect_unit_factor", "convert_lambda_to_metres", "audit_units"]


if __name__ == "__main__":
    import pandas as pd

    registry_path = _SPINDEP_ROOT / "spindep" / "results" / "tables" / "dataset_registry.csv"
    registry = pd.read_csv(registry_path)

    print(f"Loaded {len(registry)} datasets from {registry_path.name}\n")
    print("Unit factor detected per filename (first 10):")
    for filename in registry["filename"].head(10):
        factor, unit = detect_unit_factor(filename)
        print(f"  {filename:45s}  unit={unit:8s}  factor(to metres)={factor:.6e}")
