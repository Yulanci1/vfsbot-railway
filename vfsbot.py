import time
import os
import requests
from vfs_checker import check_slots  # Предположим, ты вынес парсинг в модуль
from telegram_send import send_to_telegram

# Все города VFS, где можно подать на визу во Францию
LOCATIONS = {
    "Москва": "moscow",
    "Санкт-Петербург": "saint-petersburg",
    "Екатеринбург": "ekaterinburg",
    "Казань": "kazan",
    "Новосибирск": "novosibirsk",
    "Нижний Новгород": "nizhniy-novgorod",
    "Самара": "samara",
    "Ростов-на-Дону": "rostov-on-don",
    "Краснодар": "krasnodar"
}

CHECKED_URLS = set()  # Чтобы не дублировать сообщения

SLEEP_INTERVAL = int(os.getenv("SLEEP_INTERVAL", 300))

while True:
    for city_name, city_code in LOCATIONS.items():
        try:
            print(f"🔍 Проверка слотов: {city_name}")
            result = check_slots(city_code, center="TLS")
            if result["available"]:
                if result["url"] not in CHECKED_URLS:
                    message = f"✅ Найден слот во Франции:\n📍 {city_name}\n🔗 {result['url']}"
                    send_to_telegram(message)
                    CHECKED_URLS.add(result["url"])
            else:
                print(f"❌ Нет слотов в {city_name}")
        except Exception as e:
            print(f"⚠️ Ошибка при проверке {city_name}: {e}")
    time.sleep(SLEEP_INTERVAL)
