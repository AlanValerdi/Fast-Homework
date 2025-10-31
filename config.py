import os
from dotenv import load_dotenv

load_dotenv()

# Setting up variables
gemini_api_key = os.getenv('GEMINI_API_KEY')
telegram_token = os.getenv('TELEGRAM_TOKEN')

# Handling missing variables
if not gemini_api_key:
    raise ValueError("Error: missing env var -> GEMINI_API_KEY")
if not telegram_token:
    raise ValueError("Error: missing env var -> TELEGRAM_TOKEN")