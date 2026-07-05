import os
import time

from strategy import generate_signal
from telegram_bot import send_message

SYMBOLS = [
    "OANDA:EUR_USD",
    "OANDA:GBP_USD",
    "OANDA:USD_JPY",
    "OANDA:AUD_USD",
]


def analyze_market():

    best_signal = None

    for symbol in SYMBOLS:

        signal = generate_signal(symbol)

        if signal is None:
            continue

        if best_signal is None:
            best_signal = signal
            continue

        if signal["confidence"] > best_signal["confidence"]:
            best_signal = signal

    if best_signal is None:
        print("No Signal")
        return

    message = f"""
🚀 Abod Signals

{best_signal["direction"]}

📈 الزوج:
{best_signal["symbol"]}

🎯 الثقة:
{best_signal["confidence"]}%

💰 سعر الدخول:
{best_signal["entry"]}

⏳ مدة الصفقة:
{best_signal["expiry"]}

📋 الأسباب:
"""

    for reason in best_signal["reasons"]:
        message += f"\n✅ {reason}"

    send_message(message)

    print("Signal Sent")


def main():

    print("Abod Signals Started")

    while True:

        try:

            analyze_market()

        except Exception as e:

            print(e)

        time.sleep(60)


if __name__ == "__main__":
    main()
