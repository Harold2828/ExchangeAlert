import requests
import logging
from config import EXCHANGE_API_URL, EXCHANGERATE_TARGET_CURRENCY

class ExchangeRateService:
    def __init__(self, api_url=EXCHANGE_API_URL):
        self.api_url = api_url

    def get_base_to_target_currency(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            data = response.json()
            return data["conversion_rates"][EXCHANGERATE_TARGET_CURRENCY]
        except Exception as e:
            logging.error(f"[ExchangeRateService] Error fetching rate: {e}")
            return None
