import os
import uuid
import hashlib
from datetime import datetime

import httpx
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


async def tg_send_message(chat_id: int, text: str) -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        # если токена нет — не падаем, просто молча пропускаем
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    async with httpx.AsyncClient(timeout=10) as client:
        await client.post(url, json=payload)


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
            reply_text = "ERROR • code=EMPTY_CONFLICT_TEXT\nUsage: /run <your conflict text>"
            await tg_send_message(chat_id, reply_text)
            return JSONResponse({"status": "ok"})

        run_id = str(uuid.uuid4())
        request_hash = sha256_text(conflict_text)

        reply_text = (
            f"RUN CREATED • {run_id}\n"
            f"state={STATE_PHASE0_PENDING}\n"
            f"request_hash={request_hash}"
        )
        await tg_send_message(chat_id, reply_text)

        return JSONResponse({"status": "ok"})

    # базовый ответ на любые другие сообщения (чтобы видеть, что бот жив)
    await tg_send_message(chat_id, "OK. Use /run <text> to create a run.")
    return JSONResponse({"status": "ok"})
