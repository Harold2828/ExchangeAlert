# email_notifier.py

import smtplib
from email.message import EmailMessage
import logging
from config import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_SENDER,
    EMAIL_PASSWORD,
    EMAIL_RECIPIENT,
)

class EmailNotifier:
    def __init__(self):
        self.smtp_server = EMAIL_HOST
        self.port = EMAIL_PORT
        self.sender = EMAIL_SENDER
        self.password = EMAIL_PASSWORD
        self.recipient = EMAIL_RECIPIENT

    def send_email(self, subject, body, html=False):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self.sender
            msg["To"] = self.recipient

            if html:
                msg.add_alternative(body, subtype='html')
            else:
                msg.set_content(body)

            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                server.login(self.sender, self.password)
                server.send_message(msg)

            logging.info("[EmailNotifier] Email sent.")
        except Exception as e:
            logging.error(f"[EmailNotifier] Failed to send email: {e}")
