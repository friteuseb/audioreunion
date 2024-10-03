import speech_recognition as sr
import sounddevice as sd
import numpy as np
import wave
import keyboard
import threading
from transformers import pipeline

class AudioToTextConverter:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.is_recording = False
        self.audio_frames = []
        self.text = ""
        self.summarizer = pipeline("summarization")

    def start_recording(self):
        self.is_recording = True
        self.audio_frames = []
        print("Enregistrement démarré. Appuyez sur 'q' pour arrêter.")
        with sd.InputStream(callback=self.audio_callback, channels=1, samplerate=16000):
            while self.is_recording:
                sd.sleep(100)

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_frames.append(indata.copy())

    def stop_recording(self):
        self.is_recording = False
        print("Enregistrement arrêté.")
        self.save_audio()
        self.convert_audio_to_text()
        self.generate_summary()

    def save_audio(self):
        audio_data = np.concatenate(self.audio_frames, axis=0)
        wf = wave.open("audioreunion/recorded_audio.wav", "wb")
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(16000)
        wf.writeframes(audio_data.tobytes())
        wf.close()
        print("Audio sauvegardé dans 'recorded_audio.wav'")

    def convert_audio_to_text(self):
        with sr.AudioFile("audioreunion/recorded_audio.wav") as source:
            audio = self.recognizer.record(source)
        try:
            self.text = self.recognizer.recognize_google(audio, language="fr-FR")
            print("Texte transcrit :")
            print(self.text)
        except sr.UnknownValueError:
            print("La reconnaissance vocale n'a pas pu comprendre l'audio")
        except sr.RequestError as e:
            print(f"Erreur lors de la requête au service de reconnaissance vocale; {e}")

    def generate_summary(self):
        if self.text:
            summary = self.summarizer(self.text, max_length=150, min_length=30, do_sample=False)
            print("\nRésumé de la réunion :")
            print(summary[0]['summary_text'])
        else:
            print("Pas de texte à résumer.")

def main():
    converter = AudioToTextConverter()
    print("Appuyez sur 's' pour démarrer l'enregistrement.")
    keyboard.wait('s')
    threading.Thread(target=converter.start_recording).start()
    keyboard.wait('q')
    converter.stop_recording()

if __name__ == "__main__":
    main()
