from config import telegram_token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"Command fetched, by: {update.effective_user.first_name}")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token(telegram_token).build()

app.add_handler(CommandHandler("Hello", hello))

print("Bot Up and listening")
app.run_polling()