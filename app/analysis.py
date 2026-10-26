"""Part 5 - the analysis logic, as importable functions.

In Part 3 you built this inside the notebook. Here you move it into a module so
the API can reuse it. The rules are the ones written in the notebook, Part 3
("Calling rules"). Keep them identical.

Expected shapes
---------------
layout   : DataFrame with columns  well, sample_id, sample_type
readings : DataFrame with columns  well, analyte, mfi, bead_count      (RAW / messy)
"""
from __future__ import annotations

from typing import Dict, Optional, Tuple

import pandas as pd

MIN_BEADS = 35


def clean_readings(readings: pd.DataFrame) -> pd.DataFrame:
    """Normalise well names, make `mfi` numeric (NaN when unusable) and drop
    exact duplicate rows. Must not modify the input DataFrame."""
    raise NotImplementedError


def analyze(
    layout: pd.DataFrame, readings: pd.DataFrame
) -> Tuple[pd.DataFrame, Dict[str, Optional[float]], bool]:
    """Return (results, cutoffs, run_valid).

    results   : one row per (well, analyte) with at least the columns
                well, sample_id, sample_type, analyte, net_mfi, call
    cutoffs   : {analyte: cutoff or None}
    run_valid : bool
    """
    raise NotImplementedError
