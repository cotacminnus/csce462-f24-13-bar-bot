from tts import Text2Speech, TextToSpeech
from speech_recog import Speech2Text
from poll_fr import FacialRecognition
import pump_ctrl
import time
import csv
import json
import recipe

def main():
    # Initialize Text-to-Speech, Speech-to-Text, and Facial Recognition

    tts = TextToSpeech()
    stt = Speech2Text()
    facial = FacialRecognition()

    tts.init()
    stt.init("/home/asCSCE462/Desktop/csce462-f24-13-bar-bot/model/vosk-model-small-en-us-0.15")

    # Load recipes and storage data
    recipes = recipe.load_recipes()  # Dictionary of drinks and their pump amounts

    while True:
        # Wait for a face to be recognized
        print("Polling for a face...")
        tts.text_to_speech("Scanning for a customer.")
        while not facial.poll_webcam(interval=1, save_path="output/captured_image.jpg"):
            time.sleep(1)  # Wait 1 second between polling attempts

        # Check available drinks
        available_drinks = recipe.get_available_drinks(recipes)

        if not available_drinks:
            tts.text_to_speech("I'm sorry, we're out of stock for all drinks.")
            continue
        
        print(available_drinks)

        # Greet the customer and list available drinks
        print("Face detected. Greeted the customer.")
        drink_list_str = "Howdy! Welcome to the bar bot! Available drinks are " + ", ".join(available_drinks)
        print(drink_list_str)
        tts.text_to_speech("howdy")
        
        stt.mute()
        try:
            tts.text_to_speech(drink_list_str)
        except Exception as e:
            print(f"Error in text_to_speech: {e}")
        time.sleep(3 + len(available_drinks))  #delay relative to list length
        stt.unmute()
        
        # Listen for drink choice
        try:
            recognized_text = stt.listen_until_keyword(keywords=available_drinks)
            print(f"Recognized text: {recognized_text}")
            drink_choice = next((drink for drink in available_drinks if drink in recognized_text.lower()), None)

            if drink_choice:
                tts.text_to_speech(f"Great choice! Pouring {drink_choice} now.")
                recipe.make_drink_from_list(drink_choice, recipes)
                time.sleep(7)
                tts.text_to_speech("Your drink is ready. Enjoy!")
            else:
                tts.text_to_speech("I didn't catch that. Please choose a drink from the menu.")
        except Exception as e:
            print(f"Error during interaction: {e}")
            tts.text_to_speech("Sorry, something went wrong. Please try again.")

        # Reset for the next customer
        print("Interaction complete. Resetting...")
        time.sleep(4)

        tts.stop()
        tts.run()
        
if __name__ == "__main__":
    main()
