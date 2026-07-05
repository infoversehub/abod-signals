import ta


def add_indicators(df):

    # EMA
    df["EMA20"] = ta.trend.ema_indicator(
        close=df["close"],
        window=20
    )

    df["EMA50"] = ta.trend.ema_indicator(
        close=df["close"],
        window=50
    )

    df["EMA200"] = ta.trend.ema_indicator(
        close=df["close"],
        window=200
    )

    # RSI
    df["RSI"] = ta.momentum.rsi(
        close=df["close"],
        window=14
    )

    # MACD
    df["MACD"] = ta.trend.macd(
        close=df["close"]
    )

    df["MACD_SIGNAL"] = ta.trend.macd_signal(
        close=df["close"]
    )

    df["MACD_HIST"] = ta.trend.macd_diff(
        close=df["close"]
    )

    # ATR
    df["ATR"] = ta.volatility.average_true_range(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )

    # Bollinger Bands
    df["BB_UPPER"] = ta.volatility.bollinger_hband(
        close=df["close"]
    )

    df["BB_MIDDLE"] = ta.volatility.bollinger_mavg(
        close=df["close"]
    )

    df["BB_LOWER"] = ta.volatility.bollinger_lband(
        close=df["close"]
    )

    # ADX
    df["ADX"] = ta.trend.adx(
        high=df["high"],
        low=df["low"],
        close=df["close"],
        window=14
    )

    return df
