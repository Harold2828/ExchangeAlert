import os
from dotenv import load_dotenv

load_dotenv()

# --- Exchange Rate API Configurations ---
# These variables are related to fetching exchange rates.
EXCHANGE_API_KEY = os.getenv("EXCHANGERATE_API_KEY") 
EXCHANGERATE_BASE_CURRENCY = os.getenv("EXCHANGERATE_BASE_CURRENCY")
EXCHANGERATE_TARGET_CURRENCY = os.getenv("EXCHANGERATE_TARGET_CURRENCY")

# Construct the full API URL after loading its components
# The f-string ensures the API key and base currency are integrated correctly.
EXCHANGE_API_URL = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/{EXCHANGERATE_BASE_CURRENCY}"

# --- Email (SMTP) Configurations ---
# These variables are for sending emails via an SMTP server.
SMTP_SERVER = os.getenv("SMTP_SERVER") 
SMTP_PORT = os.getenv("SMTP_PORT") 
EMAIL_SENDER = os.getenv("EMAIL_SENDER") 
EMAIL_HOST = os.getenv("EMAIL_HOST") 
EMAIL_PORT= os.getenv("EMAIL_PORT")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD") 
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT") 

# --- Application Specific Constants ---
# This variable appears to be a general application threshold.
THRESHOLD = float(os.getenv("THRESHOLD"))

# --- Scheduler Configuration ---
# This variable defines the time at which the daily job should run.
RUN_TIME = os.getenv("RUN_TIME", "09:00")  # Default to
