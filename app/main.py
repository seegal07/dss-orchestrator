
import os
import uuid
import hashlib
import asyncio
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

STATE_NEW = "NEW"
STATE_PHASE0_PENDING = "PHASE0_PENDING"

@app.get("/")
async def health():
    return {"status": "ok"}


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()

    message = payload.get("message")
    if not message:
        return JSONResponse({"status": "ignored"})

    text = message.get("text", "")
    chat_id = message["chat"]["id"]

    if text.startswith("/run"):
        conflict_text = text.replace("/run", "").strip()

        if not conflict_text:
            return JSONResponse({
                "reply": "ERROR • code=EMPTY_CONFLICT_TEXT"
            })

        run_id = str(uuid.uuid4())
        request_hash = sha256_text(conflict_text)

        # Day-1: без БД, просто возврат модели состояния
        return JSONResponse({
            "reply": f"RUN CREATED • {run_id}",
            "run_id": run_id,
            "state": STATE_PHASE0_PENDING,
            "request_hash": request_hash
        })

    return JSONResponse({"status": "ok"})
