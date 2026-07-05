from market import get_price


def generate_signal(symbol):

    data = get_price(symbol)

    if data is None:
        return None

    price = data["price"]
    open_price = data["open"]

    if price > open_price:
        direction = "🟢 BUY"
        confidence = 60
    else:
        direction = "🔴 SELL"
        confidence = 60

    return {
        "direction": direction,
        "confidence": confidence,
        "entry": price,
        "expiry": "1 Minute"
    }
