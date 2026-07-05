import pandas as pd
import ta


def add_indicators(df):

    df["EMA20"] = ta.trend.ema_indicator(df["close"], window=20)

    df["EMA50"] = ta.trend.ema_indicator(df["close"], window=50)

    df["EMA200"] = ta.trend.ema_indicator(df["close"], window=200)

    df["RSI"] = ta.momentum.rsi(df["close"], window=14)

    df["MACD"] = ta.trend.macd(df["close"])

    df["MACD_SIGNAL"] = ta.trend.macd_signal(df["close"])

    df["ATR"] = ta.volatility.average_true_range(
        df["high"],
        df["low"],
        df["close"],
        window=14
    )

    return df
