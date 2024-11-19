import pygame
from mtranslate import translate
import speech_recognition as sr
import warnings
import asyncio
from colorama import Fore,Style, init
import wolframalpha
import os
import random
import pyautogui
import edge_tts

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

def Translate_urdu_to_english(text):
    return translate(text, "en-gb")

def translate(query):
    result = Translate_urdu_to_english(query)
    say(result)