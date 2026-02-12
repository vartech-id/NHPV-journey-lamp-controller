# pc_api/main.py
from io import BytesIO
from pathlib import Path
from fastapi import FastAPI, HTTPException, Depends
from esp_client import ESP32SerialClient
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from contextlib import asynccontextmanager
import threading
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
from openpyxl import Workbook
from schemas.esp_relay import RelaysReq
from sqlalchemy.orm import Session
from db.session import get_db, engine
from models.users import Users
from schemas.users import UserCreate
from models.users import Base

serial_lock = threading.Lock()


def get_wib_timezone():
    try:
        return ZoneInfo("Asia/Jakarta")
    except ZoneInfoNotFoundError:
        # Fallback for environments without IANA tz database (common on Windows).
        return timezone(timedelta(hours=7), name="WIB")


WIB_TZ = get_wib_timezone()
DB_FILE_PATH = Path(__file__).resolve().parent / "database.db"

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    Base.metadata.create_all(bind=engine)
    try:
        esp.open()
        resp = esp.send_command("PING")
        print("ESP32 handshake:", resp)
    except Exception as exc:
        # Keep API alive so relay endpoints can trigger reconnect on demand.
        print("ESP32 handshake failed:", exc)

    yield  # app is running

    # shutdown
    try:
        esp.close()
    except Exception as exc:
        print("ESP32 close failed:", exc)

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# KONFIGURASI PORT ESP32
# =========================
ESP_PORT = "COM7" 

esp = ESP32SerialClient(port=ESP_PORT)

@app.get("/")
def root():
    return {"status": "ok", "message": "ESP32 Relay API running"}


@app.get("/relay-on/{n}")
def relay_on(n: int):
    if not (1 <= n <= 8):
        raise HTTPException(status_code=400, detail="Relay only supports 1..8")

    cmd = f"K{n}_ON"

    with serial_lock:
        try:
            resp = esp.send_command(cmd)
        except RuntimeError as exc:
            raise HTTPException(
                status_code=503, detail=f"ESP32 serial error while sending {cmd}: {exc}"
            ) from exc

    return {"sent": cmd, "resp": resp}

@app.get("/relay-off/{n}")
def relay_off(n: int):
    if not (1 <= n <= 8):
        raise HTTPException(status_code=400, detail="Relay only supports 1..8")

    cmd = f"K{n}_OFF"

    with serial_lock:                 
        try:
            resp = esp.send_command(cmd)
        except RuntimeError as exc:
            raise HTTPException(
                status_code=503, detail=f"ESP32 serial error while sending {cmd}: {exc}"
            ) from exc

    return {"sent": cmd, "resp": resp}

@app.post("/relay-on")
def relay_on_multi(req: RelaysReq):

    for n in req.relays:
        if not (1 <= n <= 8):
            raise HTTPException(status_code=400, detail="Relay only supports 1..8")

    results = []

    with serial_lock:
        for n in req.relays:
            cmd = f"K{n}_ON"
            try:
                resp = esp.send_command(cmd)
            except RuntimeError as exc:
                raise HTTPException(
                    status_code=503,
                    detail=f"ESP32 serial error while sending {cmd}: {exc}",
                ) from exc
            results.append({"n": n, "sent": cmd, "resp": resp})

    return {"count": len(results), "results": results}

@app.post("/relay-off")
def relay_off_multi(req: RelaysReq):

    for n in req.relays:
        if not (1 <= n <= 8):
            raise HTTPException(status_code=400, detail="Relay only supports 1..8")

    results = []

    with serial_lock:
        for n in req.relays:
            cmd = f"K{n}_OFF"
            try:
                resp = esp.send_command(cmd)
            except RuntimeError as exc:
                raise HTTPException(
                    status_code=503,
                    detail=f"ESP32 serial error while sending {cmd}: {exc}",
                ) from exc
            results.append({"n": n, "sent": cmd, "resp": resp})

    return {"count": len(results), "results": results}

# database
@app.post("/users")
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    now_wib = datetime.now(WIB_TZ)
    new_user = Users(
        pria=payload.pria,
        wanita=payload.wanita,
        register_timestamp=now_wib,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "id": new_user.id,
        "pria": new_user.pria,
        "wanita": new_user.wanita,
        "register_timestamp": new_user.register_timestamp.isoformat(),
    }


@app.get("/export/database")
def export_database():
    if not DB_FILE_PATH.exists():
        raise HTTPException(status_code=404, detail="Database file not found")

    filename = f"database-{datetime.now(WIB_TZ).strftime('%Y%m%d-%H%M%S')}.db"
    return FileResponse(
        path=DB_FILE_PATH,
        media_type="application/octet-stream",
        filename=filename,
    )


@app.get("/export/couples.xlsx")
def export_couples_excel(db: Session = Depends(get_db)):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "couples"
    worksheet.append(["id", "pria", "wanita", "register_timestamp"])

    users = db.query(Users).order_by(Users.id.asc()).all()
    for user in users:
        register_timestamp = (
            user.register_timestamp.isoformat() if user.register_timestamp else ""
        )
        worksheet.append([user.id, user.pria, user.wanita, register_timestamp])

    output = BytesIO()
    workbook.save(output)
    workbook.close()
    output.seek(0)

    filename = f"couples-{datetime.now(WIB_TZ).strftime('%Y%m%d-%H%M%S')}.xlsx"
    headers = {"Content-Disposition": f'attachment; filename="{filename}"'}
    return StreamingResponse(
        output,
        media_type=(
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ),
        headers=headers,
    )
