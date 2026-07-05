from market import get_price


def generate_signal(symbol):

    data = get_price(symbol)

    if data is None:
        return None

    price = data["price"]
    open_price = data["open"]
    high = data["high"]
    low = data["low"]

    score = 0
    reasons = []

    # اتجاه الحركة
    if price > open_price:
        score += 30
        reasons.append("Bullish Momentum")
        direction = "🟢 CALL"
    else:
        score += 30
        reasons.append("Bearish Momentum")
        direction = "🔴 PUT"

    # قوة الحركة
    movement = abs(price - open_price)

    if movement > 0.00030:
        score += 25
        reasons.append("Strong Candle")

    # قرب السعر من أعلى أو أقل اليوم
    if direction == "🟢 CALL":
        if price < high:
            score += 20
            reasons.append("Room To Move Up")

    if direction == "🔴 PUT":
        if price > low:
            score += 20
            reasons.append("Room To Move Down")

    # تقييم الثقة
    confidence = min(score, 100)

    if confidence < 60:
        return None

    return {
        "symbol": symbol,
        "direction": direction,
        "confidence": confidence,
        "entry": price,
        "expiry": "1 Minute",
        "reasons": reasons
    }
