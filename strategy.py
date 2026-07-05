from market import get_candles
from indicators import add_indicators


def generate_signal(symbol):

    df = get_candles(symbol)

    if df is None or len(df) < 200:
        return None

    df = add_indicators(df)

    last = df.iloc[-1]

    score = 0
    reasons = []
    direction = None

    # =========================
    # Trend (EMA)
    # =========================

    if last["EMA20"] > last["EMA50"] > last["EMA200"]:
        direction = "🟢 CALL"
        score += 20
        reasons.append("Strong Up Trend")

    elif last["EMA20"] < last["EMA50"] < last["EMA200"]:
        direction = "🔴 PUT"
        score += 20
        reasons.append("Strong Down Trend")

    else:
        return None

    # =========================
    # RSI
    # =========================

    if direction == "🟢 CALL":
        if 40 <= last["RSI"] <= 65:
            score += 15
            reasons.append("Healthy RSI")

    if direction == "🔴 PUT":
        if 35 <= last["RSI"] <= 60:
            score += 15
            reasons.append("Healthy RSI")

    # =========================
    # MACD
    # =========================

    if direction == "🟢 CALL":
        if last["MACD"] > last["MACD_SIGNAL"]:
            score += 20
            reasons.append("MACD Bullish")

    if direction == "🔴 PUT":
        if last["MACD"] < last["MACD_SIGNAL"]:
            score += 20
            reasons.append("MACD Bearish")

    # =========================
    # ATR
    # =========================

    if last["ATR"] > 0:
        score += 10
        reasons.append("Market Moving")

    # =========================
    # ADX
    # =========================

    if last["ADX"] >= 25:
        score += 15
        reasons.append("Strong Trend")

    # =========================
    # Bollinger Bands
    # =========================

    if direction == "🟢 CALL":
        if last["close"] > last["BB_MIDDLE"]:
            score += 10
            reasons.append("Above BB Middle")

    if direction == "🔴 PUT":
        if last["close"] < last["BB_MIDDLE"]:
            score += 10
            reasons.append("Below BB Middle")

    # =========================
    # Candle Strength
    # =========================

    candle = abs(last["close"] - last["open"])

    if candle > (last["ATR"] * 0.5):
        score += 10
        reasons.append("Strong Candle")

    confidence = min(score, 100)

    if confidence < 85:
        return None

    return {
        "symbol": symbol,
        "direction": direction,
        "confidence": confidence,
        "entry": round(last["close"], 5),
        "expiry": "1 Minute",
        "reasons": reasons
    }
