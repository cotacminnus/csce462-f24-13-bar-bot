import sounddevice as sd
import queue
import json
import time
from vosk import Model, KaldiRecognizer


class Speech2Text:
    def __init__(self):
        self.model = None
        self.sample_rate = 16000  # Default
        self.recognizer = None
        self.audio_queue = None
        self.muted = False
        
    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        if not self.muted:  
            self.audio_queue.put(bytes(indata))
            
    def init(self, model_path, srate=16000):
        self.model = Model(model_path)
        self.sample_rate = srate
        self.audio_queue = queue.Queue()
        self.recognizer = KaldiRecognizer(self.model, self.sample_rate)
        
    
    def listen_until_keyword(self, keywords):
        """
        Listens until one of the keywords in the list is detected.
        :param keywords: List of keywords to detect.
        :return: The recognized keyword if detected.
        """

        if not isinstance(keywords, list):
            raise ValueError("Keywords must be provided as a list.")
        with sd.RawInputStream(samplerate=self.sample_rate, blocksize=8000, dtype="int16",
                               channels=1, callback=self.audio_callback):
            print("Listening...")
            while True:
                # Get audio data from the queue
                data = self.audio_queue.get()
                # Pass data to the recognizer
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    print("Recognized:", result["text"])
                    recognized_text = result["text"].lower()
                    
                    # Check if any keyword is found in the recognized text
                    for keyword in keywords:
                        if keyword.lower() in recognized_text:
                            print(f"Keyword detected: {keyword}")
                            return keyword
