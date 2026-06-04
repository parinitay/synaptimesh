from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import EEGCommand
from command_router import route_command
from command_router import latest_command
from mqtt_client import connect_mqtt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    connect_mqtt()

@app.get("/")
def home():
    return {
        "status": "Backend Running"
    }

@app.get("/dashboard")
def dashboard():
    return {
        "backend": "running",
        "mqtt": "connected",
        "latest_command": latest_command
    }

@app.post("/command")
def receive_command(data: EEGCommand):

    route_command(
        data.command,
        data.confidence
    )

    return {
        "received": data.command,
        "confidence": data.confidence
    }