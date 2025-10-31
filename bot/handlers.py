import logging
from config import telegram_token
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from services import Process_Prompt

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
async def Get_User_Prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_Message = update.message.text
    try:
        response = await Process_Prompt(user_Message)
        await update.message.reply_text(f"Info proccessed correctly")
        logger.info(f"Handler called correctly result: {response}")
    except Exception as e:
        logger.error(f"Error in handler {e}")
        raise
    
    
# Command based handlers 