import schedule
import time
import logging
from exchange_monitor import ExchangeMonitor
from config import RUN_TIME

class DailyScheduler:
    def __init__(self, monitor: ExchangeMonitor, run_time=RUN_TIME):
        self.monitor = monitor
        self.run_time = run_time

    def start(self):
        logging.info(f"[Scheduler] Job scheduled daily at {self.run_time}")
        schedule.every().day.at(self.run_time).do(self.monitor.check_rate_and_notify)

        self.monitor.check_rate_and_notify()

        while True:
            schedule.run_pending()
            time.sleep(60)
