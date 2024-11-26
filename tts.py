import pyttsx3
import threading

# This is implemented as a class for convenience
class Text2Speech:
    engine = None

    # in case we need these
    volume = 2
    rate = None     # speed
    gender = None   # 0: Male, 1: Female
    

    def init(self):
        self.engine = pyttsx3.init()

        #in case we need these
        self.volume = self.engine.getProperty('volume')
        self.rate = self.engine.getProperty('rate')
        self.gender = self.engine.getProperty('voices')

    def _speak(self, text):
        """
        Internal method to handle speech synthesis.
        :param text: The text to be spoken aloud.
        """
        self.engine.say(text)
        self.engine.runAndWait()  # This blocks, but it's inside a thread

    def text_to_speech(self, text):
        """
        Speaks the given text asynchronously using a separate thread.
        :param text: The text to be spoken aloud.
        """
        # Create and start a thread for the speech
        thread = threading.Thread(target=self._speak, args=(text,))
        thread.start()  # Start the thread

    
    def stop(self):
        self.engine.stop()  # stops the engine

    '''

    ### If we decide to go online then we will have to implement this

    def connect(token):
                        # use API if necessary
        return False
    '''
