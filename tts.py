import pyttsx3

# This is implemented as a class for convenience
class Text2Speech:
    engine = None
    volume = 100    # in case we need it

    def init(self):
        self.engine = pyttsx3.init()

    def text_to_speech(self, text):
        self.engine.say(text)

        self.engine.runAndWait()
        # pyttsx3 will output the audio to the speaker, no return needed
        # This will probably be blocking

        # return speech   # returns an audio file if we decide to implement otherway later

    '''

    ### If we decide to go online then we will have to implement this

    def connect(token):
                        # use API if necessary
        return False
    '''