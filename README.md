> [!IMPORTANT]
> Given the scope of this small project, the free version of ExchangeRate-API is currently being used

# 📊 Exchange Alert Automation

A Python-based automation tool that checks the daily **USD to COP exchange rate** (or any pair you configure) and **sends an email alert** if the rate exceeds a specified threshold. Ideal for freelancers, travelers, or anyone monitoring currency fluctuations.

---

## 🚀 Features

- 📈 Fetches real-time exchange rate from [ExchangeRate-API](https://www.exchangerate-api.com/)
- 📨 Sends email notifications via SMTP when threshold is exceeded
- 🕒 Scheduled to run **once per day**
- 📁 Modular OOP architecture for maintainability
- 🔐 Environment variable support via `.env`
- 🪵 Logging to file for auditing

---

## 📦 Requirements

- Python 3.8+
- `pip install -r requirements.txt`

```
requests
schedule
python-dotenv
```

---

## ⚙️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/exchange-alert.git
cd exchange-alert
```

### 2. Create a `.env` File

Create a `.env` file in the root directory:

```ini
# Exchange Alert Configuration
EXCHANGERATE_API_KEY=your_api_key_here
EXCHANGERATE_BASE_CURRENCY=USD
EXCHANGERATE_TARGET_CURRENCY=COP
THRESHOLD=4200

# SMTP Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_SENDER=you@example.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECIPIENT=recipient@example.com

# Runtime Configuration
RUN_TIME=09:00
```

> 🔐 **Use app passwords** for Gmail (explained below), and never share this file publicly.

---

### 3. Gmail App Password Setup (Required for SMTP)

If you're using a Gmail account, you **must use an App Password** instead of your regular password if you have 2FA enabled.

#### ✅ Steps to Get a Gmail App Password

1. Go to your account: https://myaccount.google.com/
2. Navigate to **Security** > Ensure **2-Step Verification** is turned ON.
3. Go to: https://myaccount.google.com/apppasswords
4. Generate a new App Password:
   - App: **Mail**
   - Device: **Other (Exchange Alert)**
5. Copy the 16-character password Google gives you.
6. Paste it into your `.env` as `EMAIL_PASSWORD`.

> **Important**: Do **not** use your normal password — it will fail with a `534` error.

---

### 4. Run the App

```bash
python main.py
```

- ✅ Immediately checks the current exchange rate
- ✅ If threshold is exceeded, sends an email alert
- 🕒 Then waits and runs daily at the specified `RUN_TIME`

---

## 📁 Project Structure

```
exchange_alert/
├── config.py
├── exchange_rate_service.py
├── email_notifier.py
├── exchange_monitor.py
├── scheduler.py
├── main.py
├── .env
├── exchange_alert.log
```

---

## 🛠️ Customization

| Option                     | Description                            |
|---------------------------|----------------------------------------|
| `THRESHOLD`               | Set the target exchange rate to alert |
| `RUN_TIME`                | Time to run the script daily (e.g. `09:00`) |
| `BASE_CURRENCY` & `TARGET_CURRENCY` | Customize currency pair |
| `EMAIL_*`                 | Use your email + SMTP settings         |

---

## 🧪 Testing Tips

To force a notification during testing:

- Temporarily set `THRESHOLD=1` in `.env`
- Run: `python main.py`

---

## 🔒 Security

- Use `.gitignore` to exclude `.env` and `*.log` from version control
- Use app passwords or a transactional email service (SendGrid, Mailgun) in production