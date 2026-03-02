import os
import uuid
import hashlib
import logging

import httpx
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# --- logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("telegram")

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
        logger.warning(
            "TELEGRAM_BOT_TOKEN is missing. chat_id=%s text=%s",
            chat_id,
            text[:100],
        )
        return

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(url, json=payload)

        logger.info(
            "sendMessage -> status=%s body=%s",
            response.status_code,
            response.text[:300],
        )

    except Exception as e:
        logger.exception("sendMessage failed: %s", e)


@app.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()
    logger.info("Incoming update: %s", str(payload)[:500])

    message = payload.get("message")
    if not message:
        logger.info("No message field in update")
        return JSONResponse({"status": "ignored"})

    text = message.get("text", "")
    chat_id = message["chat"]["id"]

    logger.info("Message received: chat_id=%s text=%s", chat_id, text)

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

    # базовый ответ
    await tg_send_message(chat_id, "OK. Use /run <text> to create a run.")
    return JSONResponse({"status": "ok"})
