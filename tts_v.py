import pyttsx3
from multiprocessing import Process

class MultiprocessTextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)

    def _speak(self, text):
        """
        Synchronous speech synthesis.
        """
        self.engine.say(text)
        self.engine.runAndWait()

    def speak(self, text):
        """
        Uses a separate process for text-to-speech.
        :param text: The text to be spoken aloud.
        """
        process = Process(target=self._speak, args=(text,))
        process.start()
        process.join()

