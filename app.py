from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_telegram(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )


@app.route("/")
def home():
    return "Mcdo AI Forex Bot Running"


@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    pair = data.get("pair")
    signal = data.get("signal")
    confidence = data.get("confidence")

    msg = f"""
📊 Mcdo AI Forex Signal

Pair: {pair}

Signal: {signal}

Confidence: {confidence}%

#forex
"""

    send_telegram(msg)

    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
