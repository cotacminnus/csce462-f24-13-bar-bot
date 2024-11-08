import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Load the Vosk model
model = Model("model/vosk-model-small-en-us-0.15")  # Replace with the path to your Vosk model

# Set up the recognizer with a sample rate (16000 is standard for Vosk)
sample_rate = 16000
recognizer = KaldiRecognizer(model, sample_rate)

# Create a queue to hold audio data
audio_queue = queue.Queue()

# Define a callback function to capture audio in real time
def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))

# Open an audio stream from the microphone
with sd.RawInputStream(samplerate=sample_rate, blocksize=8000, dtype="int16",
                       channels=1, callback=audio_callback):
    print("Listening...")

    while True:
        # Get audio data from the queue
        data = audio_queue.get()

        # Pass data to the recognizer and print results
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            print("Recognized:", result["text"])
        else:
            partial_result = json.loads(recognizer.PartialResult())
            print("Partial:", partial_result["partial"])
