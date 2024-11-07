import deepspeech
import numpy as np
import pyaudio
import wave

# Load DeepSpeech model
model_file_path = 'deepspeech-0.9.3-models.pbmm'
scorer_file_path = 'deepspeech-0.9.3-models.scorer'

model = deepspeech.Model(model_file_path)
model.enableExternalScorer(scorer_file_path)

# Audio settings
CHUNK = 1024  # Number of audio frames per buffer
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Mono audio
RATE = 16000  # Sample rate (DeepSpeech is optimized for 16kHz audio)

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Function to capture audio
def record_audio():
    print("Recording...")
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Stopped recording.")
        stream.stop_stream()
        stream.close()
        return b''.join(frames)

# Function to convert audio to text
def transcribe(audio_data):
    # Convert audio data to numpy array
    audio_np = np.frombuffer(audio_data, dtype=np.int16)

    # Perform speech-to-text
    print("Transcribing...")
    text = model.stt(audio_np)
    print("You said:", text)

try:
    while True:
        audio_data = record_audio()  # Capture audio
        transcribe(audio_data)  # Transcribe captured audio
except KeyboardInterrupt:
    print("Exiting...")

# Cleanup
audio.terminate()
