import os

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

from market import get_price

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Abod Signals\n\n"
        "الأوامر:\n"
        "/signal"
    )


async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = get_price("OANDA:EUR_USD")

    if data is None:
        await update.message.reply_text("❌ فشل الاتصال بالسوق.")
        return

    await update.message.reply_text(
        f"""
📊 EUR/USD

السعر الحالي: {data['price']}
أعلى سعر: {data['high']}
أقل سعر: {data['low']}
الافتتاح: {data['open']}
إغلاق أمس: {data['previous_close']}
"""
    )


def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))

    print("Abod Signals Running...")

    app.run_polling()


if __name__ == "__main__":
    main()
