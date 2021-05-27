# Settings
plz = 12345
birthdate = "01.01.1970"

# Request
request_interval = 5*60 # Sekunden

request_interval_overnight = 60*60 # Sekunden, Drosseln der Abfragehäufigkeit über Nacht
night_start = 19
night_end = 7

request_interval_ipban = 2*60*60 # Sekunden
retry_count = 5 # Wiederholungen bei ungültigen Antworten z.B. Captcha

# Telegram
bot_token = "TOKEN" # Ein Impfbot kann mit dem "BotFather" erstellt werden
telegram_chat_ids = [00000000]  # Empfänger-IDs der Nachrichten Lässt sich mit dem "userinfobot" anzeigen
enable_telegram = True  # Versenden von Nachrichten an/ausschalten
enable_telegram_level_info = False  # False: Nur Impftermine & Fehler werden gesendet #True: Alle Meldungen (z.B. Info-Level) werden per Telegram versendet
client_id = "Device" # Eine ID, die in der Telegram-Nachricht zur Zuordnung des sendenden Clienten angezeigt wird