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

The React + Vite frontend is located in `frontend/`. Install dependencies and
start the dev server with:

```bash
cd frontend
npm install
npm run dev
```

## Legacy Flask App

The original Flask prototype remains as `app.py` and `static/`.
Run it with:

```bash
python app.py --port 8100
```
