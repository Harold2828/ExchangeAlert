import logging
from exchange_rate_service import ExchangeRateService
from email_notifier import EmailNotifier
from config import THRESHOLD, EXCHANGERATE_TARGET_CURRENCY, EXCHANGERATE_BASE_CURRENCY

class ExchangeMonitor:
    def __init__(self):
        self.rate_service = ExchangeRateService()
        self.notifier = EmailNotifier()

    def check_rate_and_notify(self):
        logging.info("[ExchangeMonitor] Checking exchange rate...")
        rate = self.rate_service.get_base_to_target_currency()
        if rate:

            logging.info(f"[ExchangeMonitor] Current {EXCHANGERATE_BASE_CURRENCY}/{EXCHANGERATE_TARGET_CURRENCY} rate: {rate}")
            if rate > THRESHOLD:
                subject = f"🚨 {EXCHANGERATE_BASE_CURRENCY}/{EXCHANGERATE_TARGET_CURRENCY} Alert"
                body = (
                    f"The current exchange rate is {rate:.2f} {EXCHANGERATE_TARGET_CURRENCY}, "
                    f"which exceeds your threshold of {THRESHOLD} {EXCHANGERATE_TARGET_CURRENCY}."
                )
                self.notifier.send_email(subject, body)
