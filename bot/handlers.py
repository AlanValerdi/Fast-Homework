from config import telegram_token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Application build 
app = ApplicationBuilder().token(telegram_token).build()

# Log Methods 
def fetchCalls(update: Update):
    print(f"Command called correctly by: {update.effective_user.first_name}")

# Handlers 

