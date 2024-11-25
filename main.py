from tts import Text2Speech
from speech_recog import Speech2Text
from poll_fr import FacialRecognition
import pump_ctrl
import time
import recipe

'''
Logic of the main function:
    Standby until a face is recognized -> Greet -> Take drink order -> Pour drink
'''

def main():
    # Initialize Text-to-Speech, Speech-to-Text, and Facial Recognition
    tts = Text2Speech()
    stt = Speech2Text()
    facial = FacialRecognition()

    tts.init()
    stt.init("/home/asCSCE462/Desktop/csce462-f24-13-bar-bot/model/vosk-model-small-en-us-0.15")

    # Get menu and storage data
    menu = recipe.get_drink_list()
    storage = pump_ctrl.read_storage()

    while True:
        # Wait for a face to be recognized
        print("Polling for a face...")
        tts.text_to_speech("Scanning for a customer.")
        while not facial.poll_webcam(interval=1, save_path="output/captured_image.jpg"):
            time.sleep(1)  # Wait 1 second between polling attempts

        # Greet the customer and list available drinks
        tts.text_to_speech("Howdy! Welcome to the bar bot!")
        print("Face detected. Greeted the customer.")
        #tts.text_to_speech("What drink would you like?")

        # List available drinks
        available_drinks = [drink for drink in menu if menu[drink] <= storage.get(drink, 0)]
        if not available_drinks:
            tts.text_to_speech("I'm sorry, we're out of stock for all drinks.")
            continue

        tts.text_to_speech("Available drinks are: " + ", ".join(available_drinks))

        # Listen for drink choice
        try:
            drink_choice = stt.listen_until_keyword(available_drinks)
            if drink_choice in available_drinks:
                tts.text_to_speech(f"Great choice! Pouring {drink_choice} now.")
                #pump_ctrl.actuate_pump(menu[drink_choice], 180)  # Adjust pump logic as needed
                storage[drink_choice] -= menu[drink_choice]  # Update storage
                tts.text_to_speech("Your drink is ready. Enjoy!")
            else:
                tts.text_to_speech("I didn't catch that. Please choose a drink from the menu.")
        except Exception as e:
            print(f"Error during interaction: {e}")
            tts.text_to_speech("Sorry, something went wrong. Please try again.")

        # Reset for the next customer
        print("Interaction complete. Resetting...")
        time.sleep(2)

if __name__ == "__main__":
    main()



'''
from tts import Text2Speech
from speech_recog import Speech2Text
from poll_fr import FacialRecognition
import pump_ctrl
import time
import recipe

'''
#Logic of the main function:
 #   standby until a face is recognized  ->  Greet   <->  answer questions ->  if requested, pour drink
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

        time.sleep(4)

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
        tts.text_to_speech("Pouring water. Make sure cup is under nozzle")

        time.sleep(1)

        #pump_ctrl.actuate_pump(4, 60) #pour roughly 6 ounces of water
        #dispense drink
        #go back
        #complete the cycle
        time.sleep(.5)

if __name__ == "__main__":
    main()

'''
