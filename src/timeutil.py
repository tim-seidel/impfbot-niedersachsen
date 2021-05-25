from datetime import datetime, timedelta
import random

import constants

def get_time_id_stamp(id) -> str:
    return "[" + id + " | " + datetime.now().strftime(
        "%H:%M:%S") + "]"


def get_current_time_string() -> str:
    return "(" + datetime.now().strftime("%H:%M:%S") + ")"

#Returns a reduced update rate if the time is between 19:00 and 07:00, otherwise the normal rate is taken
def get_request_interval_time(default_interval, nightly_interval, jitter=15) -> int:
    current_hour = datetime.now().hour
    next_overnight_hour = (datetime.now() + timedelta(minutes=60)).hour

    #Because this is just a hobby project, the paramters are not realy tested. If you edit the paramters in the constants.py file, be clever :)
    if current_hour >= constants.night_start or (current_hour < (constants.night_end - 1) and next_overnight_hour < constants.night_end):
        return int(nightly_interval + random.random()*jitter)
    else:
        return int(default_interval + random.random()*jitter)
