import pyttsx3
import threading

class ThreadedTextToSpeech:
    def __init__(self):
        """
        Initialize the TTS engine and set default properties.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)  # Adjust speech rate
        self.engine.setProperty("volume", 1.0)  # Set volume to max
        self.thread = None
        self.lock = threading.Lock()  # Ensure thread-safe execution
        self.running = False  # Flag to check if TTS is running

    def _speak(self, text):
        """
        Internal method to process speech synthesis.
        """
        with self.lock:
            self.engine.say(text)
            self.engine.runAndWait()
        self.running = False  # Mark the TTS process as complete

    def text_to_speech(self, text):
        """
        Speaks the given text in a separate thread.
        :param text: The text to be spoken aloud.
        """
        if self.running:
            print("TTS is already running. Please wait.")
            return

        self.running = True  # Mark TTS as running
        self.thread = threading.Thread(target=self._speak, args=(text,), daemon=True)
        self.thread.start()

    def wait_until_complete(self):
        """
        Waits for the current TTS process to complete.
        """
        if self.thread and self.thread.is_alive():
            self.thread.join()  # Wait for the thread to finish
        self.running = False  # Ensure the running flag is reset

