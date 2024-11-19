import os
import threading
import pygame
import edge_tts
from mtranslate import translate
import asyncio
import requests

VOICE = 'en-GB-ThomasNeural'
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, "wb"):
                pass
            os.remove(file_path)
            break
        except Exception as e:
            print(f"error : {e}")
            attempts += 1

async def amain(TEXT, output_file) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, VOICE)
        await cm_txt.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
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
            pygame.time.get_ticks()  # Removed the argument here
        pygame.quit()
    except Exception as e:
        print(f"Error : {e}")

def say(Text, output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(Text, output_file))

def Translate_urdu_to_english(text):
    english_txt = translate(text, "en-gb")
    return english_txt

def read_news():
    def get_top_headlines(api_key, country='us'):
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
        response = requests.get(url)
        articles = response.json().get('articles', [])
        return articles

    def read_article_titles(api_key):
        articles = get_top_headlines(api_key)
        if len(articles) >= 2:
            title1 = articles[0]['title']
            title2 = articles[1]['title']
            text_to_read = f"{title1}. {title2}."
            say(text_to_read)
        else:
            say("Not enough articles found.")

    # Example usage
    api_key = 'API KEY'
    read_article_titles(api_key)
