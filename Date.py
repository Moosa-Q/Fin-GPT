import pygame
import warnings
from colorama import Fore, Style, init
import edge_tts
import asyncio
import os
import datetime

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

def date() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    say(f"the current date is {day}/{month}/{year}")
    print(f"The current date is {day}/{month}/{year}")