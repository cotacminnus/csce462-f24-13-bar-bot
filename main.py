from tts import TextToSpeech
from tts import Text2Speech
from speech_recog import Speech2Text
from poll_fr import FacialRecognition
import pump_ctrl
import time
import csv
import json

# Load drink recipes from CSV
def load_recipes(filepath="pump_data/recipelist.csv"):
    recipes = {}
    with open(filepath, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            drink, *amounts = row
            recipes[drink.lower()] = [int(amount) for amount in amounts]
    return recipes

def main():
    # Initialize Text-to-Speech, Speech-to-Text, and Facial Recognition
    tts = TextToSpeech()
    tts1 = Text2Speech()
    stt = Speech2Text()
    facial = FacialRecognition()

    tts1.init()
    tts.init()
    stt.init("/home/asCSCE462/Desktop/csce462-f24-13-bar-bot/model/vosk-model-small-en-us-0.15")

    # Load recipes and storage data
    recipes = load_recipes()  # Dictionary of drinks and their pump amounts
    storage = pump_ctrl.read_storage()  # List with liquid amounts for each pump

    while True:
        # Wait for a face to be recognized
        print("Polling for a face...")
        tts1.text_to_speech("Scanning for a customer.")
        while not facial.poll_webcam(interval=1, save_path="output/captured_image.jpg"):
            time.sleep(1)  # Wait 1 second between polling attempts

        # Greet the customer and list available drinks
        #tts.text_to_speech("Howdy! Welcome to the bar bot! Available drinks are ")
        print("Face detected. Greeted the customer.")

        # List available drinks
        
        
        available_drinks = []
        for drink, pump_amounts in recipes.items():
            if all(storage[i] >= pump_amounts[i] for i in range(len(pump_amounts))):
                available_drinks.append(drink)

        if not available_drinks:
            tts.text_to_speech("I'm sorry, we're out of stock for all drinks.")
            continue


        x = "hi"
        drink_list_str = "       ".join(available_drinks)
        drink_list_str = "Howdy! Welcome to the bar bot! Available drinks are, " + available_drinks[0] + available_drinks[1] + available_drinks[2] + available_drinks[3] 
        l_list = [item.lower() for item in available_drinks]
        my_list = [f'"{item}"' for item in l_list]
        f_list = ", ".join(f'"{item}"' for item in l_list)
        

        tts.text_to_speech(drink_list_str)

        # Listen for drink choice
        try:
            recognized_text = stt.listen_until_keyword(keywords = available_drinks)  # Get raw speech
            drink_choice = next((drink for drink in available_drinks if drink in recognized_text.lower()), None)

            if drink_choice:
                tts1.text_to_speech(f"Great choice! Pouring {drink_choice} now.")

                # Get the pump amounts for the selected drink
                pump_amounts = recipes[drink_choice]

                # Dispense from each pump as needed
                for pump, amount in enumerate(pump_amounts, start=1):
                    if amount > 0:
                        #pump_ctrl.actuate_pump(pump, amount)
                        storage[pump - 1] -= amount  # Update storage

                # Save the updated storage
                pump_ctrl.write_storage(storage)
                print(storage)

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
