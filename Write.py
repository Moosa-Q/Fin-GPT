import pyautogui
import time
import pygame
import warnings
import os
from mtranslate import translate
from colorama import Fore, Style, init
import edge_tts
import asyncio
import speech_recognition as sr

pygame.init()

warnings.filterwarnings('ignore')
init(autoreset=True)

VOICE = 'en-GB-ThomasNeural'
BUFFER_SIZE = 1024


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


async def amain(TEXT, output_file):
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        play_audio(output_file)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        remove_file(output_file)


def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()
        while pygame.mixer.get_busy():
            pygame.time.wait(100)
        pygame.quit()
    except Exception as e:
        print(f"Error playing audio: {e}")


def say(text, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
    asyncio.run(amain(text, output_file))


def Translate_urdu_to_english(text):
    return translate(text, "en-gb")


def takecommand():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 270
    recognizer.pause_threshold = 0.5
    recognizer.dynamic_energy_threshold = True

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
                return translated_txt
            except sr.UnknownValueError:
                print("\r" + Fore.RED + "Sorry, I did not understand that. Please try again.")
            except Exception as e:
                print(f"\rError: {e}")
                
def write(content):
    pyautogui.hotkey('win', 's')
    time.sleep(0.5)
    pyautogui.write("word")
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(content)
