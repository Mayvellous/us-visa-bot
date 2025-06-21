import time
from main import get_telegram_bot, start_tracking

def main():
    # Crée le bot Telegram
    bot, chat_id = get_telegram_bot()

    # Lancer la surveillance des créneaux disponibles
    while True:
        try:
            start_tracking(bot, chat_id)
        except Exception as e:
            print(f"Erreur détectée : {e}")
        time.sleep(60)  # Attente entre deux vérifications

if __name__ == "__main__":
    main()
