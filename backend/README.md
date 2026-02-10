Backend (FastAPI + SQLite + ESP32)

Overview
- FastAPI server that talks to an ESP32 over serial and stores couples in SQLite.
- Database file: `backend/database.db`

Setup
1) Create venv and install deps (from `backend/`):
   - `python -m venv .venv`
   - `.venv\\Scripts\\activate`
   - `pip install -r requirements.txt`
2) Set ESP32 port in `backend/main.py`:
   - `ESP_PORT = "COM7"`

Run
- From `backend/`:
  - `uvicorn main:app --reload --host 0.0.0.0 --port 8000`

API Endpoints
- `GET /` -> health check
- `GET /relay-on/{n}` -> turn relay 1..5 on
- `GET /relay-off/{n}` -> turn relay 1..5 off
- `POST /relay-on` -> body: `{ "relays": [1,2,3] }`
- `POST /relay-off` -> body: `{ "relays": [1,2,3] }`
- `POST /users` -> body: `{ "pria": "jaka", "wanita": "reni" }`
  - Auto-save `register_timestamp` in WIB (`Asia/Jakarta`).
- `GET /export/database` -> download SQLite file (`.db`)
- `GET /export/couples.xlsx` -> download data couples in Excel (`.xlsx`)

Notes
- SQLite tables must exist before inserts. Create tables at startup or via migration.
- CORS is enabled for `http://localhost:5173` and `http://127.0.0.1:5173`.
