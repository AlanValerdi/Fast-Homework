import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Setting up variables
gemini_api_key = os.getenv('GEMINI_API_KEY')
telegram_token = os.getenv('TELEGRAM_TOKEN')

# Setring Gemini client (provisional)
client = genai.Client(api_key=gemini_api_key, vertexai=False)