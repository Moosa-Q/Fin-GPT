import requests
import os
import threading
import pygame
import edge_tts
from mtranslate import translate
import asyncio

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

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()


def weather():
    api_key = ""
    city = ""
    weather_data = get_weather(api_key, city)

    if weather_data.get("cod") != 200:
        print("Error:", weather_data.get("message"))
    else:
        main_weather = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        say(f"The weather in {city} is {main_weather} with a temperature of {temp}°C")
        print(f"The weather in {city} is {main_weather} with a temperature of {temp}°C.")