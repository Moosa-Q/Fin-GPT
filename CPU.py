import warnings
import pygame
import speech_recognition as sr
import psutil
from colorama import Fore, Style, init
import os
import edge_tts
import asyncio
from mtranslate import translate

pygame.init()

warnings.filterwarnings('ignore')
init(autoreset=True)

VOICE = 'en-GB-ThomasNeural'
BUFFER_SIZE = 1024


# Remove file with retries
def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            os.remove(file_path)
            break
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1


# Text-to-speech and play
async def amain(TEXT, output_file):
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        play_audio(output_file)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        remove_file(output_file)


# Play audio using pygame
def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.wait(100)  # Allow the mixer to finish playing
        pygame.quit()
    except Exception as e:
        print(f"Error playing audio: {e}")


# Say a message using TTS
def say(text, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
    asyncio.run(amain(text, output_file))

def Translate_urdu_to_english(text):
    return translate(text, "en-gb")

def takecommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.LIGHTGREEN_EX + "I am listening...", end="", flush=True)

        while True:
            try:
                audio = recognizer.listen(source)
                print("\r" + Fore.LIGHTYELLOW_EX + "Got it, Now recognizing...", end="", flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                translated_txt = Translate_urdu_to_english(recognized_txt)
                print("\r" + Fore.BLUE + f"Moosa said: {translated_txt}")
                return translated_txt  # Make sure the recognized and translated text is returned
            except sr.UnknownValueError:
                print("\r" + Fore.RED + "Sorry, I did not understand that. Please try again.")
            except Exception as e:
                print(f"\rError: {e}")

def cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_status = f"CPU is currently at {cpu_usage}% usage."

    say(cpu_status)
    print(cpu_status)
