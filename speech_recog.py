import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

class Speech2Text:

    model = None
    sample_rate = 16000 #default
    recognizer = None
    audio_queue = None

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_queue.put(bytes(indata))

    def init(self, model_path, srate=16000):
        self.model = Model(model_path)
        self.sample_rate = srate
        self.audio_queue = queue.Queue()
        self.recognizer = KaldiRecognizer(self.model, self.sample_rate)


    def listen_until_keyword(self, keyword):

        try:

            with sd.RawInputStream(samplerate=self.sample_rate, blocksize=8000, dtype="int16",
                        channels=1, callback=self.audio_callback):
                print("Listening...")

                buf = ""

                while buf.find(keyword) == -1:
                    # Get audio data from the queue
                    data = self.audio_queue.get()

                    # Pass data to the recognizer and print results
                    if self.recognizer.AcceptWaveform(data):
                        result = json.loads(self.recognizer.Result())
                        print("Recognized:", result["text"])

                        buf = result["text"]
                print("Hit!")
        except:
            print("Error listening, need retry...")