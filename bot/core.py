from . import handlers
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Build app 
def create_app(token: str) -> Application:

    app_builder = Application.builder().token(token)
    app = app_builder.build()

    # registering Handlers
    # Command
    # app.add_handler(CommandHandler("hello", handlers.printMessage)) 

    # Text based 
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handlers.Get_Message))

    app.add_handler(MessageHandler(filters.COMMAND, handlers.Unknown_Command))

    return app

