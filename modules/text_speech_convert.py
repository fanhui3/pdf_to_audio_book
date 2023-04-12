import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
default_voice = voices[0].id


class TextToSpeech:
    engine: pyttsx3.Engine
    global default_voice

    def __init__(self, rate: int, volume: float, voice=default_voice):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty("voice", voice)
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volumne", volume)

    def list_available_voices(self):
        voices: list = [self.engine.getProperty("voices")]

        for i, voice in enumerate(voices[0]):
            print(f"{i+1} {voice.name} {voice.age}: {voice.languages} [{voice.id}] ")

    def text_to_speech(self, text: str, save: bool = False, file_name="output.mp3"):
        # self.engine.say(text)
        print("i am saving mp3...")

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()

    def dictation(self, body: str, name=None):
        self.engine.say(text=body, name=name)
        self.engine.runAndWait()


if __name__ == "__main__":
    tts = TextToSpeech(rate=200, volume=1.0)
    tts.list_available_voices()
    # tts.text_to_speech("hello world", save=True)
