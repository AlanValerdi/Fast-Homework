import logging
from config import telegram_token
from bot.core import create_app

# Creating loggin for server events 
logging.basicConfig(
    level= logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Bot is initializing")

    app = create_app(telegram_token)
    
    logger.info("Bot is listening")
    app.run_polling()

if __name__ == "__main__":
    main()