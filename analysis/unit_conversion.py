"""
unit_conversion.py
===================
Standardise units across constraint-database platforms.

This is a thin wrapper around the real implementation in the SPINDEP
computational framework (`spindep_framework/spindep/src/unit_conversion.py`),
which is developed as a sibling repository to this one. The logic lives
there (not duplicated here) so the two repos never drift out of sync;
this file just exposes it under the name expected by this thesis repo's
`analysis/` layout and demonstrates it on the real dataset registry.

Requires `spindep_framework` checked out alongside this repo, i.e.:
    <parent>/spindep_framework/
    <parent>/exotic-spin-interactions-SME/   <- this repo
"""

import sys
from pathlib import Path

_SPINDEP_ROOT = Path(__file__).resolve().parents[2] / "spindep_framework"
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
