import logging
from exchange_monitor import ExchangeMonitor
from scheduler import DailyScheduler
from config import RUN_TIME

logging.basicConfig(
    filename="exchange_alert.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

if __name__ == "__main__":
    monitor = ExchangeMonitor()
    scheduler = DailyScheduler(monitor, run_time=RUN_TIME)
    scheduler.start()
