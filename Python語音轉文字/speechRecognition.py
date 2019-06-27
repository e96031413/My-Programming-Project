pip install SpeechRecognition
import speech_recognition as sr
r = sr.Recognizer()
r.energy_threshold = 4000
with sr.WavFile("XXXXXXXXX.wav") as source:
    audio = r.record(source)

try:
    print("Transcription: " + r.recognize_google(audio))
except LookupError:
    print("Could not understand audio")