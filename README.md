# Intercientifica - Python intern technical test

A ~4 hour, hands-on test that goes from Python basics to a small FastAPI service, on synthetic lab data (96-well plates, patient lists, reader measurements).

**Start here: [`notebooks/intern_test.ipynb`](notebooks/intern_test.ipynb)** - it contains the rules, the time guide and Parts 1-5. Part 6 is in [`DESIGN_ANSWER.md`](DESIGN_ANSWER.md); fill [`AI_LOG.md`](AI_LOG.md) at the end.

> AI tools are **allowed**. You must be able to explain everything you submit in a follow-up call.

## Setup (Python 3.10+)

```bash
python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# macOS / Linux:         source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

## Layout

```
notebooks/intern_test.ipynb   Parts 1-5 (basics, OOP, pandas, plots, API overview)
app/                          Part 5 - FastAPI service (schemas.py given, analysis.py + main.py to write)
tests/test_api.py             Part 5 - tests that must pass (add your own)
static/index.html             Part 5 bonus - tiny front-end at /ui
data/                         synthetic input files - do not edit
DESIGN_ANSWER.md              Part 6 - system design
AI_LOG.md                     how you used AI
```

## Useful commands

```bash
pytest -q                              # run the API tests
uvicorn app.main:app --reload          # run the API -> http://127.0.0.1:8000/docs  (UI: /ui)
```

## Submitting
1. Create your **private** copy from the template (do not make a public fork - other candidates could see your work) and invite the reviewer you were told about.
2. Work in a branch, commit as you go (we read the history).
3. *Restart kernel & Run All*, save the notebook **with outputs**, make sure `pytest -q` is green.
4. Send us the repo link.
