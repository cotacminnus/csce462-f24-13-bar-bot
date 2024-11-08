from vosk import Model, KaldiRecognizer
import wave
import json

model = Model("model/vosk-model-small-en-us-0.15")  # replace "model" with the path to your Vosk model folder
wf = wave.open("test.wav", "rb")
rec = KaldiRecognizer(model, wf.getframerate())

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(json.loads(rec.Result())["text"])
    else:
        print(json.loads(rec.PartialResult())["partial"])

print(json.loads(rec.FinalResult())["text"])
