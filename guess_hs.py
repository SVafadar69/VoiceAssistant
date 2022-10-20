import time
import sys
import random

# Importing from 2nd root level - figure out package imports

from mysay import print_say
from mysr import voice_to_text

print_say("Think of a number, bigger or equal to 1 but smaller or equal to 9.")
print_say("Wait five seconds bitch ")

possible_guesses = [1, 2, 3, 4, 5, 6, 7, 8, 9]


time.sleep(5)


print_say("Guess a number")
inp = voice_to_text().lower()
inp = int(inp) #converting string of spoken num to int
print(inp)

print_say("I will guess a number too. Tell me if it's too high or too low")

for i in range(len(possible_guesses)):

    choice = random.choice(possible_guesses)
    #choice = random.randint(1, len(possible_guesses)) #random num between 1 -> 9
    print_say(f"Is it {choice}")


    if inp == choice:
        print_say("That was your guess")
        sys.exit

    else:
        print("That was incorrect")
        possible_guesses.remove(choice)


message = ''' This is an example to speak triple quotation marks'''
print_say(message)