import pyttsx3
import threading

class Text2Speech:
    def init(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)
        self.lock = threading.Lock()  # Add a threading lock

    def _speak(self, text):
        with self.lock:  # Ensure only one thread speaks at a time
            self.engine.say(text)
            self.engine.runAndWait()

    def text_to_speech(self, text):
        thread = threading.Thread(target=self._speak, args=(text,))
        thread.start()
