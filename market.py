import os
import requests

API_KEY = os.getenv("FINNHUB_API_KEY")


def get_price(symbol):

    url = (
        f"https://finnhub.io/api/v1/quote"
        f"?symbol={symbol}"
        f"&token={API_KEY}"
    )

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return None

    data = response.json()

    if "c" not in data:
        return None

    return {
        "symbol": symbol,
        "price": data["c"],
        "high": data["h"],
        "low": data["l"],
        "open": data["o"],
        "previous_close": data["pc"],
    }
