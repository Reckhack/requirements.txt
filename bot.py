import ccxt
import schedule
import time
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Telegram bot token
TELEGRAM_TOKEN = '7662683236:AAEFa7MdRierChQgU0i2M7pbBqPQMVCuS4A'

# Command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is online. Type /price BTCUSDT")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = context.args[0] if context.args else 'BTC/USDT'
    exchange = ccxt.binance()
    ticker = exchange.fetch_ticker(symbol)
    await update.message.reply_text(f"{symbol} Price: {ticker['last']}")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))

print("Bot running...")
app.run_polling()
