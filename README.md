# Terminabfrage-Bot für das Impfportal Niedersachsen mit Telegram-Benachrichtung

Ein einfacher Bot, der die REST-Api des niedersächsischen Impfportals abfragt und bei verfügbaren Terminen eine Nachricht an einen Telegram-Bot sendet.   
Website des Portals: https://www.impfportal-niedersachsen.de  
**Info**: Dieser Bot informiert nur über das Vorhandensein von Terminen, diese müssen danach selber auf dem Portal gebucht werden.

## **Wichtig**
Dieser Bot ist ein Hobbyprojekt und aus privatem Interesse und zum privaten Nutzen erstellt worden. Er verwendet eine öffentliche Schnittstelle. Solltet ihr den Bot selber verwenden wollen, macht dies bitte gewissenhaft und in vernünftigen Intervallen.

## Verwendet python
- python3 (https://www.python.org/)
- Package python-telegram-bot muss installiert werden (https://github.com/python-telegram-bot/python-telegram-bot)  
Installieren mit: `pip3 install python-telegram-bot`

## Setup & Ausführen
### Telegram-Bot
- Bot mit @botfather erstellen (https://t.me/botfather)
- Kommunikation mit dem Bot in den gewünschten Empfänger-Accounts starten (https://telegram.me/deine-bot-id)
- Zum Versenden der Botnachrichten werden die User-IDs der Empfänger benötigt. Diese können mit dem @userinfobot anzeigt werden (https://t.me/userinfobot)

### Bot-Parameter
- Die Konfigurationsdatei `src/constants.edit.py` zu `src/constants.py` umbennen
- Token des Bots und Chat-IDs der gewünschten Empfänger ersetzten und eintragen (s.o.)
- Ggf. optionale Parameter anpassen

### Starten
- Starten mit `python3 src/impfbot.py`

