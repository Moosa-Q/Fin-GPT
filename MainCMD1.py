import wolframalpha

from Brain import brain
from Speak import say
from Understand import takecommand
from CPU import cpu
from Chat import message
from Date import date
from HTB_Academy import HTB
from Google import google_src
from Music import music
from SatchelOne import satchel_one
from Github import github
from Location import location
from Retro_Games import retro_gaming
from News import read_news
from Open_Apps import open_apps
from MyStudyLife import MyStudyLife
from Joke import joke
from Time import time
from Weather import weather
from Write import write
from Youtube import youtube_src


def main_commands(query):
    if "date" in query:
            date()
    elif "what's up" in query:
        say("Just busy being your digital assistant, sir!")
    elif "introduce" in query:
        say("Allow me to introduce myself. I am JARVIS, a virtual artificial intelligence, here to assist you with a variety of tasks 24/7. Don't worry; I'm always awake!")
    elif "weather" in query:
        weather()
    elif "hack" in query:
        HTB()
    elif "youtube" in query:
        src_query = takecommand()
        src_query = src_query.replace("youtube", "").replace("search", "")
        youtube_src(src_query)
    elif "time" in query:
        time()
    elif "cpu" in query:
        cpu()
    elif "calculate" in query:
        app_id = "WOLFRAMALPHA API KEY"
        client = wolframalpha.Client(app_id)
        ind = query.lower().split().index("calculate")
        text = query.split()[ind + 1:]
        res = client.query(" ".join(text))
        answer = next(res.results).text
        say("The answer is " + answer)
        print(answer)
    elif "google" in query or "search" in query:
        query = query.replace("google", "").replace("search", "")
        google_src(query)
    elif "satchel" in query:
        satchel_one()
    elif "joke" in query:
        joke()
    elif "repo" in query:
        github()
    elif "locate" in query:
        query = query.replace("locate", "").replace("jarvis", "").strip()
        location(query)
    elif "news" in query:
        read_news()
    elif "study" in query:
        MyStudyLife()
    elif "play" in query:
        query = query.replace("play", "").replace("jarvis", "").strip()
        music(query=query)
    elif "retro" in query:
        say("Opening Launchbox to provide you with retro games.")
        retro_gaming()
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        open_apps(app_name)
    elif "exit" in query or "quit" in query:
        say("Goodbye! Don't get into too much trouble, okay?")
        quit()
    elif "satisfied" in query:
        say("See you later, sir!!")
    else:
        brain(query=query)

