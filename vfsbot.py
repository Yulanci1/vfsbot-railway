import os
import time
import pytesseract
import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
SLEEP = int(os.getenv("SLEEP_INTERVAL", 300))

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def check_slots():
    # Здесь вставь реальный код проверки VFS — можно использовать selenium или requests
    send_telegram("🔍 Слотов пока нет...")

if __name__ == "__main__":
    while True:
        try:
            check_slots()
        except Exception as e:
            send_telegram(f"⚠️ Ошибка: {str(e)}")
        time.sleep(SLEEP)
