import base64
from io import BytesIO
from PIL import Image
from pydub import AudioSegment
from pydub.playback import play
import openai
from app.utils import tools
from app.config import MODEL_TEXT, MODEL_IMAGE, MODEL_AUDIO, OPENAI_API_KEY, SYSTEM_MESSAGE
from app.tools import handle_tool_call  # Asegúrate de que esté definido ahí

def initialize_agents():
    openai.api_key = OPENAI_API_KEY
    return {
        "chat": chat,
        "artist": artist,
        "talker": talker
    }


def artist(city):
    image_response = openai.images.generate(
            model="dall-e-3",
            prompt=f"Una imagen que representa unas vacaciones en {city}, mostrando lugares turísticos y todo lo único de {city}, en un vibrante estilo pop-art",
            size="1024x1024",
            n=1,
            response_format="b64_json",
        )
    image_base64 = image_response.data[0].b64_json
    image_data = base64.b64decode(image_base64)
    return Image.open(BytesIO(image_data))

def talker(message):
    if not message:
        print("Mensaje vacío, no se genera audio")
        return
    response = openai.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input=message
    )
    audio_stream = BytesIO(response.content)
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)

def chat(history):
    messages = [{"role": "system", "content": SYSTEM_MESSAGE}] + history
    response = openai.chat.completions.create(model=MODEL_TEXT, messages=messages, functions=tools,
    function_call="auto")
    image = None

    if response.choices[0].finish_reason=="tool_calls":
        message = response.choices[0].message
        response, city = handle_tool_call(message)
        messages.append(message)
        messages.append(response)
        image = artist(city)
        response = openai.chat.completions.create(model=MODEL_TEXT, messages=messages)
    
    reply = response.choices[0].message.content
    history += [{"role": "assistant", "content": reply}]

    talker(reply)

    return history, image
