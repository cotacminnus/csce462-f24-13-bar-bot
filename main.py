
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

    tts1 = Text2Speech()
    stt = Speech2Text()
    facial = FacialRecognition()

    tts1.init()
    #tts.init()
    stt.init("/home/asCSCE462/Desktop/csce462-f24-13-bar-bot/model/vosk-model-small-en-us-0.15")

    # Load recipes and storage data
    recipes = load_recipes()  # Dictionary of drinks and their pump amounts
    storage = [800,800,800,800]  # List with liquid amounts for each pump

    while True:
        # Wait for a face to be recognized
        print("Polling for a face...")
        tts1.text_to_speech("Scanning for a customer.")
        while not facial.poll_webcam(interval=1, save_path="output/captured_image.jpg"):
            time.sleep(1)  # Wait 1 second between polling attempts

        # Greet the customer and list available drinks
        tts1.text_to_speech("Howdy! Welcome to the bar bot! Available drinks are orange blue yellow water")
        print("Face detected. Greeted the customer.")

        # List available drinks

        
        available_drinks = []
        for drink, pump_amounts in recipes.items():
            if all(storage[i] >= pump_amounts[i] for i in range(len(pump_amounts))):
                available_drinks.append(drink)

        if not available_drinks:
            tts1.text_to_speech("I'm sorry, we're out of stock for all drinks.")
            continue
        print(available_drinks)

        x = "hi"
        drink_list_str = " ".join(available_drinks)
        drink_list_str = "Howdy! Welcome to the bar bot! Available drinks are  " 
        l_list = [item.lower() for item in available_drinks]
        my_list = [f'"{item}"' for item in l_list]
        f_list = ", ".join(f'"{item}"' for item in l_list)
        

        #tts.text_to_speech(drink_list_str)
        
        
        
        # Listen for drink choice
        try:
            recognized_text = stt.listen_until_keyword(keywords = available_drinks)
            # Get raw speech
            drink_choice = next((drink for drink in available_drinks if drink in recognized_text.lower()), None)

            if drink_choice:
                tts1.text_to_speech(f"Great choice! Pouring {drink_choice} now.")

                # Get the pump amounts for the selected drink
                pump_amounts = recipes[drink_choice]

                # Dispense from each pump as needed
                for pump, amount in enumerate(pump_amounts, start=1):
                    if amount > 0:
                        pump_ctrl.actuate_pump(pump, amount)
                        storage[pump - 1] -= amount  # Update storage
                        print(pump)

                # Save the updated storage
                pump_ctrl.write_storage(storage)
                print(storage)

                tts1.text_to_speech("Your drink is ready. Enjoy!")
            else:
                tts1.text_to_speech("I didn't catch that. Please choose a drink from the menu.")
        except Exception as e:
            print(f"Error during interaction: {e}")
            tts1.text_to_speech("Sorry, something went wrong. Please try again.")

        # Reset for the next customer
        print("Interaction complete. Resetting...")
        time.sleep(4)
        
if __name__ == "__main__":
    main()


