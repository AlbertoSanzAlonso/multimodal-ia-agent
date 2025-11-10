import openai
from app.agent import chat, artist, talker
from app.config import MODEL_TEXT, MODEL_IMAGE, MODEL_AUDIO, OPENAI_API_KEY, SYSTEM_MESSAGE
from app.utils import get_ticket_price

# def chat_handler(message, history):
#     messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history + [{"role": "user", "content": message}]
#     response = openai.chat.completions.create(model=MODEL_TEXT, messages=messages)


#     return response.choices[0].message.content



def initialize_agents():
    return {
        "chat": chat,
        "artist": artist,
        "talker": talker
    }

def handle_message(history=[]):
    response_text = chat(history)
    return response_text

def handle_image(city):
    return artist(city)

def handle_audio(text):
    return talker(text)