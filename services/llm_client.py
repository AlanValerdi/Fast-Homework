from config import gemini_api_key
from google import genai

# Create the client 
client = genai.Client(gemini_api_key)

# Specify AI behavior
prompt =  """
You are an expert investigator in both Spanish/English languages.
Either "secciones" or "bibliografia" will have one or more values stored in the keys.
You will get a task of what you must do, once you satisfied the task, you are going to return the following data in JSON format:
{{
    "titulo": "...",
    "secciones": [
        {{ "subtitulo": "...", "informacion": "..."}},
        {{ "subtitulo": "...", "informacion": "..."}}
    ],
    "bibliografia": ["...", "..."]
}}

"""

# GetTask will get the message from the Telegram chat 
def GetTask(message):
    pass