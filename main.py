from tts import Text2Speech
from speech_recog import Speech2Text
# from facial_recog import Facial_Recognition
from pump_ctrl import PumpCtrl
import time

'''
Logic of the main function:
    standby until a face is recognized  ->  Greet   <->  answer questions ->  if requested, pour drink
'''

def main():
    tts = Text2Speech()
    stt = Speech2Text()
    # facial = Facial_Recognition()

    tts.init()
    stt.init("/home/asCSCE462/Desktop/csce462-f24-13-bar-bot/model/vosk-model-small-en-us-0.15")

    #Facial recognition will be polling
    while True:
        #while(noface):
            #try to recognize face every second
            #if face detected, break

        #greet
        tts.text_to_speech("Howdy!")


         #while not asking for drink
            #wait for user speech
                #if getting user speech, respond
                #if asking for drink, goto drink dispensing
                #if face not recognized, go back to the beginning
        try:
            stt.listen_until_keyword("drink")
        except:
            continue
        print("Run!")
        tts.text_to_speech("Pouring drink.")


        #dispense drink
        #go back
        #complete the cycle
        time.sleep(.1)

if __name__ == "__main__":
    main()
