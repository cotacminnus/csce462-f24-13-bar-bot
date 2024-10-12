import os
import speech_recognition as sr

'''
This picks up volume from microphone
for phrase in LiveSpeech():
    print(phrase)
'''

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = r.listen(source)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
try:
    print(f"Whisper API thinks you said {r.recognize_whisper_api(audio, api_key=OPENAI_API_KEY)}")
except sr.RequestError as e:
    print(f"Could not request results from Whisper API; {e}")

'''
def speech_to_text(speech, online):
    # input an audio file, export a string
    # option to use external api
    return text
'''
def connect(token):

    return False