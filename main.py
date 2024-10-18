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

if __name__ == "__main__":
    main()
