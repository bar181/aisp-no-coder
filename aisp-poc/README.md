# Sprint 1 – AISP PoC Creator

A zero-boiler-plate demo: write one YAML idea sheet → generate specs →  
FastAPI reads those specs at startup and exposes CRUD endpoints.

## Quick-start

```bash
# 1. prepare env + install
cp .env.example .env
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. generate component specs
python generator/gen.py examples/vehicle.yml

# 3. optional: seed sample data
python scripts/seed.py

# 4. run API
uvicorn app.main:app --reload
```

Visit:

* `http://localhost:8000/docs` – Swagger UI  
* `http://localhost:8000/healthz` – health probe