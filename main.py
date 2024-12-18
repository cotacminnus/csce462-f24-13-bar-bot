from tts_v import TextTSpeech
from speech_recog import Speech2Text
from poll_fr import FacialRecognition
import time
import recipe
import logging

logging.basicConfig(level=logging.WARNING)

def main():
    # Initialize Text-to-Speech, Speech-to-Text, and Facial Recognition

    tts = TextTSpeech()
    stt = Speech2Text()
    facial = FacialRecognition()

    tts.__init__()
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
        

        try:
            tts.text_to_speech(drink_list_str)
        except Exception as e:
            print(f"Error in text_to_speech: {e}")
        time.sleep(1)

        
        # Listen for drink choice
        try:
            recognized_text = stt.listen_until_keyword(keywords=available_drinks)
            print(f"Recognized text: {recognized_text}")
            drink_choice = next((drink for drink in available_drinks if drink in recognized_text.lower()), None)

            if drink_choice:
                tts.text_to_speech(f"Great choice! Pouring {drink_choice} now.")
                recipe.make_drink_from_list(drink_choice, recipes)
                time.sleep(4)
                tts.text_to_speech("Your drink is ready. Enjoy!")
            else:
                tts.text_to_speech("I didn't catch that. Please choose a drink from the menu.")
        except Exception as e:
            print(f"Error during interaction: {e}")
            tts.text_to_speech("Sorry, something went wrong. Please try again.")

        # Reset for the next customer
        print("Interaction complete. Resetting...")
        time.sleep(4)

        
if __name__ == "__main__":
    main()
