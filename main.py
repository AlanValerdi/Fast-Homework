import logging
import asyncio
from config import telegram_token
from bot.core import create_app
from telegram import Bot


# Creating loggin for server events 
logging.basicConfig(
    level= logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def Cleanup_Telegram():
    # Clearing webhooks or polling sessions
    bot = Bot(token=telegram_token)
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Webhook cleared")

def main():
    # Initial Setup
    logger.info("Bot is initializing")
    asyncio.run(Cleanup_Telegram())

    app = create_app(telegram_token)
    
    logger.info("Bot is listening")
    app.run_polling()

if __name__ == "__main__":
    main()