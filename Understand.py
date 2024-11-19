from mtranslate import translate
import speech_recognition as sr
from colorama import Fore
import os

def Translate_urdu_to_english(text):
    return translate(text, "en-gb")

def takecommand():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.dynamic_energy_threshold = 35000  # You can adjust this if needed
    recognizer.dynamic_energy_adjustment_damping = 0.03
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.pause_threshold = 0.8  # Ensure this is greater than non_speaking_duration
    recognizer.non_speaking_duration = 0.5  # Should be lower than pause_threshold
    recognizer.operation_timeout = None

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTGREEN_EX + "I'm Listening, sir...", end="", flush=True)
            try:
                audio = recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTYELLOW_EX + "Recognizing...", end="", flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    translated_txt = Translate_urdu_to_english(recognized_txt)
                    print("\r" + Fore.BLUE + "Moosa said: " + translated_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r", end="", flush=True)

            os.system("cls" if os.name == "nt" else "clear")