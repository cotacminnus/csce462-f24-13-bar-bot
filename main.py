import Text2Speech
import Speech2Text
import Facial_Recognition
import Pumpctrl

'''
Logic of the main function:
    standby until a face is recognized  ->  Greet   <->  answer questions ->  if requested, pour drink
'''

def main():
    tts = Text2Speech()
    stt = Speech2Text()
    facial = Facial_Recognition()

    tts.init()

    #Facial recognition will be polling
    while True:
        #while(noface):
            #try to recognize face every second
            #if face detected, break

        #greet

        #while not asking for drink
            #wait for user speech
                #if getting user speech, respond
                #if asking for drink, goto drink dispensing
                #if face not recognized, go back to the beginning

        #dispense drink
        #go back to 26

        continue
        #complete the cycle

if __name__ == "__main__":
    main()
