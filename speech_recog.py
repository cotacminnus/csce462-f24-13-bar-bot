import os
import speech_recognition as sr
import vosk
import json

model = vosk.Model("path_to_model")
recognizer = vosk.KaldiRecognizer(model, 16000)

class Speech2Text:
    def listen():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        # this will use OpenAI's Whisper API
        # We found that it is unrealistic to implement the speech recognition function locally on a Raspi

        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        text = ""

        try:
            print("Fetched results from Whisper API")
            text = r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)
        except sr.RequestError as e:
            print(f"Could not request results from Whisper API; {e}")

        return text