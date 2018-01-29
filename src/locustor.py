'locustor.py'

import sys
from datetime import datetime, timedelta
import time
import schedule
from locustic_config import LocusticConfig
from log_repository import LogRepository
from log_helper import LogHelper

class Locustic:
    'Start point'

    def __init__(self):
        self.end_date = datetime.now() + timedelta(minutes=int(sys.argv[1]))

    def job(self):
        'Locustic is a simple scheduled worker which sends Locust logs to Elastic.'

        print(datetime.now())
        log_output = LogHelper().parse_log_to_json(LocusticConfig.LOCUST_CSV_LOG_FILE_PATH)
        LogRepository().add_log(log_output)

    def is_runnable(self):
        'Function is runnable'
        if self.end_date < datetime.now():
            return False
        return True

LOCUSTIC = Locustic()

schedule.every(LocusticConfig.DELAY_IN_SEC).seconds.do(LOCUSTIC.job)

while LOCUSTIC.is_runnable():
    schedule.run_pending()
    time.sleep(1)
