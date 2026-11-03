from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("9175367263:AAE73X5AC5F853kO2TKvPFqfyF8PfoPj2lk")
CHAT_ID = os.getenv("1299956817")

def send_telegram(message):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
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

    pair = data.get("pair", "Unknown")
    signal = data.get("signal", "NEUTRAL")

    message = f"""
🚀 MCDO AI FOREX SIGNAL

Pair: {pair}

Signal: {signal}

#Forex
#McdoAI
"""

    send_telegram(message)

    return "OK", 200
