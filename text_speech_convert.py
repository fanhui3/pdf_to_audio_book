import pyttsx3

voice = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
         "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"]


class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice: 
            self.engine.setProperty("voice", voice)
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volumne", volume)
    
    def list_available_voices(self):
        voices: list = [self.engine.getProperty("voices")]
        
        for i, voice in enumerate(voices[0]):
            print(f"{i+1} {voice.name} {voice.age}: {voice.languages} [{voice.id}] ")
    
    def text_to_speech(self, text:str, save:bool =False, file_name = "output.mp3"):
        # self.engine.say(text)
        print("i am saving mp3...")

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()


if __name__ == "__main__":
    tts = TextToSpeech(voice = voice[0], rate = 200, volume = 1.0)
    tts.list_available_voices()
    # tts.text_to_speech("hello world", save=True)