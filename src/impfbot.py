import json
import requests
import random
import time
from datetime import datetime, timedelta

from timeutil import get_request_interval_time
from api import fetch_appointment_status
from services import send_to_telegram

from logger import logger
import constants


def process_message(msg, is_important=False) -> None:
    logger.info(msg)

    #Servies
    send_to_telegram(msg, is_important)

def has_vaccine_in_stock(vc_list) -> bool:
    for vc in vc_list:
        logger.info(vc['name']  + ": outOfStock: " + str(vc['outOfStock']) + ", freeSlotSizeOnline: " + (str(vc['freeSlotSizeOnline']) if 'freeSlotSizeOnline' in vc else "0"))
        if not vc['outOfStock']:
            return True
    return False


def message_vaccince_in_stock(vc_list) -> None:
    try:
        for vc in vc_list:
            if not vc['outOfStock']:
                process_message(
                    "Impftermine verfügbar!\n" +
                    "Impfzentrum: " + vc['name'] + "\n" + 
                    "Impfstoff: "   + vc['vaccineName'] + "\n" +
                    "Freie Termine: " + str(vc['freeSlotSizeOnline']) + "\n"
                    "Website: https://www.impfportal-niedersachsen.de/portal/#/appointment/public", 
                    True
                )
    except Exception as e:
        logger.error(e)
        process_message("Impftermine verfügbar!\n" + "Daten: " + json.dumps(vc_list), True)


def request_vaccination_center_appointments(plz, retry_count=5) -> None:
    try:
        result = fetch_appointment_status(plz, retry_count)
     
        if result['error']:
            process_message(result['msg'], True)
            if result['error'] == 'ipban':
                time.sleep(constants.request_interval_ipban)
        else:
            vc_list = result['vc_list']

            if has_vaccine_in_stock(vc_list):
                message_vaccince_in_stock(vc_list)
            else:
                process_message("Keine Impftermine verfügbar.")
            return
    except Exception as e:  #Unknown error
        process_message("Fehler beim Anfragen oder Verarbeiten der Impfterminanfrage.\nFehler: " + str(e), True)
        return


def main():
    while True:
        request_vaccination_center_appointments(plz=constants.plz, retry_count=constants.retry_count)

        sleep_time = get_request_interval_time(default_interval=constants.request_interval, nightly_interval=constants.request_interval_overnight)
        logger.info("Erneute Anfrage in " + str(int(sleep_time/60)) + " Minuten.\n")

        time.sleep(sleep_time)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        pass
