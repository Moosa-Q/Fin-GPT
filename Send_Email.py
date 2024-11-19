from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init
import pygame
import os
import edge_tts
import asyncio
import pyautogui
import time

# Initialize Colorama
init(autoreset=True)

VOICE = 'en-GB-ThomasNeural'
BUFFER_SIZE = 1024


def Translate_urdu_to_english(text):
    return translate(text, "en-gb")


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
            pygame.time.wait(100)  # Slight wait to allow the mixer to finish playing
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

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.LIGHTGREEN_EX + "I am listening...", end="", flush=True)
        try:
            audio = recognizer.listen(source)
            print("\r" + Fore.LIGHTYELLOW_EX + "Got it, Now recognizing...", end="", flush=True)
            recognized_txt = recognizer.recognize_google(audio).lower()
            translated_txt = Translate_urdu_to_english(recognized_txt)
            print("\r" + Fore.BLUE + f"Moosa said: {translated_txt}")
            return translated_txt  # Make sure the recognized and translated text is returned
        except sr.UnknownValueError:
            print("\r" + Fore.RED + "Sorry, I did not understand that.")
            return ""  # Return an empty string when speech is not recognized
        except Exception as e:
            print(f"\rError: {e}")
            return ""  # Return an empty string in case of any other exception


def send_email(person, subject, message):
    service = Service('LOCATION TO CHROMEDRIVER')
    driver = webdriver.Chrome(service=service)
    driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fhl%3Den-GB&emr=1&hl=en-GB&ifkv=Ab5oB3qAa--8FXWkD6EBNd1CHQw1NIKIKgFFMjLyOC2TdZTVGFvDoNON8tVvuUyjAmwzu5hBOjog&ltmpl=default&ltmplcache=2&osid=1&passive=true&rm=false&scc=1&service=mail&ss=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1930060338%3A1725801121235110&ddm=0")
    driver.maximize_window()
    time.sleep(1)
    pyautogui.write("YOUR EMAIL")
    time.sleep(3)
    pyautogui.write("YOUR PASSWORD")
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(4.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write(person)
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(subject)
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(message)
    time.sleep(0.5)
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('enter')