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

    def send_email(self, subject: str, body: str):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self.sender
            msg["To"] = self.recipient
            msg.set_content(body)

            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.sender, self.password)
            server.send_message(msg)
            server.quit()

            logging.info("[EmailNotifier] Email sent.")
        except Exception as e:
            logging.error(f"[EmailNotifier] Failed to send email: {e}")
