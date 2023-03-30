from pdfminer.high_level import extract_text
import pyttsx3
import re
from text_extractor import format_text
from text_speech_convert import TextToSpeech

text = extract_text("./Book_input/depression.pdf")

cleaned_text = format_text(text=text)

tts = TextToSpeech(voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0", 
                   rate = 200, volume = 1.0)
# tts.list_available_voices()
tts.text_to_speech(cleaned_text, save=True, file_name="test.mp3")

