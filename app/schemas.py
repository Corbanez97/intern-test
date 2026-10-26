"""Pydantic models for the Part 5 API.  (Provided - read it, then finish the TODO.)

Well names look like A1..H12 (8 rows x 12 columns = 96-well plate).
"""
from __future__ import annotations

import re
from enum import Enum
from typing import Dict, List, Literal, Optional, Union

from pydantic import BaseModel, Field, field_validator, model_validator

WELL_RE = re.compile(r"^[A-H](?:[1-9]|1[0-2])$")


class SampleType(str, Enum):
    blank = "blank"
    standard = "standard"
    neg_control = "neg_control"
    pos_control = "pos_control"
    patient = "patient"


def _normalize_well(value: str) -> str:
    well = str(value).strip().upper()
    if not WELL_RE.match(well):
        raise ValueError(f"invalid well: {value!r} (expected A1..H12)")
    return well


class SampleIn(BaseModel):
    sample_id: str = Field(min_length=1)
    well: str
    sample_type: SampleType = SampleType.patient

    @field_validator("well", mode="before")
    @classmethod
    def _check_well(cls, v: str) -> str:
        return _normalize_well(v)


class RunCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    samples: List[SampleIn] = Field(min_length=1, max_length=96)

    # TODO (candidate): add a @model_validator(mode="after") that rejects a run
    # when two samples share the same well OR the same sample_id.
    # A request like that must come back as HTTP 422 (pydantic does this for you
    # when a validator raises ValueError).


class RunOut(BaseModel):
    id: int
    name: str
    n_samples: int
    n_readings: int


class ReadingIn(BaseModel):
    """One raw row coming from the reader. `mfi` is messy on purpose:
    it can be a number, a string like "23,5" or "OOR >", or null."""

    well: str
    analyte: str
    mfi: Union[float, str, None] = None
    bead_count: int = Field(ge=0)


class CallOut(BaseModel):
    well: str
    sample_id: str
    sample_type: SampleType
    analyte: str
    net_mfi: Optional[float]
    call: Literal["POS", "NEG", "INVALID"]


class ResultsOut(BaseModel):
    run_id: int
    run_valid: bool
    cutoffs: Dict[str, Optional[float]]
    calls: List[CallOut]
