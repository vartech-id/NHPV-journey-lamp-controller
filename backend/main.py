# pc_api/main.py
from fastapi import FastAPI, HTTPException,Depends
from esp_client import ESP32SerialClient
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import threading
from schemas.esp_relay import RelaysReq
from sqlalchemy.orm import Session
from db.session import get_db, engine
from models.users import Users
from schemas.users import UserCreate
from models.users import Base

serial_lock = threading.Lock()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    Base.metadata.create_all(bind=engine)
    esp.open()
    resp = esp.send_command("PING")
    print("ESP32 handshake:", resp)

    yield  # app is running

    # shutdown
    esp.close()

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
        raise HTTPException(status_code=400, detail="Relay only supports 1..5")

    cmd = f"K{n}_ON"

    with serial_lock:
        resp = esp.send_command(cmd)

    return {"sent": cmd, "resp": resp}

@app.get("/relay-off/{n}")
def relay_off(n: int):
    if not (1 <= n <= 8):
        raise HTTPException(status_code=400, detail="Relay only supports 1..5")

    cmd = f"K{n}_OFF"

    with serial_lock:                 
        resp = esp.send_command(cmd)

    return {"sent": cmd, "resp": resp}

@app.post("/relay-on")
def relay_on_multi(req: RelaysReq):

    for n in req.relays:
        if not (1 <= n <= 8):
            raise HTTPException(status_code=400, detail="Relay only supports 1..5")

    results = []

    with serial_lock:
        for n in req.relays:
            cmd = f"K{n}_ON"
            resp = esp.send_command(cmd)
            results.append({"n": n, "sent": cmd, "resp": resp})

    return {"count": len(results), "results": results}

@app.post("/relay-off")
def relay_off_multi(req: RelaysReq):

    for n in req.relays:
        if not (1 <= n <= 8):
            raise HTTPException(status_code=400, detail="Relay only supports 1..5")

    results = []

    with serial_lock:
        for n in req.relays:
            cmd = f"K{n}_OFF"
            resp = esp.send_command(cmd)
            results.append({"n": n, "sent": cmd, "resp": resp})

    return {"count": len(results), "results": results}

# database
@app.post("/users")
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    new_user = Users(pria=payload.pria, wanita=payload.wanita)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"id": new_user.id, "pria": new_user.pria, "wanita": new_user.wanita}