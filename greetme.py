import random
from Speak import say

def greet_me():
    greetings = ['Hello, sir', 'Hi, sir', 'How can i assist you today, sir', 'What shall i do, sir', 'Ready to assist, sir', 'Initiating support, please proceed, sir', 'Precision assistance, your way, sir']
    greeting_num = random.randint(1, 7)
    if greeting_num == 1:
        say(greetings[0])
        print(greetings[0])
    if greeting_num == 2:
        say(greetings[1])
        print(greetings[1])
    if greeting_num == 3:
        say(greetings[2])
        print(greetings[2])
    if greeting_num == 4:
        say(greetings[3])
        print(greetings[3])
    if greeting_num == 5:
        say(greetings[4])
        print(greetings[4])
    if greeting_num == 6:
        say(greetings[5])
        print(greetings[5])
    if greeting_num == 7:
        say(greetings[6])
        print(greetings[6])