import os
import time
import requests
import pandas as pd

API_KEY = os.getenv("FINNHUB_API_KEY")


def get_candles(symbol, resolution="1", limit=200):

    now = int(time.time())

    if resolution == "1":
        seconds = 60
    elif resolution == "5":
        seconds = 300
    elif resolution == "15":
        seconds = 900
    else:
        seconds = 60

    start = now - (limit * seconds)

    url = "https://finnhub.io/api/v1/forex/candle"

    params = {
        "symbol": symbol,
        "resolution": resolution,
        "from": start,
        "to": now,
        "token": API_KEY
    }

    response = requests.get(url, params=params, timeout=15)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("s") != "ok":
        return None

    df = pd.DataFrame({
        "time": data["t"],
        "open": data["o"],
        "high": data["h"],
        "low": data["l"],
        "close": data["c"],
        "volume": data["v"]
    })

    return df
