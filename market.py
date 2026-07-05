import os
import requests

API_KEY = os.getenv("FINNHUB_API_KEY")


def get_price(symbol):

    url = "https://finnhub.io/api/v1/quote"

    params = {
        "symbol": symbol,
        "token": API_KEY
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "price": data["c"],
            "high": data["h"],
            "low": data["l"],
            "open": data["o"],
            "previous_close": data["pc"]
        }

    except Exception:
        return None
