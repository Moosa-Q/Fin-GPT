import pygame
import warnings
import asyncio
import os
import pyautogui
import edge_tts
import time
import random

pygame.init()

warnings.filterwarnings('ignore')

VOICE = 'en-GB-RyanNeural'
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

def note(what_to_remember):
    pyautogui.FAILSAFE = False
    pyautogui.hotkey('win', 's')
    time.sleep(0.1)
    pyautogui.write("cmd")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('shift', 'tab')
    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.5)
    note_number = random.randint(1, 100)
    pyautogui.write(f"notepad.exe note num {note_number}.txt")
    time.sleep(0.3)
    pyautogui.hotkey('shift', 'tab')
    time.sleep(0.2)
    pyautogui.press('enter')
    pyautogui.write(what_to_remember)
    say("The note has been made")
