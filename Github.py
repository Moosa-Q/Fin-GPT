from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
import time
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init
import pygame
import os
import edge_tts
import asyncio


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


def github():
    service = Service(r'C:/Users/user/OneDrive - Southend High School for Boys/Desktop/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.github.com/login")
    driver.maximize_window()
    pyautogui.write("GITHUB USER NAME")
    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.write("GITHUB PASSWORD")
    time.sleep(1)
    pyautogui.press('enter')
    repo_name_field = driver.find_element(By.XPATH, '//*[@id="repository[name]"]')
    say("What shall we name this repository")
    repo_name = takecommand()
    repo_name_field.click()
    pyautogui.write(repo_name)
    say("Is this repo going to be public or private?")
    pop = takecommand()
    if "public" in pop:
        driver.find_element(By.XPATH, '//*[@id="repository[visibility]_public"]').click()
    elif "private" in pop:
        say("Working on a secret project are we, sir")
    pyautogui.press('enter')
    say("Very well, project initialised. Shall we begin?")

