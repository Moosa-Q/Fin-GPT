import pyautogui
import pygame
import os
import warnings
from colorama import init
import asyncio
import edge_tts
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from Github import takecommand

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


def MyStudyLife():
    service = Service('LOCATION')
    driver = webdriver.Chrome(service=service)
    say("Would you like version 1 or version 2")
    v1_or_v2 = takecommand().lower()
    if "one" in v1_or_v2 or "1" in v1_or_v2:
        say("Activating Version 1")
        driver.get("https://app.mystudylife.com/?utm_source=mystudylife&utm_medium=sign-in&utm_campaign=mystudylife.com")
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app-login"]/section[2]/div/section[1]/div[3]/a[1]').click()
        time.sleep(0.5)
        pyautogui.write("moosaqadeer@gmail.com")
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.write("Stingray@11")
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        try:
            say("The result is on your screen")
        except Exception as e:
            say(f"An error occurred {e}")
    elif "two" in v1_or_v2 or "2" in v1_or_v2:
        say("Activating version 2")
        driver.get("https://web.mystudylife.com/#/login")
        time.sleep(0.5)
        driver.find_element(By.XPATH, '/html/body/flutter-view').click()
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.write("moosaqadeer@gmail.com")
        time.sleep(0.5)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.write("Stingray@11")
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(0.5)
        say("The result is on your screen")

