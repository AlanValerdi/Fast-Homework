import logging
from config import telegram_token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Initialize logger
logger = logging.getLogger(__name__)

# Application build 
app = ApplicationBuilder().token(telegram_token).build()

# Log Methods 
def Log_User_Call(update: Update):
    logger.info(f"Command called correctly by: {update.effective_user.first_name}")

# Unknown handler 
async def Unknown_Command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Log_User_Call(update)
    await update.message.reply_text("The command you inserted, is not valid")

# Handlers 
# Text based handlers 
async def Get_Message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Log_User_Call(update)
    user_Message = update.message.text

    await update.message.reply_text(f"Did you perhaps said: {user_Message}")
    

# Command based handlers 