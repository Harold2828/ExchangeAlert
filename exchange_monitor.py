import logging
from datetime import datetime
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

                html_body = f"""
                <html>
                    <head>
                        <style>
                            body {{
                                font-family: Arial, sans-serif;
                                background-color: #f8f9fa;
                                color: #212529;
                                padding: 20px;
                            }}
                            .card {{
                                background-color: #ffffff;
                                border: 1px solid #dee2e6;
                                border-radius: 8px;
                                padding: 20px;
                                max-width: 500px;
                                margin: 0 auto;
                                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                            }}
                            .title {{
                                font-size: 1.25em;
                                font-weight: bold;
                                color: #dc3545;
                                margin-bottom: 10px;
                            }}
                            .rate {{
                                font-size: 1.1em;
                                color: #007bff;
                            }}
                            .footer {{
                                margin-top: 20px;
                                font-size: 0.9em;
                                color: #6c757d;
                            }}
                        </style>
                    </head>
                    <body>
                        <div class="card">
                            <div class="title">🚨 Exchange Rate Alert</div>
                            <p>
                                The current exchange rate is
                                <span class="rate">{rate:.2f} {EXCHANGERATE_TARGET_CURRENCY}</span>,
                                which exceeds your threshold of
                                <strong>{THRESHOLD} {EXCHANGERATE_TARGET_CURRENCY}</strong>.
                            </p>
                            <div class="footer">
                                Currency Pair: {EXCHANGERATE_BASE_CURRENCY}/{EXCHANGERATE_TARGET_CURRENCY}
                                <br>
                                Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                            </div>
                        </div>
                    </body>
                </html>
                """

                self.notifier.send_email(subject, html_body, html=True)


