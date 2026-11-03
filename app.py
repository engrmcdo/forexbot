from flask import Flask
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("9175367263:AAE73X5AC5F853kO2TKvPFqfyF8PfoPj2lk")
CHAT_ID = os.getenv("1299956817")

@app.route("/")
def home():
    return "Mcdo AI Forex Bot Running"

@app.route("/test")
def test():

    msg = """
🚀 MCDO AI FOREX BOT

Test message from Render.

Bot is connected successfully.
"""

    r = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        }
    )

    return r.text

if __name__ == "__main__":
    app.run()
