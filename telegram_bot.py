# telegram_bot.py

import os
import requests
from dotenv import load_dotenv

# Cargar tokens desde .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_telegram_message(message: str, parse_mode="Markdown"):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        raise ValueError("Faltan TELEGRAM_TOKEN o TELEGRAM_CHAT_ID en el .env")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": parse_mode,
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"❌ Error al enviar mensaje: {response.text}")
    else:
        print("✅ Mensaje enviado por Telegram")
