from market import get_price


def generate_signal(symbol):

    data = get_price(symbol)

    if data is None:
        return None

    price = data["price"]
    open_price = data["open"]
    previous_close = data["previous_close"]

    score = 0
    reasons = []

    # اتجاه السعر مقارنة بالافتتاح
    if price > open_price:
        direction = "🟢 CALL"
        score += 30
        reasons.append("Bullish Momentum")
    else:
        direction = "🔴 PUT"
        score += 30
        reasons.append("Bearish Momentum")

    # استمرار الحركة مقارنة بإغلاق اليوم السابق
    if direction == "🟢 CALL":
        if price > previous_close:
            score += 20
            reasons.append("Above Previous Close")

    if direction == "🔴 PUT":
        if price < previous_close:
            score += 20
            reasons.append("Below Previous Close")

    # قوة الحركة
    movement = abs(price - open_price)

    if movement >= 0.00020:
        score += 20
        reasons.append("Strong Move")

    # الابتعاد عن أعلى وأدنى السعر
    if direction == "🟢 CALL":
        if (data["high"] - price) > 0.00010:
            score += 15
            reasons.append("Space To Resistance")

    if direction == "🔴 PUT":
        if (price - data["low"]) > 0.00010:
            score += 15
            reasons.append("Space To Support")

    confidence = min(score, 100)

    if confidence < 70:
        return None

    return {
        "symbol": symbol,
        "direction": direction,
        "confidence": confidence,
        "entry": round(price, 5),
        "expiry": "1 Minute",
        "reasons": reasons
    }
