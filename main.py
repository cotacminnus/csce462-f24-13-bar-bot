from tts import Text2Speech
from speech_recog import Speech2Text
from poll_fr import FacialRecognition
import pump_ctrl
import time
import recipe

'''
Logic of the main function:
    standby until a face is recognized  ->  Greet   <->  answer questions ->  if requested, pour drink
'''

def main():
    tts = Text2Speech()
    stt = Speech2Text()
    facial = FacialRecognition()

    tts.init()
    stt.init("/home/asCSCE462/Desktop/csce462-f24-13-bar-bot/model/vosk-model-small-en-us-0.15")

    #get menu
    menu = recipe.get_drink_list()
    storage = pump_ctrl.read_storage()

    #Facial recognition will be polling
    while True:
        print("Polling for a face...")
        tts.text_to_speech("Scanning for a customer.")
        while not facial.poll_webcam(interval=1, save_path="output/captured_image.jpg"):
            time.sleep(1)  # Wait 1 second between polling attempts

        # Greet the customer
        tts.text_to_speech("Howdy! I am the bar bot! What can I get for you to drink?")
        print("Face detected. Greeted the customer.")


         #while not asking for drink
            #wait for user speech
                #if getting user speech, respond
                #if asking for drink, goto drink dispensing
                #if face not recognized, go back to the beginning

        try:
            stt.listen_until_keyword("water")
        except:
            continue
        print("Run!")
        tts.text_to_speech("Pouring water. Make sure cup is under nosel")

        time.sleep(1)

        pump_ctrl.actuate_pump(4, 60) #pour roughly 6 ounces of water
        #dispense drink
        #go back
        #complete the cycle
        time.sleep(.5)

if __name__ == "__main__":
    main()
