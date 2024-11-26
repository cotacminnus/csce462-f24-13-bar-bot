import pyttsx3

class TextToSpeech:
    def __init__(self):
        """
        Initialize the TTS engine and set default properties.
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)  # Set speech rate
        self.engine.setProperty("volume", 1.0)  # Set volume to max (1.0)

    def speak(self, input_variable):
        """
        Convert any input variable to speech without using runAndWait().
        :param input_variable: The input to be spoken. Can be a string, number, boolean, list, etc.
        """
        # Ensure the input is converted to a string
        try:
            text = str(input_variable)  # Convert variable to string
        except Exception as e:
            raise ValueError(f"Cannot convert input to string: {e}")

        # Check if the resulting string is valid
        if not text.strip():  # Check for empty or whitespace-only strings
            raise ValueError("Input is empty or invalid for TTS.")

        # Queue the text for speech
        self.engine.say(text)

    def start_speaking(self):
        """
        Process the speech queue asynchronously.
        """
        self.engine.startLoop(False)  # Start the loop without blocking
        while self.engine.isBusy():
            self.engine.iterate()  # Process events

        self.engine.endLoop()

    def stop_speaking(self):
        """
        Stop the speech engine and clear the queue.
        """
        self.engine.stop()

    def speak_list(self, input_list):
        """
        Speak each item in a list without using runAndWait().
        :param input_list: A list of items to be spoken. Items are converted to strings if needed.
        """
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list.")

        for item in input_list:
            try:
                text = str(item)  # Convert each item to a string
                if text.strip():  # Speak non-empty strings only
                    self.speak(text)  # Queue the item
                else:
                    print(f"Skipping empty item: {item}")
            except Exception as e:
                print(f"Error processing item {item}: {e}")

        self.start_speaking()  # Process the speech queue asynchronously
