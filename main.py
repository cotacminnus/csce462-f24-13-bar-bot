from tts import Text2Speech
from speech_recog import Speech2Text
from facial_recog import Facial_Recognition
from pump_ctrl import Pumpctrl

'''
Logic of the main function:
    standby until a face is recognized  ->  Greet   <->  answer questions ->  if requested, pour drink
'''

def main():
    tts = Text2Speech()
    stt = Speech2Text()
    facial = Facial_Recognition()

    tts.init()

    sentence = ''

    #Facial recognition will be polling
    while True:
        #while(noface):
            #try to recognize face every second
            #if face detected, break

        #greet
        tts.text_to_speech("Howdy!")
        tts.stop

         #while not asking for drink
            #wait for user speech
                #if getting user speech, respond
                #if asking for drink, goto drink dispensing
                #if face not recognized, go back to the beginning

        while(not (sentence.find("pour") and sentence.find("drink"))):
            #listen
            # sentence = listen
            sentence = ''

        #dispense drink
        #go back

        continue
        #complete the cycle

if __name__ == "__main__":
    main()
