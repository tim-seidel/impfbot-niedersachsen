# Terminabfrage-Bot für das Impfportal Niedersachsen mit Telegram-Benachrichtung

Ein einfacher Bot, der die REST-Api des niedersächsischen Impfportals abfragt und bei verfügbaren Terminen eine Nachricht an einen Telegram-Bot sendet.   
Website des Portals: https://www.impfportal-niedersachsen.de  
**Info**: Dieser Bot informiert nur über das Vorhandensein von Terminen, diese müssen danach selber auf dem Portal gebucht werden.

## **Wichtig**
Dieser Bot ist ein Hobbyprojekt und aus privatem Interesse und zum privaten Nutzen erstellt worden. Er verwendet eine öffentliche Schnittstelle. Benutzt den Bot daher gewissenhaft und in vernünftigen Intervallen.

## Verwendet python
- python3
- package python-telegram-bot

## Setup & Ausführen
- Die Konfigurationsdatei `constants.edit.py` zu `constants.py` umbennen
- Erforderliche Parameter (wie z.B. die Telegram-Token oder Chat-IDs) anpassen
- ggf. optionale Parameter anpassen
- Starten mit `python3 impfbot.py`

