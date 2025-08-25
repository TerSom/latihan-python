import os
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! 👋 Aku bot buatan Terry. Kirim pesan apa saja, aku akan meng-echo balik."
    )

# /help command
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start untuk mulai, ketik apa saja untuk di-echo.")

# handler pesan biasa
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"SYBAU")

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN belum di-set di .env")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Bot jalan... (Ctrl+C untuk stop)")
    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
