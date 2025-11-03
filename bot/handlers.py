import logging
from telegram import Update
from telegram.ext import ContextTypes
from services import Process_Prompt, generate_report

# Initialize logger
logger = logging.getLogger(__name__)

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
    message_Id = update.message.message_id
    
    try:
        # Generate Response
        fileName = f"Tarea_{update.effective_user.name}.docx"
        response = await Process_Prompt(user_Message)
        await update.message.reply_text(f"Info proccessed correctly, wait until the file is made")
        logger.info(f"Response: {response}")


        # Generate File
        report_Path = generate_report(
            data= response,
            output_File_Name= fileName
        )

        # Send File
        try:
            with open(report_Path, 'rb') as document_file:
                await context.bot.send_document(
                    chat_id=update.effective_chat.id,
                    document=document_file,
                    caption="Here is your document",
                    reply_to_message_id=message_Id,
                )
                await update.message.reply_text("Document sent successfully")
        except FileNotFoundError as e:
            await update.message.reply_text(f"Document were not send, something went wrong {e}")
        except Exception as e:
            logger.error(f"document were not created {e}")

        logger.info(f"Handler called correctly result: {response}")
    except Exception as e:
        logger.error(f"Error in handler {e}")
        raise
    
    
# Command based handlers 