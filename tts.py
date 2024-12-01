import pyttsx3
import threading
from queue import Queue

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)
        self.queue = Queue()
        self.worker_thread = threading.Thread(target=self._process_queue, daemon=True)
        self.worker_thread.start()

    def sanitize_text(self, text):
        return ''.join(char for char in text if char.isprintable())

    def _process_queue(self):
        while True:
            text = self.queue.get()
            if text is None:
                break
            self._speak(text)
            self.queue.task_done()

    def _speak(self, text):
        sanitized_text = self.sanitize_text(text)
        if not sanitized_text.strip():
            print("TTS Error: Sanitized text is empty.")
            return
        with threading.Lock():
            print(f"TTS Speaking: {sanitized_text}")
            self.engine.say(sanitized_text)
            self.engine.runAndWait()

    def text_to_speech(self, text):
        if not isinstance(text, str) or not text.strip():
            print("TTS Error: Received invalid or empty text for speech.")
            return
        self.queue.put(text)

    def stop(self):
        self.queue.put(None)
        self.worker_thread.join()
        self.engine.stop()

'''
class TextToSpeech:
    def init(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)
        self.lock = threading.Lock()

    def sanitize_text(self, text):
        # Remove unsupported characters
        return ''.join(char for char in text if char.isprintable())

    def _speak(self, text):
        sanitized_text = self.sanitize_text(text)
        if not sanitized_text.strip():
            print("TTS Error: Sanitized text is empty.")
            return
        with self.lock:
            print(f"TTS Speaking: {sanitized_text}")  # Debugging output
            self.engine.say(sanitized_text)
            self.engine.runAndWait()

    def text_to_speech(self, text):
        try:
            if not isinstance(text, str) or not text.strip():
                print("TTS Error: Received invalid or empty text for speech.")
                return
            thread = threading.Thread(target=self._speak, args=(text,))
            thread.start()
            thread.join()
        except Exception as e:
            print(f"TTS Error: {e}")

    def stop(self):
        with self.lock:
            self.engine.stop()

'''

class Text2Speech:
    engine = None

    # in case we need these
    volume = 1.0
    rate = 150     # speed
    gender = None   # 0: Male, 1: Female
    

    def init(self):
        self.engine = pyttsx3.init()

        #in case we need these
        self.volume = self.engine.getProperty('volume')
        self.rate = self.engine.getProperty('rate')
        self.gender = self.engine.getProperty('voices')

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    
    def stop(self):
        self.engine.stop()  # stops the engine


'''
    ### If we decide to go online then we will have to implement this

    def connect(token):
                        # use API if necessary
        return False
'''
