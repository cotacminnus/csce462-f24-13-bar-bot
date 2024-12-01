from gtts import gTTS
import os
import threading

class TextTSpeech:
    def __init__(self):
        self.lock = threading.Lock()

    def sanitize_text(self, text):
        # Remove unsupported characters
        return ''.join(char for char in text if char.isprintable())

    def _speak(self, text):
        sanitized_text = self.sanitize_text(text)
        if not sanitized_text.strip():
            print("TTS Error: Sanitized text is empty.")
            return
        with self.lock:
            try:
                print(f"TTS Speaking: {sanitized_text}")  # Debugging output
                tts = gTTS(sanitized_text)
                file_path = "output.mp3"
                tts.save(file_path)
                os.system(f"mpg321 {file_path}")  # Play the audio file
                os.remove(file_path)  # Clean up the audio file after playing
            except Exception as e:
                print(f"TTS Error: {e}")

    def text_to_speech(self, text):
        try:
            if not isinstance(text, str) or not text.strip():
                print("TTS Error: Received invalid or empty text for speech.")
                return
            thread = threading.Thread(target=self._speak, args=(text,))
            thread.start()
            thread.join()
        except Exception as e:
            print(f"TTS Error: {e}")
    
    def stop(self):
        # This method is not applicable with gTTS as the playback is managed externally.
        print("TTS stop functionality is not supported with gTTS.")

