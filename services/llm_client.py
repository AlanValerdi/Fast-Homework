import logging
import asyncio
from config import gemini_api_key
from google import genai

# Instantiate logging
logger = logging.getLogger(__name__)

# Create the client 
client = genai.Client(api_key=gemini_api_key)

# Specify AI behavior
prompt =  """
You are an expert investigator in both Spanish/English languages.
Either "secciones" or "bibliografia" will have one or more (max 5) values stored in the keys.
You will get a task of what you must do, once you satisfied the task, you are going to return the following data in JSON format:
{
    "titulo": "...",
    "secciones": [
        {"subtitulo": "...", "informacion": "..."},
        {"subtitulo": "...", "informacion": "..."}
    ],
    "bibliografia": ["...", "..."]
}
Always return a JSON response. Respond in Spanish by default, unless the user explicitly requests English.
"""

# GetTask will get the message from the Telegram chat 
async def Process_Prompt(message: str):
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: client.models.generate_content(
                model="gemini-2.5-flash",
                contents= [message, prompt],
                config= {
                    "response_mime_type": "application/json",
                    "response_schema": {
                        "type": "object",
                        "properties": {
                            "titulo": {
                                "type": "string",
                                "description": "Analize user prompt and generate the best title for the homework investigation"
                            },
                            "secciones": {
                                "type": "array",
                                "min_items": 2,
                                "max_items": 5,
                                "items": {
                                    "type": "object",
                                    "properties":{
                                        "subtitulo":{
                                            "type": "string",
                                            "description": "Here will be the subtitles of the investigation you made"
                                        },
                                        "informacion":{
                                            "type": "string",
                                            "description": "Here will be the information about the subtitle"
                                        }
                                    }
                                }
                            },
                            "bibliografia": {
                                "type": "array",
                                "min_items": 2,
                                "max_items": 5,
                                "items":{
                                    "type": "string",
                                    "description": "Here will be the bibliography of the research, it will be formatted in `APA 7ma edicion`"
                                }
                            }

                        }
                    }
                }
            )
        )
        return response
    except Exception as e:
        logger.error(f"Api error {e}")
        raise
        
        
        