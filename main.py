import os
from dotenv import load_dotenv
import speech_recognition as sr
import cohere
from gtts import gTTS


load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise RuntimeError("Set COHERE_API_KEY in .env")

AUDIO_PATH = "Recording.wav"             
TRANSCRIPT_LANG = "en-US"   
TTS_LANG = "en"              

#   audio -> text 
r = sr.Recognizer()
with sr.AudioFile(AUDIO_PATH) as src:
    audio = r.record(src)

try:
    transcript = r.recognize_google(audio, language=TRANSCRIPT_LANG)
except sr.UnknownValueError:
    transcript = ""
except sr.RequestError as e:
    raise RuntimeError(f"Speech API error: {e}")

print(f"[User transcript]: {transcript}")

#   text -> LLM response (Cohere) 
co = cohere.Client(COHERE_API_KEY)

# keep it super-stable by using the classic generate endpoint
prompt = (
    "You are a helpful assistant. Reply concisely.\n\n"
    f"User said: \"{transcript}\"\n"
    "Assistant:"
)
resp = co.generate(model="command", prompt=prompt, max_tokens=150, temperature=0.5)
reply = resp.generations[0].text.strip()
print(f"[LLM reply]: {reply}")

#  text -> audio  
tts = gTTS(reply, lang=TTS_LANG)
tts.save("response.mp3")
print("Saved speech to response.mp3")
