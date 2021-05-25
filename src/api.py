import json
import requests
import time
from datetime import datetime

from logger import logger
import constants


#Request function with output handling
def fetch_appointment_status(plz, retry_count=5):
    recaptcha_counter = 0
    logger.info("Impftermine werden abgefragt...")

    param_birthdate =  int(datetime.strptime(constants.birthdate, "%d.%m.%Y").timestamp()*1000)
    url = f'https://www.impfportal-niedersachsen.de/portal/rest/appointments/findVaccinationCenterListFree/{plz}?stiko=&count=1&birthdate={param_birthdate}'

    try:
        while recaptcha_counter < retry_count:
            response = requests.get(
                url,
                headers={
                    'Accept': 'application/json',
                    'User-Agent': 'impftermin-anfrage'
                },
                timeout=15
            )
            
            if response.status_code != 200:
                return {
                    'error' : "http", 
                    'msg': "Die Impfterminanfrage war nicht erfolgreich: " + str(response.status_code),
                    'vc_list': []
                }

            if "recaptcha" in response.content.decode('utf-8'):
                recaptcha_counter += 1
                logger.info("Der Server erfordert ein Captcha. (Versuch " + str(recaptcha_counter) + " von " + str(retry_count) + ")")
                time.sleep(recaptcha_counter)
                continue

            return {
                'vc_list': response.json()['resultList'],
                'error': None,
                'msg': None
            }
          
    except Exception as e:  #Unknown error
        return {
            'error' : "unknown", 
            'msg': "Fehler beim Anfragen oder Verarbeiten der Impfterminanfrage.\nFehler: " + str(e),
            'vc_list': []
        }
    
    #Only reached when retry limit exceeded
    return {
            'error' : "ipban", 
            'msg': "Scheinbar liegt ein IP-Ban vor. Setzte die nächsten Anfragen aus...",
            'vc_list': []
    }