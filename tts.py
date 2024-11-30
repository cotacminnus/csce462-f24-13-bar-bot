import pyttsx3
import threading

class TextToSpeech:
    def init(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.engine.setProperty("volume", 1.0)
        self.lock = threading.Lock()  # Add a threading lock

    def _speak(self, text):
        #with self.lock:  # Ensure only one thread speaks at a time
        self.engine.say(text)
        self.engine.runAndWait()

    def text_to_speech(self, text):
        thread = threading.Thread(target=self._speak, args=(text,))
        thread.start()


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
