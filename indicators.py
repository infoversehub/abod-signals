def ema(values, period):

    if len(values) < period:
        return None

    multiplier = 2 / (period + 1)

    ema_value = sum(values[:period]) / period

    for price in values[period:]:
        ema_value = (price - ema_value) * multiplier + ema_value

    return round(ema_value, 5)


def sma(values, period):

    if len(values) < period:
        return None

    return round(sum(values[-period:]) / period, 5)


def price_change(open_price, close_price):

    if open_price == 0:
        return 0

    return round(((close_price - open_price) / open_price) * 100, 2)
