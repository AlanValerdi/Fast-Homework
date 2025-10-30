from config import telegram_token
from handlers import app


print("Bot Up and listening")
app.run_polling()