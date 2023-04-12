from modules.text_speech_convert import TextToSpeech
import pyttsx3

steris = TextToSpeech(rate=200, volume=1.0)

body = "knock knock who's there? I am a lazy dog looking to settle in a lazy house"

steris.dictation(body=body)
steris.list_available_voices()

# engine = pyttsx3.init()
# voices = engine.getProperty("voices")
# default_voice = voices[0].id
# print(type(default_voice))
