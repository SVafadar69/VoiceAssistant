import random
from mysay import print_say
import time

def joke():

    with open("mptpkg/jokes.txt") as jokes:
        content = jokes.read() #reading txt file - returns amount in chars

        joke_list = content.split('\n\n')
        print(joke_list)
        one_joke = random.choice(joke_list)
        print_say(one_joke)

joke()
