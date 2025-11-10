import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno desde .env

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Modelos OpenAI para distintos usos
MODEL_TEXT = "gpt-4o-mini"        # Modelo para texto/chat
MODEL_IMAGE = "dall-e-3"          # Modelo para generación de imágenes
MODEL_AUDIO = "whisper-1"         # Modelo para procesamiento de audio

def check_api_key():
    if OPENAI_API_KEY:
        print(f"OpenAI API Key exists and begins with: {OPENAI_API_KEY[:8]}")
    else:
        print("⚠️ OpenAI Key not configured")

SYSTEM_MESSAGE = (
    "Eres un asistente útil para una aerolínea llamada FlightAI. "
    "Da respuestas breves y corteses, de no más de una oración. "
    "Se siempre preciso. Si no sabes la respuesta, dilo."
)


TICKET_PRICES = {"londres": "$799", "parís": "$899", "tokyo": "$1400", "berlín": "$499"}