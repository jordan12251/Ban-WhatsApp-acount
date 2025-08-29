import subprocess
import requests
import time
import json

# 🔑 Ton token et chat_id Telegram
TELEGRAM_TOKEN = "7767041903:AAEL4enFf0gWivFoZsOf"
CHAT_ID = "7874160840"

def get_last_sms():
    try:
        output = subprocess.check_output(["termux-sms-list"])
        sms_list = json.loads(output.decode("utf-8"))
        if sms_list:
            return sms_list[0]  # dernier SMS
    except Exception as e:
        print("Erreur:", e)
    return None

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

last_id = None
while True:
    sms = get_last_sms()
    if sms and sms["received"] != last_id:
        sender = sms.get("number", "Inconnu")
        body = sms.get("body", "")
        msg_id = sms.get("received", "")
        formatted = f"📩 Nouveau SMS\n👤 De: {sender}\n💬 {body}"
        send_telegram(formatted)
        print(formatted)
        last_id = msg_id
    time.sleep(5)
