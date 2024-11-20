from Speak import say
from MainCMD1 import main_commands

def main(query):
    main_commands(query=query)

if __name__ == "__main__":
    say('Hello. I am FEIN, your personal assistant here to make your life easier. Say "I am satisfied with my care" to shut me down')
    while True:
        cmd = input("Master: ")
        main(cmd)
