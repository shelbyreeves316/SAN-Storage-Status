# SAN Storage Status

This project provides a web interface for monitoring Btrfs volumes and SMART data on an Arch Linux system.

## Backend

A new FastAPI backend lives under `backend/`.
Install dependencies and run the API:

```bash
pip install -r backend/requirements.txt
uvicorn app.main:app --reload --app-dir backend/app
```

## Frontend

A React + Vite frontend will live under `frontend/` (placeholder for now).

## Legacy Flask App

The original Flask prototype remains as `app.py` and `static/`.
Run it with:

```bash
python app.py --port 8100
```
