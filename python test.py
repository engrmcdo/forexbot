import requests

BOT_TOKEN = "9175367263:AAE73X5AC5F853kO2TKvPFqfyF8PfoPj2lk"
CHANNEL_ID = "-1299956817"

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHANNEL_ID,
        "text": "✅ Mcdo AI Forex Bot Test Message"
    }
)
