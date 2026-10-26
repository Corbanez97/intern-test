"""Part 5 - FastAPI service (skeleton).

Run it:   uvicorn app.main:app --reload
Docs:     http://127.0.0.1:8000/docs
Tests:    pytest -q

Endpoints you must build (see README for the full contract):
    GET  /health                    (given)
    POST /runs                      -> 201 RunOut
    GET  /runs/{run_id}             -> RunOut      | 404
    POST /runs/{run_id}/readings    -> {"added": n}| 404
    GET  /runs/{run_id}/results     -> ResultsOut  | 404 | 409 (no readings yet)

Do NOT rename `get_repo` - the tests replace it with a fresh repository.
"""
from __future__ import annotations

from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

from app import analysis
from app.schemas import ReadingIn, ResultsOut, RunCreate, RunOut  # noqa: F401


class RunRepository:
    """In-memory storage for runs.

    TODO (candidate): design the data you need to keep per run
    (name, samples, readings) and add the methods you need. Keep storage logic
    here and HTTP logic in the endpoints below.
    """

    def __init__(self) -> None:
        pass


_repo = RunRepository()


def get_repo() -> RunRepository:
    return _repo


app = FastAPI(title="Intern Test API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# TODO (candidate): the four endpoints above go here.


# Bonus (optional): a tiny front-end served from ./static at http://127.0.0.1:8000/ui
_static = Path(__file__).resolve().parent.parent / "static"
if _static.exists():
    app.mount("/ui", StaticFiles(directory=_static, html=True), name="ui")
